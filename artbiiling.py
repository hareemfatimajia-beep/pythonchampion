def greet_customer():
    print("Welcome to the Art Supplies Store!")
    print("Quality art supplies for every artist!")

greet_customer()

item_name = input("Enter the art supply name: ")
price_per_item = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity purchased: "))

def calculate_total(price, qty):
    total = price * qty
    return total

total_cost = calculate_total(price_per_item, quantity)
rounded_total = round(total_cost, 2)

print("Total Cost:", rounded_total)

amount_paid = float(input("Enter the amount paid by customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

print()
print("===== ART SUPPLIES RECEIPT =====")
print("Item Name:", item_name)
print("Price Per Item:", price_per_item)
print("Quantity Purchased:", quantity)
print("Total Cost:", rounded_total)
print("Amount Paid:", amount_paid)
print("Change Due:", rounded_change)
print("================================")