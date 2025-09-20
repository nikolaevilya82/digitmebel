from dataclasses import dataclass
from typing import List, Callable


@dataclass
class Detail:
    """Класс, представляющий деталь с геометрическими параметрами."""
    part_id: int
    length: int
    width: int
    rotation: bool

    @property
    def get_square(self):
        """Вычисляет площадь детали."""
        return self.length * self.width

    def rotate_detail(self):
        """
        Поворачивает деталь на 90 градусов, если разрешено rotation.

        Меняет местами длину и ширину, инвертирует флаг rotation.
        Действует только если rotation изначально True.
        """
        if self.rotation:
            self.length, self.width = self.width, self.length
            self.rotation = not self.rotation


def preparing_details(parts: List[Detail]) -> List[Detail]:
    """
    Подготавливает и сортирует детали для оптимальной компоновки.

    Алгоритм:
    1. Создает копию списка деталей и сортирует по убыванию площади
    2. Формирует блоки деталей с одинаковой шириной
    3. Обрабатывает поворотные детали для совмещения по ширине
    4. Возвращает отсортированный список деталей

    Args:
        parts (List[Detail]): Список деталей для обработки

    Returns:
        List[Detail]: Отсортированный и сгруппированный список деталей

    Note:
        Функция модифицирует оригинальные объекты деталей при повороте.
        Рекомендуется передавать копии объектов если нужны оригинальные данные
    """
    parts_copy = sorted(parts.copy(), key=lambda detail: detail.get_square, reverse=True)
    parts_sorted = []

    for i_detail in parts_copy:
        parts_block = []

        for j_detail in parts_copy[1:]:
            if i_detail.width == j_detail.width:
                parts_block.append(j_detail)
                parts_copy.remove(j_detail)
            elif j_detail.rotation:
                if j_detail.length == i_detail.width:
                    parts_block.append(j_detail.rotate_detail())

        parts_sorted += parts_block
    return parts_sorted


