import unittest
from main import *

class UnitTests(unittest.TestCase) :
      def test_cdf(self) :
          mycdf = sy.integrate( sy.integrate( k*(x**2*y**2 + x*y**3),(x,1,u)),(y,0,v))
          self.assertTrue( mycdf=cdf, "the cumulative distribution you have evaluated is incorrect" )
