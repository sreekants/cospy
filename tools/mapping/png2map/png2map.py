#!/usr/bin/env python3
"""Generate land and sea polygons from a color-coded PNG map.

The input image is expected to use:
- shades of green for land
- shades of blue for sea

The script classifies the pixels, merges them into polygon regions, and writes the
result to `land.s3db` and `sea.s3db` using the same `isohypses` schema already
used elsewhere in this repository.
"""

from __future__ import annotations

import argparse
import sqlite3
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from PIL import Image
from scipy import ndimage
from shapely.geometry import Polygon, box
from shapely.ops import unary_union


@dataclass(frozen=True)
class LayerSpec:
    name: str
    color: str
    type_code: int
    z_field: str
    z_value: float


LAND = LayerSpec("land", "#3CB371", 100000, "height", 0.0)
SEA = LayerSpec("sea", "#47B9C6", 100000, "depth", 0.0)


def parse_size(value: str) -> tuple[int, int]:
    text = value.lower().replace(",", "x")
    parts = [part.strip() for part in text.split("x") if part.strip()]
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("Size must be formatted as WIDTHxHEIGHT.")
    return int(parts[0]), int(parts[1])


def rgb_to_hsv_metrics(rgb: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rgbf = rgb.astype(np.float32) / 255.0
    r = rgbf[..., 0]
    g = rgbf[..., 1]
    b = rgbf[..., 2]

    maxc = np.max(rgbf, axis=-1)
    minc = np.min(rgbf, axis=-1)
    delta = maxc - minc

    hue = np.zeros_like(maxc)
    nonzero = delta > 1e-6

    rmask = nonzero & (maxc == r)
    gmask = nonzero & (maxc == g)
    bmask = nonzero & (maxc == b)

    hue[rmask] = ((g[rmask] - b[rmask]) / delta[rmask]) % 6.0
    hue[gmask] = ((b[gmask] - r[gmask]) / delta[gmask]) + 2.0
    hue[bmask] = ((r[bmask] - g[bmask]) / delta[bmask]) + 4.0
    hue *= 60.0

    saturation = np.zeros_like(maxc)
    value_mask = maxc > 1e-6
    saturation[value_mask] = delta[value_mask] / maxc[value_mask]
    return hue, saturation, maxc


def classify_masks(rgb: np.ndarray, dominance: int, min_value: int) -> tuple[np.ndarray, np.ndarray]:
    hue, saturation, value = rgb_to_hsv_metrics(rgb)
    channels = rgb.astype(np.int16)
    red = channels[..., 0]
    green = channels[..., 1]
    blue = channels[..., 2]

    bright_enough = value >= (min_value / 255.0)

    sea_mask = (
        ((blue - np.maximum(red, green)) >= dominance)
        | (((hue >= 150.0) & (hue <= 260.0)) & (saturation >= 0.15))
    ) & bright_enough

    land_mask = (
        ((green - np.maximum(red, blue)) >= dominance)
        | (((hue >= 60.0) & (hue <= 170.0)) & (saturation >= 0.15))
    ) & bright_enough

    # Keep the classes exclusive.
    land_mask &= ~sea_mask
    return land_mask, sea_mask


def clean_mask(mask: np.ndarray, smoothing: int, min_pixels: int) -> np.ndarray:
    result = mask.astype(bool)

    if smoothing > 1:
        structure = np.ones((smoothing, smoothing), dtype=bool)
        result = ndimage.binary_closing(result, structure=structure)
        result = ndimage.binary_opening(result, structure=structure)

    result = ndimage.binary_fill_holes(result)

    labels, count = ndimage.label(result)
    if count and min_pixels > 1:
        sizes = ndimage.sum(result, labels, index=np.arange(1, count + 1))
        keep = np.zeros(count + 1, dtype=bool)
        keep[1:] = sizes >= min_pixels
        result = keep[labels]

    return result.astype(bool)


def mask_to_rectangles(mask: np.ndarray) -> list:
    rectangles = []
    for y, row in enumerate(mask):
        xs = np.flatnonzero(row)
        if xs.size == 0:
            continue

        breaks = np.where(np.diff(xs) > 1)[0]
        starts = np.r_[xs[0], xs[breaks + 1]]
        ends = np.r_[xs[breaks], xs[-1]]

        for start, end in zip(starts, ends, strict=False):
            rectangles.append(box(float(start), float(y), float(end + 1), float(y + 1)))

    return rectangles


def flatten_polygons(geometry) -> list[Polygon]:
    if geometry.is_empty:
        return []
    if geometry.geom_type == "Polygon":
        return [geometry]
    if hasattr(geometry, "geoms"):
        polygons = []
        for item in geometry.geoms:
            polygons.extend(flatten_polygons(item))
        return polygons
    return []


def extract_polygons(mask: np.ndarray, simplify: float, min_area: float) -> list[Polygon]:
    rectangles = mask_to_rectangles(mask)
    if not rectangles:
        return []

    merged = unary_union(rectangles)
    polygons = []

    for polygon in flatten_polygons(merged):
        geom = polygon.buffer(0)
        if geom.is_empty:
            continue

        if simplify > 0:
            geom = geom.simplify(simplify, preserve_topology=True)

        for item in flatten_polygons(geom):
            if item.area >= min_area and len(item.exterior.coords) >= 4:
                polygons.append(item)

    polygons.sort(key=lambda item: item.area, reverse=True)
    return polygons


def reduce_polygon_points(polygon: Polygon, max_points: int) -> Polygon:
    if max_points < 3:
        raise ValueError("max_points must be at least 3.")

    def sample_coords(points: list[tuple[float, float]], limit: int) -> list[tuple[float, float]]:
        indexes = np.linspace(0, len(points) - 1, num=limit, dtype=int)
        sampled = []
        for index in indexes:
            point = points[int(index)]
            if not sampled or point != sampled[-1]:
                sampled.append(point)
        return sampled

    def ensure_limit(geom: Polygon) -> Polygon:
        points = list(geom.exterior.coords)[:-1]
        if len(points) <= max_points:
            return geom

        sampled_points = sample_coords(points, max_points)
        if len(sampled_points) < 3:
            return geom.convex_hull

        simplified = Polygon(sampled_points).buffer(0)
        candidates = flatten_polygons(simplified)
        if candidates:
            return max(candidates, key=lambda item: item.area)
        return geom.convex_hull

    coords = list(polygon.exterior.coords)[:-1]
    if len(coords) <= max_points:
        return polygon

    minx, miny, maxx, maxy = polygon.bounds
    span = max(maxx - minx, maxy - miny, 1.0)

    for factor in (0.001, 0.002, 0.004, 0.008, 0.016, 0.032, 0.064):
        simplified = polygon.simplify(span * factor, preserve_topology=True)
        candidates = flatten_polygons(simplified)
        if not candidates:
            continue

        candidate = ensure_limit(max(candidates, key=lambda item: item.area))
        candidate_coords = list(candidate.exterior.coords)[:-1]
        if 3 <= len(candidate_coords) <= max_points:
            return candidate

    sampled_polygon = ensure_limit(polygon)
    sampled_coords = list(sampled_polygon.exterior.coords)[:-1]
    if 3 <= len(sampled_coords) <= max_points:
        return sampled_polygon

    hull = ensure_limit(polygon.convex_hull)
    return hull


def apply_level_of_detail(polygons: list[Polygon], max_polygons: int, max_points: int) -> list[Polygon]:
    limited = []
    for polygon in polygons[:max_polygons]:
        lod_polygon = reduce_polygon_points(polygon, max_points)
        if not lod_polygon.is_empty and lod_polygon.area > 0:
            coords = list(lod_polygon.exterior.coords)
            if len(coords) >= 4:
                limited.append(lod_polygon)

    return limited


def polygon_to_path(
    polygon: Polygon,
    input_size: tuple[int, int],
    output_size: tuple[int, int],
    invert_y: bool,
) -> str:
    src_w, src_h = input_size
    out_w, out_h = output_size
    scale_x = out_w / float(src_w)
    scale_y = out_h / float(src_h)

    coords = []
    for x, y in list(polygon.exterior.coords)[:-1]:
        mapped_x = x * scale_x
        mapped_y = y * scale_y
        if invert_y:
            mapped_y = out_h - mapped_y
        coords.append(f"{mapped_x:.2f},{mapped_y:.2f}")

    return " ".join(coords)


def initialise_database(db_path: Path, layer: LayerSpec, overwrite: bool) -> sqlite3.Connection:
    if overwrite and db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    conn.executescript(
        f"""
        CREATE TABLE IF NOT EXISTS configs (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(64) NULL,
            type VARCHAR(32) NULL,
            value VARCHAR(128) NULL
        );

        CREATE TABLE IF NOT EXISTS isohypses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(80) NULL,
            guid VARCHAR(48) NULL,
            key VARCHAR(16) NULL,
            type INTEGER NULL,
            path TEXT NULL,
            {layer.z_field} REAL NULL,
            color VARCHAR(16) NULL,
            visible BOOLEAN NULL
        );
        """
    )

    conn.execute("DELETE FROM configs")
    conn.execute("DELETE FROM isohypses")
    conn.executemany(
        "INSERT INTO configs(name, type, value) VALUES (?, ?, ?)",
        [
            ("map.scale.x", "display.configuration", "1.0"),
            ("map.scale.y", "display.configuration", "1.0"),
        ],
    )
    conn.commit()
    return conn


def write_layer(
    out_dir: Path,
    layer: LayerSpec,
    polygons: Iterable[Polygon],
    input_size: tuple[int, int],
    output_size: tuple[int, int],
    invert_y: bool,
    overwrite: bool,
) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_dir = out_dir / "csv"
    csv_dir.mkdir(exist_ok=True)

    conn = initialise_database(out_dir / f"{layer.name}.s3db", layer, overwrite)
    count = 0

    with conn:
        for index, polygon in enumerate(polygons, start=1):
            path = polygon_to_path(polygon, input_size, output_size, invert_y)
            if not path:
                continue

            name = f"{layer.name.title()}.{index}"
            guid = str(uuid.uuid4())
            conn.execute(
                f"""
                INSERT INTO isohypses(name, guid, key, type, path, {layer.z_field}, color, visible)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (name, guid, "", layer.type_code, path, layer.z_value, layer.color, "Y"),
            )

            (csv_dir / f"{layer.name.lower()}-{index}.csv").write_text(path, encoding="utf-8")
            count += 1

    conn.close()
    return count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate land/sea polygons from a PNG map.")
    parser.add_argument("--input", required=True, help="Path to the source PNG image.")
    parser.add_argument("--output", required=True, help="Directory where land.s3db and sea.s3db will be written.")
    parser.add_argument(
        "--fit",
        type=parse_size,
        default=None,
        help="Optional output size as WIDTHxHEIGHT. Defaults to the PNG size.",
    )
    parser.add_argument(
        "--min-pixels",
        type=int,
        default=32,
        help="Discard connected regions smaller than this many pixels.",
    )
    parser.add_argument(
        "--min-area",
        type=float,
        default=25.0,
        help="Discard polygons smaller than this area after conversion.",
    )
    parser.add_argument(
        "--simplify",
        type=float,
        default=1.5,
        help="Simplification tolerance for the polygon boundary.",
    )
    parser.add_argument(
        "--dominance",
        type=int,
        default=12,
        help="How much stronger the green/blue channel must be than the others.",
    )
    parser.add_argument(
        "--min-value",
        type=int,
        default=24,
        help="Ignore very dark pixels below this brightness value.",
    )
    parser.add_argument(
        "--smoothing",
        type=int,
        default=3,
        help="Morphological smoothing kernel size in pixels.",
    )
    parser.add_argument(
        "--invert-y",
        action="store_true",
        help="Invert the y-axis so the origin becomes bottom-left instead of top-left.",
    )
    parser.add_argument(
        "--land-height",
        type=float,
        default=0.0,
        help="Height value written to generated land polygons.",
    )
    parser.add_argument(
        "--sea-depth",
        type=float,
        default=0.0,
        help="Depth value written to generated sea polygons.",
    )
    parser.add_argument(
        "--max-polygons",
        type=int,
        default=15,
        help="Maximum number of polygons to keep per layer.",
    )
    parser.add_argument(
        "--max-points",
        type=int,
        default=20,
        help="Maximum number of points per polygon.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Delete any existing output databases before writing.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)

    image = Image.open(input_path).convert("RGB")
    rgb = np.asarray(image)
    input_size = (image.width, image.height)
    output_size = args.fit or input_size

    land_mask, sea_mask = classify_masks(rgb, args.dominance, args.min_value)
    land_mask = clean_mask(land_mask, args.smoothing, args.min_pixels)
    sea_mask = clean_mask(sea_mask, args.smoothing, args.min_pixels)

    land_polygons = apply_level_of_detail(
        extract_polygons(land_mask, args.simplify, args.min_area),
        args.max_polygons,
        args.max_points,
    )
    sea_polygons = apply_level_of_detail(
        extract_polygons(sea_mask, args.simplify, args.min_area),
        args.max_polygons,
        args.max_points,
    )

    land_layer = LayerSpec(LAND.name, LAND.color, LAND.type_code, LAND.z_field, args.land_height)
    sea_layer = LayerSpec(SEA.name, SEA.color, SEA.type_code, SEA.z_field, args.sea_depth)

    land_count = write_layer(
        output_dir,
        land_layer,
        land_polygons,
        input_size,
        output_size,
        args.invert_y,
        args.overwrite,
    )
    sea_count = write_layer(
        output_dir,
        sea_layer,
        sea_polygons,
        input_size,
        output_size,
        args.invert_y,
        args.overwrite,
    )

    print(f"Input image     : {input_path}")
    print(f"Output directory: {output_dir}")
    print(f"Canvas size     : {input_size[0]}x{input_size[1]} -> {output_size[0]}x{output_size[1]}")
    print(f"LOD limit       : {args.max_polygons} polygons/layer, {args.max_points} points/polygon")
    print(f"Land polygons   : {land_count}")
    print(f"Sea polygons    : {sea_count}")
    print("Generates       : land.s3db, sea.s3db, and csv/*.csv")
    return 0


if __name__ == "__main__":
    main()
