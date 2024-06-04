from app.controllers.math import inc, minus, power 



def test_inc():
    assert inc(3) == 4


def test_minus():
    assert minus(3) == 2 
    

def power():
    assert power(2,3) == 8