#+-------------------+
#|    A Stranger     |
#|    Final Exam     |
#+-------------------+

##---Question One---##

import turtle
def drawSquare(cecil, length):
    for aLine in range (4):
        cecil.forward(length)
        cecil.left(90)
def startProcess(cecil, length, amount):
    for aSquare in range(amount):
        cecil.penup
        cecil.goto(-length/2, -length/2)
        cecil.pendown
        drawSquare(cecil, length)
        length = length + 20
def main():
    cecil = turtle.Turtle()
    length = 20
    amt = int(input("How many squares would you like?"))
    startProcess(cecil, length, amt)
    cecil.ht()
main()

##---Question Two---##

class Dog:
    def __init__(self, breed, age=0):
        self.breed = breed
        self.age = age
    def getBreed(self):
        return self.breed
    def getAge(self):
        return self.age
    def calcDoggyYears(self):
        oldness = self.getAge()
        return (int(oldness)*7)
    
    def setAge(self, age):
        self.age = age
    def live(self, ageMod):
        oldness = self.getAge()
        self.setAge(oldness + ageMod)
    

def main2():
    fido = Dog ("Poodle")
    pickle = Dog("Border Collie")
    fido.live(2)
    pickle.live(4)
    fido.live(4)
    print(fido.getBreed() + " is " + str(fido.getAge()) + " years old")
    fido.live(1)
    print(fido.getBreed() + " is " + str(fido.calcDoggyYears()) + " in people years.");
    print(pickle.getBreed() + " is " + str(pickle.calcDoggyYears()) + " in people years.");
main2()

##--Question Three--##

##In "won't compile" quarantine.

##import matplotlib.pyplot as plt
##import pandas as pd
##
##def main3():
##    data_frame = pd.read_csv("life.csv")
##    #I have no idea what I'm doing. This is fun.
##    
##    data_frame.plot.scatter(x="Age", y="% bald", c="black", s="star")
##    #Throws an error with 'sqrt' on my machine. I dunno-- No time left. I'm done.
##    
##    plt.title("Tracking Hunter's Hair")
##    plt.xlabel("Age")
##    plt.ylabel("% Bald")
##main3()



