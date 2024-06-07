"""
Module contains the A star implementation
"""

from typing import Tuple, List, Set
from queue import PriorityQueue
from algo.a_to_b.a_to_b_abstract import AToBWalker
from algo.result import Result
from utils.map_utils import cost_between_points, GridMap, Move, get_new_position
from utils.heuristics import bird_path as heuristic


# pylint: disable=locally-disabled, too-few-public-methods
class AStar(AToBWalker):
    """
    Here the Agent will use the A Star
    path finding algorithm to find the most
    optimal path. It is a twist on Dijkstra's
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

        curr_pos: Tuple[int, int] = pos_start
        curr_cost: float = heuristic(curr_pos, destination_pos)
        pq: PriorityQueue = PriorityQueue()

        visited: Set[Tuple[int, int]] = set()

        for mv in Move:
            t_valid, t_new_pos = get_new_position(mapp, curr_pos, mv)
            if not t_valid:
                continue

            t_cost = cost_between_points(
                mapp,
                curr_pos,
                t_new_pos,
            )
            if t_new_pos not in visited:
                pq.put(
                    (
                        heuristic(t_new_pos, destination_pos) + curr_cost + t_cost,
                        (t_new_pos, [curr_pos]),
                    )
                )
                visited.add(t_new_pos)

        while not pq.empty():
            curr_cost, t_path = pq.get()
            curr_pos = t_path[0]
            selected_path: List[Tuple[int, int]] = t_path[1]

            if curr_pos == destination_pos:
                return Result(
                    __name__,
                    selected_path,
                    number_of_comparisons,
                )

            for mv in Move:
                t_valid, t_new_pos = get_new_position(mapp, curr_pos, mv)
                if not t_valid:
                    continue

                t_cost = cost_between_points(
                    mapp,
                    curr_pos,
                    t_new_pos,
                )
                if t_new_pos not in visited:
                    pq.put(
                        (
                            bird_path(t_new_pos, destination_pos) + curr_cost + t_cost,
                            (t_new_pos, selected_path + [curr_pos]),
                        )
                    )
                    visited.add(t_new_pos)

        raise SystemError("Failed to find path")
