import unittest
from flaskr.services.SlotMachineService import SlotMachineService
from flaskr.app import app

class SlotMachineServiceTest(unittest.TestCase):
    def setUp(self):
        self.slotMachineService = SlotMachineService()
        self.app = app
        self.client = app.test_client

    def test_spin(self):
        request = {
            'user_id': "lkajsfu483ijz6932kj12fasjl4",
            'bet': 500,
            'jeton': 2000,
        }

        res = self.client().patch('/slotmachine/spin', json=request)
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
