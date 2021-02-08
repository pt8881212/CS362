import unittest 
import calculator

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculator.multiply(3,2), 6)

    def test2(self):
        self.assertEqual(calculator.multiply(4,1), 4)

if __name__== '__main__':
    unittest.main(verbosity=2)
