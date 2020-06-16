import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import Jeton


class CasinoTestCase(unittest.TestCase):
    """This class represents the casino test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        self.new_jeton = {
            'userId': 'lkajsfu483ijz6932kj12fasjl4',
            'jeton_amount': 2000
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    
    # Correct test create_jeton() request
    def test_create_jeton(self):
        res = self.client().post('/jeton', json=self.new_jeton)
        self.assertEqual(res.status_code, 200)
    
    # Correct test get_jeton(lkajsfu483ijz6932kj12fasjl4) endpoint for retrieving a jeton
    def test_get_jeton(self):
        res = self.client().get('/jetons/asdf1234fdsa')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json['jeton_amount'], 204820)
        self.assertEqual(res.json['user_id'], 'asdf1234fdsa')

    # Error test get_jeton() request
    def test_get_jeton_not_found(self):
        res = self.client().get('/jetons/thisoneisnothere')
        self.assertEqual(res.status_code, 404)

    # Error test create_jeton() internal server error
    def test_create_jeton_internal_server_error(self):
        res = self.client().post('/jetons', json={'question':'Hello'})
        self.assertEqual(res.status_code, 500)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()