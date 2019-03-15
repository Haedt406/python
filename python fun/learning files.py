census_file = open("census.txt", "r")

total = 0
for one_line in census_file:

    values = one_line.split()
    print("State: " + values[0] + ", Population: " +  values[1])
    total += int(values[1])

print(total)

    
census_file.close()


