result = 50
numbers = [25, 10, 5]

while result > 0:
    print("Amount due:", result)
    amount = int(input("Insert coin: "))
    if amount in numbers:
        result -= amount
        if result == 0:
            print("Amount owed: 0")
    else:
        print("Invalid coin. Please insert 25, 10, or 5.")
   

   

