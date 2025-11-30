from typing import Iterable


class IPAdress:
    @staticmethod
    def validate_ip(ip: str | Iterable[int]) -> str:
        if isinstance(ip, str):
            parts: list[str] = ip.split(".")
        else:
            parts = [str(part) for part in ip]
        if len(parts) != 4:
            raise ValueError
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                raise ValueError
        return ".".join(parts)

    def __init__(self, ip: str | Iterable[int]) -> None:
        self._ip: str = self.validate_ip(ip)

    @property
    def ip(self) -> str:
        return self._ip

    @ip.setter
    def ip(self, value: str) -> None:
        self._ip = self.validate_ip(value)

    def __str__(self) -> str:
        return self._ip

    def __repr__(self) -> str:
        return f"IPAdress('{self._ip}')"


def main() -> None:
    ip1 = IPAdress("123.123.123.123")
    print(ip1)
    ip2 = IPAdress([255, 255, 0, 0])
    print(repr(ip2))
    print([ip1, ip2])
    try:
        ip3 = IPAdress("256.100.50.25")
        ip3.ip = "999.999.999.999"
    except ValueError:
        print("Invalid")


if __name__ == "__main__":
    main()
