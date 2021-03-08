# Pratiksha Aga
# Fizz buzz test
# Homework 7 

import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz.fbfunc(30), "FizzBuzz");
    def test2(self):
        self.assertEqual(fizzbuzz.fbfunc(12), "Fizz");
    def test3(self):
        self.assertEqual(fizzbuzz.fbfunc(20), "Buzz");
    
if __name__ == '__main__':
    unittest.main();