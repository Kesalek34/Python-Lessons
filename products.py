filename = "products.txt"

#display menu and options 
def display_menu():
    print("Product Management System")
    print("1. Load products from file")
    print("2. Add new product(s)")
    print("3. View all products")
    print("4. Show product summary")
    print("5. Save products to file")
    print("6. Exit")
    
def load_products():
    product_names = [] #Intilize an empty list to store product names
    product_names_prices = [] #Intilize an empty list to store product prices

    file = open(filename, "r") #open the file for reading
    name = file.readline() #read the first line of the file
    while name != "": #While the name is not empty
        product_names.append(name.strip()) 

        price = float(file.readline().strip())
        product_names_prices.append(price)

        name = file.readline() #read the next product name so that the loop can continue until the end of the file is reached

    file.close() #close the file
    print(len(product_names), "products loaded successfully.")
    return product_names, product_names_prices #it is what u wanna see as an output when the function is called


def add_product(product_names , product_names_prices):
    
    choice = "y"
    while choice.lower() == "y": #while the user wants to add more products

        name = input("Enter product name:")
        price = float(input("Enter product price:"))

        product_names.append(name) #add the name to the list of product names
        product_names_prices.append(price) #add the price to the list of product prices

        print(f"Added: {name} with price R{price:.2f}")
        choice = input("Do you want to add another product? (y/n):") #ask the user if they want to add another product


def view_prodcucts(product_names, product_names_prices):
    print("Product List:")

    for i in range (len(product_names)):
        print(f"{i + 1}. {product_names[i]} - R{product_names_prices[i]:.2f}")

    print(f"Total products: {len(product_names)}")

def show_summary(product_names, product_prices):
    print("Product Summary:")

    total_products = len(product_names)
    total_value = sum(product_prices)

    print(f"Total products: {total_products}")
    print(f"Total value of products: R{total_value:.2f}")

#HIGHEST
    if total_products > 0:
        highest_price = max(product_prices) #highest price 
        index = product_prices.index(highest_price) #position of highestprice
        most_expensive = product_names[index]  #call highest price product name using the index

        print(f"Most expensive product: {most_expensive} - R{highest_price:.2f}")

def save_products(product_names, product_names_prices):
    file = open(filename,"w") #open the file for writing

    for i in range(len(product_names)):
        file.write(product_names[i] + "\n") #write the product name on one line
        file.write(str(product_names_prices[i]) + "\n") #write the product price on the next line
    
    file.close() #close the file
    print("Products saved successfully.")

def main():
    product_names = [] #Intilize an empty list to store product names
    product_names_prices = [] #Intilize an empty list to store product prices

    while True:
        display_menu()
        choice = input("Enter your choice (1-6):")

        if choice == "1":
           product_names, product_names_prices = load_products() #call the load products function and store the returned values in the respective lists
        elif choice == "2":
            add_product(product_names, product_names_prices)
        elif choice == "3":
            view_prodcucts(product_names, product_names_prices)
        elif choice == "4":
            show_summary(product_names, product_names_prices)
        elif choice == "5":
            save_products(product_names, product_names_prices)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()





        




    












   
   







