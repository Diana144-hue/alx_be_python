import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.Testcase):

  def setUp(self):
      """Set up the SimpleCalculatoer instance before each test.."""
      self.calc = SimpleCalculator()

  def test_addition(self):
    
