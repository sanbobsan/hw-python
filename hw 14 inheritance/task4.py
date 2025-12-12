import abc
from math import pi, sqrt


class Shape(abc.ABC):
    @abc.abstractmethod
    def get_area(self) -> float: ...

    @abc.abstractmethod
    def get_volume(self) -> float: ...


"""
Можно сделать еще подклассы, которые будут основой для объемных фигур в виде фигур на плоскости,
например круг: для сферы, цилиндра и эллипсоида и прямоугольник для куба и параллелепипеда
"""


class Cube(Shape):
    def __init__(self, a: float) -> None:
        self.a: float = a

    def get_area(self) -> float:
        return 6 * self.a**2

    def get_volume(self) -> float:
        return self.a**3


class Sphere(Shape):
    def __init__(self, r: float) -> None:
        self.r: float = r

    def get_area(self) -> float:
        return 4 * pi * self.r**2

    def get_volume(self) -> float:
        return 4 / 3 * pi * self.r**3


class Cylinder(Shape):
    def __init__(self, r: float, h: float) -> None:
        self.r: float = r
        self.h: float = h

    def get_area(self) -> float:
        return 2 * pi * self.r * (self.r + self.h)

    def get_volume(self) -> float:
        return pi * self.r**2 * self.h


class Parallelepiped(Shape):
    def __init__(self, a, b, c) -> None:
        self.a: float = a
        self.b: float = b
        self.c: float = c

    def get_area(self) -> float:
        return 2 * (self.a * self.b + self.b * self.c + self.c * self.a)

    def get_volume(self) -> float:
        return self.a * self.b * self.c


class Ellipsoid(Shape):
    def __init__(self, a, b, c) -> None:
        self.a: float = a
        self.b: float = b
        self.c: float = c

    def get_area(self) -> float:
        return (
            4
            * pi
            * sqrt(
                (self.a**2 * self.b**2 + self.a**2 * self.c**2 + self.b**2 * self.c**2)
                / 3
            )
        )

    def get_volume(self) -> float:
        return 4 / 3 * pi * self.a * self.b * self.c


def volume_bigger_than_all_others_combined(shapes: list[Shape]) -> float:
    max: float = 0

    for shape in shapes:
        if max < shape.get_volume():
            max = shape.get_volume()

    return max


def main() -> None:
    cub = Cube(2.0)
    sph = Sphere(1.0)
    cyl = Cylinder(1.0, 2.0)
    prl = Parallelepiped(1.0, 2.0, 3.0)
    elp = Ellipsoid(1.0, 2.0, 3.0)

    print("=" * 32)
    print("Объемы фигур   | Объем | Площадь")
    print(f"Куб            |{cub.get_volume():<7.2f}| {cub.get_area():<.2f}")
    print(f"Сфера          |{sph.get_volume():<7.2f}| {sph.get_area():<.2f}")
    print(f"Цилиндр        |{cyl.get_volume():<7.2f}| {cyl.get_area():<.2f}")
    print(f"Параллелепипед |{prl.get_volume():<7.2f}| {prl.get_area():<.2f}")
    print(f"Эллипсоид      |{elp.get_volume():<7.2f}| {elp.get_area():<.2f}")
    print("=" * 32)

    shapes = [cub, sph, cyl, prl, elp]
    print(f"Наибольший объем: {volume_bigger_than_all_others_combined(shapes):.5f}")


if __name__ == "__main__":
    main()
