# unit testing for cube volume
import unittest;
import cube;

class TestCube(unittest.TestCase):
    def test1(self):
        self.assertEqual(cube.cubeVolume(5), 125)
        
        
    def test2(self):
        self.assertRaises(ValueError,cube.cubeVolume,0);

    def test3(self):
        self.assertRaises(ValueError,cube.cubeVolume,-1);


if (__name__ == '__main__'):
    unittest.main(verbosity=2);