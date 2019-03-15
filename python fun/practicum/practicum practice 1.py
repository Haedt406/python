import turtle

def bobcat_line(alex, number, length):
    
    alex.goto(0,0)
    while number > 0:
        if number % 2 == 0:
            alex.color("blue")
        else:
            alex.color("gold")
        alex.forward(length)
        number =  number - 1
        print(str(number) + ' left')
##        alex.right(90)
    print('done')

number_segments = int(input("Enter number of segments: ")) # Assume the user will enter an integer >= 1
segment_length = int(input("Enter length of a segment: ")) # Assume the user will enter an integer >= 10
 
drawing_turtle = turtle.Turtle()
drawing_turtle.width(3)
drawing_turtle.hideturtle()
bobcat_line(drawing_turtle, number_segments, segment_length)
