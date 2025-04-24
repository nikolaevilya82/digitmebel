class Drawer:
    def __init__(self, slide_model, depth, width, height, color):
        self.name: str = slide_model
        self.depth: int = depth
        self.width: int = width
        self.height: int = height
        self.color: str = color