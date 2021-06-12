class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def total_mass(self, weight=40, thickness=15):
        return f"{self._length} m * {self._width} m * {weight} kg * {thickness} cm =" \
               f" {(self._length * self._width * weight * thickness) / 1000} t"


road_1 = Road(3000, 15)
print(road_1.total_mass())
