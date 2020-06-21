import unittest

from PaymentStrategy import PaymentContext, PaymentStrategy, TwintPayment, CreditcardPayment

class PaymentStrategyTestCase(unittest.TestCase):
    """This class represents the payment strategy test case"""

    def setUp(self):
        self.context = PaymentContext(TwintPayment)

    def test_creditcard_strategy(self):
        self.context.strategy = CreditcardPayment()
        self.assertTrue(self.context.payWithMethod())

    def test_anotherPayment_strategy(self):
        self.context.strategy = TwintPayment()
        self.assertFalse(self.context.payWithMethod())



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()