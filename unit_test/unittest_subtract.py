import unittest 
import calculator

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculator.subtract(4,2), 2)

    def test2(self):
        self.assertEqual(calculator.subtract(8,2), 6)

if __name__== '__main__':
    unittest.main(verbosity=2)