"""Minecraft automation module."""
from mcpi.minecraft import Minecraft
from mcpi import block
import math

mc = Minecraft.create()
mc.postToChat("Python is awesome!")


def build_square_tower(x_origin, y_origin, z_origin,
                       width, length, height,
                       block_type):
    """
    Build a square tower centered at origin coordinates x, z
    with dimensions width, length, height.
    """
    try:
        for y in range(y_origin, y_origin + height + 1):
            for x in range(x_origin - (width // 2),
                           x_origin + (width // 2) + 1 + (width % 2)):
                for z in range(z_origin - (length // 2),
                               z_origin + (length // 2) + 1 + (width % 2)):
                    mc.setBlock(x, y, z, block_type)
    except Exception as build_square_tower_Error:
        print("build_square_tower_Error:", build_square_tower_Error)


def build_square_pyramid(x_origin, y_origin, z_origin,
                         width, length,
                         block_type):
    """
    Build a square pyramid centered at origin coordinates x, z
    with provided dimensions width and length.
    """
    try:
        height = (width // 2) + (width % 2)
        for y in range(y_origin, y_origin + height + 1):
            for x in range(x_origin - (width // 2),
                           x_origin + (width // 2) + 1 + (width % 2)):
                for z in range(z_origin - (length // 2),
                               z_origin + (length // 2) + 1 + (width % 2)):
                    mc.setBlock(x, y, z, block_type)
            if width > 1:
                width -= 2
            if length > 1:
                length -= 2
    except Exception as build_square_tower_Error:
        print("build_square_pyramid_Error:", build_square_tower_Error)


def build_round_tower(x_origin, y_origin, z_origin,
                      diameter, height, block_type):
    """Build a round tower."""
    try:
        r = diameter // 2
        for y in range(y_origin, y_origin + height + 1):
            for x, z in circle_coordinates(x_origin, z_origin, r):
                mc.setBlock(x, y, z, block_type)
    except Exception as build_round_tower_Error:
        print("build_round_tower_Error:", build_round_tower_Error)


def circle_coordinates(x_origin, z_origin, radius):
    try:
        coords = []
        for deg in range(361):
            rad = (deg / 360) * 2 * math.pi
            x = int(radius * math.cos(rad)) + x_origin
            z = int(radius * math.sin(rad)) + z_origin
            coord = (x, z)
            if coord not in coords:
                coords.append(coord)
    except Exception as circle_coordinates_Error:
        print("circle_coordinates_Error:", circle_coordinates_Error)
    return coords


if __name__ == "__main__":
    try:
        x, y, z = mc.player.getPos()
        print("Position:", x, y, z)
        print("Build Position:", int(x), int(y), int(z))
        mc.player.setPos(int(x), int(y), int(z))
        # build_square_tower(int(x + 10), int(y), int(z + 10), 10, 10, 100, block.STONE.id)
        # build_square_pyramid(int(x + 10), int(y), int(z + 10), 10, 10, block.STONE.id)
        build_round_tower(int(x) + 10, int(y), int(z) + 10, 10, 10, block.STONE.id)
    except Exception as main_Error:
        print("Error:", main_Error)
