# foo_param/tests/test_core.py
import unittest
from foo_param.core import calculate_volume

class TestCoreFunctions(unittest.TestCase):
    
    def test_calculate_volume(self):
        self.assertAlmostEqual(calculate_volume(1), 4.18879, places=5)
        self.assertAlmostEqual(calculate_volume(0), 0)
        
    def test_calculate_volume_negative(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1)
    
if __name__ == '__main__':
    unittest.main()
