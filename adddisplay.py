filename = "coffee.txt"
print("Coffee Roasters")

#This code will write the describtion of the coffee and also the quantity of the coffee in the file

anotherrecord = 'y'
while anotherrecord.lower() == 'y':
    try:
        name = input("Enter the name of the coffee: ")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        

        quantity = float(input("Enter the quantity of the coffee: "))
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        
        file = open(filename, 'a') #that the file must allow us to add new records 
        file.write(name + '\n')
        file.write(str(quantity) + '\n')
        file.close()
        print("Record added successfully.")

    except ValueError as e:
        print(f" Invalid error: {e}") #Handles all iinvalid input errors

    except IOError as e:
        print(f"File error: {e}") #Handles all file related errors
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}") #Handles any other unexpected errors

        anotherrecord = input("Do you want to add another record? (y/n): ")

print("All records are saved in the file.")







    









