class Jeton():
    user_id: str = ''
    jeton_amount: int = 0

    def __init__(self, user_id, jeton_amount):
        self.user_id = user_id
        self.jeton_amount = jeton_amount