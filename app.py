import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from configparser import ConfigParser

from casino_singleton import CasinoSingleton

#user = config['1']['name']
#jetons = config['1']['jeton_ammount']
#print(user)
#print(jetons)

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app, resources={r"/*": {"origins": "*"}})
  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

# ROUTES
'''
GET /jetons/<id>
'''
@app.route('/jetons/<string:user_id>', methods=['GET'])
def get_jeton(user_id):
  try:
    jeton = CasinoSingleton.get_jeton_by_user_id(user_id)
    factor = CasinoSingleton.get_jeton_factor()
    return jsonify({
        'success': True,
        'jeton_amount': jeton.jeton_amount,
        'user_id': jeton.user_id,
        'factor': factor
    }), 200
  except Exception as e:
    print('ERROR', e)
    abort(404)


'''
POST /jetons
'''
@app.route('/jetons', methods=['POST'])
def post_jetons():
  try:
    body = request.get_json()
    if not ('user_id' in body and 'jeton_amount' in body):
      abort(422)

    return jsonify({
      'success': True,
    }), 200

  except Exception as e:
    print(e)
    abort(404)