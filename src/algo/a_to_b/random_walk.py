from algo.a_to_b.AToBWalker import AToBWalker
from abc import ABC, abstractmethod
from typing import Tuple
from algo.map_utils import Grid_Map
from algo.result import Result



class RandomWalk(AToBWalker):
    def calculate_path(
        mapp: Grid_Map,
        start_pos: Tuple[int, int],
        destination_pos: Tuple[int, int],
    ):
        raise NotImplementedError
