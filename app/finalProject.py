#Josh Antonson, section G, jantonso

import string
import copy      
from points import points
from addFavorite import *
from playersStatsPoints import *
from rotisseriePoints import *
from draw import *

#Style = Done
def getDesktopPath(filename = ""):
    # next line is odd, but works in Windows/Mac/Linux
    homepath = os.getenv('USERPROFILE') or os.getenv('HOME')
    return homepath + os.sep + "term_project" + os.sep + filename
#Used to have images from online

from Tkinter import *

###############################################################################

#Button Callbacks

#Style = Done
def nextTwenty():
    maxHitterPage = 11
    maxPitcherPage = 7
    if canvas.data.display == "Hitters":
        if canvas.data.statsPageNumber < maxHitterPage:
            canvas.data.statsPageNumber += 1
    else:
        if canvas.data.statsPageNumber < maxPitcherPage:
            canvas.data.statsPageNumber += 1

#Style = Done
def previousTwenty():
    if canvas.data.statsPageNumber > 0:
        canvas.data.statsPageNumber -= 1

#Style = Done
def changeTypeOfPlayer():
    if canvas.data.display == "Hitters":
        canvas.data.display = "Pitchers"
    else:
        canvas.data.display = "Hitters"
    canvas.data.statsPageNumber = 0

#Style = Done
def PreviousTwentyFive():
    if canvas.data.pickedPageNumber > 0:
        canvas.data.pickedPageNumber -= 1

#Style = Done, one line is 93
def nextTwentyFive():
    playersPerPage = 25
    if (canvas.data.pickedPageNumber+1)*playersPerPage < len(canvas.data.pickedPlayersList):
         canvas.data.pickedPageNumber += 1

###############################################################################

from mousePress import *

#Style = too long lines
#Helper function for enterDraft
def createRosters(canvas):
    indexLeft,indexRight,size = 25,75,60
    if canvas.data.scoreSettings == "Points":
        points(canvas.data.hitterList,canvas.data.hitterStats,canvas.data.hitterPointList,canvas.data.hitter,canvas.data.pointSettings)
        points(canvas.data.pitcherList,canvas.data.pitcherStats,canvas.data.pitcherPointList,canvas.data.pitcher,canvas.data.pointSettings)
        #Creates the point list if the user has chosen the pointSettings
        canvas.data.hitterPointList = canvas.data.hitterPointList[::-1]
        canvas.data.pitcherPointList = canvas.data.pitcherPointList[::-1]
        #So that it is sorted from high to low instead of low to high
    else:
        temp_settings = []
        for j in xrange(len(canvas.data.rotisserieSettings)):
            temp_settings += [[copy.deepcopy(canvas.data.rotisserieSettings[j]),0]]
        for i in xrange(canvas.data.numberOfTeams):
            canvas.data.projectedStats += [copy.deepcopy(temp_settings)]
        #Make a list with the stats for each team
    for i in xrange(2*canvas.data.numberOfTeams+2):
        canvas.data.first_x_indexes += [[indexLeft+size*i,indexRight+size*i]]
    #Creates a list of the x-indexes used to see if a team's roster has been selected to display
    for i in xrange(canvas.data.numberOfTeams):
        canvas.data.allTeams += [copy.deepcopy(canvas.data.autoDraftedTeam)]
    #Creates a list of the rosters of each team
    createPickOrder(canvas)
    
#Style = done
#Helper function for createRosters
def createPickOrder(canvas):
    for i in xrange(1,canvas.data.numberOfTeams+1):
        canvas.data.pickNumber += [i]
        canvas.data.teamPickOrder += ["Team " + str(i)]
        canvas.data.teamRosterOrder += ["Team " + str(i)]
    canvas.data.pickNumber += ["Round"]
    canvas.data.teamPickOrder += [2]
    for j in xrange(canvas.data.numberOfTeams,0,-1):
        canvas.data.pickNumber += [j]
        canvas.data.teamPickOrder += ["Team " + str(j)]
    canvas.data.pickNumber += ["Round"]
    canvas.data.teamPickOrder += [3]
    #Properly creates the pickNumber and pickOrder lists

