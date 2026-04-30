import pytest
from fitness_logic import calculate_bmi_value, calculate_bmi


# -------------------------------
# BMI VALUE TESTS
# -------------------------------

def test_bmi_normal():
    result = calculate_bmi_value(70, 1.75)
    assert round(result, 2) == 22.86

def test_bmi_underweight():
    result = calculate_bmi_value(45, 1.70)
    assert round(result, 2) == 15.57

def test_bmi_overweight():
    result = calculate_bmi_value(90, 1.70)
    assert round(result, 2) == 31.14


# -------------------------------
# VALIDATION TESTS
# -------------------------------

def test_zero_height():
    with pytest.raises(ValueError):
        calculate_bmi_value(70, 0)

def test_negative_values():
    with pytest.raises(ValueError):
        calculate_bmi_value(-70, 1.75)


# -------------------------------
# PARAMETERIZED TESTS
# -------------------------------

@pytest.mark.parametrize("weight,height,expected", [
    (60, 1.70, 20.76),
    (80, 1.80, 24.69),
    (90, 1.60, 35.16),
])
def test_bmi_multiple(weight, height, expected):
    result = calculate_bmi_value(weight, height)
    assert pytest.approx(result, 0.01) == expected


# -------------------------------
# BMI CATEGORY TESTS
# -------------------------------

def test_bmi_category():
    assert calculate_bmi(50, 1.75) == "Underweight"
    assert calculate_bmi(70, 1.75) == "Normal"
    assert calculate_bmi(85, 1.75) == "Overweight"
    assert calculate_bmi(100, 1.75) == "Obese"
