from interfaces import IJetonContext
from configparser import ConfigParser
from models import Jeton

database_ini = "casino_bank.ini"
config_ini = "config.ini"

config = ConfigParser()
database = ConfigParser()

config.read(config_ini)
database.read(database_ini)

class IniFileJetonContext(IJetonContext):
    
    def get_jeton(user_id) -> Jeton:
        jeton_amount = database[user_id]['jeton_amount']
        return Jeton(user_id, jeton_amount)
    
    def get_jeton_factor() -> float:
        return float(config['jeton']['factor'])
