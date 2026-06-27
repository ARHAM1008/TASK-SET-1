try:
    age = int(input("Enter your age: "))
    print("Age entered:", age)
except ValueError:
    print("Age must be numeric.")
