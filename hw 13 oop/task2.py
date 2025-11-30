class User:
    def __init__(self, name: str, age: int) -> None:
        self.__name: str = name
        self._age: int = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name or any(char.isdigit() for char in name):
            raise ValueError("Некорректное имя")
        self.__name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if 0 < age > 110 or not isinstance(age, int):
            raise ValueError("Некорректный возраст")
        self._age = age

    def __str__(self) -> str:
        return f"Имя: {self.__name}, Возраст: {self._age}"


def main() -> None:
    user = User("Марк", 25)
    print(user)

    user.name = "Марк Второй"
    user.age = 26
    print(user)

    try:
        user.age = -5
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
