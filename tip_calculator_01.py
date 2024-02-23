print("Welcome to the tip Calculator")
bill = float(input("What was the total bill: $"))
tip = int(input("What percentage tip would you like to give: $"))
n = int(input("How many peoples to split the bill: "))
a = (bill + bill*(tip/100))/n
print(f"Each person should pay {a}")