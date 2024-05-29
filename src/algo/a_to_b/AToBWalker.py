from abc import ABC, abstractmethod
from typing import Tuple
from algo.map_utils import Grid_Map
from algo.result import Result


class AToBWalker(ABC):

    @staticmethod
    @abstractmethod
    def calculate_path(
        mapp: Grid_Map,
        start_pos: Tuple[int, int],
        destination_pos: Tuple[int, int],
    ) -> Result:
        """This function traverses through the map and find a path from the starting position to the desired ending position

        Args:
            mapp (Grid_Map): Grid of blocks
            start_pos (Tuple[int, int]): Starting position of the agent
            destination_pos (Tuple[int, int]): Desired ending position of the agent

        Returns:
            Result: This captures the necessary resulting information
        """
        ...
