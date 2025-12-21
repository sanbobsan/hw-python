from abc import ABC, abstractmethod


class Date(ABC):
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year: int = year
        self.month: int = month
        self.day: int = day

    @abstractmethod
    def format(self) -> str:
        pass

    def iso_format(self) -> str:
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


class USADate(Date):
    def format(self) -> str:
        return f"{self.month:02d}-{self.day:02d}-{self.year}"


class ItalianDate(Date):
    def format(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year}"


def main() -> None:
    usa_date = USADate(2023, 1, 5)
    italian_date = ItalianDate(2023, 1, 5)

    print(f"USA   {usa_date.format()} \tISO  {usa_date.iso_format()}")
    print(f"Italy {italian_date.format()} \tISO  {usa_date.iso_format()}")


if __name__ == "__main__":
    main()
