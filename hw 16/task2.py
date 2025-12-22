from datetime import date


class BirthInfo:
    def __init__(
        self, birth_date: date | str | list[int] | tuple[int, int, int]
    ) -> None:
        try:
            if isinstance(birth_date, str):
                birth_date = date.fromisoformat(birth_date)
            elif isinstance(birth_date, (list, tuple)):
                birth_date = date(birth_date[0], birth_date[1], birth_date[2])
        except ValueError:
            raise ValueError("Некорректная дата")

        if not isinstance(birth_date, date):
            raise TypeError("Аргумент переданного типа не поддерживается")

        self.birth_date: date = birth_date

    @property
    def age(self) -> int:
        """Возвращает текущий возраст в годах"""
        today: date = date.today()
        age_years: int = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age_years -= 1
        return age_years

    def __repr__(self) -> str:
        return f"BirthInfo(birth_date={self.birth_date})"


def main() -> None:
    birthinfo1 = BirthInfo(date(2006, 9, 30))
    print(birthinfo1.birth_date, birthinfo1.age)

    birthinfo2 = BirthInfo("1990-05-15")
    print(birthinfo2.birth_date, birthinfo2.age)

    birthinfo3 = BirthInfo([2020, 12, 22])
    print(birthinfo3.birth_date, birthinfo3.age)

    birthinfo4 = BirthInfo(date(2024, 12, 23))
    print(birthinfo4.birth_date, birthinfo4.age)


if __name__ == "__main__":
    main()
