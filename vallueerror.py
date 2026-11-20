try:
    number = int(input("enter a number"))
    print("The number entered id ",number)

except ValueError as ex:
    print("Expection",ex)
    