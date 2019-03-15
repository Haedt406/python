##import math
##
##def main():   
##    Quizzes = int(input("How many quizzes did you have? "))
##    step = 0
##    QScore = 0
##    QTotalScore = 0
##    quizAverage = 0
##    finalExam = 0
##    for i in range(0, Quizzes):
##        step = step + 1
##        QScore = int(input(("What was your score on quiz ")+str(step)+("? ")))
##        QTotalScore = QTotalScore + QScore
##    quizAverage = float((QTotalScore)/(Quizzes))
##    finalExam = float(input("What was your score on the final exam? "))
##    GradePercentage = ((finalExam * 0.6)+(quizAverage*0.4))
##    print(("Your final grade percentage: ")+str(GradePercentage))
##main()


import turtle

def imprint(turtleName, xCoord, yCoord, color):
    turtleName.color = color
    turtleName.pu()
    turtleName.goto((xCoord), (yCoord))
    turtleName.pd()
    turtleName.stamp()
    turtleName.pu()

some_turtle = turtle.Turtle()
some_turtle.shape("turtle")
some_turtle.hideturtle()

imprint(some_turtle, 0, 0, "red")
imprint(some_turtle, 100, -50, "blue")
imprint(some_turtle, -75, -25, "purple")
