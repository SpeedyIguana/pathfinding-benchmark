"""
This module contains all of the heuristics
that could possibly be used by the different algorithms
"""

from typing import Tuple


def bird_path(
    strt: Tuple[int, int],
    end: Tuple[int, int],
) -> float:
    """As the crow flies

    Args:
        strt (Tuple[int, int]): start coordinate
        end (Tuple[int, int]): end coordinate

    Returns:
        float: straight line length
            between the start and end position
    """
    return (((strt[0] - end[0]) ** 2) + ((strt[1] - end[1]) ** 2)) ** 0.5
