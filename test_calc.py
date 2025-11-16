import math
from calc import discriminant, solve_quadratic

def test_discriminant():
    assert discriminant(1, 2, 1) == 0
    assert discriminant(1, 5, 6) == 1
    assert discriminant(1, 0, -4) == 16

def test_solve_quadratic_delta_zero():
    sol = solve_quadratic(1, 2, 1)
    assert len(sol) == 1
    assert sol[0] == -1

def test_solve_quadratic_delta_positive():
    sol = solve_quadratic(1, -3, 2)
    assert len(sol) == 2
    assert sol[0] == 1
    assert sol[1] == 2

def test_solve_quadratic_delta_negative():
    sol = solve_quadratic(1, 2, 5)
    x1, x2 = sol
    assert isinstance(x1, complex)
    assert isinstance(x2, complex)
    assert x1.real == x2.real
    assert x1.imag == -x2.imag

def test_error_a_zero():
    try:
        solve_quadratic(0, 2, 3)
        assert False  # ne devrait jamais arriver
    except ValueError:
        assert True
