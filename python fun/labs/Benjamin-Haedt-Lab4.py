# --------------------------------------
# CSCI 127, Lab 4
# February 7, 2019
# Benjamin Haedt
# --------------------------------------

def process_season(season, games_played, points_earned):
    wins = 0
    loss = 0
    tie = 0
    x = True
    count = 0
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
              ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")
    while x == True:
        wins = points_earned // 3 - count
        tie = points_earned % 3 + (count * 3)
        loss = games_played - (wins + tie)
        count += 1
        if wins <= 0 or loss <= 0:
            x = False
        print(wins, " - ", tie, " - ",  loss)


    print()

# --------------------------------------

def process_seasons(seasons):

    for i in range(len(seasons)):
        games_played = seasons[i][0]
        points_earned = seasons[i][1]
        process_season(i, games_played, points_earned)

# --------------------------------------

def main():
    # format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]
    process_seasons(soccer_seasons)
    

# --------------------------------------

main()