#Style = Done, one line is 90
def enterDraft(canvas,x,y):
    xmin,xmax,ymin,ymax = 770,930,545,585
    minimumNumberOfTeams = 3
    if x >= xmin and x <= xmax:
        if y >= ymin and y <= ymax:
            if canvas.data.numberOfTeams > minimumNumberOfTeams:
                canvas.data.missingTeams = False
                if canvas.data.scoreSettings != "None":
                    canvas.data.missingTeams,canvas.data.missingScoreSettings = False,False
                    missingPoints()
                    if (canvas.data.pitchingPoint == True and canvas.data.hittingPoint == True) or (canvas.data.hittingRotisserie == True and canvas.data.pitchingRotisserie == True):
                        createRosters(canvas)
                        canvas.data.settingsScreen = False
                        #Makes sure all the tests are passed
                else:
                    canvas.data.missingScoreSettings = True                    
            else:
                if canvas.data.scoreSettings == "None":
                    canvas.data.missingScoreSettings = True
                else:
                    canvas.data.missingScoreSettings = False
                    missingPoints()
                canvas.data.missingTeams = True

#Style = Done
def mousePressed(event):
    #Checks if a pick has been made/ updates team
    if canvas.data.settingsScreen == False:
        checkPick(canvas,event.x,event.y)
    else:
        #Checks if we can enter the draft and does so if possible
        enterDraft(canvas,event.x,event.y)
        #Choose a favorite team
        favoriteTeamMousePress(canvas,event.x,event.y)
        #Choose a rival team
        rivalTeamMousePress(canvas,event.x,event.y)
        #Choose the number of teams
        numberOfTeamsMousePress(canvas,event.x,event.y)
        #Choose the number of SP,RP,OF
        numberOfSPRPOFMousePress(canvas,event.x,event.y)
        #Choose the number of Utility and Bench
        numberOfUtilityAndBenchMousePress(canvas,event.x,event.y)
        #Choose whether rotisserie or points settings
        rotisserieOrPointsMousePress(canvas,event.x,event.y)
        #Choose rotisserie settings
        rotisserieSettingsMousePress(canvas,event.x,event.y)
        #Enter Values for each point setting
        enterValuesMousePress(canvas,event.x,event.y)
        #Choose whether team focus is hitting or pitching
        focusMousePress(canvas,event.x,event.y)
        #Checks if the user has selected their favorite team from the list of teams
        chooseFavoriteTeamMousePress(canvas,event.x,event.y)
        #Checks if the user has selected their rival team from the list of teams
        chooseRivalTeamMousePress(canvas,event.x,event.y)
        #Adds the rosters
        addRosters(canvas)
    redrawAll()

###############################################################################

#Style = Done
def keyPressed(event):
    if event.keysym in string.digits:
            for i in xrange(len(canvas.data.pointSettings)):
                if canvas.data.pointSettingsLast == canvas.data.pointSettings[i][0]:
                    canvas.data.pointSettings[i][1] = int(event.keysym)
    #Let's the user type in values for each point setting
    if (event.char == 'p'):
        if canvas.data.paused == False:
            canvas.data.paused = True
        else:
            canvas.data.paused = False
    redrawAll()

###############################################################################

