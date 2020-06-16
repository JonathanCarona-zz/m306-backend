import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser
import json

'''
Jeton
a persistent jeton entity, extends the base SQLAlchemy Model
'''
class Jeton():
    user_id = ''
    jeton_amount = 0

    def __init__(self, user_id, jeton_amount):
        self.user_id = user_id
        self.jeton_amount = jeton_amount