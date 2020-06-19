from __future__ import annotations
from typing import Optional
from flask import Flask, request, abort, jsonify
from inifile_jeton_context import IniFileJetonContext
from models import Jeton

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
    def get_jeton_by_user_id(user_id: str) -> Jeton:
        return IniFileJetonContext.get_jeton(user_id)

    def get_jeton_factor() -> float:
        return IniFileJetonContext.get_jeton_factor()
    
    def post_jeton(user_id: str, jeton_amount: int) -> Jeton:
        return IniFileJetonContext.post_jeton(user_id, jeton_amount)
