from typing import Self


class SampleObject:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> Self:
        self.value += 1

        return self

    def double(self) -> Self:
        self.value *= 2

        return self

    def add(self, n) -> Self:
        self.value += n

        return self
