def richter_magnitude_info(magnitude):
    if magnitude >= 1.0 and magnitude < 2.0:
        return "Microearthquakes not felt or rarely felt"
    elif magnitude >= 2.0 and magnitude < 4.0:
        return "Very rarely causes damage"
    elif magnitude >= 4.0 and magnitude < 5.0:
        return "Damage done to weak buildings"
    elif magnitude >= 5.0 and magnitude < 6.0:
        return "Cause damage to poorly constructed buildings"
    elif magnitude >= 6.0 and magnitude < 7.0:
        return "Causes damage to well-built structures"
    elif magnitude >= 7.0 and magnitude < 8.0:
        return "Causes damage to most buildings"
    elif magnitude >= 8.0 and magnitude < 9.0:
        return "Causes major destruction"
    elif magnitude >= 9.0:
        return "Causes unbelievable damage"
    else:
        return "Magnitude value not within defined ranges"

def main():
    try:
        magnitude = float(input("Enter the Richter magnitude value: "))
        info = richter_magnitude_info(magnitude)
        print("Magnitude Information:", info)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

    
