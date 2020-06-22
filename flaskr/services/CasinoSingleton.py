from __future__ import annotations
from typing import Optional
from flaskr.helper.IniFileJetonContext import IniFileJetonContext
from flaskr.models.Jeton import Jeton
from flaskr.services.PaymentStrategy import PaymentContext, CreditcardPayment, TwintPayment


class CasinoSingletonMeta(type):

    _instance: Optional[CasinoSingleton] = None

    def __call__(self) -> CasinoSingleton:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class CasinoSingleton(metaclass=CasinoSingletonMeta):
    @classmethod
    def run_checkout(cls, paymentmethod: str, userid: str, payamount: float) -> bool:
        context = PaymentContext()
        if paymentmethod == "creditcard":
            context.strategy = CreditcardPayment()
        elif paymentmethod == "twint":
            context.strategy = TwintPayment()
        else:
            return False
        payment_successful = context.pay_with_method(payamount)

        if (payment_successful == True):
            jeton_amount = cls.get_jeton_by_user_id(userid).jeton_amount
            pay_amount_time_factor = payamount * cls.get_jeton_factor()
            cls.set_player_jeton(userid, int(jeton_amount + pay_amount_time_factor))
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