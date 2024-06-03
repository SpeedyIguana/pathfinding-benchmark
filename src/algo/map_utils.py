from enum import Enum
from typing import Dict, List, Self, Set, Tuple


class Block(Enum):
    GRASS = 1
    WATER = 2
    LAVA = 4


class Grid_Map:
    def __init__(
        self: Self,
        name: str,
        arr: List[List[Block]],
        starts: Set[Tuple[int, int]],
        goals: Set[Tuple[int, int]],
        width: int,
        height: int,
    ):
        self._name = name
        self._arr = arr
        self._starts = starts
        self._goals = goals
        self._width: int = width
        self._height: int = height

    def get_block_at(
        self: Self,
        x: int,
        y: int,
    ) -> Block:
        try:
            return self._arr[y][x]
        except IndexError as e:
            raise Exception(
                f"Error in trying to access a block outside of the map:{self._name} at position {(x, y)=}"
            )

    def get_starts(
        self: Self,
    ) -> Set[Tuple[int, int]]:
        return self._starts

    def get_goals(
        self: Self,
    ) -> Set[Tuple[int, int]]:
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
):
    if tuple((source, destination)) not in movement_costs:
        raise ValueError("Invalid movement attempted")
    return movement_costs[tuple((source, destination))]


class Move(Enum):
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
    mapp: Grid_Map,
    pos: Tuple[int, int],
    move: Move,
) -> Tuple[bool, Tuple[int, int]]:
    if not isinstance(move, Move):
        raise ValueError("`move` must be of type `Move`")
    if not move in moveset:
        raise Exception(f"Move {move} does not have movement implemented")
    x, y = tuple([sum(x) for x in zip(list(pos), moveset.get(move))])
    out_of_bounds: bool = (
        (x < 0) or (y < 0) or (x > mapp._width - 1) or (y > mapp._height - 1)
    )
    return not out_of_bounds, (x, y)


def is_path_valid(
    mapp: Grid_Map,
    selected_path: List[Tuple[int, int]],
) -> bool:
    raise NotImplementedError


def cost_between_posA_posB(
    mapp: Grid_Map,
    pos_A: Tuple[int, int],
    pos_B: Tuple[int, int],
) -> int:
    block_A = mapp.get_block_at(pos_A[0], pos_A[1])
    block_B = mapp.get_block_at(pos_B[0], pos_B[1])
    return get_movement_cost(block_A, block_B)
