# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Benjamin Haedt
# Last Modified: January 18, 2019 
# ---------------------------------------
# This calculates GPA
# ---------------------------------------

def translate(x):
    g1 = (input("Enter grade for course " + str(x + 0) + ": ")).lower()
    while g1 not in ('a', 'a-', 'b+', 'b', 'b-', 'c+', 'c', 'c-', 'd+', 'd', 'f'):
        g1 = (input(g1 + " is not a valid entry. \nPlease enter grade for course " + str(x + 0) + ": ")).lower()        
    if g1 == 'a':
        return float(4.0);
    if g1 == 'a-':
        return float(3.7);
    if g1 == 'b+':
        return float(3.3);
    if g1 == 'b':
        return float(3.0);
    if g1 == 'b-':
        return float(2.7);
    if g1 == 'c+':
        return float(2.3);
    if g1 == 'c':
        return float(2.0);
    if g1 == 'c-':
        return float(1.7);
    if g1 == 'd+':
        return float(1.3);
    if g1 == 'd':
        return float(1.0);
    if g1 == 'f':
        return float(0.0);

def main():
    courses = (input ("Enter the number of courses you are taking: "))   
    while courses.isdigit() == False:
            courses = (input ("You need to enter a number between 1 and 7. Please try again. \nEnter the number of courses you are taking: "))
    while int(courses) not in range (1,8):
            courses = (input ("You need to enter a number between 1 and 7. Please try again. \nEnter the number of courses you are taking: "))
    print()
    cn = int(courses)
    result = []
    c1 = []
    NU = 0
    DE = 0
    for i in range(cn):
                result.append(translate(i + 1))
                c1.append(int(input("Enter credits for course " + str(i + 1) + ": ")))
                NU += (result[i] * c1[i])
                DE += c1[i]
    final = (str(round(NU / DE, 2)))
    print ("Your GPA is " + final)

main()










