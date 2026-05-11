
filename = "coffee.txt"
print("Mindnight Coffee Roasters")

anotherrec = 'y'

while anotherrec.lower() == 'y':

    description = input("Enter a description of the coffee: ")
    quantity = float(input("Enter the quantity of coffee: "))


    file = open(filename, 'a') # open file for appending

    file.write(description + '\n') # write description to file

    file.write(str(quantity) + '\n') # write quantity to file

    file.close() # close the file


    print("Record saved.")
    anotherrec = input("Do you want to enter another record? (y/n): ")

print("All records saved")







