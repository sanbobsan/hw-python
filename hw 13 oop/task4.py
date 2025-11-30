from functools import total_ordering


@total_ordering
class Word:
    @staticmethod
    def validate_word(word: str) -> str:
        if not word.isalpha():
            raise ValueError
        return word

    def __init__(self, word: str) -> None:
        self._word: str = self.validate_word(word)

    def __str__(self) -> str:
        return self._word.capitalize()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Word):
            return NotImplemented
        return len(self._word) == len(other._word)

    def __gt__(self, other: "Word") -> bool:
        if not isinstance(other, Word):
            return NotImplemented
        return len(self._word) > len(other._word)


def main() -> None:
    word1 = Word("hello")
    word2 = Word("world")
    word3 = Word("hi")

    print(f"1 = {word1}   | 2 = {word2}  | 3 = {word3}")
    print(f"1 == 2 {word1 == word2} | 1 > 3 {word1 > word3} | 2 < 3 {word2 < word3}")


if __name__ == "__main__":
    main()
