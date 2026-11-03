print(f"=== Grocery Billing Queue ===\n")

total_customers = 0
total_sales = 0

serving = True

while serving:                                 
    name = input("Enter customer name: ")

    items_count = int(input(f"How many items does {name}  have? "))

    if items_count <= 0:
        print("Invalid number of items.\n")
        continue

    print(f"\nBilling items for {name}:")

    bill = 0
    item_no = 1

    while item_no <= items_count:               
        item_name = input(f"Enter item {item_no} name: ")
        price = float(input(f"Enter price of {item_name}: "))

        bill += price

        print(f"  {item_name}: {price:.2f}")
        item_no += 1

    print(f"\nTotal Bill for {name}: {bill:.2f}")

    total_customers += 1
    total_sales += bill

    print(f"Customer {name} served successfully!\n")

    again = input("Next customer? (yes/no): ").strip().lower()

    if again != "yes":
        serving = False

print("\n=== Daily Grocery Report ===")

for customer in range(1, total_customers + 1):  
    print(f"Customer {customer}: ", end="")

    for mark in range(customer):             
        print("*", end="")

    print()

print(f"\nCustomers served : {total_customers}")
print(f"Total sales      : {total_sales:.2f}")
print("Store closed. Goodbye!")