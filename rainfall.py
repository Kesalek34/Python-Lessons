#FILES AND EXCEPTIONS AND  FUNCTIONS
#Each city stored in 2 lines (CityName, RainfallAmount)
#Calculates average
#Handles exceptions 
#Find the highest rainfall
#Write results to rainfall_summary.txt

# Function to read rainfall data from a file
def read_rainfall_data(filename):
    file = open(filename,'r') # read file 
    city = file.readline() # read first line (city name)

#2 data types = 2 exception file handling 
#Check if file is empty
    if city == "":
       file.close() #checks if file contains citydata 
       raise ValueError("No city data") # exception handling 
    data =[]   
    while city != "": #Loop until the end of the file 
        city = city.strip() # remove newline from the city name
        rainfall = file.readline()

        if rainfall == "":
            file.close() #checks if file ccontains rainfalldata 
            raise ValueError("No rainfall data ")

        rainfall = int(rainfall.strip()) # remove newline from the rainfall amount
        data.append((city,rainfall)) # add city and rainfall to the data list

        city = file.readline() # read the next city name
    file.close()
    return data


def calculate_average(data):
    total = 0

    for city, rainfall in data: #go through data indvidaully 
        total += rainfall
        average = total/len(data)
        return average
    
def find_highest(data):
    highest_city = data[0][0]
    highest_rainfall = data [0][1]


    for city,rainfall in data: #goes through data indivaully 
        if rainfall > highest_rainfall:
            highest_city = city
            highest_rainfall = rainfall

    return highest_city, highest_rainfall


def write_summary(filename,average,highest_city,highest_rainfall):
    file = open(filename,"w")

    file.write("Rainfall summary")
    file.write("-------------------------\n")

    file.write("Average rainfall" + str(round(average,2)) + "mm\n")
    file.write("highest rainfall: " + highest_city + "-"+ str(highest_rainfall) + "mm\n")

    file.close()

def main():
    try:
        rainfalldata = read_rainfall_data("rainfall.txt")
        average = calculate_average(rainfalldata)
        highestcity,highestrain = find_highest(rainfalldata)

        print("Average rainfall" ,round(average,2), "mm\n")
        print("Highest rainfall:", highestcity, "-",highestrain, "mm\n" )

        write_summary("rainfall.txt",average,highestcity,highestrain)
        print("Summary written")

    except FileNotFoundError: #HANDLES FILES 
        print("Error: file not found")
    
    except ValueError as e: #handles invalid data and unexpected errors
        print("Error", e)

    except Exception as e:
        print("Unexpected error:", e)
main()







    



            


        

    






        
       


       
    


       




    
    




