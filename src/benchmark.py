"""
Module to benchmark all the algorithms
"""

from typing import Dict, List, Tuple
import time

# from algo.a_to_b.random_walk import RandomWalk # unreliable
from algo.a_to_b.a_to_b_abstract import AToBWalker
from algo.a_to_b.follow_compass import CompassWalker
from algo.a_to_b.dijkstra import Dijkstra
from algo.a_to_b.a_star import AStar
from algo.map_utils import GridMap
from algo.result import Result
from file_utils import map_load, output_image_to_file


a_to_b_map_paths = [
    "maps/point_to_point/simple_obstacle_00.png",
    "maps/point_to_point/simple_obstacle_01.png",
    "maps/point_to_point/abstract_maze_00.png",
]
a_to_b_maps: List[GridMap] = list(map(map_load, a_to_b_map_paths))
a_to_b_map_dict: Dict[str, GridMap] = dict(zip(a_to_b_map_paths, a_to_b_maps))

a_to_b_algos: List[AToBWalker] = [
    # RandomWalk, # unreliable
    CompassWalker,
    Dijkstra,
    AStar,
]

outcomes: List[
    Tuple[
        str,                # grid
        Tuple[int, int],    # pos_start
        Tuple[int, int],    # pos_end
        Result,             # res
    ]
] = []

time_start: int = 0
time_end: int = 0
res: Result = None

for GridMap in a_to_b_maps:
    for algo in a_to_b_algos:
        for pos_end in GridMap.get_goals():
            for pos_start in GridMap.get_starts():
                time_start = time.perf_counter_ns()
                res = algo.calculate_path(
                    GridMap,
                    pos_start,
                    pos_end,
                )
                time_end = time.perf_counter_ns()
                res.time_taken = time_end - time_start
                outcomes.append(
                    (
                        GridMap.name,
                        pos_start,
                        pos_end,
                        res,
                    )
                )

for map_name, pos_start, pos_end, resu in outcomes:
    output_image_to_file(
        map_name,
        resu.algo_name,
        a_to_b_map_dict.get(map_name),
        resu.selected_path,
    )
