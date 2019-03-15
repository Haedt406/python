scores = [0, 31, 27, 31, 49, 21, 17, 25]

wins = 0
losses = 0

while scores != []:
    if scores[0] > scores[1]:
        wins += 1
    else:
        losses += 1
    scores = scores[2:]

##for i in range(0, len(scores), 2):
##    if scores[i] > scores[i + 1]:
##         wins += 1
##    elif scores[i] < scores[i + 1]:
##        losses += 1
##    print(scores[i], scores [i + 1])
##    i + 1

print("MSU has", wins, "win(s) and", losses, "loss(es)")
