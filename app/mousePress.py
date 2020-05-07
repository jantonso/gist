#Style = done
def checkPick(canvas,x,y):
    minX,maxX = 40,180
    minPickY,maxPickY = 247,562
    minIndexY,maxIndexY = 25,85
    if x >= minX and x <= maxX:
        if y >= minPickY and y <= maxPickY:
            canvas.data.pickPlayer = True
            canvas.data.x,canvas.data.y = x,y
    #Switches the team roster that is displayed
    if y >= minIndexY and y <= maxIndexY:
        for i in xrange(len(canvas.data.first_x_indexes)):
            if x >= canvas.data.first_x_indexes[i][0] and x <= canvas.data.first_x_indexes[i][1]:
                if type(canvas.data.teamPickOrder[i]) == str:
                    canvas.data.currentTeam = canvas.data.teamPickOrder[i]

#style = done
def favoriteTeamMousePress(canvas,x,y):
    minX,maxX = 735,745
    minY,maxY = 70,80
    if x >= minX and x <= maxX:
        if y >= minY and y <= maxY:
            if canvas.data.chooseFavoriteTeam == False:
                if canvas.data.rivalTeamDisplay == False:
                    canvas.data.chooseFavoriteTeam = True
                    canvas.data.lastChosen = "FavoriteTeam"
            else:
                canvas.data.chooseFavoriteTeam = False
                canvas.data.favoriteTeamDisplay = False
                canvas.data.favoriteTeam,canvas.data.selectedFavoriteTeam = "None","None"
        
#STyle = done
def rivalTeamMousePress(canvas,x,y):
    rivalMinX,rivalMaxX = 925,935
    rivalMinY,rivalMaxY = 70,80
    if x >= rivalMinX and x <= rivalMaxX:
        if y >= rivalMinY and y <= rivalMaxY:
            if canvas.data.chooseRivalTeam == False:
                if canvas.data.favoriteTeamDisplay == False:
                    canvas.data.chooseRivalTeam = True
                    canvas.data.rivalTeamDisplay = False
                    canvas.data.lastChosen = "RivalTeam"
            else:
                canvas.data.chooseRivalTeam = False
                canvas.data.rivalTeam,canvas.data.selectedRivalTeam = "None","None"
            
#Style = done
def numberOfTeamsMousePress(canvas,x,y):
    minY,maxY,fourMinX,fourMaxX,fiveMinX,fiveMaxX = 90,110,20,40,65,85
    sixMinX,sixMaxX,sevenMinX,sevenMaxX,eightMinX,eightMaxX = 110,130,155,175,200,220
    nineMinX,nineMaxX,tenMinX,tenMaxX,elevenMinX= 245,265,290,310,335
    elevenMaxX,twelveMinX,tweleveMaxX = 355,380,400
    if y >= minY and y <= maxY:
        if x >= fourMinX and x <= fourMaxX:
            canvas.data.numberOfTeams = 4
        elif x >= fiveMinX and x <= fiveMaxX:
            canvas.data.numberOfTeams = 5
        elif x >= sixMinX and x <= sixMaxX:
            canvas.data.numberOfTeams = 6
        elif x>= sevenMinX and x <= sevenMaxX:
            canvas.data.numberOfTeams = 7
        elif x>= eightMinX and x <= eightMaxX:
            canvas.data.numberOfTeams = 8
        elif x >= nineMinX and x <= nineMaxX:
            canvas.data.numberOfTeams = 9
        elif x >= tenMinX and x <= tenMaxX:
            canvas.data.numberOfTeams = 10
        elif x >= elevenMinX and x <= elevenMaxX:
            canvas.data.numberOfTeams = 11
        elif x >= twelveMinX and x <= tweleveMaxX:
            canvas.data.numberOfTeams = 12

