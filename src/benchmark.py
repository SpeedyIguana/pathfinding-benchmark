import sys
from typing import List

from algo.a_to_b.AToBWalker import AToBWalker
from algo.a_to_b.random_walk import RandomWalk
from algo.map_utils import Grid_Map
from file_utils import map_load

a_to_b_maps = [
    "maps/point_to_point/simple_obstacle_00.png",
]

a_to_b_algos: List[AToBWalker] = [
    RandomWalk,
]

for file_path in a_to_b_maps:
    grid_map: Grid_Map = map_load(file_path)
    for algo in a_to_b_algos:
        for pos_end in grid_map.get_goals():
            for pos_start in grid_map.get_starts():
                algo.calculate_path(
                    grid_map,
                    pos_start,
                    pos_end,
                )
