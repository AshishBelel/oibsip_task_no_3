def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if weight <= 0:
                print("Weight must be greater than zero.")
            else:
                return weight
        except ValueError:
            print("Invalid input. Please enter a valid weight.")

def get_valid_height():
    while True:
        try:
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                print("Height must be greater than zero.")
            else:
                return height
        except ValueError:
            print("Invalid input. Please enter a valid height.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")

    weight = get_valid_weight()
    height = get_valid_height()

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")

if __name__ == "__main__":
    main()

