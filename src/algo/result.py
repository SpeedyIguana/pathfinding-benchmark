from typing import Self, List, Tuple


class Result:
    def __init__(
        self: Self,
        selected_path: List[Tuple[int, int]],
        number_of_comparisons: int,
    ):
        self.selected_path: List[Tuple[int, int]] = selected_path
        self.number_of_comparisons: int = number_of_comparisons

