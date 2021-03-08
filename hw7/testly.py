

import unittest
import checkLeapYear

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertEqual(checkLeapYear.ly(2020), "Leap year");

	def test2(self):
		self.assertEqual(checkLeapYear.ly(2021), "Not a leap year");

if __name__ == '__main__':
	unittest.main();