#STyle = done
def numberOfSPRPOFMousePress(canvas,x,y):
    minX,maxX,column_step = 100,120,30
    minY,maxY,row_step = 170,190,30
    if x >= minX and x <= maxX:
        if y >= minY and y <= maxY:
            canvas.data.numberOfSP = 3
        elif y >= minY+row_step and y <= maxY+row_step:
            canvas.data.numberOfRP = 1
        elif y >= minY+2*row_step and y <= maxY+2*row_step:
            canvas.data.numberOfOF = 3
    elif x >= minX+column_step and x <= maxX+column_step:
        if y >= minY and y <= maxY:
            canvas.data.numberOfSP = 4
        elif y >= minY+row_step and y <= maxY+row_step:
            canvas.data.numberOfRP = 2
        elif y >= minY+2*row_step and y <= maxY+2*row_step:
            canvas.data.numberOfOF = 4
    elif x >= minX+2*column_step and x <= maxX+2*column_step:
        if y >= minY and y <= maxY:
            canvas.data.numberOfSP = 5
        elif y >= minY+row_step and y <= maxY+row_step:
            canvas.data.numberOfRP = 3
        elif y >= minY+2*row_step and y <= maxY+2*row_step:
            canvas.data.numberOfOF = 5

#Style = done
def numberOfUtilityAndBenchMousePress(canvas,x,y):
    minX,maxX,column_step = 340,360,30
    minY,maxY,row_step = 185,205,30
    if x >= minX and x <= maxX:
        if y >= minY and y <= maxY:
            canvas.data.numberOfUtil = 0
        elif y >= minY+row_step and y <= maxY+row_step:
            canvas.data.numberOfBench = 2
    elif x >= minX+column_step and x <= maxX+column_step:
        if y >= minY and y <= maxY:
            canvas.data.numberOfUtil = 1
        elif y >= minY+row_step and y <= maxY+row_step:
            canvas.data.numberOfBench = 3
    elif x >= minX+2*column_step and x <= maxX+2*column_step:
        if y >= minY and y <= maxY:
            canvas.data.numberOfUtil = 2
        elif y >= minY+row_step and y <= maxY+row_step:
            canvas.data.numberOfBench = 4

#STyle = done
def rotisserieOrPointsMousePress(canvas,x,y):
    minRotX,maxRotX = 115,125
    minPointsX,maxPointsX = 305,315
    minY,maxY = 375,385
    if x >= minRotX and x <= maxRotX:
        if y >= minY and y <= maxY:
            canvas.data.scoreSettings = "Rotisserie"
    elif x >= minPointsX and x <= maxPointsX:
        if y >= minY and y <= maxY:
            canvas.data.scoreSettings = "Points"

########################################################################

#Style = done
#Helper function for rotisserieSettingsMousePress
def checkFirstColumnHittingStats(canvas,x,y):
    minX,maxX = 70,80
    minAvgY,maxAvgY = 525,535
    minHRY,maxHRY = 545,555
    minRY,maxRY = 565,575
    if x >= minX and x <= maxX:
        if y >= minAvgY and y <= maxAvgY:
            if "AVG" in canvas.data.rotisserieSettings:
                canvas.data.rotisserieSettings.remove("AVG")
            else:
                canvas.data.rotisserieSettings += ["AVG"]
        elif y >= minHRY and y <= maxHRY:
            if "HR" in canvas.data.rotisserieSettings:
                canvas.data.rotisserieSettings.remove("HR")
            else:
                canvas.data.rotisserieSettings += ["HR"]
        elif y >= minRY and y <= maxRY:
            if "R" in canvas.data.rotisserieSettings:
                canvas.data.rotisserieSettings.remove("R")
            else:
                canvas.data.rotisserieSettings += ["R"]

#Style = done
#Helper function for rotisserieSettingsMousePress
def checkSecondColumnHittingStats(canvas,x,y):
    minX,maxX = 150,160
    minRBIY,maxRBIY = 525,535
    minSBY,maxSBY = 545,555
    if x >= minX and x <= maxX:
        if y >= minRBIY and y <= maxRBIY:
            if "RBI" in canvas.data.rotisserieSettings:
                canvas.data.rotisserieSettings.remove("RBI")
            else:
                canvas.data.rotisserieSettings += ["RBI"]
        elif y >= minSBY and y <= maxSBY:
            if "SB" in canvas.data.rotisserieSettings:
                canvas.data.rotisserieSettings.remove("SB")
            else:
                canvas.data.rotisserieSettings += ["SB"]

