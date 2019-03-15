import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Benjamin Haedt    
# Last Modified: 13 March 2019               
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

class Pokemon:
    def __init__(self, name, number, combat_points, types):
        self.name = name
        self.number = number
        self.combat_points = combat_points
        self.type = " and ".join(types)
    def getName(self):
        return self.name.capitalize()
    def getNumber(self):
        return self.number
    def getCombat_points(self):
        return self.combat_points
    def getType(self):
        return self.type
    
def average_hit_points(pokedex):
    number = 0
    total = 0
    for i in pokedex:
        number += Pokemon.getCombat_points(i)
        total += 1
    final_total = int(number) / total
    print("Average Pokemon combat points = {0:.2f}" .format(final_total))
    
def total_by_type(pokedex, pokemon_type):
    count = 0
    for i in pokedex:
        if pokemon_type in Pokemon.getType(i):
            count += 1
    print("Number of Pokemon that contain type {} = {}".format(pokemon_type, count))

def lookup_by_number(pokedex, number):
    did_you_find_one = 0
    for i in pokedex:
        if Pokemon.getNumber(i) == number:
            print("Number: {}, Name: {}, CP: {}: Type: {}" .format(Pokemon.getNumber(i),Pokemon.getName(i), Pokemon.getCombat_points(i), Pokemon.getType(i)))
            did_you_find_one += 1
    if did_you_find_one == 0:
        print("There is no Pokemon number", number)
        
def lookup_by_name(pokedex, name):
    did_you_find_one = 0
    for i in pokedex:
        if Pokemon.getName(i) == name.capitalize():
            print("Number: {}, Name: {}, CP: {}: Type: {}" .format(Pokemon.getNumber(i),Pokemon.getName(i), Pokemon.getCombat_points(i), Pokemon.getType(i)))
            did_you_find_one += 1
    if did_you_find_one == 0:
        print("There is no Pokemon named", name)

def print_pokedex(pokedex):
    print("\nThe Pokedex\n-----------")
    for i in pokedex:
        print("Number: {}, Name: {}, CP: {}: Type: {}" .format(Pokemon.getNumber(i),Pokemon.getName(i), Pokemon.getCombat_points(i), Pokemon.getType(i)))

def print_menu():
    print("1. Print Pokedex \n2. Print Pokemon by Name \n3. Print Pokemon by Number\
    \n4. Count Pokemon with Type \n5. Print Average Pokemon Combat Points\n6. Quit\n")



# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()
