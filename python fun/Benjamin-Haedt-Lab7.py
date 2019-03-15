# --------------------------------------
# CSCI 127, Lab 7                      |
# February 28, 2019                    |
# Benjamin Haedt                        |
# --------------------------------------

## The comma character and space character have to be treated different because of how python reads the data from the csv file. The comma is the standard character used in CSV files to denote a Delimiter, or -
## to seperate each peice of data. The space character isnt seen by python.

def translate(sentence, dictionary, file_name):
    with open(file_name, 'w') as f:
        for i in sentence:
            a = dictionary.get(i)
            if not a:
                a = "UNKNOWN"
            f.write(" " + i + " " + a + "\n")
def create_dictionary(input_file):
    dictionary = {}
    with open(input_file) as file:
        reader = csv.reader(file, quoting=csv.QUOTE_NONE)
        for row in reader:
            dictionary[row[1]]=row[0]
    del dictionary['space']
    del dictionary['comma']
    dictionary[' '] = "100000"
    dictionary[','] = "101100"
    return (dictionary)
# --------------------------------------

def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called!"
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Bozeman, MT  59717"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "The value is ~$25.00"
    translate(sentence, dictionary, "output-3.txt")

# --------------------------------------

import csv
main()
