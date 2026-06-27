try:
    with open("report.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Report file missing.")
