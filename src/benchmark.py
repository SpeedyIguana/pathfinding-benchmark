"""
Main runtime for benchmarking
"""

from typing import Dict, List, Tuple
import time

# from algo.a_to_b.random_walk import RandomWalk # unreliable
from algo.a_to_b.AToBWalker import AToBWalker
from algo.a_to_b.follow_compass import CompassWalker
from algo.a_to_b.dijkstra import Dijkstra
from algo.a_to_b.a_star import A_Star
from algo.map_utils import Grid_Map
from algo.result import Result
from file_utils import map_load, output_image_to_file


a_to_b_map_paths = [
    "maps/point_to_point/simple_obstacle_00.png",
    "maps/point_to_point/simple_obstacle_01.png",
    "maps/point_to_point/abstract_maze_00.png",
]
a_to_b_maps: List[Grid_Map] = list(map(map_load, a_to_b_map_paths))
a_to_b_map_dict: Dict[str, Grid_Map] = dict(zip(a_to_b_map_paths, a_to_b_maps))

a_to_b_algos: List[AToBWalker] = [
    # RandomWalk, # unreliable
    CompassWalker,
    Dijkstra,
    A_Star,
]

outcomes: List[
    Tuple[
        str,  # grid
        Tuple[int, int],  # pos_start
        Tuple[int, int],  # pos_end
        Result,  # res
    ]
] = []

time_start: int = 0
time_end: int = 0
res: Result = None

for grid_map in a_to_b_maps:
    for algo in a_to_b_algos:
        for pos_end in grid_map.get_goals():
            for pos_start in grid_map.get_starts():
                time_start = time.perf_counter_ns()
                res = algo.calculate_path(
                    grid_map,
                    pos_start,
                    pos_end,
                )
                time_end = time.perf_counter_ns()
                res.time_taken = time_end - time_start
                outcomes.append(
                    (
                        grid_map.name,
                        pos_start,
                        pos_end,
                        res,
                    )
                )

for map_name, pos_start, pos_end, resu in outcomes:
    output_image_to_file(
        map_name=map_name,
        algo_name=resu.algo_name,
        mapp=a_to_b_map_dict.get(map_name),
        selected_path=resu.selected_path,
    )
