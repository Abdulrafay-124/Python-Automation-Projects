from employee import Employee
import pytest

# A simple test for checking the functionality of Employee class

@pytest.fixture
def employee():
    """Employee function with a fixture"""
    employee = Employee("Tel","Son",0)
    return employee

def test_give_default_raise(employee):

    employee.give_raise()
    assert employee.annual_salary == 5000


def test_give_custom_raise(employee):

    employee.give_raise(10000)
    assert employee.annual_salary == 10000

