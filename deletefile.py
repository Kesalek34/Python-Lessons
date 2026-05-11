#import os module to to be able to delete the file or rename file

import os

filename = "coffee.txt"

temp_filename = "tempcoffee.txt"

print("Midnight coffee roaster")

print("Display records")
file = open(filename, 'r') # open file for reading
line = file.readline()

while line != '': # loop until end of file
    description = line.strip()
    quantity = file.readline().strip()

    print("Description: " + description)
    print("Quantity: " + quantity)

    line = file.readline() # read next line

file.close() # close the file


#Step 2 ask user which record they want to delete
search = input("Enter the description of the record you want to delete: ").strip()
found = False

file = open(filename, 'r') # open file for reading
temp_file = open(temp_filename, 'w') # open temp file for writing
line = file.readline()

while line != '': # loop through all records
    description = line.strip()
    quantity = file.readline().strip()

    if description.lower() == search.lower(): # if record matches search term
        found = True
    else:
        temp_file.write(description + '\n') # write description to temp file
        temp_file.write(quantity + '\n') # write quantity to temp file

    line = file.readline() # read next line

file.close() # close the original file
temp_file.close() # close the temp file

if found:
    os.remove(filename) # delete original file
    os.rename(temp_filename,filename) # rename temp file to original file name
    print("Record deleted.")
else:
    os.remove(temp_filename) # delete temp file
    print("Record not found.")














