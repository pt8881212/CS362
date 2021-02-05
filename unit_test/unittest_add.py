import unittest 
import calculator

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculator.add(2,2), 4)

    def test2(self):
        self.assertEqual(calculator.add(8,2), 10)

if __name__== '__main__':
    unittest.main(verbosity=2)

