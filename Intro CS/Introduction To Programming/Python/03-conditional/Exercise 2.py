try:
    Hours = float(input("Enter Hours: "))
    Rate = float(input("Enter Rate: "))
    print(f"{Hours * Rate}")
except:
    print("Error, please enter numeric input")
