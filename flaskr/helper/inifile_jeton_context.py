from helper.IJetonContext import IJetonContext
from configparser import ConfigParser
from models.Jeton import Jeton

database_ini = "data/casino_bank.ini"
config_ini = "configuration/config.ini"

config = ConfigParser()
database = ConfigParser()

config.read(config_ini)
database.read(database_ini)

class IniFileJetonContext(IJetonContext):
    """
    Overwrite
    IJetonContext.get_jeton()
    """
    def get_jeton(user_id: str) -> Jeton:
        database.read(database_ini)
        jeton_amount = int(database[user_id]['jeton_amount'])
        return Jeton(user_id, jeton_amount)
    
    """
    Overwrite
    IJetonContext.get_jeton_factor()
    """
    def get_jeton_factor() -> float:
        config.read(config_ini)
        return float(config['jeton']['factor'])

    """
    Overwrite
    IJetonContext.post_jeton()
    """
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
    
    """
    Overwrite
    IJetonContext.set_player_jeton()
    """
    def set_player_jeton(user_id: str, amount_of_jeton: int) -> Jeton:
        database.read(database_ini)
        database.set(user_id, 'jeton_amount', str(amount_of_jeton))

        with open(database_ini, 'w') as configfile:
            database.write(configfile)
            configfile.close()
        
        new_jeton_amount = int(database[user_id]['jeton_amount'])

        return Jeton(user_id, new_jeton_amount)