#Style = Done
#Helper function for rotisserieSettingsMousePress
def checkFirstColumnPitchingStats(canvas,x,y):
    minX,maxX = 270,280
    minWinY,maxWinY = 525,535
    minKY,maxKY = 545,555
    minERAY,maxERAY = 565,575
    if x >= minX and x <= maxX:
        if y >= minWinY and y <= maxWinY:
            if "W" in canvas.data.rotisserieSettings:
                canvas.data.rotisserieSettings.remove("W")
            else:
                canvas.data.rotisserieSettings += ["W"]
        elif y >= minKY and y <= maxKY:
            if "K" in canvas.data.rotisserieSettings:
                canvas.data.rotisserieSettings.remove("K")
            else:
                canvas.data.rotisserieSettings += ["K"]
        elif y >= minERAY and y <= maxERAY:
            if "ERA" in canvas.data.rotisserieSettings:
                canvas.data.rotisserieSettings.remove("ERA")
            else:
                canvas.data.rotisserieSettings += ["ERA"]

#STyle = Done
#Helper function for rotisserieSettingsMousePress
def checkSecondColumnPitchingStats(canvas,x,y):
    minX,maxX = 360,370
    minWhipY,maxWhipY = 525,535
    minSVY,maxSVY = 545,555
    if x >= minX and x <= maxX:
        if y >= minWhipY and y <= maxWhipY:
            if "WHIP" in canvas.data.rotisserieSettings:
                canvas.data.rotisserieSettings.remove("WHIP")
            else:
                canvas.data.rotisserieSettings += ["WHIP"]
        elif y >= minSVY and y <= maxSVY:
            if "SV" in canvas.data.rotisserieSettings:
                canvas.data.rotisserieSettings.remove("SV")
            else:
                canvas.data.rotisserieSettings += ["SV"]

def rotisserieSettingsMousePress(canvas,x,y):
    checkFirstColumnHittingStats(canvas,x,y)
    checkSecondColumnHittingStats(canvas,x,y)
    checkFirstColumnPitchingStats(canvas,x,y)
    checkSecondColumnPitchingStats(canvas,x,y)

###############################################################################
    
#Style = done
def enterValuesMousePress(canvas,x,y):
    minX,maxX,firstStep = 70,100,80
    minY,maxY,yStep = 515,535,30
    minSVX,maxSVX = 360,390
    minWKX,maxWKX = 270,300
    if x >= minX and x <= maxX:
        if y >= minY and y <= maxY:
            canvas.data.pointSettingsLast = "HR"
        elif y >= minY+yStep and y <= maxY+yStep:
            canvas.data.pointSettingsLast = "R"
    elif x >= minX+firstStep and x <= maxX+firstStep:
        if y >= minY and y <= maxY:
            canvas.data.pointSettingsLast = "RBI"
        elif y >= minY+yStep and y <= maxY+yStep:
            canvas.data.pointSettingsLast = "SB"
    elif x >= minWKX and x <= maxWKX:
        if y >= minY and y <= maxY:
            canvas.data.pointSettingsLast = "W"
        elif y >= minY+yStep and y <= maxY+yStep:
            canvas.data.pointSettingsLast = "K"
    elif x >= minSVX and x <= maxSVX:
        if y >= minY and y <= maxY:
            canvas.data.pointSettingsLast = "SV"

#Style = done
def focusMousePress(canvas,x,y):
    minPitchingX,maxPitchingX = 910,920
    minHittingX,maxHittingX = 715,725
    minY,maxY = 225,235
    if x >= minPitchingX and x <= maxPitchingX:
        if y >= minY and y <= maxY:
            if canvas.data.teamFocus == "Pitching":
                canvas.data.teamFocus = "None"
            else:
                canvas.data.teamFocus = "Pitching"
    elif x >= minHittingX and x <= maxHittingX:
        if y >= minY and y <= maxY:
            if canvas.data.teamFocus == "Hitting":
                canvas.data.teamFocus = "None"
            else:
                canvas.data.teamFocus = "Hitting"

###############################################################################

#Style = done
#Helper function for CHooseLeagueAndTeamMousePress
def setSelectedFavoriteTeam(canvas,x,y):
    minLeagueY,maxLeagueY = 415,445
    minTeamY,maxTeamY = 475,505
    if y >= minLeagueY and y <= maxLeagueY:
        if canvas.data.teamListDisplay == "NL":
            canvas.data.teamListDisplay = "AL"
            canvas.data.favoriteTeam = "None"
        else:
            canvas.data.teamListDisplay = "NL"
            canvas.data.favoriteTeam = "None"
    #A favorite team has been selected
    elif y >= minTeamY and y <= maxTeamY:
        if canvas.data.favoriteTeam != "None" and canvas.data.favoriteTeam != canvas.data.selectedRivalTeam:
            canvas.data.selectedFavoriteTeamLeague= canvas.data.teamListDisplay
            canvas.data.selectedFavoriteTeam = canvas.data.favoriteTeam
        else:
            canvas.data.favoriteTeam = "None"

