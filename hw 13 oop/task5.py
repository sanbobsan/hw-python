from typing import Callable


class FoodInfo:
    def __init__(
        self, proteins: int | float, fats: int | float, carbohydrates: int | float
    ) -> None:
        self._proteins: int | float = proteins
        self._fats: int | float = fats
        self._carbohydrates: int | float = carbohydrates

    def __repr__(self) -> str:
        return f"FoodInfo(<{self._proteins}>, <{self._fats}>, <{self._carbohydrates}>)"

    def __add__(self, other: "FoodInfo") -> "FoodInfo":
        if not isinstance(other, FoodInfo):
            return NotImplemented
        return FoodInfo(
            self._proteins + other._proteins,
            self._fats + other._fats,
            self._carbohydrates + other._carbohydrates,
        )

    def _apply_math_operation(
        self,
        num: int | float,
        func: Callable[[int | float, int | float], int | float],
    ) -> "FoodInfo":
        if not isinstance(num, (int, float)):
            return NotImplemented
        return FoodInfo(
            func(self._proteins, num),
            func(self._fats, num),
            func(self._carbohydrates, num),
        )

    def __mul__(self, num: int | float) -> "FoodInfo":
        return self._apply_math_operation(num=num, func=lambda x, y: x * y)

    def __truediv__(self, num: int | float) -> "FoodInfo":
        return self._apply_math_operation(num=num, func=lambda x, y: x / y)

    def __floordiv__(self, num: int | float) -> "FoodInfo":
        return self._apply_math_operation(num=num, func=lambda x, y: x // y)


def main() -> None:
    food1 = FoodInfo(10, 20, 30)
    food2 = FoodInfo(30, 20, 100)
    print(food1, food2)
    print(food1 + food2)
    print(food1 * 20 / 5 // 2)


if __name__ == "__main__":
    main()
