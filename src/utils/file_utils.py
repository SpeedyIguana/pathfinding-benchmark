"""
Holds all the utils to open map files and output to map files
In the future, it should also hold outputting benchmarking graphs
"""

from typing import List, Tuple
import os

from matplotlib import image as mpl_image
from PIL import Image as pil_image
import numpy as np
from utils.map_utils import Block, GridMap

_blocks = (
    (
        [0, 1, 0, 1],
        Block.GRASS,
    ),
    (
        [0, 0, 1, 1],
        Block.WATER,
    ),
    (
        [1, 0, 0, 1],
        Block.LAVA,
    ),
    # Assume agent always starts and ends on grass
    (
        [1, 1, 1, 1],
        Block.GRASS,
    ),
    (
        [0, 0, 0, 1],
        Block.GRASS,
    ),
)


def map_load(
    file_path: str,
) -> GridMap:
    """opens a png map file to generate a map

    Args:
        file_path (str): file path of the png

    Returns:
        Grid_Map: the generated map
    """

    def map_block(arr):
        for t_arr, t_block in _blocks:
            if np.array_equal(arr, t_arr):
                return t_block
        raise ValueError(f"Unexpected clr found {arr} in map {file_path}")

    img_obj = mpl_image.imread(
        file_path,
    )
    img = img_obj.tolist()

    starts = set()
    goals = set()

    for y, col in enumerate(img):
        for x, cell in enumerate(col):
            if np.array_equal(
                np.array([0, 0, 0, 1], dtype="float32"),
                cell,
            ):
                goals.add(tuple((x, y)))
            elif np.array_equal(
                np.array([1, 1, 1, 1], dtype="float32"),
                cell,
            ):
                starts.add(tuple((x, y)))

    if len(starts) == 0 or len(goals) == 0:
        raise ValueError(f"Missing start or end positions in map {file_path}")

    return GridMap(
        name=file_path,
        arr=[[map_block(clr_cell) for clr_cell in unit_row] for unit_row in img],
        key_points=(starts, goals),
        shape=(img_obj.shape[1], img_obj.shape[0]),
    )


def output_image_to_file(
    map_name: str,
    algo_name: str,
    mapp: GridMap,
    selected_path: List[Tuple[int, int]],
    clr_path=np.array([186 / 255, 48 / 255, 206 / 255], dtype="float32"),
) -> None:
    """Takes a map and outputs to a png with the chosen path

    Args:
        map_name (str): helps with the outputted file name
        algo_name (str): helps with the outputted file name
        mapp (Grid_Map): helps with the outputted file name
        selected_path (List[Tuple[int, int]]): helps with the outputted file name
        clr_path (np.array, optional): helps with the outputted
          file name. Defaults to np.array([186 / 255, 48 / 255, 206 / 255], dtype="float32").

    Raises:
        Exception: if an unexpected block was found

    Returns:
        None
    """

    pos_start = selected_path[0]
    pos_end = selected_path[-1]

    def map_block_to_clr(block: Block):
        for t_arr, t_block in _blocks:
            if block == t_block:
                return t_arr[0:3]
        raise ValueError(f"Unexpected block found {block}")

    arr = list(map(lambda x: list(map(map_block_to_clr, x)), mapp.arr))

    for pos in selected_path:
        x, y = pos
        arr[y][x] = clr_path

    np_arr = np.array(arr, dtype="float32") * 255
    img = pil_image.fromarray(np_arr.astype(np.uint8), mode="RGB")

    save_name: str = os.path.join(
        "dist/",
        f"{os.path.splitext(map_name)[0]}"
        f"_{algo_name}_{pos_start}"
        f"_{pos_end}.png",
    )

    os.makedirs(
        os.path.join(
            os.path.split(save_name)[0],
        ),
        exist_ok=True,
    )
    img.save(save_name)
