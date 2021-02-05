import unittest 
import calculator

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculator.divide(75,5), 15)

    def test2(self):
        self.assertEqual(calculator.divide(14,4), 3.5)

if __name__== '__main__':
    unittest.main(verbosity=2)