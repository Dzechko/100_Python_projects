print("Welcome to the tip Calculator")
x = int(input("What was the total bill: $"))
t = int(input("What percentage tip would you like to give: $"))
n = int(input("How many peoples to split the bill: "))
a = (x - x*(t/100))/n
print(f"Each person should pay {a}")