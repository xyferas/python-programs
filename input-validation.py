while True:
    pin = input("Enter your 4-digit PIN: ")
    if len(pin) == 4 and pin.isdigit():
        print("PIN Setup Successful.")
        break
    else:
        print("Invalid PIN. Pin length should be 4 digits and should be a number.")