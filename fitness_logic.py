from datetime import datetime

def calculate_bmi(weight, height):
    bmi = calculate_bmi_value(weight, height)   

    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi_value(weight, height):
    if height <= 0:
    	raise ValueError("Height must be greater than zero")

    if weight <= 0:
    	raise ValueError("Weight must be greater than zero")
	
    return weight / (height ** 2)