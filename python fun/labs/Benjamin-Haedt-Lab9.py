score_differences = {}
score_differences["October 7, 2017"] = 8
score_differences["October 14, 2017"] = -12
score_differences["October 21, 2017"] = 3

wins = 0
losses = 0
for values in score_differences.values():
    if values > 0:
        wins += 1
    else:
        losses += 1

print(wins, "wins -", losses, "losses")


class Appliance():
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

class Refrigerator(Appliance):
    def __init__(self, manufacturer, coolant):
        Appliance.__init__(self,manufacturer)
        self.coolant = coolant
    def __str__(self):
        return ("The {} refrigerator contains refrigerant {}").format(self.manufacturer, self.coolant)


my_refrigerator = Refrigerator("Samsung", "R134a") # R134a is the refrigerant (cooling agent) used
print(my_refrigerator)
