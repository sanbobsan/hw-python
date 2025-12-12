import abc


class Student(abc.ABC):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        group: str,
        avg_mark: int,
    ) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.group: str = group
        self.avg_mark: int = avg_mark

    @abc.abstractmethod
    def get_scholarship(self) -> int:
        pass


class Bachelor(Student):
    def get_scholarship(self) -> int:
        scholarship: int = (
            10000 if self.avg_mark == 5 else 5000 if self.avg_mark > 3 else 0
        )
        return scholarship


class Undergraduate(Student):
    def get_scholarship(self) -> int:
        scholarship: int = (
            15000 if self.avg_mark == 5 else 7500 if self.avg_mark > 3 else 0
        )
        return scholarship


def main() -> None:
    students: list[Student] = [
        Bachelor("Алексей", "Лебедев", "101", 5),
        Bachelor("Кирилл", "Волков", "102", 4),
        Bachelor("Петр", "Васильев", "101", 3),
        Bachelor("Дмитрий", "Кузнецов", "102", 2),
        Undergraduate("Алексей", "Смирнов", "201", 5),
        Undergraduate("Кирилл", "Волков", "202", 4),
        Undergraduate("Артем", "Лебедев", "202", 3),
        Undergraduate("Василий", "Синицын", "202", 2),
        Undergraduate("Алексей", "Лебедев", "201", 5),
    ]
    for student in students:
        print(
            f"{student.first_name} {student.last_name}: {student.get_scholarship()} руб."
        )


if __name__ == "__main__":
    main()