#Style = too long lines
#Helper function for timerFired
def changePickOrder():
    time = 50
    if canvas.data.pickNumber[0] == "Round":
        canvas.data.pickNumber = canvas.data.pickNumber[1:] + [canvas.data.pickNumber[0]]
    if type(canvas.data.teamPickOrder[0]) != str:
        canvas.data.teamPickOrder = canvas.data.teamPickOrder[1:] + [canvas.data.teamPickOrder[0]+2]
    #Makes sure that once the Round Number is the first element, it becomes the last element
    if canvas.data.paused == False:
        if canvas.data.time[1] % 2 == 0:
            canvas.data.time[0] -= 1
        #In order to get the clock to count down in seconds
        canvas.data.time[1] += 1
        if canvas.data.time[0]== 0:
            canvas.data.time[0] = time
            canvas.data.teamPickOrder = canvas.data.teamPickOrder[1:] + [canvas.data.teamPickOrder[0]]
            if canvas.data.pickNumber[-1] != 'Round':
                canvas.data.pickNumber = canvas.data.pickNumber[1:] + [canvas.data.pickNumber[-1]+1]
            else:
                canvas.data.pickNumber = canvas.data.pickNumber[1:] + [canvas.data.pickNumber[-2]+1]
        #Accounts for when the last element is "Round"
    #This is a snake style draft, so it will go to the end and then snake back around
    #Basically like 1,2,3,4,5,5,4,3,2,1,1,2,3,etc.

#Style = too long lines
#Helper function for timerFired
def calculateLastPicked():
    maxY = 559
    offset = 262
    size = 15
    playersPerPage = 20
    if canvas.data.y > maxY:
        canvas.data.y = maxY
    #Accounts for the player on the bottom having a larger box
    canvas.data.pickedPlayerIndex = (canvas.data.y - offset) / size
    if canvas.data.display == "Hitters":
        canvas.data.lastPicked[0] = canvas.data.hitterList[canvas.data.statsPageNumber*playersPerPage+canvas.data.pickedPlayerIndex]
    else:
        canvas.data.lastPicked[0] = canvas.data.pitcherList[canvas.data.statsPageNumber*playersPerPage+canvas.data.pickedPlayerIndex]
    #Determines if the last picked player is a hitter or pitcher

#Style = too long lines
#Helper function for timerFired
def addPlayer():
    added_player = False
    team_index = canvas.data.teamRosterOrder.index(canvas.data.teamPickOrder[0])
    #Find the index of the current team in the rosters for all teams
    if canvas.data.display == "Hitters":
        if addPlayerToNonAutoDraftedTeam(canvas.data.lastPicked[0],canvas.data.hitterList,canvas.data.hitterStats,canvas.data.hitterPointList,canvas.data.allTeams[team_index],"Hitter") == True:
            added_player = True
    else:
        if addPlayerToNonAutoDraftedTeam(canvas.data.lastPicked[0],canvas.data.pitcherList,canvas.data.pitcherStats,canvas.data.pitcherPointList,canvas.data.allTeams[team_index],"Pitcher") == True:
            added_player = True
        #Adds the player to the roster for that team
    if added_player == True:
        if canvas.data.scoreSettings == "Rotisserie":
            if canvas.data.display == "Pitchers":
                addPitcherStats(canvas.data.lastPicked[0],canvas.data.pitcherList,canvas.data.pitcherStats,canvas.data.projectedStats,canvas.data.teamPickOrder[0],canvas.data.projectedStats,canvas.data.teamRosterOrder,canvas.data.averageWHIP,canvas.data.averageERA)
            else:
                addHitterStats(canvas.data.lastPicked[0],canvas.data.hitterList,canvas.data.hitterStats,canvas.data.projectedStats,canvas.data.teamPickOrder[0],canvas.data.projectedStats,canvas.data.teamRosterOrder,canvas.data.averageBA)
        return True
    return False

#Style = too long lines
#Helper function for timerFired
def updatePickOrder(player):
    time = 50
    canvas.data.teamPickOrder = canvas.data.teamPickOrder[1:] + [canvas.data.teamPickOrder[0]]
    if canvas.data.pickNumber[-1] != 'Round':
        canvas.data.pickNumber = canvas.data.pickNumber[1:] + [canvas.data.pickNumber[-1]+1]
    else:
        canvas.data.pickNumber = canvas.data.pickNumber[1:] + [canvas.data.pickNumber[-2]+1]
    #Accounts for when the last element of pickNumber is "Round"
    if player == True:
        canvas.data.pickedPlayersList += [canvas.data.lastPicked[0]]
        #Add the player to the list of drafted players
    if canvas.data.paused == False:
        canvas.data.time[0] = time
    #Reset the pick timer

