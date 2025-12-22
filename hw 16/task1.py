from typing import TypeVar

T = TypeVar("T", int, bool, float)


class Negator:
    @staticmethod
    def neg(arg: T) -> T:
        if isinstance(arg, bool):
            return not arg
        elif isinstance(arg, (int, float)):
            return -arg
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")


def main() -> None:
    a: int = Negator.neg(555)
    b: float = Negator.neg(-.228)
    c: bool = Negator.neg(True)

    print(a, b, c)


if __name__ == "__main__":
    main()
