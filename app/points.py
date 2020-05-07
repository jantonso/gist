#Style = Done
def points(players,stats,pointList,type_of_player,pointValues):
    if type_of_player == "Hitter":
        for i in xrange(len(players)):
            total = 0
            total += (int(stats[i][3]) * pointValues[1][1])
            #Runs
            total += (int(stats[i][4]) * pointValues[0][1])
            #Hrs
            total += (int(stats[i][5]) * pointValues[2][1])
            #RBIs
            total += (int(stats[i][6]) * pointValues[3][1])
            #SB
            pointList += [(total,players[i])]
        pointList.sort()
    else:
        for j in xrange(len(players)):
            total = 0
            total += (int(stats[j][1]) * pointValues[4][1])
            #Wins
            total += (int(stats[j][2]) * pointValues[6][1])
            #Saves
            total += (int(stats[j][3]) * pointValues[5][1])
            #StrikeOuts
            pointList += [(total,players[j])]
        pointList.sort()