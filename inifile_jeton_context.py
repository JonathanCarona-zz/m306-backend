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
    
    def get_jeton(user_id: str) -> Jeton:
        database.read(database_ini)
        jeton_amount = int(database[user_id]['jeton_amount'])
        return Jeton(user_id, jeton_amount)
    
    def get_jeton_factor() -> float:
        config.read(config_ini)
        return float(config['jeton']['factor'])

    def post_jeton(user_id: str, jeton_amount: int) -> Jeton:
        database.read(database_ini)

        database.add_section(user_id)
        database.set(
            user_id, 
            "jeton_amount", str(jeton_amount)
        )

        cfgfile = open(database_ini, 'w')
        database.write(cfgfile)
        cfgfile.close()

        database.read(database_ini)
        new_jeton_amount = int(database[user_id]['jeton_amount'])

        return Jeton(user_id, new_jeton_amount)