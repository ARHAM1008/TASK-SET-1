try:
    amount = float(input("Enter payment amount: "))
    print("Payment processed:", amount)
except ValueError:
    print("Invalid amount entered.")
