"""
This module will hold the abstract class
"""

from abc import ABC, abstractmethod
from typing import Tuple
from utils.map_utils import GridMap
from algo.result import Result


# pylint: disable=locally-disabled, too-few-public-methods
class AToBWalker(ABC):
    """
    abstract class
    """
    @staticmethod
    @abstractmethod
    def calculate_path(
        mapp: GridMap,
        pos_start: Tuple[int, int],
        destination_pos: Tuple[int, int],
    ) -> Result:
        """This function traverses through the map and
            find a path from the starting position to the desired ending position

        Args:
            mapp (Grid_Map): Grid of blocks
            start_pos (Tuple[int, int]): Starting position of the agent
            destination_pos (Tuple[int, int]): Desired ending position of the agent

        Returns:
            Result: This captures the necessary resulting information
        """
