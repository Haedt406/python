# -----------------------------------------+                    ## the latest edit of this on 2/8/2019, i changed where points prints from, instead of printing form print_hand, 
# Benjamin Haedt                           |                    ## it now prints from evauluate_hand, i believe this was how it was intended in the assignment, the old code is commented out to show changes. 
# CSCI 127, Program 2                      |                    
# Last Updated: 28 January, 2019           |
# -----------------------------------------|
# A simplified Cribbage scoring system.    |
# -----------------------------------------+

def fifteen(hand):
        total = 0
        number = []
        for card in hand:                               #this for statement turns all the str data from hand and turns it into numbers, this could be simplified with a recursive function or loop, but i am unsure how to do this at this time.
                if card == "Two":
                       number.append(2)
                if card == "Three":
                        number.append(3)
                if card == "Four":
                        number.append(4)
                if card == "Five":
                        number.append(5)
                if card == "Six":
                        number.append(6)
                if card == "Seven":
                        number.append(7)
                if card == "Eight":
                        number.append(8)
                if card == "Nine":
                        number.append(9)
                if card == "Ten":
                        number.append(10)
                if card == "Jack":
                        number.append(10)
                if card == "Queen":
                        number.append(10)
                if card == "King":
                        number.append(10)
                if card == "Ace":
                        number.append(11)

        for i in range(len(number)):                    #takes the list of numbers and tries to add them all to eachother, when the sum of one pair == 15, it adds a value to the total
                                                        #since each card is checked against eachother twice, i add a value of one, and it will return the correct score of 2
                if number[i] + int(number[0]) == 15:
                         total += 1
                if number[i] + int(number[1]) == 15:
                        total += 1
                if number[i] + int(number[2]) == 15:
                        total += 1
                if number[i] + int(number[3]) == 15:
                        total += 1
                if number[i] + int(number[4]) == 15:
                        total += 1
        return total 


def pair(hand):
                                                        #should be self explanitory function, it counts the number of times a str is found in a list and returns the number of pairs based on an equation n(n-1)
        total = 0                                       #again, a loop would have made this a lot shorter and nicer, i was unsure how to do this
        count = hand.count("Two")
        total += int(count * (count - 1))
        count = hand.count("Three")
        total += int(count * (count - 1))
        count = hand.count("Four")
        total +=  int(count * (count - 1))
        count = hand.count("Five")
        total +=  int(count * (count - 1))
        count = hand.count("Six")
        total +=  int(count * (count - 1))
        count = hand.count("Seven")
        total +=  int(count * (count - 1))
        count = hand.count("Eight")
        total +=  int(count * (count - 1))
        count = hand.count("Nine")
        total +=  int(count * (count - 1))
        count = hand.count("Ten")
        total +=  int(count * (count - 1))
        count = hand.count("Jack")
        total +=  int(count * (count - 1))
        count = hand.count("Queen")
        total +=  int(count * (count - 1))
        count = hand.count("King")
        total +=  int(count * (count - 1))
        count = hand.count("Ace")
        total +=  int(count * (count - 1))
        return total
        
def flush(hand):                                        #also pretty easy, just counts each hand and if the count = 5 it returns a score of 5
        count_diamonds = hand.count('Diamonds')
        count_spades = hand.count('Spades')    
        count_clubs = hand.count('Clubs')
        count_hearts = hand.count('Hearts')
        if count_spades == 5:
            return 5 
        if count_clubs == 5:
            return 5
        if count_diamonds == 5:
            return 5
        if count_hearts == 5:
            return 5
        else:
            return 0


def print_hand(hand_as_list, number):                   #prints the hand with correct data from evaluate_hand
        hand = []
        for card in hand_as_list:
                hand.append(card[0])
                hand.append(card[1])
        print("Hand", str(number) + ":", str(hand[0]), str(hand[1]) + ",", str(hand[2]), str(hand[3]) + ",", str(hand[4]), str(hand[5]) + ",", str(hand[6]), str(hand[7]) + ",", str(hand[8]), str(hand[9]))
##        print("Points scored:" , evaluate_hand(hand_as_list))

def evaluate_hand(hand_as_list):                        #calls functions and collects the values to add to point total
        hand_numbers = []
        hand_suits = []
        points = 0
        for card in hand_as_list:
                hand_suits.append(card[1])
                hand_numbers.append(card[0])
        points += fifteen(hand_numbers)
        points += flush(hand_suits)
        points += pair(hand_numbers)
        print("Points scored:", points)
##        return points
     
# -----------------------------------------+
# Do not change anything below this line.  |
# -----------------------------------------+

def process_hands(cribbage_input, cards_in_hand):
    number = 1
    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0].capitalize(), hand[1].capitalize()])
            hand = hand[2:]
        print_hand(hand_as_list, number)
        evaluate_hand(hand_as_list)
        number += 1

# -----------------------------------------+

def main():
    cribbage_file= open("cribbage.txt", "r")
    process_hands(cribbage_file, 5)
    cribbage_file.close()

# -----------------------------------------+

main()
