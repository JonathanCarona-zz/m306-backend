from models import Jeton

class IJetonContext():

    def get_jeton(self, user_id: str) -> Jeton:
        """Get jeton from database"""
        pass
    
    def get_jeton_factor(self) -> float:
        """Get jeton factor from database"""
        pass

    def post_jeton(self, user_id: str, jeton_amount: int) -> Jeton:
        """Post jeton to database"""
        pass
