import random
from algo.a_to_b.AToBWalker import AToBWalker
from abc import ABC, abstractmethod
from typing import Tuple, List
from algo.map_utils import Grid_Map, Move, get_new_position
from algo.result import Result


class RandomWalk(AToBWalker):
    """
    Random walk algorithm just chooses, at random,
    a valid move to make at every step until
    the agent reaches the final destination
    """

    def calculate_path(
        mapp: Grid_Map,
        start_pos: Tuple[int, int],
        destination_pos: Tuple[int, int],
    ) -> Result:
        moves: List[Move] = [x for x in Move]

        selected_path: List[Tuple[int, int]] = []
        selected_path.append(start_pos)

        curr_pos = start_pos

        number_of_comparisons: int = 0

        while curr_pos != destination_pos:
            number_of_comparisons += 1

            chosen_move: Move = random.choice(moves)

            t_valid, new_pos = get_new_position(
                mapp,
                curr_pos,
                chosen_move,
            )

            number_of_comparisons += 1
            if not t_valid:
                continue

            selected_path.append(new_pos)

            curr_pos = new_pos

        return Result(
            selected_path=selected_path,
            number_of_comparisons=number_of_comparisons,
        )
