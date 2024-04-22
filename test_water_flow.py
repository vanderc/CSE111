from water_flow import water_column_height, pressure_gain_from_water_height
import pytest

def test_water_column_height():
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0, 0) == 0.001
    assert pressure_gain_from_water_height(30.2, 295.628) == 0.001
    assert pressure_gain_from_water_height(50, 489.450) == 0.001