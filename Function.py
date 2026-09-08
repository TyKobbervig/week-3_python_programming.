# Function Definition
def calculate_total(price, quantity):
    return price * quantity

# Function definition
def display_receipt(item, price, quantity):
    total = calculate_total(price, quantity)

    print("Receipt")
    print("-------")
    print("Item", item)
    print("Price: $", price)
    print("Quantity:", quantity)
    print("Total: $", total)

display_receipt("Notebook", 2.50, 4)