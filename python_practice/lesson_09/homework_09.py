class Rhombus:
    def __init__(self, side_a, corner_a, corner_b = None):
        self.side_a = side_a
        self.corner_a = corner_a

    def __setattr__(self, name, value):
        if name == 'side_a':
            if value <= 0:
                raise ValueError(f"Для створення фігури 'ромб' довжина сторони повинна бути більшою за 0")

        elif name == 'corner_a':
            if not (0 < value < 180):
                print("Кут A повинен бути більше 0 але менше 180 градусів")
                return
            super().__setattr__('corner_b', 180 - value)

        elif name == 'corner_b':
            if not (0 < value < 180):
                print("Кут B повинен бути більше 0 але менше 180 градусів")
                return
            super().__setattr__('corner_a', 180 - value)

        super().__setattr__(name, value)


rhombus = Rhombus(1,4)

print(rhombus.side_a, rhombus.corner_a, rhombus.corner_b)
rhombus.corner_b = 34
print(rhombus.side_a, rhombus.corner_a, rhombus.corner_b)