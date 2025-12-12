class Product:
    def __init__(self, name: str, price: float, weight: float) -> None:
        self.__name: str = name
        self.__price: float = price
        self.__weight: float = weight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value) -> None:
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Цена не может быть отрицательной")

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, value) -> None:
        if value >= 0:
            self.__weight = value
        else:
            raise ValueError("Вес не может быть отрицательным")


class Buy(Product):
    def __init__(self, name: str, price: float, weight: float, amount: int) -> None:
        super().__init__(name, price, weight)
        self.__amount: int = amount

    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, value) -> None:
        if value >= 0:
            self.__amount = value
        else:
            raise ValueError("Количество не может быть отрицательным")

    def get_total_price(self) -> float:
        return self.price * self.amount

    def get_total_weight(self) -> float:
        return self.weight * self.amount


class Check(Buy):
    def __init__(self, name: str, price: float, weight: float, amount: int) -> None:
        super().__init__(name, price, weight, amount)

    def display(self) -> None:
        print("=" * 30)
        print("КАССОВЫЙ ЧЕК:")
        print("=" * 30)
        print(f"Название: {self.name}")
        print(f"Цена один товар: {self.price:.2f} руб")
        print(f"Вес одного товара: {self.weight:.2f} кг")
        print(f"Количество товара: {self.amount} шт")
        print("-" * 30)
        print(f"Общая стоимость: {self.get_total_price():.2f} руб")
        print(f"Общий вес: {self.get_total_weight():.2f} кг")
        print("=" * 30)


def main() -> None:
    apple = Product("Яблоки", 100.0, 0.2)
    apple.price = 120.0
    apple.weight = 0.25

    try:
        apple.price = -50
    except ValueError:
        pass

    milk_buy = Buy("Молоко", 79.9, 1.0, 3)
    milk_buy.amount = 5
    milk_buy.price = 89.99

    bread_check = Check("Хлеб", 45.5, 0.5, 2)
    bread_check.amount = 5
    bread_check.price = 55.2
    bread_check.name = "Хлеб бородинский"

    apple_check = Check(apple.name, apple.price, apple.weight, 4)
    milk_check = Check(milk_buy.name, milk_buy.price, milk_buy.weight, milk_buy.amount)

    products: list[Check] = [
        Check("Кофе", 350, 0.25, 1),
        bread_check,
        apple_check,
        milk_check,
    ]

    total_all_price = 0.0
    total_all_weight = 0.0

    print("=" * 30)
    for i, product in enumerate(products, 1):
        print(f"\tТовар {i}:")
        product.display()
        total_all_price += product.get_total_price()
        total_all_weight += product.get_total_weight()
        print()

    print("\n" + "=" * 30)
    print(f"Общая стоимость: {total_all_price:.2f} руб")
    print(f"Общий вес: {total_all_weight:.2f} кг")
    print("=" * 30)


if __name__ == "__main__":
    main()
