#Style = done
def getPositionOfPitcher(players,stats,index_of_player):
    max_wins_for_starting_pitcher = 5
    if int(stats[index_of_player][1]) <= max_wins_for_starting_pitcher:
        if players[index_of_player] != "Travis Wood":
        #Only starting pitcher with less than 5 projected wins
            position = "RP"
        else:
            position = "SP"
    else: 
        if players[index_of_player] != "Tyler Clippard":
        #Only relief pitcher with more than 5 projected wins
            position = "SP"
        else:
            position = "RP"
    return position

#Style = done
def getPositionOfPlayer(name,players,stats,type_of_player):
#Returns the position of a player
    if type_of_player == "Hitter":
        for i in xrange(len(players)):
            if players[i] == name:
                index_of_player = i
                break
        position_of_player = stats[index_of_player][1]
        return position_of_player    
    else:
        for j in xrange(len(players)):
            if players[j] == name:
                index_of_player = j
                break
        position = getPositionOfPitcher(players,stats,index_of_player)
        return position 

#STyle = done
def checkUtilityAndBench(position_of_player,currentTeam,name):
    #if a player has not been added, check for the utility position    
    if position_of_player != "SP" and position_of_player != "RP":
        for index in xrange(len(currentTeam)):
            if currentTeam[index][0] == "Util" and currentTeam[index][1] == "Empty":
                currentTeam[index] = ["Util",name]
                return True
    #Checks to make sure that there isn't already a utility player
    for k in xrange(len(currentTeam)):
        if currentTeam[k][0] == "Bench" and currentTeam[k][1] == "Empty":
            currentTeam[k] = ["Bench",name]
            return True
    #Adds the player to the bench unless it is full
    return False

#Style = done
def addPlayerToCurrentTeam(name,players,stats,pointList,currentTeam,type_of_player,rivalTeam):
#Adds a player to the currentTeam only if position is not full   
    max_position_length = 4
    for i in xrange(len(players)):
        if players[i] == name:
            team = stats[i][0]
    if team == rivalTeam:
        return False
    #Checks to make sure that the player is not on your chosen rival team
    add_player_to_team = True
    position_of_player = getPositionOfPlayer(name,players,stats,type_of_player)
    if len(position_of_player) > max_position_length:
        return False
    #OF/3B/2B etc.
    elif position_of_player == 'DH':
        position_of_player = "Util"
    #For multiple position Players Must fix this later !!!!!!!!
    for j in xrange(len(currentTeam)):
        if position_of_player == currentTeam[j][0]:
            if currentTeam[j][1] == "Empty":
                currentTeam[j] = [position_of_player,name]
                return True
    if checkUtilityAndBench(position_of_player,currentTeam,name) == True:
        return True
    return False

###############################################################################

#Style = done
def checkFavoriteHitters(hitters,hitterStats,hitterPointList,pickedPlayers,favorite_team):
    top_ten = 10
    favorite_hitter = "None"
    for i in xrange(len(hitterPointList)):
        added_player = False
        player = hitterPointList[i][1]
        if player in pickedPlayers:
            continue
        new_index = hitters.index(player)
        j = 0
        tries = 0
        while j < top_ten:
            player = hitterPointList[i+tries+j][1]
            if player in pickedPlayers:
                tries += 1
                continue
            else:
                j += 1
                new_index = hitters.index(player)
                if hitterStats[new_index][0] == favorite_team:
                    favorite_hitter = (player,hitterPointList[i+tries+j][0])
                    break
            #Checks if any hitters in the top 10 are on the selected favorite team
        break
    return favorite_hitter

#Style = done
def checkFavoritePitchers(pitchers,pitcherStats,pitcherPointList,pickedPlayers,favorite_team):
    top_ten = 10
    favorite_pitcher = "None"
    for i in xrange(len(pitcherPointList)):
        added_player = False
        player = pitcherPointList[i][1]
        if player in pickedPlayers:
            continue
        new_index = pitchers.index(player)
        k = 0
        tries = 0
        while k < top_ten:
            player = pitcherPointList[i+tries+k][1]
            if player in pickedPlayers:
                tries += 1
                continue
            else:
                k += 1
                new_index = pitchers.index(player)
                if pitcherStats[new_index][0] == favorite_team:
                    favorite_pitcher = (player,pitcherPointList[i+tries+k][0])
                    break
        break
            #checks if any pitchers in the top 10 are from the selected Favorite Team 
    return favorite_pitcher

def comparePitcherAndHitter(favorite_pitcher,favorite_hitter,pickedPlayers,lastPicked,hitters,pitchers,hitterStats,pitcherStats,pitcherPointList,hitterPointList,currentTeam,rivalTeam):
    if favorite_pitcher[1] > favorite_hitter[1]:
        if addPlayerToCurrentTeam(favorite_pitcher[0],pitchers,pitcherStats,pitcherPointList,currentTeam,"Pitcher",rivalTeam) == True:
            pickedPlayers += [favorite_pitcher[0]]
            lastPicked[0] = favorite_pitcher[0]
            return True
            #favorite_pitcher has a better ranking
    else:
        if addPlayerToCurrentTeam(favorite_hitter[0],hitters,hitterStats,hitterPointList,currentTeam,"Hitter",rivalTeam) == True:
            pickedPlayers += [favorite_hitter[0]]
            lastPicked[0] = favorite_hitter[0]
            return True
            #favorite_hitter has a better ranking
    return False

