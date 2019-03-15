def cribbage_sequence(card_list):
    test = (card_list[0] + card_list[1] + card_list[2]) / 3
    if test == card_list[0]:
        return True
    elif test == card_list[1]:
        return True
    elif test == card_list[2]:
        return True
    else:
        return False
    




card_list = [2,3,1]
print (cribbage_sequence(card_list))
