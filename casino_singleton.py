from __future__ import annotations
from typing import Optional
from inifile_jeton_context import IniFileJetonContext
from models import Jeton
from PaymentStrategy import PaymentContext, CreditcardPayment, TwintPayment

"""
The Singleton class can be implemented in different ways in Python. Some
possible methods include: base class, decorator, metaclass. We will use the
metaclass because it is best suited for this purpose.
"""
class CasinoSingletonMeta(type):

    _instance: Optional[CasinoSingleton] = None

    def __call__(self) -> CasinoSingleton:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class CasinoSingleton(metaclass=CasinoSingletonMeta):
    @classmethod
    def run_checkout(cls, paymentMethod: str, userId: str, payAmount: float) -> bool:
        context = PaymentContext()
        if (paymentMethod == "creditcard"):
            context.strategy = CreditcardPayment()
        elif (paymentMethod == "twint"):
            context.strategy = TwintPayment()
        else:
            return False
        paymentSuccessful = context.payWithMethod(payAmount)

        if (paymentSuccessful == True):
            cls.set_player_jeton(userId, int(cls.get_jeton_by_user_id(userId).jeton_amount + payAmount * cls.get_jeton_factor()))
        return True

    def get_jeton_by_user_id(user_id: str) -> Jeton:
        return IniFileJetonContext.get_jeton(user_id)

    @classmethod
    def get_jeton_factor(cls) -> float:
        return IniFileJetonContext.get_jeton_factor()
    
    def post_jeton(user_id: str, jeton_amount: int) -> Jeton:
        return IniFileJetonContext.post_jeton(user_id, jeton_amount)

    def set_player_jeton(user_id: str, amount_of_jeton: int) -> Jeton:
        return IniFileJetonContext.set_player_jeton(user_id, amount_of_jeton)