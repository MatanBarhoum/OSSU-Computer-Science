try:
    Hours = float(input("Enter Hours: "))
    Rate = float(input("Enter Rate: "))
    if (Hours > 40):
        ExtraHours = Hours - 40
        print(f"Pay: {(Hours - ExtraHours) * Rate + ExtraHours * (Rate * 1.5)}")
    else:
        print(f"Pay: {Hours * Rate}")
except:
    print("Error, please enter numeric input")

