from CH11 import Employee
import pytest

@pytest.fixture
def emp():
    """Create Instance for other tests."""
    emp = Employee('Mario','Rossi',10000)
    return emp

def test_give_default_rise(emp):
    """Test default raise of 5000 works properly."""
    emp.give_raise()
    assert emp.salary == 15000

def test_give_custom_rise(emp):
    """Test custom raise works properly."""
    emp.give_raise(10000)
    assert emp.salary == 20000