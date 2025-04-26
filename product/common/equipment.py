class KitchenEquipment:
    def __init__(self, name=None, width=None, depth=None, height=None):
        self.name: str = name
        self.width: int = width
        self.depth: int = depth
        self.height: int = height


class Dishwasher(KitchenEquipment):
    def __init__(self, is_built_in, width, name):
        super().__init__(name=name, width=width, depth=None, height=None)
        self.is_built_in: bool = is_built_in


class Oven(KitchenEquipment):
    def __init__(self, width, height, name):
        super().__init__(name=name, width=width, depth=None, height=height)


class Cooktop(KitchenEquipment):
    def __init__(self, name, width, depth, number_hobs):
        super().__init__(name=name, width=width, depth=depth, height=None)
        self.number_hobs: int = number_hobs


class Hood(KitchenEquipment):
    def __init__(self, name, mounting_type, width, depth, height ):
        super().__init__(name=name, width=width, depth=depth, height=height)
        self.mounting_type: str = mounting_type


class Washer(KitchenEquipment):
    def __init__(self, name, is_built_in, width, depth, height ):
        super().__init__(name=name, width=width, depth=depth, height=height)
        self.mounting_type: bool = is_built_in


class Microwave(KitchenEquipment):
    def __init__(self, name, is_built_in, width, depth, height ):
        super().__init__(name=name, width=width, depth=depth, height=height)
        self.mounting_type: bool = is_built_in


class Fridge(KitchenEquipment):
    def __init__(self, name, is_built_in, width, depth, height ):
        super().__init__(name=name, width=width, depth=depth, height=height)
        self.mounting_type: bool = is_built_in