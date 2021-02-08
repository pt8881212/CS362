#Unit testing for full name
import unittest;
import name;

class TestFullName(unittest.TestCase):
    def test1(self):
        self.assertEqual(name.fullName("Pratiksha","Aga"), "Pratiksha Aga");

    def test2(self):
        self.assertRaises(ValueError,name.fullName,"","Pratiksha");

    def test3(self):
        self.assertRaises(ValueError,name.fullName,"Aga","");
        
    def test4(self):
        self.assertRaises(TypeError,name.fullName,"12","Three Four");

if (__name__ == '__main__'):
    unittest.main(verbosity=2);