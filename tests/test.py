import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_division_success(self):
        assert self.calc.division(10, 2) == 5

    def test_multiply_success(self):
        assert self.calc.multiply(6, 3) == 18

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(8, 0)

    def test_subtraction_success(self):
        assert self.calc.subtraction(20, 10) == 10

    def test_adding_success(self):
        assert self.calc.adding(100, 1) == 101
