def calculate_bmi(weight, height):
    """
    Calculate BMI using weight in kg and height in meters.
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    return weight / (height ** 2)


def determine_weight_target(bmi, height):
    """
    Determine the weight target based on BMI and height.
    """
    if bmi <= 0 or height <= 0:
        raise ValueError("BMI and height must be greater than zero.")
    target_bmi_low, target_bmi_high = 18.5, 24.9
    if bmi < target_bmi_low:
        return target_bmi_low * (height ** 2), 'gain'
    elif bmi > target_bmi_high:
        return target_bmi_high * (height ** 2), 'lose'
    else:
        return None, 'maintain'

def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    try:
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI: {bmi:.1f}")

        target_weight, action = determine_weight_target(bmi, height)
        if target_weight:
            difference = target_weight - weight
            print(f"To reach a normal BMI, you need to {action} {abs(difference):.1f} kg.")
        else:
            print("Your weight is within the normal range.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
