from algo.a_to_b.AToBWalker import AToBWalker
from typing import Tuple, List, Set
from algo.map_utils import cost_between_posA_posB, Grid_Map, Move, get_new_position
from algo.result import Result
from queue import PriorityQueue


class Dijkstra(AToBWalker):
    """
    Here the Agent will use the Dijkstra's
    path finding algorithm to find the most
    optimal path.
    """

    def calculate_path(
        mapp: Grid_Map,
        pos_start: Tuple[int, int],
        destination_pos: Tuple[int, int],
    ) -> Result:

        if pos_start == destination_pos:
            raise Exception(
                f"Start position {pos_start} should not be the same as the destination position."
            )

        number_of_comparisons: int = 0

        curr_pos: Tuple[int, int] = pos_start
        curr_cost: float = 0.0
        pq: PriorityQueue = PriorityQueue()

        visited: Set[Tuple[int, int]] = set()

        for mv in Move:
            t_valid, t_new_pos = get_new_position(mapp=mapp, pos=curr_pos, move=mv)
            if not t_valid:
                continue

            t_cost = cost_between_posA_posB(
                mapp=mapp,
                pos_A=curr_pos,
                pos_B=t_new_pos,
            )
            if t_new_pos not in visited:
                pq.put(
                    (
                        curr_cost + t_cost,         # curr_cost
                        (t_new_pos, [curr_pos]),    # t_path
                    )
                )
                visited.add(t_new_pos)

        while not pq.empty():
            curr_cost, t_path = pq.get()
            curr_pos = t_path[0]
            selected_path: List[Tuple[int, int]] = t_path[1]

            if curr_pos == destination_pos:
                return Result(
                    algo_name=__name__,
                    selected_path=selected_path,
                    number_of_comparisons=number_of_comparisons,
                )

            for mv in Move:
                t_valid, t_new_pos = get_new_position(mapp=mapp, pos=curr_pos, move=mv)
                if not t_valid:
                    continue

                t_cost = cost_between_posA_posB(
                    mapp=mapp,
                    pos_A=curr_pos,
                    pos_B=t_new_pos,
                )
                if t_new_pos not in visited:
                    pq.put(
                        (
                            curr_cost + t_cost,
                            (t_new_pos, selected_path + [curr_pos]),
                        )
                    )
                    visited.add(t_new_pos)

        raise Exception("Failed to find path")