#Style = too long of lines
#Helper function for timerFired
def makeAutoDraftPick():
    team_index = canvas.data.teamRosterOrder.index(canvas.data.teamPickOrder[0])
    #Gets the index of the team's roster in the list of all the teams rosters
    if canvas.data.scoreSettings == "Points":
        makePointsPick(canvas.data.autoDraftedTeam,canvas.data.lastPicked,canvas.data.hitterList,canvas.data.pitcherList,canvas.data.hitterStats,canvas.data.pitcherStats,canvas.data.hitterPointList,canvas.data.pitcherPointList,canvas.data.allTeams[team_index],canvas.data.pickedPlayersList,canvas.data.selectedFavoriteTeam,canvas.data.selectedRivalTeam)
    #Actually make the autopick and then go on to the next team       
    else:
        calculateStatValues(canvas.data.projectedStats,canvas.data.teamRosterOrder,canvas.data.rotisserieSettings)
        #Calculate your current rankings for each stat
        canvas.data.rotisseriePointsList = makeRotisseriePoints(canvas.data.lastPicked,canvas.data.hitterList,canvas.data.pitcherList,canvas.data.hitterStats,canvas.data.pitcherStats,canvas.data.teamPickOrder[0],canvas.data.pickedPlayersList,canvas.data.favoriteTeam,canvas.data.rivalTeam,canvas.data.projectedStats,canvas.data.teamRosterOrder,canvas.data.rotisserieSettings)
        #make the rotisserie points list
        makeRotisseriePick(canvas.data.lastPicked,canvas.data.hitterList,canvas.data.pitcherList,canvas.data.hitterStats,canvas.data.pitcherStats,canvas.data.allTeams[team_index],canvas.data.pickedPlayersList,canvas.data.favoriteTeam,canvas.data.rivalTeam,canvas.data.projectedStats,canvas.data.rotisseriePointsList)
        #actually make the rotisserie pick
        if canvas.data.display == "Pitchers":
            addPitcherStats(canvas.data.lastPicked[0],canvas.data.pitcherList,canvas.data.pitcherStats,canvas.data.projectedStats,canvas.data.teamPickOrder[0],canvas.data.projectedStats,canvas.data.teamRosterOrder,canvas.data.averageWHIP,canvas.data.averageERA)
        else:
            addHitterStats(canvas.data.lastPicked[0],canvas.data.hitterList,canvas.data.hitterStats,canvas.data.projectedStats,canvas.data.teamPickOrder[0],canvas.data.projectedStats,canvas.data.teamRosterOrder,canvas.data.averageBA)

#Style = Done
def timerFired():
    delay = 500 # milliseconds
    if canvas.data.settingsScreen == False:
    #The draft has begun
        canvas.data.draftOver = True
        for i in xrange(len(canvas.data.allTeams)):
            for j in xrange(len(canvas.data.allTeams[i])):
                if canvas.data.allTeams[i][j][1] == "Empty":
                    canvas.data.draftOver = False
                    break
        #Checks to see if the draft is complete
        if canvas.data.draftOver == False:
            changePickOrder()
            if canvas.data.pickPlayer == True:
            #A player has been picked
                calculateLastPicked()
                if canvas.data.lastPicked[0] in canvas.data.pickedPlayersList:
                    pass
                    #Player has already been picked
                else:
                    if addPlayer() == True:
                        updatePickOrder(True)
                canvas.data.pickPlayer = False
            if canvas.data.autoDraftTeam == canvas.data.teamPickOrder[0]:
            #Auto drafted team is up to pick
                makeAutoDraftPick()
                updatePickOrder(False)
    redrawAll()
    canvas.after(delay, timerFired) # pause, then call timerFired again

