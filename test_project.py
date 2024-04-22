from project import square_root, area_rectangle, perimeter_triangle, area_circle
from pytest import approx
import pytest

def test_square_root():
    assert square_root(9) == approx(3, 0.1)
    assert square_root(20) == approx(4.47, 0.1)
    assert square_root(12) == approx(3.46, 0.1)
    assert square_root(28) == approx(5.29, 0.1)



def test_area_rectangle():
    assert area_rectangle(8, 5) == 40
    assert area_rectangle(7, 6) == 42
    assert area_rectangle(20, 15) == 300
    assert area_rectangle(30, 20) == 600

def test_perimeter_triangle():
    assert perimeter_triangle(5, 6, 4) == 15
    assert perimeter_triangle(10, 18, 12) == 40
    assert perimeter_triangle(5, 5, 10) == 20

def test_area_circle():
    assert area_circle(5) == approx(78.54, 0.1)
    assert area_circle(10) == approx(314.16, 0.1)
    assert area_circle(2) == approx(12.57, 0.1)
    assert area_circle(1) == approx(3.14, 0.1)

pytest.main(["-v", "--tb=line", "-rN", __file__])