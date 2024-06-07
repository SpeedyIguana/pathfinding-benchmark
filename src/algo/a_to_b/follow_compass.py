"""
Module contains simple compass follower
"""

from typing import Tuple, List
from algo.a_to_b.a_to_b_abstract import AToBWalker
from algo.result import Result
from utils.map_utils import GridMap


# pylint: disable=locally-disabled, too-few-public-methods
class CompassWalker(AToBWalker):
    """
    Here, the agent simply follows the compass.
    Until they reach their goal, assuming there are no walls
    in their path, the agent will simple try to go in the shortest
    path given their goal without optimizing for cost.
    """

    @staticmethod
    def calculate_path(
        mapp: GridMap,
        pos_start: Tuple[int, int],
        destination_pos: Tuple[int, int],
    ) -> Result:

        curr_pos = pos_start

        move_order = 0

        selected_path: List[Tuple[int, int]] = [
            curr_pos,
        ]

        number_of_comparisons: int = 0

        while curr_pos != destination_pos:

            diff = list(
                map(
                    lambda x: 1 if x > 0 else (0 if x == 0 else -1),
                    map(lambda x: x[0] - x[1], zip(destination_pos, curr_pos)),
                ),
            )

            new_pos = list(curr_pos)
            new_pos[move_order] += diff[move_order]
            move_order = (move_order + 1) % 2

            if diff[0] == 0 or diff[1] == 0:
                new_pos = tuple(map(sum, zip(curr_pos, diff)))

            selected_path.append(new_pos)
            curr_pos = tuple(new_pos)

        return Result(
            __name__,
            selected_path,
            number_of_comparisons,
        )
