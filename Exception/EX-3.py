try:
    seat = int(input("Enter seat number: "))
    if seat <= 0:
        raise ValueError("Invalid seat number")
    print("Seat booked:", seat)
except ValueError as e:
    print(e)
