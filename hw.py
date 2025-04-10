def count_lens(words: list[str]) -> dict[int, int]:
    idx: int = 0
    counted: dict[int, int] = {}
    while idx < len(words):
        if len(words[idx]) in counted:
            counted[len(words[idx])] += 1
            idx += 1
        else:
            counted[len(words[idx])] = 1
            idx += 1
    return counted


print(count_lens(["a", "b", "cc", "d"]))


def count_lens_test() -> None:
    assert count_lens(["a", "bb", "ccc", "dddd"]) == {1: 1, 2: 1, 3: 1, 4: 1}


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_length(self) -> float:
        return (
            (self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2
        ) ** 0.5

    def get_slope(self) -> float:
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)
