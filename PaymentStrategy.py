from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class PaymentContext():
    def __init__(self, strategy: PaymentStrategy = None) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> PaymentStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def payWithMethod(self, paymentAmount: float) -> bool:
        return self._strategy.run_checkout(paymentAmount)


class PaymentStrategy(ABC):
    @abstractmethod
    def run_checkout(self, paymentAmount: float):
        pass


class CreditcardPayment(PaymentStrategy):
    def run_checkout(self, paymentAmount: float) -> bool:
        return True;


class AnotherPayment(PaymentStrategy):
    def run_checkout(self, paymentAmount: float) -> bool:
        return False
