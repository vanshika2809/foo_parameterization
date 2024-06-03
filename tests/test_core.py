
import unittest
from foo_parameterization.core import calculate_volume

class TestFooParameterization(unittest.TestCase):
    
    def test_calculate_volume(self):
        self.assertAlmostEqual(calculate_volume(1), 4.1887902047863905)
        self.assertAlmostEqual(calculate_volume(0), 0)
        self.assertAlmostEqual(calculate_volume(3), 113.09733552923255)
        
    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1)

if __name__ == '__main__':
    unittest.main()
