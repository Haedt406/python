# --------------------------------------
# CSCI 127, Lab 6                      |
# February 21, 2019                    |
# Benjamin Haedt                       |
# --------------------------------------

def average_magnitude(file_name):
    file = open(file_name, "r")
    value = 0
    file.readline()
    amount = 0
    for line in file:
        information = line.split(",")
        information.reverse()
        value += float(information[7])
        amount += 1
    calculated_value = value / amount
    file.close()
    return calculated_value

def earthquake_locations(file_name):
    file = open(file_name, "r")
    file.readline()
    locations = []
    print("Alphabetical Order of Earthquake Locations\n" + "------------------------------------------")    
    for line in file:
        information = line.split(",")
        if information[12] not in locations:
            locations.append(information[12])
        if information[13] not in locations:
            locations.append(information[13])   
    locations.sort()
    locations = [locations for locations in locations if not locations.isdigit()]
    for i in range(len(locations)):
        if i < 9:
            print("   " + str(i + 1) + ".", str(locations[i]))
        else:
            print("  " + str(i + 1) + ".", str(locations[i]))


def count_earthquakes(file_name, lower, upper):
    file = open(file_name, "r")
    file.readline()
    values = []
    count = 0
    for line in file:
        information = line.split(",")
        information.reverse()
        values.append(information[7])
    for x in values:
        if upper >= float(x) >= lower:
            count += 1
    return count
                     
# --------------------------------------

def main(file_name):
    magnitude = average_magnitude(file_name)
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))
    earthquake_locations(file_name)
    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")
