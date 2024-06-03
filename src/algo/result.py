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
        # time_taken measured in ns
        self.time_taken: int = 0

