class KitchenEquipment:
    def __init__(self, name=None, width=None, depth=None, height=None):
        self.name: str = name
        self.width: int = width
        self.depth: int = depth
        self.height: int = height


class Dishwasher(KitchenEquipment):
    def __init__(self, is_built_in, width, name=None):
        super().__init__(name=name, width=width, depth=None, height=None)
        self.is_built_in: bool = is_built_in


class Oven(KitchenEquipment):
    def __init__(self, width, height, name=None):
        super().__init__(name=name, width=width, depth=None, height=height)



