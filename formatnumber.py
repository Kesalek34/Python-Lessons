print("Welcome to Kesa Mini store")

name = input("Please enter your name: ")

item_count = int(input("How many items do you want to buy? "))
total  = 0
#for loop is basically loop through a list or things individually
for i in range(item_count):
    price = input(f"Enter the item price of item: {i +1}:")
    total = total + int(price)


print(f"Your total is: {total}")

discount_card = input("Do you have a discount card? (yes/no): ")
if discount_card == "yes":
    discount = total* 0.10
else:
    dicount = 0

final_total  = total - discount

vat = final_total * 0.15
finalwithvat = final_total + vat


print("customername: ", name)
print(f"subtotal: R  {total:.2f}")
print(f"discount: R {discount:.2f}")
print(f"VAT: R:  {vat:.2f}")
print(f"final total: R , {finalwithvat:.2f}")




