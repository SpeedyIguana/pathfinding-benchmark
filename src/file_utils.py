from matplotlib import image as mpl_image
from typing import List
from algo.map_utils import Block, Grid_Map
import numpy as np


def map_load(
    file_path: str,
) -> Grid_Map:

    _blocks = (
        (
            np.array([0, 1, 0, 1], dtype="float32"),
            Block.GRASS,
        ),
        (
            np.array([0, 0, 1, 1], dtype="float32"),
            Block.WATER,
        ),
        (
            np.array([1, 0, 0, 1], dtype="float32"),
            Block.LAVA,
        ),
        # Assume agent and destination as grass
        (
            np.array([1, 1, 1, 1], dtype="float32"),
            Block.GRASS,
        ),
        (
            np.array([0, 0, 0, 1], dtype="float32"),
            Block.GRASS,
        ),
    )

    def map_block(arr):
        for t_arr, t_block in _blocks:
            if np.array_equal(arr, t_arr):
                return t_block
        raise Exception("Unexpected clr found: %s", arr)

    img = mpl_image.imread(
        file_path,
    ).tolist()

    starts = set()
    goals = set()

    for x in range(len(img)):
        for y in range(len(img[x])):
            if np.array_equal(
                np.array([0, 0, 0, 1], dtype="float32"),
                img[y][x],
            ):
                goals.add(tuple((x, y)))
            elif np.array_equal(
                np.array([1, 1, 1, 1], dtype="float32"),
                img[y][x],
            ):
                starts.add(tuple((x, y)))

    return Grid_Map(
        arr=[[map_block(clr_cell) for clr_cell in unit_row] for unit_row in img],
        starts=starts,
        goals=goals
    )
