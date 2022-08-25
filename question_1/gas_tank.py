class GasTank:
    def __init__(self, initial: int = 0):
        assert initial >= 0
        self._remaining = initial

    def fill(self, amount: int) -> None:
        assert amount >= 0
        self._remaining += amount

    def consume(self, amount: int) -> None:
        assert 0 <= amount <= self._remaining
        self._remaining -= amount

    def remaining(self) -> int:
        return self._remaining
