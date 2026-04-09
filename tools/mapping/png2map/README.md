# PNG to Map Polygon Generator

`png2map.py` converts a color-coded PNG into polygon layers for this repository's map format.

## Expected input

- **Green shades** → land
- **Blue shades** → sea

## Output

The script writes:

- `land.s3db`
- `sea.s3db`
- `csv/land-*.csv`
- `csv/sea-*.csv`

The SQLite files use the same `isohypses` schema already used by the existing map assets.

## Example

```bash
python tools/mapping/png2map/png2map.py \
  --input temp/map.png \
  --output temp/pngmap \
  --fit 1200x800 \
  --overwrite
```

## Useful options

- `--fit 1200x800` scale the output coordinates to a target canvas size
- `--simplify 2.0` reduce polygon detail
- `--min-pixels 50` ignore tiny specks/noise
- `--land-height 500 --sea-depth 5` set default height/depth values
- `--invert-y` switch to bottom-left origin

## Notes

- The generated polygons store the **outer boundary** of each region.
- Inner holes are not preserved in the `path` field because the current `isohypses` schema only stores a single polygon path per record.
- In practice this still works well for layered rendering where land is drawn over sea.
