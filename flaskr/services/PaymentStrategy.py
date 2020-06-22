from __future__ import annotations
from abc import ABC, abstractmethod


class PaymentContext():
    def __init__(self, strategy: PaymentStrategy = None) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> PaymentStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def pay_with_method(self, paymentamount: float) -> bool:
        return self._strategy.run_checkout(paymentamount)


class PaymentStrategy(ABC):
    @abstractmethod
    def run_checkout(self, paymentamount: float):
        pass


class CreditcardPayment(PaymentStrategy):
    def run_checkout(self, paymentamount: float) -> bool:
        return True;


class TwintPayment(PaymentStrategy):
    def run_checkout(self, paymentamount: float) -> bool:
        return False