#Style  = done
#Helper function for ChooseLeagueAndTeamMousePress
def setSelectedRivalTeam(canvas,x,y):
    minLeagueY,maxLeagueY = 415,445
    minTeamY,maxTeamY = 475,505
    if y >= minLeagueY and y <= maxLeagueY:
        if canvas.data.teamListDisplay == "NL":
            canvas.data.teamListDisplay = "AL"
            canvas.data.rivalTeam = "None"
        else:
            canvas.data.teamListDisplay = "NL"
            canvas.data.rivalTeam = "None"
    #A favorite team has been selected
    elif y >= minTeamY and y <= maxTeamY:
        if canvas.data.rivalTeam != "None" and canvas.data.rivalTeam != canvas.data.selectedFavoriteTeam:
            canvas.data.selectedRivalTeamLeague= canvas.data.teamListDisplay
            canvas.data.selectedRivalTeam = canvas.data.rivalTeam
        else:
            canvas.data.rivalTeam = "None"

#Style = Done
#Helper function for chooseFavoriteTeamMousePress
def chooseLeagueAndTeamMousePress(canvas,x,y,team,selectedTeam,selectedTeamLeague):
    minX,maxX = 820,930
    if team == canvas.data.favoriteTeam:
        if x >= minX and x <= maxX:
            #Change the leagues
            setSelectedFavoriteTeam(canvas,x,y)       
    else:
        if x >= minX and x <= maxX:
            #Change the leagues
            setSelectedRivalTeam(canvas,x,y)

#Style = Done
#Helper function for choose NL
def chooseNLWest(canvas,x,y,team):
    minLAD,maxLAD = 380,405
    minSF,maxSF = 405,430
    minARI,maxARI = 430,455
    minCOL,maxCOL = 455,480
    minSD,maxSD = 480,505
    if team == canvas.data.favoriteTeam:
        if y >= minLAD and y <= maxLAD:
            canvas.data.favoriteTeam = "LAD"
        elif y >= minSF and y <= maxSF:
            canvas.data.favoriteTeam = "SF"
        elif y >= minARI and y <= maxARI:
            canvas.data.favoriteTeam = "ARI"
        elif y >= minCOL and y <= maxCOL:
            canvas.data.favoriteTeam = "COL"
        elif y >= minSD and y <= maxSD:
            canvas.data.favoriteTeam = "SD"
    else:
        if y >= minLAD and y <= maxLAD:
            canvas.data.rivalTeam = "LAD"
        elif y >= minSF and y <= maxSF:
            canvas.data.rivalTeam = "SF"
        elif y >= minARI and y <= maxARI:
            canvas.data.rivalTeam = "ARI"
        elif y >= minCOL and y <= maxCOL:
            canvas.data.rivalTeam = "COL"
        elif y >= minSD and y <= maxSD:
            canvas.data.rivalTeam = "SD"

#Style = done
#Helper function for chooseNL
def chooseNLEast(canvas,x,y,team):
    minWSH,maxWSH = 380,405
    minATL,maxATL = 405,430
    minNYM,maxNYM = 430,455
    minPHI,maxPHI = 455,480
    minFLA,maxFLA = 480,505
    if team == canvas.data.favoriteTeam:
        if y >= minWSH and y <= maxWSH:
            canvas.data.favoriteTeam = "WSH"
        elif y >= minATL and y <= maxATL:
            canvas.data.favoriteTeam = "ATL"
        elif y >= minNYM and y <= maxNYM:
            canvas.data.favoriteTeam = "NYM"
        elif y >= minPHI and y <= maxPHI:
            canvas.data.favoriteTeam = "PHI"
        elif y >= minFLA and y <= maxFLA:
            canvas.data.favoriteTeam = "FLA"
    else:
        if y >= minWSH and y <= maxWSH:
            canvas.data.rivalTeam = "WSH"
        elif y >= minATL and y <= maxATL:
            canvas.data.rivalTeam = "ATL"
        elif y >= minNYM and y <= maxNYM:
            canvas.data.rivalTeam = "NYM"
        elif y >= minPHI and y <= maxPHI:
            canvas.data.rivalTeam = "PHI"
        elif y >= minFLA and y <= maxFLA:
            canvas.data.rivalTeam = "FLA"

