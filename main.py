#A shopping system (Functions/Methods)

def calc_total(price,quantity):
    total = price * quantity
    return total

#Apply discount if total > 100
def apply_discount(total):
    if total > 100:
        return total * 0.9
    return total

def calculate_vat(amount):
    return amount * 0.15


#Input from users
Item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

total = calc_total(price,quantity)
disctotal = apply_discount(total)

vat = calculate_vat(disctotal)

finalamount = disctotal + vat

#Output
print("Receipt-------------------")
print(f"Item: {Item}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")
print(f"Discounted Total: {disctotal}")
print(f"VAT: {vat:.2f}")
print(f"Final Amount: {finalamount:.2f}")








