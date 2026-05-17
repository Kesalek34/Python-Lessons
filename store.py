#FUNCTIONS - LISTS - EXCEPTIONS - FILES(STORE MARKEY SYSTEM)
#Dictonary basically stores key- value pairs (product + price)
#Key = product name;
#Value = price;

products = {"bread": 15.50,
            "milk":18.00,
            "sugar":32.00,
            "rice": 120.00,
            "eggs": 45.00
            }

#get total
#generate arecipt 
#Save to file 
# read to file

def calculate_total(price, qty):
    total = 0
    total = price*qty
    return total #we return something we want to show on output in future

def generate_receipt(productsdict):
    receipt = ""

    print("STORE RECIEPT")
    grandtotal = 0


    for product, price in productsdict.items(): #LOOP THROUGH LIST (bread-milk-sugar-rice-eggs)
        qty =  input(f"Enter quantity for {product}")

#input exception handling 

        if qty.isdigit():  #CHECK IF ITS A NUMBER
            qty_input = int(qty) #CONVERT TO INT

            total = calculate_total(price,   qty_input)
            grandtotal += total  #Because there is different totals for specific products so all we do is add together 

            receipt += f"{product}  |R{price} X {qty_input} = R{total:.2f}\n"

        else:
            receipt += f"{product} |Invalid quantity \n"

            receipt += f"GRAND TOTAL: R{grandtotal:.2f}"

    return receipt

def save_to_file (filename,content):
    #Write file with exception handling 

    try:
        file = open(filename,"w") #Writing to a file 
        file.write(content)
        file.close()
        print("Receipt saved succesfully")

    except Exception as e:
        print("file write error", e)
    
def read_file(filename):
    try:
    #Reading with exception handling 
        file = open(filename,"r") #reading thee file
        print("------------RECEIPT FILE READING-----------------")
        print(file.read())
        file.close()
    except Exception as e:
        print("File raed error", e)

#----------PROGRAM RUN-----------------
receipt = generate_receipt(products)
save_to_file ("store_recipt.txt",receipt)
read_file("store_recipt.txt")





















    
    








