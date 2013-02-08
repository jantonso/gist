#Style = Super Long Functions
import copy

#STyle = done
#Helper function for makeRotisseriePoints
def findHitterStat(j):
    if j < 2 or j > 6:
        stat = "None"
    elif j == 2:
        stat = "AVG"
    elif j == 3:
        stat = "R"
    elif j == 4:
        stat = "HR"
    elif j == 5:
        stat = "RBI"
    elif j == 6:
        stat = "SB"
    return stat

#STyle = done
#Helper function for makeRotisseriePoints
def findPitcherStat(j):
    if j < 1 or j > 5:
        stat = "None"
    elif j == 1:
        stat = "W"
    elif j == 2:
        stat = "SV"
    elif j == 3:
        stat = "K"
    elif j == 4:
        stat = "ERA"
    elif j == 5:
        stat = "WHIP"
    return stat

#Style = too long lines
#Helper function for makeRotisseriePoints
def addHitterValues(hitters,hitterStats,pickedPlayers,rotisserie_stats,rotisserieSettings,BA_multiplier,BA_divisor,rank,all_players_values):
    for i in xrange(len(hitterStats)):
        if hitters[i] in pickedPlayers:
            continue
        else:
            player_value = 0
            individual_stats = copy.deepcopy(rotisserie_stats)
            for j in xrange(len(hitterStats[i])):
                stat = findHitterStat(j)
                if stat not in rotisserieSettings:
                    continue
                else:   
                    stats_index = rotisserieSettings.index(stat)
                    individual_stats[stats_index] = hitterStats[i][j]
            for k in xrange(len(rotisserie_stats)):
                if type(individual_stats[k]) == str:
                    if rotisserieSettings[k] == 'AVG':
                        player_value += (((float(individual_stats[k])*
                                           BA_multiplier)/BA_divisor)*rank[k][0])
                        #Since Batting average is normally around .300, this normalizes .300 to equal 100 points
                    else:
                        player_value += (float(individual_stats[k])*rank[k][0])
            all_players_values += [[player_value,hitters[i]]]

#Style = too long lines
#Helper function for makeRotisseriePoints
def addPitcherValues(pitchers,pitcherStats,pickedPlayers,rotisserie_stats,rotisserieSettings,pitching_multiplier,max_ERA,max_WHIP,min_ERA,min_WHIP,rank,all_players_values):
    for i in xrange(len(pitcherStats)):
        if pitchers[i] in pickedPlayers:
            continue
        else:
            player_value = 0
            individual_stats = copy.deepcopy(rotisserie_stats)
            for j in xrange(len(pitcherStats[i])):
                stat = findPitcherStat(j)
                if stat not in rotisserieSettings:
                    continue
                else:   
                    stat_index = rotisserieSettings.index(stat)
                    individual_stats[stat_index] = pitcherStats[i][j]
            for k in xrange(len(rotisserie_stats)):
                if type(individual_stats[k]) == str:
                    if rotisserieSettings[k] == "ERA":
                        if float(individual_stats[k]) > min_ERA:
                            player_value += ((max_ERA-(float(individual_stats[k])*pitching_multiplier))*rank[k][0])
                        else:
                            player_value += (float(individual_stats[k])*pitching_multiplier)*rank[k][0]
                    elif rotisserieSettings[k] == "WHIP":
                        if float(individual_stats[k]) > min_WHIP:
                            player_value += ((max_WHIP-(float(individual_stats[k])*pitching_multiplier))*rank[k][0])    
                    #Since we want ERA and WHIP to be as low as possible
                    else:
                        player_value += (float(individual_stats[k])*rank[k][0])
            all_players_values += [[player_value,pitchers[i]]]

