from typing import Self, List, Tuple


class Result:
    def __init__(
        self: Self,
        algo_name: str,
        selected_path: List[Tuple[int, int]],
        number_of_comparisons: int,
    ):
        self.algo_name = algo_name
        self.selected_path: List[Tuple[int, int]] = selected_path
        self.number_of_comparisons: int = number_of_comparisons
        self.time_taken: float = 0.0 # to be overwritten

