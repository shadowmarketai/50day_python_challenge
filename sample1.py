def get_weight():
    unit = input("Enter weight unit (kg/pound): ").lower()
    weight = float(input("Enter weight: "))
    if unit == "pound" or unit == "lb" or unit == "lbs":
        weight = weight * 0.453592  # convert pounds to kg
    elif unit != "kg":
        print("Invalid weight unit. Defaulting to kg.")
    return weight

def get_height():
    unit = input("Enter height unit (m/cm): ").lower()
    height = float(input("Enter height: "))
    if unit == "cm":
        height = height / 100  # convert cm to meters
    elif unit != "m":
        print("Invalid height unit. Defaulting to meters.")
    return height

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main program
print("💪 BMI Calculator")

try:
    weight = get_weight()
    height = get_height()
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print("\nYour BMI is:", round(bmi, 2))
    print("Category:", category)

except ValueError:
    print("❌ Invalid input. Please enter numeric values.")
