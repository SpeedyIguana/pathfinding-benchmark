"""
Module contains the breadth first search algo implementation
"""

from typing import Tuple, List, Set
from queue import Queue
from collections import deque
from algo.a_to_b.a_to_b_abstract import AToBWalker
from algo.result import Result
from utils.map_utils import cost_between_points, GridMap, Move, get_new_position


class BFS(AToBWalker):
    """
    Here the Agen will use the BFS algorithm to find the most optimal path
    """

    @staticmethod
    def calculate_path(
        mapp: GridMap,
        pos_start: Tuple[int, int],
        destination_pos: Tuple[int, int],
    ) -> Result:

        if pos_start == destination_pos:
            raise ValueError(
                f"Start position {pos_start} should not be the same as the destination position."
            )

        number_of_comparisons: int = 0

        q = deque(maxlen=mapp.height * mapp.width)

        q.append(
            (
                [pos_start],
                set(),
                0.0,
            ),
        )

        while q:

            ob: Tuple[
                List[int, int],
                Set[Tuple[int, int]],
                float,
            ] = q.popleft()
            selected_path, visited, curr_cost = ob
            curr_pos: Tuple[int, int] = selected_path[-1]

            visited.add(curr_pos)

            if curr_pos == destination_pos:
                return Result(
                    __name__,
                    selected_path,
                    number_of_comparisons,
                )

            for mv in Move:
                t_valid, t_new_pos = get_new_position(mapp, curr_pos, mv)
                if not t_valid or t_new_pos in selected_path:
                    continue

                t_cost = cost_between_points(
                    mapp,
                    curr_pos,
                    t_new_pos,
                )

                q.append(
                    (
                        selected_path + [t_new_pos],
                        visited,
                        curr_cost + t_cost,
                    ),
                )

        raise SystemError("Failed to find path")