#Style = done
def makeRotisseriePoints(lastPicked,hitters,pitchers,hitterStats,pitcherStats,currentTeam,pickedPlayers,favorite_team,rival_team,projectedStats,rosterOrder,rotisserieSettings):
    rank = calculateStatValues(projectedStats,rosterOrder,rotisserieSettings)
    rotisserie_stats = []
    all_players_values = []
    BA_multiplier = 1000
    BA_divisor = 3
    for stats in rotisserieSettings:
        rotisserie_stats += [[]]
    addHitterValues(hitters,hitterStats,pickedPlayers,rotisserie_stats,rotisserieSettings,BA_multiplier,BA_divisor,rank,all_players_values)
    pitching_multiplier = 100
    max_ERA = 500
    max_WHIP = 200
    min_ERA = 2.0
    min_WHIP = 0.75
    addPitcherValues(pitchers,pitcherStats,pickedPlayers,rotisserie_stats,rotisserieSettings,pitching_multiplier,max_ERA,max_WHIP,min_ERA,min_WHIP,rank,all_players_values)
    all_players_values = sorted(all_players_values)
    all_players_values = all_players_values[::-1]
    return all_players_values

#style = done
def calculateStatValues(projectedStats,rosterOrder,rotisserieSettings):
    stats = []
    rank = []
    for i in xrange(len(rotisserieSettings)):
        stats += [[]]
        rank += [[1]]
    for j in xrange(len(projectedStats)):
        for i in xrange(len(projectedStats[j])):
            stats[i] += [[projectedStats[j][i][1],rosterOrder[j]]]
    for k in xrange(len(stats)):
        for l in xrange(len(stats[k])):
            if stats[k][l][1] != "Team 2":
                if stats[k][l][0] > stats[k][1][0]:
                    rank[k][0] += 1
    return rank
    #This gives you a ranking based on your stats compared to the rest of the teams
    #1 means you're the best in that category, up to the number of teams+1

#Style = done
def addHitterStats(name,players,stats,teamStats,currentTeam,projectedStats,rosterOrder,averageBA):
    total_AVG = 0
    for i in xrange(len(players)):
        if name == players[i]:
            player_index = i
    team_index = rosterOrder.index(currentTeam)
    for stat in projectedStats[team_index]:
        if stat[0] == "AVG":
            averageBA += [float(stats[player_index][2])]
            for AVG in averageBA:
                total_AVG += AVG
            stat[1] = (total_AVG / len(averageBA))
            #Calculates the average batting average
        elif stat[0] == "R":
            stat[1] = stat[1] + (int(stats[player_index][3]))
        elif stat[0] == "HR":
            stat[1] = stat[1] + (int(stats[player_index][4]))
        elif stat[0] == "RBI":
            stat[1] = stat[1] + (int(stats[player_index][5]))
        elif stat[0] == "SB":
            stat[1] = stat[1] + (int(stats[player_index][6]))

#Style = done
def addPitcherStats(name,players,stats,teamStats,currentTeam,projectedStats,rosterOrder,averageWHIP,averageERA):
    total_ERA = 0
    total_WHIP = 0
    for i in xrange(len(players)):
        if name == players[i]:
            player_index = i
    team_index = rosterOrder.index(currentTeam)
    for stat in projectedStats[team_index]:
        if stat[0] == "W":
            stat[1] = stat[1] + (int(stats[player_index][1]))
        elif stat[0] == "SV":
            stat[1] = stat[1] + (int(stats[player_index][2]))
        elif stat[0] == "K":
            stat[1] = stat[1] + (int(stats[player_index][3]))
        elif stat[0] == "ERA":
            averageERA += [float(stats[player_index][4])]
            for ERA in averageERA:
                total_ERA += ERA
            stat[1] = (total_ERA / len(averageERA))
            #Calculates the average ERA
        elif stat[0] == "WHIP":
            averageWHIP += [float(stats[player_index][5])]
            for WHIP in averageWHIP:
                total_WHIP += WHIP
            stat[1] = (total_WHIP / len(averageWHIP))
            #Calculates the average WHIP