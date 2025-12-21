from abc import ABC, abstractmethod
from typing import Literal

type MoodType = Literal["neutral", "strict", "kind"] | str


class Human(ABC):
    def __init__(self, mood: MoodType = "neutral") -> None:
        self.mood: MoodType = mood

    @abstractmethod
    def greet(self) -> str:
        pass


class Father(Human):
    def greet(self) -> str:
        return "Hello!"

    def be_strict(self) -> None:
        self.mood = "strict"


class Mother(Human):
    def greet(self) -> str:
        return "Hi, honey!"

    def be_kind(self) -> None:
        self.mood = "kind"


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass


def main() -> None:
    father = Father()
    mother = Mother()
    daughter = Daughter()
    son = Son()

    print(f"\nFather: {father.greet()}, mood: {father.mood}")
    father.be_strict()
    print(f"mood: {father.mood}")

    print(f"\nMother: {mother.greet()}, mood: {mother.mood}")
    mother.be_kind()
    print(f"mood: {mother.mood}")

    print(f"\nDaughter: {daughter.greet()}, mood: {daughter.mood}")
    daughter.be_kind()
    print(f"mood: {daughter.mood}")
    daughter.be_strict()
    print(f"mood: {daughter.mood}")

    print(f"\nSon: {son.greet()}, mood: {son.mood}")
    son.be_kind()
    print(f"mood: {son.mood}")
    son.be_strict()
    print(f"mood: {son.mood}")

    print(f"\nDaughter: {[cls.__name__ for cls in Daughter.__mro__]}")
    print(f"Son: {[cls.__name__ for cls in Son.__mro__]}")


if __name__ == "__main__":
    main()
