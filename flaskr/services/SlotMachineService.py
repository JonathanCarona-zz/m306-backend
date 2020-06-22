from flask import Flask, request, abort, jsonify
from flaskr.helper.IniFileJetonContext import IniFileJetonContext

class SlotMachineService():
    def spin(user_id: str, bet: int, current_amount: int):
        if(IniFileJetonContext.get_jeton(user_id) != current_amount):
            abort(404)

        if(current_amount < bet):
            abort(404)



        return 0

    def evaluate_price(user_id: str, bet: int) -> int:

        return 0

