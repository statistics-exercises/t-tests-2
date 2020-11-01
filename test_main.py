import unittest
import scipy.stats
from main import *

class UnitTests(unittest.TestCase) :
    def test_t_variable(self) :
        for i in range(2,11) :
            ttt = gen_t_variable(i)
            self.assertTrue( ttt>scipy.stats.t.ppf(0.01,i) and ttt<scipy.stats.t.ppf(0.99,i), "your function for generating t variables appears not to be working correclty" )
