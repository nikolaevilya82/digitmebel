from cutting_plates import Detail, preparing_details
from typing import List
from random import randint


def generator_details(quantity: int, ) -> List[Detail]:
    """
    Генерирует список случайных деталей для тестирования.

    Создает заданное количество деталей со случайными параметрами:
    - Длина: случайное значение
    - Ширина: случайное значение (узкий диапазон для тестирования группировки)
    - Возможность поворота: случайное булево значение
    Returns:
        List[Detail]: Список сгенерированных объектов Detail
    """
    details_list = []
    for i_num in range(quantity):
        i_detail = Detail(
            part_id=(i_num + 1),
            length=randint(50, 2700),
            width=randint(1000, 1002),
            rotation=bool(randint(0, 1))
        )
        details_list.append(i_detail)
    return details_list


if __name__ == '__main__':
    for i_elem in preparing_details(generator_details(10)):
        print(i_elem)