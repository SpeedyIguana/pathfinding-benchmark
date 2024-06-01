from typing import Dict, List, Tuple

from algo.a_to_b.AToBWalker import AToBWalker
from algo.a_to_b.random_walk import RandomWalk
from algo.a_to_b.follow_compass import CompassWalker
from algo.map_utils import Grid_Map
from algo.result import Result
from file_utils import map_load, output_image_to_file


a_to_b_map_paths = [
    "maps/point_to_point/simple_obstacle_00.png",
    "maps/point_to_point/simple_obstacle_01.png",
]
a_to_b_maps: List[Grid_Map] = list(map(map_load, a_to_b_map_paths))
a_to_b_map_dict: Dict[str, Grid_Map] = dict(zip(a_to_b_map_paths, a_to_b_maps))

a_to_b_algos: List[AToBWalker] = [
    RandomWalk,
    CompassWalker,
]

results: Dict[Tuple[str, Tuple[int, int], Tuple[int, int]], Result] = dict()

for grid_map in a_to_b_maps:
    for algo in a_to_b_algos:
        for pos_end in grid_map.get_goals():
            for pos_start in grid_map.get_starts():
                results[tuple((grid_map._name, pos_start, pos_end))] = (
                    algo.calculate_path(
                        grid_map,
                        pos_start,
                        pos_end,
                    )
                )

for map_name, pos_start, pos_end in results.keys():
    ky = tuple((map_name, pos_start, pos_end))
    val: Result = results[ky]
    output_image_to_file(
        map_name=map_name,
        algo_name=val.algo_name,
        mapp=a_to_b_map_dict.get(map_name),
        selected_path=val.selected_path,
    )