###############################################################################

#Helper function for drawMissing
def missingPoints():
    canvas.data.hittingPoint = False
    canvas.data.pitchingPoint = False
    canvas.data.hittingRotisserie = False
    canvas.data.pitchingRotisserie = False
    if canvas.data.scoreSettings == "Points":
        for i in xrange(len(canvas.data.pointSettings)):
            if i < 4:
                if canvas.data.pointSettings[i][1] != 0:
                    canvas.data.hittingPoint = True
            else:
                if canvas.data.pointSettings[i][1] != 0:
                    canvas.data.pitchingPoint = True
            #Checks if a player has entered at least one value for a hitting and pitching category
    else:
        for stat in canvas.data.rotisserieSettings:
            if stat == "AVG" or stat == "HR" or stat=="R" or stat=="RBI" or stat=="SB":
                canvas.data.hittingRotisserie = True
            elif stat == "WHIP" or stat == "K" or stat == "SV" or stat == "ERA" or stat == "W":
                canvas.data.pitchingRotisserie = True

#Style = done
#Helper function for drawMissing
def drawMissingPointsSettings(canvas):
    rLeft,rTop,rRight,rBottom = 565,230,950,330
    textCenter = 750
    fontSize = 15
    singleHeight,firstHeight,secondHeight = 280,260,300
    if canvas.data.missingScoreSettings == True or canvas.data.missingTeams == True or canvas.data.hittingPoint == False or canvas.data.pitchingPoint == False:
        canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="yellow")
    if canvas.data.missingTeams == True and canvas.data.missingScoreSettings:
        canvas.create_text(textCenter,firstHeight,text="Please Select a Scoring Setting!",font=("Halvetica",fontSize,"bold"))
        canvas.create_text(textCenter,secondHeight,text="Please Select Number of Teams!",font=("Halvetica",fontSize,"bold"))
    elif canvas.data.missingScoreSettings == True:
        canvas.create_text(textCenter,singleHeight,text="Please Select a Scoring Setting!",font=("Halvetica",fontSize,"bold"))
    elif canvas.data.missingTeams == True:
        canvas.create_text(textCenter,singleHeight,text="Please Select Number of Teams!",font=("Halvetica",fontSize,"bold"))
    if canvas.data.hittingPoint == False and canvas.data.pitchingPoint == False:
        canvas.create_text(textCenter,firstHeight,text="Please Choose a Value for a Pitching Category!",font=("Halvetica",fontSize,"bold"))
        canvas.create_text(textCenter,secondHeight,text="Please Choose a Value for a Hitting Category!",font=("Halvetica",fontSize,"bold"))
    elif canvas.data.pitchingPoint == False:
        canvas.create_text(textCenter,singleHeight,text="Please Choose a Value for a Pitching Category!",font=("Halvetica",fontSize,"bold"))
    elif canvas.data.hittingPoint == False:
        canvas.create_text(textCenter,singleHeight,text="Please Choose a Value for a Hitting Category!",font=("Halvetica",fontSize,"bold"))

