from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class PaymentContext():
    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> PaymentStrategy:

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: PaymentStrategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def payWithMethod(self) -> None:
        return self._strategy.run_checkout()


class PaymentStrategy(ABC):
    @abstractmethod
    def run_checkout(self, data: List):
        pass


class CreditcardPayment(PaymentStrategy):
    def run_checkout(self) -> bool:
        return True;


class AnotherPayment(PaymentStrategy):
    def run_checkout(self) -> bool:
        return False


if __name__ == "__main__":
    context = PaymentContext(CreditcardPayment())
    print("Client: Strategy is set to normal sorting.")
    context.payWithMethod()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = AnotherPayment()
    context.payWithMethod()