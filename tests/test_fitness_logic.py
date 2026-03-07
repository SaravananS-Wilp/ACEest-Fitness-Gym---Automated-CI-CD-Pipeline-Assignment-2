from fitness_logic import calculate_bmi_value

def test_bmi_normal():
    result = calculate_bmi_value(70, 1.75)
    assert round(result, 2) == 22.86

def test_bmi_underweight():
    result = calculate_bmi_value(45, 1.70)
    assert round(result, 2) == 15.57

def test_bmi_overweight():
    result = calculate_bmi_value(90, 1.70)
    assert round(result, 2) == 31.14