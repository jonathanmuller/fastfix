import unittest
from fastfix import Util

class TestUtil(unittest.TestCase):
    
    def test_phase(self):
        
        self.assertAlmostEqual(Util.phase_delta(0.999,0.001), 0.002)
        self.assertAlmostEqual(Util.phase_delta(0.99, 0.01), 0.02, 4)

