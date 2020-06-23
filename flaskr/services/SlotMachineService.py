from flask import abort, jsonify
from flaskr.helper.IniFileJetonContext import IniFileJetonContext
import random

class SlotMachineService:
    def spin(self, user_id: str, bet: int, current_amount: int):
        if(current_amount < bet):
            abort(404)

        IniFileJetonContext.set_player_jeton(user_id, IniFileJetonContext.get_jeton(user_id).jeton_amount - bet)

        random_elements = [
            0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2
        ]

        slotmachine_result = [random.choice(random_elements), random.choice(random_elements), random.choice(random_elements)]
        profit = 0

        if (slotmachine_result[0] == 0 and slotmachine_result[1] == 0 and slotmachine_result[2] == 0):
            IniFileJetonContext.set_player_jeton(user_id, bet * 7 + IniFileJetonContext.get_jeton(user_id).jeton_amount)
            profit = bet * 7
        elif (slotmachine_result[0] == 1 and slotmachine_result[1] == 1 and slotmachine_result[2] == 1):
            IniFileJetonContext.set_player_jeton(user_id, bet * 5 + IniFileJetonContext.get_jeton(user_id).jeton_amount)
            profit = bet * 5
        elif (slotmachine_result[0] == 2 and slotmachine_result[1] == 2 and slotmachine_result[2] == 2):
            IniFileJetonContext.set_player_jeton(user_id, bet * 2 + IniFileJetonContext.get_jeton(user_id).jeton_amount)
            profit = bet * 2

        new_amount = IniFileJetonContext.get_jeton(user_id).jeton_amount


        return jsonify({
        'success': True,
        'slotmachine_result': slotmachine_result,
        'jeton_amount': new_amount,
        'profit': profit
    }), 200


