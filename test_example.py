from example import add 
from example import subtract

def test_add():
    sum = add(2, 3) 
    assert sum == 5

def test_subtract():
    assert subtract(5,4) == 1