#style = done
def makeFavoritePick(lastPicked,hitters,pitchers,hitterStats,pitcherStats,hitterPointList,pitcherPointList,currentTeam,pickedPlayers,favorite_team,rivalTeam):
    favorite_hitter = "None"
    favorite_pitcher = "None"
    favorite_hitter = checkFavoriteHitters(hitters,hitterStats,hitterPointList,pickedPlayers,favorite_team)
    favorite_pitcher = checkFavoritePitchers(pitchers,pitcherStats,pitcherPointList,pickedPlayers,favorite_team)
    if favorite_pitcher != "None" and favorite_hitter != "None":
        if comparePitcherAndHitter(favorite_pitcher,favorite_hitter,pickedPlayers,lastPicked,hitters,pitchers,hitterStats,pitcherStats,pitcherPointList,hitterPointList,currentTeam,rivalTeam) == True:
            return True
    elif favorite_pitcher != "None":
        if addPlayerToCurrentTeam(favorite_pitcher[0],pitchers,pitcherStats,pitcherPointList,currentTeam,"Pitcher",rivalTeam) == True:
                lastPicked[0] = favorite_pitcher[0]
                pickedPlayers += [lastPicked[0]]
                return True
                #There is only a favorite_pitcher
    elif favorite_hitter != "None":
        if addPlayerToCurrentTeam(favorite_hitter[0],hitters,hitterStats,hitterPointList,currentTeam,"Hitter",rivalTeam) == True:
                lastPicked[0] = favorite_hitter[0]
                pickedPlayers += [lastPicked[0]]
                return True
                #There is only a favorite_hitter
    return False
    #If there is no favorite player or if that player cannot be picked

def addPlayerToNonAutoDraftedTeam(name,players,stats,pointList,currentTeam,type_of_player):
    added_player = False
    position_of_player = getPositionOfPlayer(name,players,stats,type_of_player)
    if position_of_player == "DH":
        position_of_player = "Util"  
    for i in xrange(len(currentTeam)):
        if position_of_player == currentTeam[i][0]:
            if currentTeam[i][1] == "Empty":
                currentTeam[i] = [position_of_player,name]
                return True
    #If a player has not been added, check the utility spot
    if position_of_player != "SP" and position_of_player != "RP":
        for j in xrange(len(currentTeam)):
            if currentTeam[j][0] == "Util" and currentTeam[j][1] == "Empty":
                currentTeam[j] = ["Util",name]
                return True
    #Adds the player to the bench unless it is full
    for k in xrange(len(currentTeam)):
        if currentTeam[k][0] == "Bench" and currentTeam[k][1] == "Empty":
            currentTeam[k] = ["Bench",name]
            return True
    #Could not add the player
    return False

def makePick(autoDraftedTeam,hitters,pitchers,top_hundred_hitters,top_hundred_pitchers,hitterPointList,pitcherPointList,hitterStats,pitcherStats,currentTeam,rivalTeam,max_hitter_value,max_pitcher_value,pickedPlayers,lastPicked):
    made_pick = False
    hi,pi = 0,0
    #hitters/pitcher index
    hitter_index = hitters.index(top_hundred_hitters[hi])
    pitcher_index = pitchers.index(top_hundred_pitchers[pi])
    #Gets the actual index of the players in the player/stats lists
    check_hitters = hitterPointList[hitter_index][hi]
    check_pitchers = pitcherPointList[pitcher_index][pi]
    #Used to compare points values
    has_pitchers = False
    for i in xrange(len(autoDraftedTeam)):
        if autoDraftedTeam[i][0] == "SP" or autoDraftedTeam[i][0] == "RP":
            has_pitchers = True
    while made_pick != True:
        if has_pitchers == False:
            check_pitchers = -1
        if check_hitters > check_pitchers:
            if addPlayerToCurrentTeam(top_hundred_hitters[hi],hitters,hitterStats,hitterPointList,currentTeam,"Hitter",rivalTeam) == True:
                pickedPlayers += [top_hundred_hitters[hi]]
                lastPicked[0] = top_hundred_hitters[hi]
                made_pick = True
            else:
                hi += 1
                if hi == max_hitter_value:
                    check_hitters = -1
                    #-1 incase they don't assign a hitter category any points
        else:
            if addPlayerToCurrentTeam(top_hundred_pitchers[pi],pitchers,pitcherStats,pitcherPointList,currentTeam,"Pitcher",rivalTeam) == True:
                pickedPlayers += [top_hundred_pitchers[pi]]
                lastPicked[0] = top_hundred_pitchers[pi]
                made_pick = True
            else: 
                pi += 1
                if pi == max_pitcher_value:
                    check_pitchers = -1
                    #-1 incase they don't assign a pitcher category any points

