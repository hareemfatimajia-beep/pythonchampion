while True:
    try:
        bill = float(input("Bill: "))
        discount = float(input("Discount %: "))
        people = int(input("People: "))

        total = bill - (bill * discount / 100)
        print("Each person pays:", total / people)
        break

    except:
        print("Please enter valid numbers!")