#STyle = done
#Helper function for chooseNL
def chooseNLCentral(canvas,x,y,team):
    minSTL,maxSTL = 380,405
    minCIN,maxCIN = 405,430
    minMIL,maxMIL = 430,455
    minPIT,maxPIT = 455,480
    minHOU,maxHOU = 480,505
    minCHC,maxCHC = 505,530
    if team == canvas.data.favoriteTeam:
        if y >= minSTL and y <= maxSTL:
            canvas.data.favoriteTeam = "STL"
        elif y >= minCIN and y <= maxCIN:
            canvas.data.favoriteTeam = "CIN"
        elif y >= minMIL and y <= maxMIL:
            canvas.data.favoriteTeam = "MIL"
        elif y >= minPIT and y <= maxPIT:
            canvas.data.favoriteTeam = "PIT"
        elif y >= minHOU and y <= maxHOU:
            canvas.data.favoriteTeam = "HOU"
        elif y >= minCHC and y <= maxCHC:
            canvas.data.favoriteTeam = "CHC"
    else:
        if y >= minSTL and y <= maxSTL:
            canvas.data.rivalTeam = "STL"
        elif y >= minCIN and y <= maxCIN:
            canvas.data.rivalTeam = "CIN"
        elif y >= minMIL and y <= maxMIL:
            canvas.data.rivalTeam = "MIL"
        elif y >= minPIT and y <= maxPIT:
            canvas.data.rivalTeam = "PIT"
        elif y >= minHOU and y <= maxHOU:
            canvas.data.rivalTeam = "HOU"
        elif y >= minCHC and y <= maxCHC:
            canvas.data.rivalTeam = "CHC"

#style  = done
#Helper function for chooseFavoriteTeamMousePress
def chooseNL(canvas,x,y,team):
    minNLWest,maxNLWest = 580,620
    minNLCentral,maxNLCentral = 655,695
    minNLEast,maxNLEast = 730,770
    if x >= minNLWest and x <= maxNLWest:
        chooseNLWest(canvas,x,y,team)
    elif x >= minNLCentral and x <= maxNLCentral:
        chooseNLCentral(canvas,x,y,team)
    elif x >= minNLEast and x <= maxNLEast:
        chooseNLEast(canvas,x,y,team)

#STyle = done
#Helper function for chooseAL
def chooseALWest(canvas,x,y,team):
    minTEX,maxTEX = 380,405
    minOAK,maxOAK = 405,430
    minSEA,maxSEA = 430,455
    minLAA,maxLAA = 455,480
    if team == canvas.data.favoriteTeam:
        if y >= minTEX and y <= maxTEX:
            canvas.data.favoriteTeam = "TEX"
        elif y >= minOAK and y <= maxOAK:
            canvas.data.favoriteTeam = "OAK"
        elif y >= minSEA and y <= maxSEA:
            canvas.data.favoriteTeam = "SEA"
        elif y >= minLAA and y <= maxLAA:
            canvas.data.favoriteTeam = "LAA"
    else:
        if y >= minTEX and y <= maxTEX:
            canvas.data.rivalTeam = "TEX"
        elif y >= minOAK and y <= maxOAK:
            canvas.data.rivalTeam = "OAK"
        elif y >= minSEA and y <= maxSEA:
            canvas.data.rivalTeam = "SEA"
        elif y >= minLAA and y <= maxLAA:
            canvas.data.rivalTeam = "LAA"

#Style = done
#Helper function for chooseAL
def chooseALEast(canvas,x,y,team):
    minTB,maxTB = 380,405
    minBAL,maxBAL = 405,430
    minNYY,maxNYY = 430,455
    minTOR,maxTOR = 455,480
    minBOS,maxBOS = 480,505
    if team == canvas.data.favoriteTeam:
        if y >= minTB and y <= maxTB:
            canvas.data.favoriteTeam = "TB"
        elif y >= minBAL and y <= maxBAL:
            canvas.data.favoriteTeam = "BAL"
        elif y >= minNYY and y <= maxNYY:
            canvas.data.favoriteTeam = "NYY"
        elif y >= minTOR and y <= maxTOR:
            canvas.data.favoriteTeam = "TOR"
        elif y >= minBOS and y <= maxBOS:
            canvas.data.favoriteTeam = "BOS"  
    else:
        if y >= minTB and y <= maxTB:
            canvas.data.rivalTeam = "TB"
        elif y >= minBAL and y <= maxBAL:
            canvas.data.rivalTeam = "BAL"
        elif y >= minNYY and y <= maxNYY:
            canvas.data.rivalTeam = "NYY"
        elif y >= minTOR and y <= maxTOR:
            canvas.data.rivalTeam = "TOR"
        elif y >= minBOS and y <= maxBOS:
            canvas.data.rivalTeam = "BOS"

