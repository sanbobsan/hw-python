class Counter:
    def __init__(self, start: int = 0) -> None:
        self._value: int = start

    @staticmethod
    def positive(value: int) -> int:
        if value < 0:
            return 0
        return value

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, new_value: int) -> None:
        self._value = Counter.positive(value=new_value)

    def inc(self, num: int = 1) -> None:
        self.value += num

    def dec(self, num: int = 1) -> None:
        self.value -= num


class NonDecCounter(Counter):
    def dec(self, num: int = 1) -> None:
        pass


class LimitedCounter(Counter):
    def __init__(self, start: int = 0, limit: int = 10) -> None:
        super().__init__(start)
        self._limit: int = limit

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, new_value: int) -> None:
        self._limit = self.positive(value=new_value)
        if self._limit < self._value:
            self._value = self._limit

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, new_value: int) -> None:
        if new_value > self._limit:
            self._value = self._limit
            return
        self._value = self.positive(value=new_value)


def main() -> None:
    c = Counter(start=5)
    print(c.value)
    c.inc(num=3)
    print(c.value)
    c.dec(num=10)
    print(c.value)
    print("-" * 30)

    ndc = NonDecCounter(start=10)
    print(ndc.value)
    ndc.dec(num=2000)
    print(ndc.value)
    print("-" * 30)

    lc = LimitedCounter(start=5, limit=20)
    print(lc.value, lc.limit)
    lc.inc(num=2)
    print(lc.value, lc.limit)
    lc.inc(num=200)
    print(lc.value, lc.limit)
    lc.limit = -777
    print(lc.value, lc.limit)
    lc.value = 5
    print(lc.value, lc.limit)


if __name__ == "__main__":
    main()
