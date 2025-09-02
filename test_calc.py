from first_class_test import Calculator
import pytest

# This is a Group test for the Calculator class

class TestCaluclator:
    @pytest.fixture
    def calc(self):
        """Creates a test class instance"""
        self.calc = Calculator(6,2)
        return self.calc

    def test_add(self,calc):
        """Tests the addition function"""
        assert self.calc.add() == 8

    def test_sub(self,calc):
        """Tests the subtraction function"""
        assert self.calc.sub() == 4

    def test_mul(self,calc):
        """Tests the multiplication function"""
        assert self.calc.mul() == 12

    def test_div(self,calc):
        """Tests the division function"""
        assert self.calc.div() == 3
