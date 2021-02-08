#unit testing for average element
import unittest;
import element;

class TestArray(unittest.TestCase):
    def test1(self):
        self.assertEqual(element.avg_element([1,2,3]), 2)
        
    def test2(self):
        self.assertRaises(TypeError,element.avg_element,([0,0]), 0);

    def test3(self):
        self.assertRaises(ValueError,element.avg_element,[]);


if (__name__ == '__main__'):
    unittest.main(verbosity=2);

    