#STyle = done
#Helper function for drawMissing
def drawMissingRotisserieSettings(canvas):
    rLeft,rTop,rRight,rBottom = 565,230,950,330
    textCenter = 750
    fontSize = 15
    singleHeight,firstHeight,secondHeight = 280,260,300
    if canvas.data.missingScoreSettings == True or canvas.data.missingTeams == True or canvas.data.hittingRotisserie == False or canvas.data.pitchingRotisserie == False:
        canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="yellow")
    if canvas.data.missingTeams == True and canvas.data.missingScoreSettings:
        canvas.create_text(textCenter,firstHeight,text="Please Select a Scoring Setting!",font=("Halvetica",fontSize,"bold"))
        canvas.create_text(textCenter,secondHeight,text="Please Select Number of Teams!",font=("Halvetica",fontSize,"bold"))
    elif canvas.data.missingScoreSettings == True:
        canvas.create_text(textCenter,singleHeight,text="Please Select a Scoring Setting!",font=("Halvetica",fontSize,"bold"))
    elif canvas.data.missingTeams == True:
        canvas.create_text(textCenter,singleHeight,text="Please Select Number of Teams!",font=("Halvetica",fontSize,"bold"))
    if canvas.data.hittingRotisserie == False and canvas.data.pitchingRotisserie == False:
        canvas.create_text(textCenter,firstHeight,text="Please Choose a Pitching Category!",font=("Halvetica",fontSize,"bold"))
        canvas.create_text(textCenter,secondHeight,text="Please Choose a Hitting Category!",font=("Halvetica",fontSize,"bold"))
    elif canvas.data.pitchingRotisserie== False:
        canvas.create_text(textCenter,singleHeight,text="Please Choose a Pitching Category!",font=("Halvetica",fontSize,"bold"))
    elif canvas.data.hittingRotisserie == False:
        canvas.create_text(textCenter,singleHeight,text="Please Choose a Hitting Category!",font=("Halvetica",fontSize,"bold"))


#STyle = too long of lines
#Helper function for drawSettingsScreen
def drawMissing(canvas):
    if canvas.data.scoreSettings == "Points":
        drawMissingPointsSettings(canvas)
    else:
        drawMissingRotisserieSettings(canvas)

#Style = too long of lines
#Helper function for redrawALL
def drawSettingsScreen(canvas):
    canvasHeight,canvasWidth,rLeft,rTop,rRight,rBottom = 1000,600,770,545,930,585
    dsCenter,dsHeight,autoCenter,autoHeight,tCenter,tHeight = 200,25,750,25,850,565
    canvas.create_rectangle(0,0,canvasHeight,canvasWidth,fill="dark grey")
    canvas.create_text(dsCenter,dsHeight,text="Choose Draft Settings:",fill="white")
    canvas.create_text(autoCenter,autoHeight,text="Choose AutoDraft Settings:",fill="white")
    canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="white")
    canvas.create_text(tCenter,tHeight,text="Enter the Draft Room",fill="dark blue")
    drawFavoriteAndRival(canvas)   
    drawNumbers(canvas)
    drawScoringSystem(canvas)
    if canvas.data.scoreSettings == "Rotisserie":
        drawRotisserieSettings(canvas)
    elif canvas.data.scoreSettings == "Points":
        drawPointSettings(canvas)
    drawFavoriteTeamList(canvas)
    drawRivalTeamList(canvas)
    drawMissing(canvas)

#Style = Done
#Helper function for redrawAll
def drawDraftScreen(canvas):
    fontSize,apCenter,apHeight = 15,250,230
    rLeft,rTop,rRight,rBottom,rstep = 55,125,105,175,5
    timeCenter,timeHeight = 80,150
    draftCenter,draftHeight = 200,150
    dLeft,dTop,dRight,dBottom = 100,125,300,175
    canvas.create_text(apCenter,apHeight,text="Available Players:",
                       font=("Halvetica",fontSize,"bold"))
    drawPickOrder(canvas)
    drawStatTableAndHeaders(canvas)
    drawStats(canvas)
    drawCurrentTeam(canvas)
    drawPickedPlayersList(canvas)
    if canvas.data.draftOver == False:
        canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="dark blue")
        canvas.create_rectangle(rLeft+rstep,rTop+rstep,rRight-rstep,
                                rBottom-rstep,fill="dark grey")
        canvas.create_text(timeCenter,timeHeight,text=canvas.data.time[0],font=
                           ("Halvetica",fontSize,"bold"),fill="white")
    else:
        canvas.create_rectangle(dLeft,dTop,dRight,dBottom,fill="dark grey")
        canvas.create_text(draftCenter,draftHeight,text="Draft is Complete!",font=("Halvetica",20,"bold"))

