from typing import Protocol


class HaveBalance(Protocol):
    """Протокол для объектов, которые имеют атрибут: баланс и метод: депозит.
    Таким образом, мы можем пополнить не только другой банковский счет, но и любой другой объект, который можно пополнить.
    Утиная типизация
    """

    __balance: int

    def deposit(self, amount: int) -> None: ...


class BankAccount:
    def __init__(self, balance: int = 0) -> None:
        self.__balance: int = balance

    def get_balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Нельзя внести отрицательную сумму")

    def withdraw(self, amount: int) -> None:
        if amount > self.__balance:
            raise ValueError("На счете недостаточно средств")
        elif amount <= 0:
            raise ValueError("Нельзя снять отрицательную сумму")
        self.__balance -= amount

    def transfer(self, other: HaveBalance, amount: int) -> None:
        if amount > self.__balance:
            raise ValueError("На счете недостаточно средств")
        elif amount <= 0:
            raise ValueError("Нельзя перевести отрицательную сумму")
        self.withdraw(amount)
        other.deposit(amount)


def main() -> None:
    account1 = BankAccount(1000)
    account2 = BankAccount(500)

    print(f"Баланс счета 1: {account1.get_balance()}")
    print(f"Баланс счета 2: {account2.get_balance()}")

    account1.transfer(account2, 300)

    print("После перевода 300 со счета 1 на счет 2:")
    print(f"Баланс счета 1: {account1.get_balance()}")
    print(f"Баланс счета 2: {account2.get_balance()}")


if __name__ == "__main__":
    main()
