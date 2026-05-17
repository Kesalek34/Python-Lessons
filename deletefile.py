import os # a module that allows you to delete and rename files

filename = "coffee.txt" # Original file that contains the coffee records
temp_filename = "temp_coffee.txt" # Temporary file will allow to store all records you did not delete

print("Coffee Roasters")

#display all existing records)
print("Displaying all existing records:")

file = open(filename, 'r') #we read original file to display the records
line = file.readline() #reads the first line of the file

while line != '': #lOOP UNTILL THE END OF THE FILE

    name = line.strip() #removes newlines and any extra spaces from the name
    quantity = file.readline().strip()

    print("name", name)
    print("quantity", quantity)

    line = file.readline() #reads the next line of the file
    file.close() #closes the file after reading


search = input("Enter the name of the coffee you want to delete: ") 

file = open(filename, 'r') 
temp_file = open(temp_filename, 'w')
line = file.readline()

while line != '':
    name = line.strip()
    quantity = file.readline().strip()

    if name.lower() == search.lower():
        found = True
    else:
        temp_file.write(name + '\n')
        temp_file.write(quantity + '\n')
        line = file.readline()

file.close()
temp_file.close()


if found:
    os.remove(filename)
    os.rename(temp_filename, filename)
    print("Record deleted successfully.")
else:
    os.remove(temp_filename)
    print("Record not found.")
    













