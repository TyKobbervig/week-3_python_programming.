    def calculate_total(price, quantity):
def means defining a function.
calculate_total is the function name.
price and quantity are parameters, which are values passed into the function.
the colon tells python the function body starts on the next line.
    return price * quantity
mutiplies price by quantity
return sends the result back to whatever called the function.
    def display_receipt(item, price, quantity):
creates a second function called display_receipt.
It accepts three parameters:
item (name of the product)
price (cost per item)
quantity(how many were purchased)
    total = calculate_total(price, quantity)
calls the calculate_total() function.
passes price and quantity into it.
stores the returned value in a variable named total.
    print("Receipt")
display the word Receipt
