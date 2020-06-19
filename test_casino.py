import os
import unittest
import json

from app import app

class CasinoTestCase(unittest.TestCase):
    """This class represents the casino test case"""

    def setUp(self):
        self.app = app
        self.client = app.test_client

        self.new_jeton = {
            'user_id': 'lkajsfu483ijz6932kj12fasjl4',
            'jeton_amount': 2000
        }

        self.patch_jeton = {
            'jeton_amount': 10000
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    
    # Correct test create_jeton() request
    def test_create_jeton(self):
        res = self.client().post('/jetons', json=self.new_jeton)
        self.assertEqual(res.status_code, 200)
    
    # Correct test get_jeton(asdf1234fdsa) endpoint for retrieving a jeton
    def test_get_jeton(self):
        res = self.client().get('/jetons/lkajsfu483ijz6932kj12fasjl4')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json['user_id'], 'lkajsfu483ijz6932kj12fasjl4')

    # Correct test patch_jeton(asdf1234fdsa) endpoint for retrieving a jeton
    def test_patch_jeton(self):
        res = self.client().patch('/jetons/lkajsfu483ijz6932kj12fasjl4', json=self.patch_jeton)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json['user_id'], 'lkajsfu483ijz6932kj12fasjl4')
        self.assertEqual(res.json['jeton_amount'], 10000)

    # Error test create_jeton() request
    def test_create_jeton_already_exists(self):
        res = self.client().post('/jetons', json=self.new_jeton)
        self.assertEqual(res.status_code, 404)

    # Error test get_jeton() request
    def test_get_jeton_not_found(self):
        res = self.client().get('/jetons/qwertzuiop234567890')
        self.assertEqual(res.status_code, 404)

    # Error test create_jeton() internal server error
    def test_create_jeton_internal_server_error(self):
        res = self.client().post('/jetons/jetons', json={'question':'Hello'})
        self.assertEqual(res.status_code, 405)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()