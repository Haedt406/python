# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Benjamin Haedt
# Last Modified: January 18, 2019 
# ---------------------------------------
# This calculates GPA
# ---------------------------------------


courses = (input ("Enter the number of courses you are taking: "))
while courses.isdigit() == False:
        courses = (input ("You need to enter a number between 1 and 7. Please try again. \nEnter the number of courses you are taking: "))
while not int(courses) in range (1,7):
        courses = (input ("You need to enter a number between 1 and 7. Please try again. \nEnter the number of courses you are taking: "))
 
