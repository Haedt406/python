def process_file(input_file, output_file):
    line = input_file.readline()
    output_file.write(line[:-1] + ", Average \n")
    
    for line in input_file:
        values = line.split(",")
        average = (int(values[1]) + int(values[2])) / 2
        output_file.write(line[:-1] + ", " + str(average) + "\n")

def main(input_file_name, output_file_name):
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")

    process_file(input_file, output_file)

    input_file.close()
    output_file.close()

main("grades.csv", "grades2.csv")    
