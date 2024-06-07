"""
File should hold utilities to
manupilate a map while in memory
"""

from enum import Enum
from typing import Dict, List, Self, Set, Tuple


class Block(Enum):
    """
    Enum to show all available block types in a map
    """

    GRASS = 1
    WATER = 2
    LAVA = 4


class GridMap:
    """
    A class to hold memory for a generated map
    """

    def __init__(
        self: Self,
        name: str,
        arr: List[List[Block]],
        key_points: Tuple[Set[Tuple[int, int]], Set[Tuple[int, int]]],
        shape: Tuple[int, int],
    ):
        """_summary_

        Args:
            self (Self):
            name (str): Name for the map
            arr (List[List[Block]]): The grid for the map
            key_points (Tuple[Set[Tuple[int, int]], Set[Tuple[int, int]]]):
                (starts, goals)
            shape (Tuple[int, int]): (width, height)
        """
        self.name = name
        self.arr = arr
        self._starts, self._goals = key_points
        self.width: int = shape[0]
        self.height: int = shape[1]

    def get_block_at(
        self: Self,
        x: int,
        y: int,
    ) -> Block:
        """_summary_

        Args:
            self (Self):
            x (int): horizontal coordinate
            y (int): vertical coordinate

        Raises:
            IndexError: if trying to access inaccessible memory

        Returns:
            Block: the type of block at that location
        """
        try:
            return self.arr[y][x]
        except IndexError as iee:
            raise IndexError(
                f"Error in trying to access a block"
                f" outside of the map:{self.name} at position {(x, y)=}"
            ) from iee

    def get_starts(
        self: Self,
    ) -> Set[Tuple[int, int]]:
        """
        A getter for starts
        """
        return self._starts

    def get_goals(
        self: Self,
    ) -> Set[Tuple[int, int]]:
        """
        A getter for goals
        """
        return self._goals


movement_costs: Dict[Tuple[Block, Block], int] = {
    # From Grass
    (Block.GRASS, Block.GRASS): 1,
    (Block.GRASS, Block.WATER): 2,
    (Block.GRASS, Block.LAVA): 30,
    # From Water
    (Block.WATER, Block.GRASS): 3,
    (Block.WATER, Block.WATER): 4,
    (Block.WATER, Block.LAVA): 20,
    # From Lava
    (Block.LAVA, Block.GRASS): 20,
    (Block.LAVA, Block.WATER): 10,
    (Block.LAVA, Block.LAVA): 1e3,
}


def get_movement_cost(
    source: Block,
    destination: Block,
) -> int | float:
    """Find the movement cost between two blocks

    Args:
        source (Block)
        destination (Block)

    Raises:
        ValueError: if not a block

    Returns:
        int|float: the cost of movement
    """
    if tuple((source, destination)) not in movement_costs:
        raise ValueError("Invalid movement attempted")
    return movement_costs[tuple((source, destination))]


class Move(Enum):
    """
    Holds possible moves
    """

    N = 1
    E = 2
    S = 4
    W = 8


moveset: Dict[Move, List[int]] = {
    Move.S: [0, 1],
    Move.N: [0, -1],
    Move.E: [1, 0],
    Move.W: [-1, 0],
}


def get_new_position(
    mapp: GridMap,
    pos: Tuple[int, int],
    move: Move,
) -> Tuple[bool, Tuple[int, int]]:
    """Finds the coordinate of movement when
    given a source and move

    Args:
        mapp (GridMap)
        pos (Tuple[int, int]): source
        move (Move)

    Raises:
        ValueError: if move is not of appropriate type
        NotImplementedError: if movement for
            said move is not implemented

    Returns:
        Tuple[bool, Tuple[int, int]]: _description_
    """
    if not isinstance(move, Move):
        raise ValueError("`move` must be of type `Move`")
    if not move in moveset:
        raise NotImplementedError(f"Move {move} does not have movement implemented")
    x, y = [sum(x) for x in zip(list(pos), moveset.get(move))]
    out_of_bounds: bool = (
        (x < 0) or (y < 0) or (x > mapp.width - 1) or (y > mapp.height - 1)
    )
    return not out_of_bounds, (x, y)


def is_path_valid(
    mapp: GridMap,
    start: Tuple[int, int],
    end: Tuple[int, int],
    selected_path: List[Tuple[int, int]],
) -> bool:
    """Takes in a map and a path and returns
        if the path taken is valid. It returns
        false if any positions are repeated
        and if the start and end do not match the
        selected path.

    Args:
        mapp (GridMap): the map
        start (Tuple[int, int]): start position
        end (Tuple[int, int]): end position
        selected_path (List[Tuple[int, int]]): the positions
            travelled

    Returns:
        bool
    """
    raise NotImplementedError


def cost_between_points(
    mapp: GridMap,
    pos_a: Tuple[int, int],
    pos_b: Tuple[int, int],
) -> int:
    """Given two positions, based on their blocks,
        a cost is calculated.

    Args:
        mapp (GridMap): the map
        pos_a (Tuple[int, int])
        pos_b (Tuple[int, int])

    Returns:
        int: the cost
    """
    block_a = mapp.get_block_at(pos_a[0], pos_a[1])
    block_b = mapp.get_block_at(pos_b[0], pos_b[1])
    return get_movement_cost(block_a, block_b)