#STyle = too long of lines
def placeButtons(canvas):
    nextTwentyButtonX,nextTwentyButtonY = 350,570
    previousTwentyButtonX,previousTwentyButtonY = 210,570
    changeTypeOfPlayerButtonX,changeTypeOfPlayerButtonY = 50,570
    nextTwentyFiveButtonX,nextTwentyFiveButtonY = 630,560
    previousTwentyFiveButtonX,previousTwentyFiveButtonY = 530,560
    if canvas.data.placeButtons == True:
        nextTwentyButton = Button(canvas,text="Next 20",bd=0,command=nextTwenty)
        nextTwentyButton.place(x=nextTwentyButtonX,y=nextTwentyButtonY)
        previousTwentyButton = Button(canvas,text="Previous 20",command=previousTwenty)
        previousTwentyButton.place(x=previousTwentyButtonX,y=previousTwentyButtonY)
        changeTypeOfPlayerButton = Button(canvas,text="Hitters/Pitchers",command=changeTypeOfPlayer)
        changeTypeOfPlayerButton.place(x=changeTypeOfPlayerButtonX,y=changeTypeOfPlayerButtonY)
        nextTwentyFiveButton = Button(canvas,text="Next 25",command=nextTwentyFive)
        nextTwentyFiveButton.place(x=nextTwentyFiveButtonX,y=nextTwentyFiveButtonY)
        PreviousTwentyFiveButton = Button(canvas,text="Previous 25",command=PreviousTwentyFive)
        PreviousTwentyFiveButton.place(x=previousTwentyFiveButtonX,y=previousTwentyFiveButtonY)
        canvas.data.placeButtons = False

#Style = Done
def redrawAll():
    canvas.delete(ALL)
    if canvas.data.settingsScreen == True:
        drawSettingsScreen(canvas)
    else:
        canvas.create_image(0,0,image=canvas.data.photo,anchor=NW)
        drawDraftScreen(canvas)
        placeButtons(canvas)

###############################################################################

#Helper funtion for init
def initLists():
    canvas.data.hitterList = []
    canvas.data.hitterStats = []
    canvas.data.hitterPointList = []
    canvas.data.pitcherList = []
    canvas.data.pitcherStats = []
    canvas.data.pitcherPointList = []
    canvas.data.pickNumber = []
    canvas.data.teamPickOrder = []
    canvas.data.teamRosterOrder = []
    #canvas.data.pickNumber = [1,2,3,4,5,"Round",6,7,8,9,10,"Round"]
    #canvas.data.teamPickOrder = ["Team 1","Team 2","Team 3","Team 4","Team 5",2,"Team 5","Team 4","Team 3","Team 2","Team 1",3]
    canvas.data.time = [50,0]
    canvas.data.pickedPlayersList = []
    canvas.data.lastPicked = ['Waiting for a player']
    canvas.data.autoDraftTeam = "Team 2"
    canvas.data.autoDraftedTeam = [["C","Empty"],["1B","Empty"],["2B","Empty"],["SS","Empty"],["3B","Empty"]]