#Style = done
#Helper function for chooseAL
def chooseALCentral(canvas,x,y,team):
    minCLE,maxCLE = 380,405
    minCWS,maxCWS = 405,430
    minDET,maxDET = 430,455
    minKC,maxKC = 455,480
    minMIN,maxMIN = 480,505
    if team == canvas.data.favoriteTeam:
        if y >= minCLE and y <= maxCLE:
            canvas.data.favoriteTeam = "CLE"
        elif y >= minCWS and y <= maxCWS:
            canvas.data.favoriteTeam = "CWS"
        elif y >= minDET and y <= maxDET:
            canvas.data.favoriteTeam = "DET"
        elif y >= minKC and y <= maxKC:
            canvas.data.favoriteTeam = "KC"
        elif y >= minMIN and y <= maxMIN:
            canvas.data.favoriteTeam = "MIN"
    else:
        if y >= minCLE and y <= maxCLE:
            canvas.data.rivalTeam = "CLE"
        elif y >= minCWS and y <= maxCWS:
            canvas.data.rivalTeam = "CWS"
        elif y >= minDET and y <= maxDET:
            canvas.data.rivalTeam = "DET"
        elif y >= minKC and y <= maxKC:
            canvas.data.rivalTeam = "KC"
        elif y >= minMIN and y <= maxMIN:
            canvas.data.rivalTeam = "MIN"

#Style = Done
#Helper function for chooseFavoriteTeamMousePress
def chooseAL(canvas,x,y,team):
    minALWest,maxALWest = 580,620
    minALCentral,maxALCentral = 655,695
    minALEast,maxALEast = 730,770
    if x >= minALWest and x <= maxALWest:
        chooseALWest(canvas,x,y,team)
    elif x >= minALCentral and x <= maxALCentral:
        chooseALCentral(canvas,x,y,team)
    elif x >= minALEast and x <= maxALEast:
        chooseALEast(canvas,x,y,team)

#Style = Done 
def chooseFavoriteTeamMousePress(canvas,x,y):
    if canvas.data.lastChosen == "FavoriteTeam":
        chooseLeagueAndTeamMousePress(canvas,x,y,canvas.data.favoriteTeam,canvas.data.selectedFavoriteTeam,canvas.data.selectedFavoriteTeamLeague)
        if canvas.data.teamListDisplay == "NL":
            chooseNL(canvas,x,y,canvas.data.favoriteTeam)
        else:
            chooseAL(canvas,x,y,canvas.data.favoriteTeam)

#Style = Done
def chooseRivalTeamMousePress(canvas,x,y):
    if canvas.data.lastChosen == "RivalTeam":
        chooseLeagueAndTeamMousePress(canvas,x,y,canvas.data.rivalTeam,canvas.data.selectedRivalTeam,canvas.data.selectedRivalTeamLeague)
        if canvas.data.teamListDisplay == "NL":
            chooseNL(canvas,x,y,canvas.data.rivalTeam)
        else:
            chooseAL(canvas,x,y,canvas.data.rivalTeam)

###############################################################################

def addRosters(canvas):
    canvas.data.autoDraftedTeam = [["C","Empty"],["1B","Empty"],["2B","Empty"],["SS","Empty"],["3B","Empty"]]
    canvas.data.autoDraftedTeam += [["OF","Empty"]]*canvas.data.numberOfOF
    canvas.data.autoDraftedTeam += [["SP","Empty"]]*canvas.data.numberOfSP
    canvas.data.autoDraftedTeam += [["RP","Empty"]]*canvas.data.numberOfRP
    if canvas.data.numberOfUtil != 3:
        canvas.data.autoDraftedTeam += [["Util","Empty"]]*canvas.data.numberOfUtil
    canvas.data.autoDraftedTeam += [["Bench","Empty"]]*canvas.data.numberOfBench
    #Changes the team rosters based on the chosen numbers at each position