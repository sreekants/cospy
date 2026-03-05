"""
Predator-prey boid simulation (Python + pygame)
Single-file rewrite of the JS repo:
- Retains class names: Vector, Prey, Predator
- Retains helper concepts: turn(), drawTriangle(), drawLine()
- Toroidal wraparound world: bound(), boundedDist(), shortestBoundedPathTo()
- Hard-coded parameters in this file (CONFIG)
- Console application: run from terminal: python main.py
"""


import math
from typing import List, Tuple
from cos.math.geometry.Vector import Vector
from cos.behavior.swarm.Prey import Prey   
from cos.behavior.swarm.Predator import Predator
from cos.behavior.swarm.Swarm import Swarm
from Toroid import Toroid

from cos.behavior.swarm.Prey import Config as PreyConfig
from cos.behavior.swarm.Predator import Config as PredatorConfig

import pygame



# =========================
# Hard-coded parameters
# =========================
CONFIG = {
    "env": {
        "width": 900,
        "height": 600,
        "fps": 60,
        "bg": (255, 255, 255),
    },
    "prey": {
        "count": 25,
        "speed": 2.6,
        "maxTurnAngle": math.radians(9.0),   # per tick
        "minSeparation": 18.0,
        "minFlockDist": 55.0,
        "predatorSightDist": 160.0,
        "weights": {
            "cohesion": 0.70,
            "alignment": 0.90,
            "separation": 1.30,
            "flee": 2.50,
        },
        "triangle": {
            "length": 12,
            "width": 7,
        }
    },
    "predator": {
        "count": 2,
        "speed": 3.2,
        "maxTurnAngle": math.radians(8.0),
        "killDist": 10.0,
        "triangle": {
            "length": 16,
            "width": 10,
        }
    },
    "controls": {
        "enable_player_prey0": True,  # prey[0] is red and can be controlled
        "left_keys": (pygame.K_LEFT, pygame.K_a),
        "right_keys": (pygame.K_RIGHT, pygame.K_d),
    },
    "debug": {
        "draw_predator_target_line": True,
        "print_stats_every_n_frames": 120,
    }
}



def drawTriangle(
    surface: pygame.Surface,
    pos: Vector,
    vel: Vector,
    color: Tuple[int, int, int],
    length: float,
    width: float,
) -> None:
    """
    Draw a triangle representing agent heading.
    """
    heading = vel.heading()
    forward = Vector.from_angle(heading) * length
    left = Vector.from_angle(heading + math.pi * 0.75) * width
    right = Vector.from_angle(heading - math.pi * 0.75) * width

    p1 = (pos.x + forward.x, pos.y + forward.y)
    p2 = (pos.x + left.x, pos.y + left.y)
    p3 = (pos.x + right.x, pos.y + right.y)

    pygame.draw.polygon(surface, color, [p1, p2, p3])


def drawLine(
    surface: pygame.Surface,
    a: Vector,
    b: Vector,
    color: Tuple[int, int, int],
    width: int = 1,
) -> None:
    pygame.draw.line(surface, color, (a.x, a.y), (b.x, b.y), width)


def render( surface, groups, world, preyList, predatorList ):
    surface.fill(CONFIG["env"]["bg"])

    # Draw prey
    prey_tri = CONFIG["prey"]["triangle"]
    for i, p in enumerate(preyList):
        color = (255, 0, 0) if i == 0 else (0, 0, 0)
        drawTriangle(surface, p.pos, p.vel, color, prey_tri["length"], prey_tri["width"])

    # Draw predators + optional target line
    pred_tri = CONFIG["predator"]["triangle"]
    for pred in predatorList:
        drawTriangle(surface, pred.pos, pred.vel, (0, 0, 255), pred_tri["length"], pred_tri["width"])

        if pred.target_index is None:
            continue

        if CONFIG["debug"]["draw_predator_target_line"] and pred.target_index < len(preyList):
            # draw shortest bounded line: show line to the wrapped target position
            target = preyList[pred.target_index].pos
            disp = world.shortestBoundedPathTo(pred.pos, target)
            # end point in screen coordinates:
            end = pred.pos+disp
            drawLine(surface, pred.pos, end, (0, 0, 255), 1)

    return 

    for typename, cfg, actors, fn in groups:
        match typename:
            case 'prey':
                # Draw prey
                prey_tri = CONFIG["prey"]["triangle"]
                for i, p in enumerate(actors):
                    color = (255, 0, 0) if i == 0 else (0, 0, 0)
                    drawTriangle(surface, p.pos, p.vel, color, prey_tri["length"], prey_tri["width"])

            case 'predator':
                # Draw predators + optional target line
                pred_tri = CONFIG["predator"]["triangle"]
                for pred in actors:
                    drawTriangle(surface, pred.pos, pred.vel, (0, 0, 255), pred_tri["length"], pred_tri["width"])

                    if pred.target_index is None:
                        continue

                    if CONFIG["debug"]["draw_predator_target_line"] and pred.target_index < len(preyList):
                        # draw shortest bounded line: show line to the wrapped target position
                        target = preyList[pred.target_index].pos
                        disp = world.shortestBoundedPathTo(pred.pos, target)
                        # end point in screen coordinates:
                        end = pred.pos+disp
                        drawLine(surface, pred.pos, end, (0, 0, 255), 1)


def createSwarm(screen_vec):
    swarm = Swarm()

    preycfg = PreyConfig()
    predcfg = PredatorConfig()
    preyList = swarm.setPreys(preycfg, [Prey.create(preycfg.speed, screen_vec) for _ in range(preycfg.count)])
    predList = swarm.setPredators(predcfg, [Predator.create(predcfg.speed, screen_vec) for _ in range(predcfg.count)])
    return swarm, preyList, predList

def main() -> int:
    pygame.init()
    pygame.display.set_caption("Predator-Prey Boid Sim (Python)")

    width = CONFIG["env"]["width"]
    height = CONFIG["env"]["height"]
    fps = CONFIG["env"]["fps"]
    screen_vec = Vector(float(width), float(height))

    surface = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    swarm, preyList, predList = createSwarm(screen_vec)

    paused = False
    frame = 0

    print("Controls:")
    print("  Space: pause/unpause")
    print("  R: reset simulation")
    if CONFIG["controls"]["enable_player_prey0"]:
        print("  A/D or Left/Right: steer prey[0] (red)")
    print("  Esc / Close window: quit")
    print()

    while True:
        dt = clock.tick(fps)  # milliseconds since last frame (not used; JS was fixed-step)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return 0
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_r:
                    swarm, preyList, predList = createSwarm(screen_vec)

        world = Toroid(screen_vec)
        if not paused:
            swarm.move(world)

        render(surface, swarm.groups, world, preyList, predList)
        pygame.display.flip()

        frame += 1
        n = CONFIG["debug"]["print_stats_every_n_frames"]
        if n and frame % n == 0:
            print(f"[frame {frame}] prey={len(preyList)} predators={len(predList)} paused={paused}")

        # If all prey are dead, keep running but print once
        if len(preyList) == 0 and frame % (fps * 2) == 0:
            print("All prey eliminated. Press R to reset.")

    # unreachable
    # return 0


if __name__ == "__main__":
    raise SystemExit(main())