def getHitters(hitterPointList,pickedPlayers):
    length = 100
    hitter_index = 0
    taken_hitters = 0
    top_hundred_hitters = []
    #Keeps track of hitters already picked
    for i in xrange(len(hitterPointList)):
        hitter = hitterPointList[i][1]
        if hitter in pickedPlayers:
            taken_hitters += 1
            continue
        else:
            hitter_index += 1
            top_hundred_hitters += [hitter]
            if hitter_index == (len(hitterPointList) - taken_hitters):
                max_hitter_value = hitter_index
            if hitter_index == length:
                max_hitter_value = length
                break
    return (max_hitter_value,top_hundred_hitters)

def getPitchers(pitcherPointList,pickedPlayers):
    length = 100
    taken_pitchers = 0
    #Keeps track of pitchers already picked
    pitcher_index = 0
    top_hundred_pitchers = []
    for k in xrange(len(pitcherPointList)):
        pitcher = pitcherPointList[k][1]
        if pitcher in pickedPlayers:
            taken_pitchers += 1
            continue
        else:
            pitcher_index += 1
            top_hundred_pitchers += [pitcher]
            if pitcher_index == (len(pitcherPointList)-taken_pitchers):
                max_pitcher_value = pitcher_index
                break
            elif pitcher_index == length:
                max_pitcher_value = length
                break
    return (max_pitcher_value,top_hundred_pitchers)

def makePointsPick(autoDraftedTeam,lastPicked,hitters,pitchers,hitterStats,pitcherStats,hitterPointList,pitcherPointList,currentTeam,pickedPlayers,favorite_team,rivalTeam):
    top_hundred_hitters = []
    top_hundred_pitchers = []
    length = 100
    made_pick = False
    if makeFavoritePick(lastPicked,hitters,pitchers,hitterStats,pitcherStats,hitterPointList,pitcherPointList,currentTeam,pickedPlayers,favorite_team,rivalTeam) == True:
        return True
    #No favorite player in the top 10 available pitchers/hitters
    else:
        (max_hitter_value,top_hundred_hitters) = getHitters(hitterPointList,pickedPlayers)
        (max_pitcher_value,top_hundred_pitchers) = getPitchers(pitcherPointList,pickedPlayers)
        makePick(autoDraftedTeam,hitters,pitchers,top_hundred_hitters,top_hundred_pitchers,hitterPointList,pitcherPointList,hitterStats,pitcherStats,currentTeam,rivalTeam,max_hitter_value,max_pitcher_value,pickedPlayers,lastPicked)

def tryFavoriteTeamPick(hitters,pitchers,hitterStats,pitcherStats,rotisseriePointsList,pickedPlayers,currentTeam,rival_team,i,favorite_team):
    favorite_team_check_length = 10
    for j in xrange(favorite_team_check_length):
        if rotisseriePointsList[i+j][1] in hitters:
            index = hitters.index(rotisseriePointsList[i+j][1])
            team = hitterStats[index][0]
            type_of_player = "Hitter"
        else:
            index = pitchers.index(rotisseriePointsList[i+j][1])
            team = pitcherStats[index][0]
            type_of_player = "Pitcher"
        if team == favorite_team:
            if type_of_player == "Hitter":
                if addPlayerToCurrentTeam(rotisseriePointsList[i+j][1],hitters,hitterStats,rotisseriePointsList,currentTeam,type_of_player,rival_team) == True:
                    pickedPlayers += [rotisseriePointsList[i+j][1]]
                    return True
            else:
                 if addPlayerToCurrentTeam(rotisseriePointsList[i+j][1],pitchers,pitcherStats,rotisseriePointsList,currentTeam,type_of_player,rival_team) == True:
                    pickedPlayers += [rotisseriePointsList[i+j][1]]
                    return True
    return False

def makeRotisseriePick(lastPicked,hitters,pitchers,hitterStats,pitcherStats,currentTeam,pickedPlayers,favorite_team,rival_team,projectedStats,rotisseriePointsList):
    for i in xrange(len(rotisseriePointsList)):
        if tryFavoriteTeamPick(hitters,pitchers,hitterStats,pitcherStats,rotisseriePointsList,pickedPlayers,currentTeam,rival_team,i,favorite_team) == True:
            return True
        elif rotisseriePointsList[i][1] in hitters:
            index = hitters.index(rotisseriePointsList[i][1])
            team = hitterStats[index][0]
            if team == rival_team:
                continue
            if addPlayerToCurrentTeam(rotisseriePointsList[i][1],hitters,hitterStats,rotisseriePointsList,currentTeam,"Hitter",rival_team) == True:
                pickedPlayers += [rotisseriePointsList[i][1]]
                return True
        else:
            index = pitchers.index(rotisseriePointsList[i][1])
            team = pitcherStats[index][0]
            if team == rival_team:
                continue
            if addPlayerToCurrentTeam(rotisseriePointsList[i][1],pitchers,pitcherStats,rotisseriePointsList,currentTeam,"Pitcher",rival_team) == True:
                pickedPlayers += [rotisseriePointsList[i][1]]
                return True
    return False