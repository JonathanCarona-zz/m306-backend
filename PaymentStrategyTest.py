import unittest

from PaymentStrategy import PaymentContext, PaymentStrategy, AnotherPayment, CreditcardPayment

class PaymentStrategyTestCase(unittest.TestCase):
    """This class represents the payment strategy test case"""

    def setUp(self):
        self.context = PaymentContext(AnotherPayment)

    def test_creditcard_strategy(self):
        self.context.strategy = CreditcardPayment()
        self.assertTrue(self.context.payWithMethod())

    def test_anotherPayment_strategy(self):
        self.context.strategy = AnotherPayment()
        self.assertFalse(self.context.payWithMethod())



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()