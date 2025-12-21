from abc import ABC, abstractmethod
from typing import Literal

type HorizontalType = Literal["a", "b", "c", "d", "e", "f", "g", "h"]


class ChessPiece(ABC):
    def __init__(
        self,
        horizontal: HorizontalType,
        vertical: int,
    ) -> None:
        if horizontal not in "abcdefgh" or vertical not in range(1, 9):
            raise ValueError("Некорректные координаты")
        self.horizontal: HorizontalType = horizontal
        self.vertical: int = vertical

    @abstractmethod
    def can_move(self, horizontal: HorizontalType, vertical: int) -> bool:
        pass


class King(ChessPiece):
    def can_move(self, horizontal: HorizontalType, vertical: int) -> bool:
        if horizontal not in "abcdefgh" or vertical not in range(1, 9):
            raise ValueError("Некорректные координаты")

        current_h: int = ord(self.horizontal) - ord("a")
        target_h: int = ord(horizontal) - ord("a")

        return abs(current_h - target_h) <= 1 and abs(self.vertical - vertical) <= 1


class Knight(ChessPiece):
    def can_move(self, horizontal: HorizontalType, vertical: int) -> bool:
        if horizontal not in "abcdefgh" or vertical not in range(1, 9):
            raise ValueError("Некорректные координаты")

        current_h: int = ord(self.horizontal) - ord("a")
        target_h: int = ord(horizontal) - ord("a")

        delta_h: int = abs(current_h - target_h)
        delta_v: int = abs(self.vertical - vertical)

        return (delta_h == 2 and delta_v == 1) or (delta_h == 1 and delta_v == 2)


def main() -> None:
    king = King("e", 4)
    print("Король на e4:")
    test_moves_king: list[tuple[HorizontalType, int]] = [
        ("e", 5),
        ("f", 4),
        ("f", 5),
        ("e", 6),
        ("g", 4),
    ]
    for h, v in test_moves_king:
        print(f"Может ли король пойти на {h}{v}? {king.can_move(h, v)}")

    knight = Knight("e", 4)
    print("Конь на e4:")
    test_moves_knight: list[tuple[HorizontalType, int]] = [
        ("f", 6),
        ("g", 5),
        ("g", 3),
        ("f", 2),
        ("c", 2),
        ("a", 3),
        ("b", 5),
        ("h", 6),
    ]
    for h, v in test_moves_knight:
        print(f"Может ли конь пойти на {h}{v}? {knight.can_move(h, v)}")


if __name__ == "__main__":
    main()
