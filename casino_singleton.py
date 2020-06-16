from __future__ import annotations
from typing import Optional
from flask import Flask, request, abort, jsonify
from configparser import ConfigParser
from models import Jeton

database_ini = "casino_bank.ini"
config_ini = "config.ini"

config = ConfigParser()
database = ConfigParser()

config.read(config_ini)
database.read(database_ini)

class CasinoSingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instance: Optional[CasinoSingleton] = None

    def __call__(self) -> CasinoSingleton:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class CasinoSingleton(metaclass=CasinoSingletonMeta):

    def get_jeton_by_user_id(user):
        jeton_amount = database[user]['jeton_amount']
        return Jeton(user, jeton_amount)

    def get_jeton_factor():
        return config['jeton']['factor']
    