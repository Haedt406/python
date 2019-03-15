# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Weather CSV Library           |
# Benjamin Haedt                         |
# Last Modified: 21 February, 2019         |
# -----------------------------------------+
# Provide a brief overview of the program. |
# -----------------------------------------+

def coldest_temperature(input_file):
    coldest_temperature = 1000
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            if int(coldest_temperature) > int(row[7]):
                coldest_temperature = row[7]
                location = row[5]
                date = row[4]
    location_without_comma = location.replace(",", "")
    print("Coldest Fahrenheit temperature reading:" , coldest_temperature)
    print("Location:", location_without_comma)
    print("Date:", date)

def average_temperature(input_file, location):
    count = 0
    temperature = 0
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            if location.lower() == row[5].lower():
                count += 1
                temperature += float(row[0])
        if count != 0:
            average = temperature / count
            print("Number of readings:", count)
            print("Average temperature:", '%.2f' % average)
        else:
            print("Number of readings: 0")
            print("Average temperature: Not Applicable")

    
def all_stations_by_state(input_file, state):
    locations = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            if state.lower() == row[11].lower():
                if row[1] not in locations:
                    locations.append(row[1])
        if locations == []:
            print("There are no recording stations")
        else:
            print("Recording Stations")
            print("------------------")
            for i in range(len(locations)):
                if i < 9:
                    print(" " +str(i + 1) + ".", locations[i])
                else:
                    print(" " +str(i + 1) + ".", locations[i])
def average_precipitation_by_month(input_file, number):
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = month_list[(int(number) - 1)]
    count = 0
    precipitation = 0
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            if number == row[8]:
                count += 1
                precipitation += float(row[9])
        average = precipitation / count
        print("The average precipitation reading during the month of", str(month) + ":", '%.2f' % average) 

# -----------------------------------------+
# Do not change anything below this file   |
# with the exception of code related to    |
# option 4.                                |
# -----------------------------------------+

# -----------------------------------------+
# menu                                     |
# -----------------------------------------+
# Prints a menu of options for the user.   |
# -----------------------------------------+

def menu():
    print()
    print("1. Identify coldest temperature.")
    print("2. Identify average temperature for a given location.")
    print("3. Identify all recording station locations by state.")
    print("4. Identify average precipitation readings by month.")
    print("5. Quit.")
    print()

# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Repeatedly query the user for options.   |
# -----------------------------------------+

def main():
    input_file = "weather.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            coldest_temperature(input_file)
        elif (choice == 2):
            location = input("Enter desired location (e.g. Miles City, MT): ")
            average_temperature(input_file, location)
        elif (choice == 3):
            state = input("Enter name of state (e.g. Montana): ")
            all_stations_by_state(input_file, state)
        elif (choice == 4):
            month = input("Enter month numerically (e.g. '1' for January): ")
            average_precipitation_by_month(input_file, month)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

import csv
main()
