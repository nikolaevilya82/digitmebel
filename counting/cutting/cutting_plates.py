from dataclasses import dataclass
from typing import List, Callable


@dataclass
class Detail:
    part_id: int
    length: int
    width: int
    rotation: bool

    @property
    def get_square(self):
        return self.length * self.width

    def rotate_detail(self):
        if self.rotation:
            self.length, self.width = self.width, self.length
            self.rotation = not self.rotation

    @property
    def get_max(self):
        return max(self.length, self.width)


def sort_parts_by_square(parts: List[Detail]) -> List[Detail]:
    parts_copy = parts.copy()
    return sorted(parts_copy, key=lambda detail: detail.get_square)