#Helper function for init
def initSettingsScreen():
    canvas.data.settingsScreen = True
    canvas.data.placeButtons = True
    canvas.data.chooseFavoriteTeam = False
    canvas.data.chooseRivalTeam = False
    canvas.data.numberOfTeams = 0
    #Default number of teams is 0
    canvas.data.numberOfSP = 0
    canvas.data.numberOfOF = 0
    canvas.data.numberOfRP = 0
    canvas.data.numberOfUtil = 3
    #Becuase 0,1,2 are options for utility,i will have the default be 3
    canvas.data.numberOfBench = 0
    canvas.data.scoreSettings = "None"
    canvas.data.rotisserieSettings = []
    canvas.data.pointSettings = [["HR",0],["R",0],["RBI",0],["SB",0],["W",0],["K",0],["SV",0]]
    canvas.data.pointSettingsLast = "None"
    #Used to keep tracked of last changed point setting
    canvas.data.teamFocus = "None"
    canvas.data.teamListDisplay = "NL"
    canvas.data.NLTeams = [[["LAD","Los Angeles Dodgers"],["SF","San Francisco Giants"],["ARI","Arizona DiamondBacks"],["COL","Colorado Rockies"],["SD","San Diego Padres"]],[["STL","St. Louis Cardinals"],["CIN","Cincinnati Reds"],["MIL","Milwaukee Brewers"],["PIT","Pittsburgh Pirates"],["HOU","Houston Astros"],["CHC","Chicago Cubs"]],[["WSH","Washington Nationals"],["ATL","Atlanta Braves"],["NYM","New York Mets"],["PHI","Philadelphia Phillies"],["FLA","Florida Marlins"]]]
    canvas.data.ALTeams = [[["TEX","Texas Rangers"],["OAK","Oakland Athletics"],["SEA","Seattle Mariners"],["LAA","Los Angeles Angels"]],[["CLE","Cleveland Indians"],["CWS","Chicago White Sox"],["DET","Detroit Tigers"],["KC","Kansas City Royals"],["MIN","Minnesota Twins"]],[["TB","Tampa Bay Rays"],["BAL","Baltimore Orioles"],["NYY","New York Yankees"],["TOR","Toronto Blue Jays"],["BOS","Boston Red Sox"]]]
    canvas.data.favoriteTeam = "None"
    canvas.data.selectedFavoriteTeam = "None"
    canvas.data.selectedFavoriteTeamLeague = "None"
    canvas.data.rivalTeam = "None"
    canvas.data.selectedRivalTeam = "None"
    canvas.data.selectedRivalTeamLeague = "None"
    canvas.data.lastChosen = "None"
    canvas.data.favoriteTeamDisplay = False
    canvas.data.rivalTeamDisplay = False
    canvas.data.hittingPoint = "None"
    canvas.data.pitchingPoint = "None"
    canvas.data.pitchingRotisserie = "None"
    canvas.data.hittingRotisserie = "None"

#Helper function for init
def makeStatsList():
    makePlayersList(canvas.data.hitterList,canvas.data.hitter)
    makeStatList(canvas.data.hitterList,canvas.data.hitterStats,canvas.data.hitter)
    #Make the hitters list of players,stats, and projected points
    makePlayersList(canvas.data.pitcherList,canvas.data.pitcher)
    makeStatList(canvas.data.pitcherList,canvas.data.pitcherStats,canvas.data.pitcher)
    #Make the pitchers list of players,stats, and projected points

def init():
    initLists()
    initSettingsScreen()
    canvas.data.statsPageNumber = 0
    canvas.data.pickedPageNumber = 0
    canvas.data.hitter = "Hitter"
    canvas.data.pitcher = "Pitcher"
    canvas.data.display = "Hitters"
    #Determines which stats and players to display, hitters vs pitchers
    canvas.data.x,canvas.data.y = 0,0
    canvas.data.pickPlayer = False
    canvas.data.pickedPlayerIndex = 0
    canvas.data.roundNumber = 1
    canvas.data.totalPicksSoFar = 0
    canvas.data.photo = PhotoImage(file=getDesktopPath("background.gif"))
    #Background Photo
    canvas.data.allTeams = []
    canvas.data.currentTeam = "Team 2"
    #Used to see which team's roster is selected
    canvas.data.first_x_indexes = []
    canvas.data.second_x_indexes = []
    #Used to keep track of the total projected stats for each team
    canvas.data.projectedStats = []
    #Average whip, average ERA, and average BA are used to average these stats
    canvas.data.averageWHIP = []
    canvas.data.averageERA = []
    canvas.data.averageBA = []
    canvas.data.missingTeams = False
    canvas.data.missingScoreSettings = False
    canvas.data.draftOver = False
    makeStatsList()
    canvas.data.paused = False

###############################################################################

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width=1000, height=600)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()