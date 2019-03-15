class Card:
    """Card class for representing and manipulating one playing card"""

    def __init__(self, rank, suit):
        """A constructor method that sets the suit and rank"""
        self.suit = suit
        self.rank = rank
        self.value = self.assign_value(rank)

    def __str__(self):
        return self.rank.capitalize() + " of " + self.suit.capitalize()

    def get_suit(self):
        """A reader method that returns the suit of the card"""
        return self.suit

    def get_rank(self):
        """A reader method that returns the rank of the card"""
        return self.rank

    def get_value(self):
        """ A reader method that returns the blackjack value of the card"""
        return self.value

    def assign_value(self, rank):
        if self.rank == "two":
            return 2
        elif self.rank == "three":
            return 3
        elif self.rank == "four":
            return 4
        elif self.rank == "five":
            return 5
        elif self.rank == "six":
            return 6
        elif self.rank == "seven":
            return 7
        elif self.rank == "eight":
            return 8
        elif self.rank == "nine":
            return 9
        elif self.rank == "ace":
            return 11
        else:
            return 10
