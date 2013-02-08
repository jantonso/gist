from Tkinter import *

#Style = Few Long Lines
#Helper function for drawPickOrder
def drawPicks(canvas):
    minx,miny,textLeft,size,maxx,maxy,textUp = 25,25,50,60,75,80,40
    fontSize,nowSize,modded,roundLeft,eleven,twelve,thirteen = 10,6,10,65,11,12,13
    for i in xrange(canvas.data.teamSize):
        canvas.create_rectangle(minx+size*i,miny,maxx+size*i,maxy,fill="dark blue")
        if i == 0:
            canvas.create_text(textLeft,textUp,text="Now Picking",fill="white",font=("Halvetica",nowSize,"bold"))
        else:
            if canvas.data.pickNumber[i] == "Round":
                canvas.create_text(textLeft+size*i,textUp,font=("Halvetica",fontSize,"bold"),text=str(canvas.data.pickNumber[i]),fill="white")
            elif canvas.data.pickNumber[i] % modded == 1 and canvas.data.pickNumber[i] != eleven:
                canvas.create_text(textLeft+size*i,textUp,font=("Halvetica",fontSize,"bold"),text=str(canvas.data.pickNumber[i]) + "st",fill="white")
            elif canvas.data.pickNumber[i] % modded == 2 and canvas.data.pickNumber[i] != twelve:
                canvas.create_text(textLeft+size*i,textUp,font=("Halvetica",fontSize,"bold"),text=str(canvas.data.pickNumber[i]) + "nd",fill="white")
            elif canvas.data.pickNumber[i] % modded == 3 and canvas.data.pickNumber[i] != thirteen:
                canvas.create_text(textLeft+size*i,textUp,font=("Halvetica",fontSize,"bold"),text=str(canvas.data.pickNumber[i]) + "rd",fill="white")
            else:
                canvas.create_text(textLeft+size*i,textUp,font=("Halvetica",fontSize,"bold"),text=str(canvas.data.pickNumber[i]) + "th",fill="white")
            #In order to get it to be 1st,2nd,3rd,4th,etc.
        if i == 0 and type(canvas.data.teamPickOrder[i]) != str:
            pass
        else:
            canvas.create_text(textLeft+size*i,roundLeft,font=("Halvetica",fontSize,"bold"),text=canvas.data.teamPickOrder[i],fill="white")
        #In order to allow the Round Numbers to more smoothly move to the end

#Style = Few long lines
def drawPickOrder(canvas):
    teamDeterminant,rectangleTop = 6,20
    rectangleLeft,rectangleRight,step,bottom = 20,140,120,85
    lineLeft,lineStep,lineTop = 80,60,20
    if canvas.data.numberOfTeams > teamDeterminant:
        canvas.data.teamSize = 16
        rectangleSize = 7
    else:
        canvas.data.teamSize = len(canvas.data.teamPickOrder)
        rectangleSize = (len(canvas.data.pickNumber) / 2) - 1
    #Allows for resizing based on the number of teams
    canvas.create_rectangle(rectangleLeft,rectangleTop,rectangleRight+step*rectangleSize,bottom,fill="dark grey")
    drawPicks(canvas)
    for j in xrange(len(canvas.data.teamPickOrder)):
        canvas.create_line(lineLeft+lineStep*j,lineTop,lineLeft+lineStep*j,bottom,fill="black")
    #Pick order and pick number

###########################################################################

#Style = Done
#Helper function for drawStatTableAndHeaders
def drawHitterStats(canvas):
    avgCenter,rCenter,hrCenter,rbiCenter,sbCenter = 285,325,355,385,415
    textHeight = 255
    canvas.create_text(avgCenter,textHeight,text="Avg",fill="white")
    #Batting Average Column Header
    canvas.create_text(rCenter,textHeight,text="R",fill="white")
    #Runs Column Header
    canvas.create_text(hrCenter,textHeight,text="HR",fill="white")
    #Home Runs Column Header
    canvas.create_text(rbiCenter,textHeight,text="RBI",fill="white")
    #RBI Column Header
    canvas.create_text(sbCenter,textHeight,text="SB",fill="white")
    #SB Column Header

#Style = Done
#Helper function for drawStatTableAndHeaders
def drawPitcherStats(canvas):
    wCenter,svCenter,kCenter,eraCenter,whipCenter = 270,305,340,375,415
    textHeight = 255
    canvas.create_text(wCenter,textHeight,text="W",fill="white")
    #Wins Column Header
    canvas.create_text(svCenter,textHeight,text="SV",fill="white")
    #Saves Column Header
    canvas.create_text(kCenter,textHeight,text="K",fill="white")
    #Strikeouts Column Header
    canvas.create_text(eraCenter,textHeight,text="ERA",fill="white")
    #ERA Column Header
    canvas.create_text(whipCenter,textHeight,text="WHIP",fill="white")
    #Whip Column Header

#Style = Done, one line is too long
def drawStatTableAndHeaders(canvas):
    length,rectangleLeft,rectangleTop,size = 21,40,247,15
    teamLeft,posLeft,textCenter = 200,240,255
    rectangleBottom,rectangleRight = 262,440
    for j in xrange(length):
        if j == 0:
            fillColor = "grey"
        elif j % 2 == 0:
            fillColor = "dark blue"
        else:
            fillColor = "black"
        #In order to alternate fill colors so it looks a little better
        canvas.create_rectangle(rectangleLeft,rectangleTop+(size*j),rectangleRight,rectangleBottom+(size*j),fill=fillColor)
    canvas.create_text(teamLeft,textCenter,text="Team",fill="white")
    #Team Column Header
    canvas.create_text(posLeft,textCenter,text="Pos",fill="white")
    #Position Column Header
    if canvas.data.display == "Hitters":
        drawHitterStats(canvas)
    else:
        drawPitcherStats(canvas)

###############################################################################

#Style = lines too long
#Helper function for drawStats
def displayHitterStats(canvas,i):
    playersPerPage,maxIndex,textLeft,size = 20,5,240,15
    lineLeft,textCenter,step,statLength = 221,270,30,7
    lineTop,lineBottom,playerLeft = 247,562,108
    teamLeft,rLeft,restLeft = 200,285,235
    if canvas.data.hitterList[i+(playersPerPage*canvas.data.statsPageNumber)] not in canvas.data.pickedPlayersList:
        canvas.create_text(playerLeft,textCenter+size*i,fill="white",text=canvas.data.hitterList[i+(playersPerPage*canvas.data.statsPageNumber)])
        for k in xrange(statLength):
            if k > 2:
                canvas.create_text(restLeft+step*k,textCenter+size*i,fill="white",text=canvas.data.hitterStats[i+(playersPerPage*canvas.data.statsPageNumber)][k])
                canvas.create_line(lineLeft+step*k,lineTop,lineLeft+step*k,lineBottom,fill="white")
            elif k == 1: 
                if len(canvas.data.hitterStats[i+(playersPerPage*canvas.data.statsPageNumber)][k]) < maxIndex:
                    canvas.create_text(textLeft,textCenter+size*i,fill="white",text=canvas.data.hitterStats[i+(playersPerPage*canvas.data.statsPageNumber)][k])
                else:
                    canvas.create_text(textLeft,textCenter+size*i,fill="white",text=canvas.data.hitterStats[i+(playersPerPage*canvas.data.statsPageNumber)][k][:maxIndex])
            elif k == 0:
                canvas.create_text(teamLeft,textCenter+size*i,fill="white",text=canvas.data.hitterStats[i+(playersPerPage*canvas.data.statsPageNumber)][k])
            else:
                canvas.create_text(rLeft,textCenter+size*i,fill="white",text=canvas.data.hitterStats[i+(playersPerPage*canvas.data.statsPageNumber)][k])
        #Goes through each stat for each player and draws it onto the stat table

#STyle = too long lines
#Helper function for displayPitcherStats
def getPitcherPosition(canvas,i):
    max_wins = 5
    playersPerPage = 20
    if int(canvas.data.pitcherStats[i+(playersPerPage*canvas.data.statsPageNumber)][1]) <= max_wins:
        if canvas.data.pitcherList[i+(playersPerPage*canvas.data.statsPageNumber)] != "Travis Wood":
        #Only starting pitcher with less than 5 projected wins
            position = "RP"
        else:
            position = "SP"
    else: 
        if canvas.data.pitcherList[i+(playersPerPage*canvas.data.statsPageNumber)] != "Tyler Clippard" or canvas.data.pitcherList[i+(playersPerPage*canvas.data.statsPageNumber)] != "Heath Bell":
        #Only relief pitcher with more than 5 projected wins
            position = "SP"
        else:
            position = "RP"
    return position

#STyle = long lines
#Helper function for drawStats
def displayPitcherStats(canvas,i):
    playersPerPage,length,textCenter,textStep  = 20,7,270,15
    lineTop,lineBottom,textLeft,size = 247,562,200,35
    playerLeft,lineLeft,lineRight = 105,180,395
    wLeft,svLeft,restLeft = 240,270,415
    if canvas.data.pitcherList[i+(playersPerPage*canvas.data.statsPageNumber)] not in canvas.data.pickedPlayersList:    
        canvas.create_text(playerLeft,textCenter+textStep*i,fill="white",text=canvas.data.pitcherList[i+(playersPerPage*canvas.data.statsPageNumber)])
        for k in xrange(length):
            if k > 2 and k != length-1:
                canvas.create_text(textLeft+size*k,textCenter+textStep*i,fill="white",text=canvas.data.pitcherStats[i+(playersPerPage*canvas.data.statsPageNumber)][k-1])
                canvas.create_line(lineLeft+size*k,lineTop,lineLeft+size*k,lineBottom,fill="white")
            elif k == length-1:
                canvas.create_text(restLeft,textCenter+textStep*i,fill="white",text=canvas.data.pitcherStats[i+(playersPerPage*canvas.data.statsPageNumber)][k-1])
                canvas.create_line(lineRight,lineTop,lineRight,lineBottom,fill="white")
            elif k == 1: 
                position = getPitcherPosition(canvas,i)
                canvas.create_text(wLeft,textCenter+textStep*i,fill="white",text=position)
            elif k == 0:
                canvas.create_text(textLeft,textCenter+textStep*i,fill="white",text=canvas.data.pitcherStats[i+(playersPerPage*canvas.data.statsPageNumber)][k])
            else:
                canvas.create_text(svLeft,textCenter+textStep*i,fill="white",text=canvas.data.pitcherStats[i+(playersPerPage*canvas.data.statsPageNumber)][k-1])
            #In order to get everything spaced out nicely

#Style = Long Lines
def drawStats(canvas):
    playersPerPage = 20
    lineOneLeft,lineTwoLeft,lineThreeLeft = 218,180,262
    lineTop,lineBottom,lineFourLeft = 247,562,255
    for i in xrange(playersPerPage):
        if canvas.data.display == "Hitters":
            if i+(canvas.data.statsPageNumber*playersPerPage) >= len(canvas.data.hitterList):
                break
            else:
                #To make sure we don't go out of the index of hitterList or hitterStats
                displayHitterStats(canvas,i)
                canvas.create_line(lineOneLeft,lineTop,lineOneLeft,lineBottom,fill="white")
                canvas.create_line(lineTwoLeft,lineTop,lineTwoLeft,lineBottom,fill="white")
                canvas.create_line(lineThreeLeft,lineTop,lineThreeLeft,lineBottom,fill="white")
        else:
            if i+(canvas.data.statsPageNumber*playersPerPage) >= len(canvas.data.pitcherList):
                break
            else:
                displayPitcherStats(canvas,i)
                canvas.create_line(lineOneLeft+2,lineTop,lineOneLeft+2,lineBottom,fill="white")
                canvas.create_line(lineTwoLeft,lineTop,lineTwoLeft,lineBottom,fill="white")
                canvas.create_line(lineFourLeft,lineTop,lineFourLeft,lineBottom,fill="white")

###############################################################################

#STyle = long lines
def drawCurrentTeam(canvas):
    rLeft,rRight,rTop,rBottom,size = 775,980,120,140,20
    fontSize,textStep,textCenter = 14,130,105
    firstTextLeft,lastTextLeft,benchFirstLeft,benchSecondLeft = 780,870,830,810
    team_index = canvas.data.teamRosterOrder.index(canvas.data.currentTeam)
    for i in xrange(len(canvas.data.allTeams[team_index])):
        if i % 2 == 0:
            fillColor = "dark blue"
        else:
            fillColor = "black"
        canvas.create_rectangle(rLeft,rTop+size*i,rRight,rBottom+size*i,fill=fillColor)
        canvas.create_text(firstTextLeft,textStep+size*i,anchor=W,text=canvas.data.allTeams[team_index][i][0]+":",fill="white")
        if canvas.data.allTeams[team_index][i][1] != "Empty":
            if canvas.data.allTeams[team_index][i][0] == "Bench":
                canvas.create_text(benchFirstLeft,textStep+size*i,anchor=W,text=canvas.data.allTeams[team_index][i][1],fill="white")
            else:
                canvas.create_text(benchSecondLeft,textStep+size*i,anchor=W,text=canvas.data.allTeams[team_index][i][1],fill="white")
    canvas.create_text(lastTextLeft,textCenter,font=("Halvetica",fontSize,"bold"),text=canvas.data.currentTeam + ":")

###############################################################################

#Style = Done
#Helper function for drawPickedPlayersList
def drawLinesAndRectangles(canvas):
    left,top,right,bottom,fontSize = 480,170,750,545,14
    rLeft,rTop,rRight,rBottom = 470,140,760,555
    lBottom,lSame,lLeft,lSide = 190,700,650,530
    lTop,tLeft,tCenter,tSide,tEdge,lRight = 180,505,155,635,615,480
    canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="dark blue")
    canvas.create_rectangle(left,top,right,bottom,fill="black")
    canvas.create_rectangle(left,top,right,lBottom,fill="dark grey")
    canvas.create_text(tLeft,lTop,text="Pick",fill="white",font=("Halvetica",fontSize,"bold"))
    canvas.create_text(tSide,lTop,text="Player",fill="white",font=("Halvetica",fontSize,"bold"))
    canvas.create_text(tEdge,tCenter,text="Pick History:",fill="white")
    canvas.create_line(lSide,top,lSide,bottom,fill="white")
    canvas.create_line(lLeft,lBottom-1,lLeft,bottom,fill="white")
    canvas.create_line(lSame,lBottom-1,lSame,bottom,fill="white")
    canvas.create_line(left,top,lRight,bottom,fill="white")
    canvas.create_line(right,top,right,bottom,fill="white")
    canvas.create_line(left,bottom,right,bottom,fill="white")
    canvas.create_line(left,top,right,top,fill="white")

#Style = too long lines
def drawPickedPlayersList(canvas):
    playersPerPage,fontSize,step,center,lCenter = 25,12,14,198,190
    pLeft,tLeft,lLeft,playerLeft,nLeft = 725,675,480,590,505
    drawLinesAndRectangles(canvas)
    for i in xrange(playersPerPage):
        if i+playersPerPage*canvas.data.pickedPageNumber < len(canvas.data.pickedPlayersList):
            canvas.create_text(playerLeft,center+step*i,text=canvas.data.pickedPlayersList[i+playersPerPage*canvas.data.pickedPageNumber],font=("Halvetica",fontSize,"bold"),fill="white")
            canvas.create_line(lLeft,lCenter+step*i,750,lCenter+step*i,fill="white")
            canvas.create_text(nLeft,center+step*i,text=(i+1)+(canvas.data.pickedPageNumber*playersPerPage),fill="white")
            #Display regardless of hitters and pitchers
            if canvas.data.pickedPlayersList[i+playersPerPage*canvas.data.pickedPageNumber] in canvas.data.hitterList:
                index = canvas.data.hitterList.index(canvas.data.pickedPlayersList[i+playersPerPage*canvas.data.pickedPageNumber])
                canvas.create_text(tLeft,center+step*i,text=canvas.data.hitterStats[index][0],font=("Halvetica",fontSize,"bold"),fill="white")
                canvas.create_text(pLeft,center+step*i,text=canvas.data.hitterStats[index][1],font=("Halvetica",fontSize,"bold"),fill="white")
                #Display team and position for hitters
            else:
                index = canvas.data.pitcherList.index(canvas.data.pickedPlayersList[i+playersPerPage*canvas.data.pickedPageNumber])
                canvas.create_text(tLeft,center+step*i,text=canvas.data.pitcherStats[index][0],font=("Halvetica",fontSize,"bold"),fill="white")
                #Displays team for pitchers
                position = getPitcherPosition(canvas,i)
                canvas.create_text(pLeft,center+step*i,text=position,font=("Halvetica",fontSize,"bold"),fill="white")
                #Displays position for pitchers

###############################################################################

#Style = Done
#Helper function for drawFavoriteAndRival
def getFillColor(canvas):
    if canvas.data.chooseFavoriteTeam == True:
        favoriteFillColor = "black"
    else:
        favoriteFillColor = "white"
    if canvas.data.chooseRivalTeam == True:
        rivalFillColor = "black"
    else:
        rivalFillColor = "white"
    return (favoriteFillColor,rivalFillColor)

#Style = too long lines
def drawFavoriteAndRival(canvas):
    (favoriteFillColor,rivalFillColor) = getFillColor(canvas)
    fLeft,fRight,fTop,fBottom = 735,745,70,80
    rivLeft,rivRight,rivTop,rivBottom = 925,935,70,80
    favoriteCenter,favoriteHeight,rivalCenter,rivalHeight = 650,75,850,75
    fontSize,rTop,rBottom,rLeft,rRight = 9,100,200,568,752
    recLeft,recRight,favTextLeft,rivTextLeft,rivStep = 768,952,572,780,5
    rivTextLeft,favTextCenter,favStep,faLeft = 780,120,30,580
    canvas.create_text(favoriteCenter,favoriteHeight,text="Choose a Favorite Team:")
    canvas.create_rectangle(fLeft,fTop,fRight,fBottom,fill=favoriteFillColor)
    canvas.create_text(rivalCenter,rivalHeight,text="Choose a Rival Team:")
    canvas.create_rectangle(rivLeft,rivTop,rivRight,rivBottom,fill=rivalFillColor)
    canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="white")
    canvas.create_rectangle(recLeft,rTop,recRight,rBottom,fill="white")
    canvas.create_text(favTextLeft,favTextCenter,anchor=W,font=("Halvetica",fontSize,"bold"),text="By enabling the Favorite Team feature") 
    canvas.create_text(faLeft,favTextCenter+favStep,anchor=W,font=("Halvetica",fontSize,"bold"),text="the auto draft will try its best to")    
    canvas.create_text(favTextLeft,favTextCenter+2*favStep,anchor=W,font=("Halvetica",fontSize,"bold"),text="draft players from your favorite team")
    canvas.create_text(rivTextLeft,favTextCenter,anchor=W,font=("Halvetica",fontSize,"bold"),text="By enabling the Rival Team feature") 
    canvas.create_text(rivTextLeft+rivStep,favTextCenter+favStep,anchor=W,font=("Halvetica",fontSize,"bold"),text="the auto draft will avoid drafting")    
    canvas.create_text(rivTextLeft+2*rivStep,favTextCenter+2*favStep,anchor=W,font=("Halvetica",fontSize,"bold"),text="players from your rival team")

###############################################################################

#Style = done
#Helper function for drawNumbers
def getFillColors(canvas,i):
    if i+3 == canvas.data.numberOfSP:
        spFillColor = "black"
    else:
        spFillColor = "white"
    if i+1 == canvas.data.numberOfRP:
        rpFillColor = "black"
    else:
        rpFillColor = "white"
    if i+3 == canvas.data.numberOfOF:
        ofFillColor = "black"
    else:
        ofFillColor = "white"
    if i == canvas.data.numberOfUtil:
        utilFillColor = "black"
    else:
        utilFillColor = "white"
    if i+2 == canvas.data.numberOfBench:
        benchFillColor = "black"
    else:
        benchFillColor = "white"
    return spFillColor,rpFillColor,ofFillColor,utilFillColor,benchFillColor
    #If an option is chosen then fill in that option black

#Style = Too long of lines
#Helper function for drawNumbers
def drawCurrentRoster(canvas):
    crTextCenter,crTextHeight = 200,270
    textLeft,textStep,textHeight,textCenter = 30,40,300,325
    canvas.create_text(crTextCenter,crTextHeight,text="Current Rosters:",fill="black")
    has_relief_pitchers = False
    for i in xrange(len(canvas.data.autoDraftedTeam)):
        if canvas.data.autoDraftedTeam[i][0] == "RP":
            index = i
            has_relief_pitchers = True
            break
        else:
            canvas.create_text(textLeft+textLeft*i,textHeight,text=canvas.data.autoDraftedTeam[i][0],fill="black")
    if has_relief_pitchers == True:
        for j in xrange(index,len(canvas.data.autoDraftedTeam)):
            canvas.create_text(textLeft+textStep*(j-index),textCenter,text=canvas.data.autoDraftedTeam[j][0],fill="black")

#Style = Done
#Helper function for drawNumbers
def drawText(canvas):
    spLeft,rpLeft,ofLeft,textLeft = 75,75,75,200
    utilLeft,benchLeft,utilCenter,benchCenter = 300,300,195,225
    ofCenter,spCenter,rpCenter,textCenter = 240,180,210,150
    canvas.create_text(textLeft,textCenter,text="Size of Roster:")
    canvas.create_text(spLeft,spCenter,text="SP:")
    canvas.create_text(rpLeft,rpCenter,text="RP:")
    canvas.create_text(utilLeft,utilCenter,text="Utility:")
    canvas.create_text(benchLeft,benchCenter,text="Bench:")
    canvas.create_text(ofLeft,ofCenter,text="OF:")

#Style = too long
#Helper function for drawNumbers
def drawRectangleAndText(canvas,i):
    spFillColor,rpFillColor,ofFillColor,utilFillColor,benchFillColor=getFillColors(canvas,i)
    #Gets the fill colors for SP,RP,OF,Utility, and Bench Options
    rLeft,recLeft,rsize,rstep,rTop,recTop = 100,340,20,30,170,185
    tLeft,textLeft,tstep = 110,350,30
    tCenter,textstep = 180,15
    canvas.create_rectangle(rLeft+rstep*i,rTop,rLeft+rsize+rstep*i,rTop+rsize,fill=spFillColor)
    canvas.create_rectangle(rLeft+rstep*i,rTop+rstep,rLeft+rsize+rstep*i,rTop+rsize+rstep,fill=rpFillColor)
    canvas.create_rectangle(rLeft+rstep*i,rTop+2*rstep,rLeft+rsize+rstep*i,rTop+2*rstep+rsize,fill=ofFillColor)
    canvas.create_rectangle(recLeft+rstep*i,recTop,recLeft+rsize+rstep*i,recTop+rsize,fill=utilFillColor)
    canvas.create_rectangle(recLeft+rstep*i,recTop+rstep,recLeft+rsize+rstep*i,recTop+rsize+rstep,fill=benchFillColor)
    canvas.create_text(tLeft+tstep*i,tCenter,text=i+3)
    canvas.create_text(tLeft+tstep*i,tCenter+tstep,text=i+1)
    canvas.create_text(tLeft+tstep*i,tCenter+2*tstep,text=i+3)
    canvas.create_text(textLeft+tstep*i,tCenter+textstep,text=i)
    canvas.create_text(textLeft+tstep*i,tCenter+tstep+textstep,text=i+2)

#Style = too long
def drawNumbers(canvas):
    numTeamsLeft,numteamsCenter = 100,70
    minTeams,maxTeams,step = 4,13,45
    rLeft,rRight,tCenter,tHeight = 20,40,30,100
    canvas.create_text(numTeamsLeft,numteamsCenter,text="Number of Teams:")     
    for i in xrange(minTeams,maxTeams):
        if i == canvas.data.numberOfTeams:
            fillColor = "black"
        else:
            fillColor = "white"
        canvas.create_rectangle(rLeft+step*(i-minTeams),2*step,rRight+step*(i-minTeams),110,fill=fillColor)
        canvas.create_text(tCenter+step*(i-minTeams),tHeight,text=i)
    drawText(canvas)
    for i in xrange(minTeams-1):
        drawRectangleAndText(canvas,i)
    drawCurrentRoster(canvas)
    #Displays the current roster based on the chosen options

###############################################################################

#Style = Too long lines
#Helper function for drawScoringSystem
def drawTextAndRectangles(canvas):
    fontSize,tLeft,textLeft,tstep,tCenter,tHeightStep = 9,35,235,10,450,20
    rLeft,recLeft,rRight,recRight = 20,220,180,380
    rTop,rBottom,recTop,recBottom = 400,480,400,480
    canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="white")
    canvas.create_rectangle(recLeft,recTop,recRight,recBottom,fill="white")
    canvas.create_text(tLeft,tCenter-2*tHeightStep,anchor=W,font=("Halvetica",fontSize,"bold"),text="This scoring system lets you")
    canvas.create_text(tLeft-tstep,tCenter-tHeightStep,anchor=W,font=("Halvetica",fontSize,"bold"),text="choose which categories will be")
    canvas.create_text(tLeft,tCenter,anchor=W,font=("Halvetica",fontSize,"bold"),text="used, with the goal being to")
    canvas.create_text(tLeft+tstep,tCenter+tHeightStep,anchor=W,font=("Halvetica",fontSize,"bold"),text="maximize each category")
    canvas.create_text(textLeft,tCenter-2*tHeightStep,anchor=W,font=("Halvetica",fontSize,"bold"),text="This scoring system lets you")
    canvas.create_text(textLeft,tCenter-tHeightStep,anchor=W,font=("Halvetica",fontSize,"bold"),text="assign point values to each")
    canvas.create_text(textLeft-tstep,tCenter,anchor=W,font=("Halvetica",fontSize,"bold"),text="category, which are then totaled")
    canvas.create_text(textLeft+tstep,tCenter+tHeightStep,anchor=W,font=("Halvetica",fontSize,"bold"),text="to determine the winner")

#Style = Too long lines
def drawScoringSystem(canvas):
    drawTextAndRectangles(canvas)
    ssCenter,ssHeight = 200,350
    rCenter,rHeight = 75,380
    pCenter,pHeight = 275,380
    rotoLeft,rotoRight,rotoTop,rotoBottom = 115,125,375,385
    pointsLeft,pointsRight,pointsTop,pointsBottom = 305,315,375,385
    canvas.create_text(ssCenter,ssHeight,fill="black",text="Scoring Settings:")
    canvas.create_text(rCenter,rHeight,fill="black",text="Rotisserie:")
    canvas.create_text(pCenter,pHeight,fill="black",text="Points:")
    if canvas.data.scoreSettings == "Rotisserie":
        rotoFillColor = "black"
    else:
        rotoFillColor = "white"
    if canvas.data.scoreSettings == "Points":
        pointsFillColor = "black"
    else:
        pointsFillColor = "white"
    canvas.create_rectangle(rotoLeft,rotoTop,rotoRight,rotoBottom,fill=rotoFillColor)
    canvas.create_rectangle(pointsLeft,pointsTop,pointsRight,pointsBottom,fill=pointsFillColor)

###############################################################################

#Style = too many lines and too long of lines
#Helper function for drawRotisserieSettings
def drawHittingSettings(canvas):
    rLeft,rRight,rTop,rBottom,rstep,tstep = 70,80,525,535,20,20
    recLeft,recRight,tCenter,tHeight,textCenter = 150,160,50,530,130
    if "AVG" in canvas.data.rotisserieSettings:
        canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="black")
    else:
        canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="white")
    canvas.create_text(tCenter,tHeight,text="AVG:")
    if "HR" in canvas.data.rotisserieSettings:
        canvas.create_rectangle(rLeft,rTop+rstep,rRight,rBottom+rstep,fill="black")
    else:
        canvas.create_rectangle(rLeft,rTop+rstep,rRight,rBottom+rstep,fill="white")
    canvas.create_text(tCenter,tHeight+tstep,text="HR:")
    if "R" in canvas.data.rotisserieSettings:
        canvas.create_rectangle(rLeft,rTop+2*rstep,rRight,rBottom+2*rstep,fill="black")
    else:
        canvas.create_rectangle(rLeft,rTop+2*rstep,rRight,rBottom+2*rstep,fill="white")
    canvas.create_text(tCenter,tHeight+2*tstep,text="R:")
    if "RBI" in canvas.data.rotisserieSettings:
        canvas.create_rectangle(recLeft,rTop,recRight,rBottom,fill="black")
    else:
        canvas.create_rectangle(recLeft,rTop,recRight,rBottom,fill="white")
    canvas.create_text(textCenter,tHeight,text="RBI:")
    if "SB" in canvas.data.rotisserieSettings:
        canvas.create_rectangle(recLeft,rTop+rstep,recRight,rBottom+rstep,fill="black")
    else:
        canvas.create_rectangle(recLeft,rTop+rstep,recRight,rBottom+rstep,fill="white")
    canvas.create_text(textCenter,tHeight+tstep,text="SB")

#STyle = too long of lines and too long of function
#Helper function for drawRotisserieSettings
def drawPitchingSettings(canvas):
    rLeft,rTop,rRight,rBottom,rstep,textCenter = 270,525,280,535,20,340
    recLeft,recRight,tCenter,tHeight,tstep = 360,370,250,530,20
    if "W" in canvas.data.rotisserieSettings:
        canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="black")
    else:
        canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="white")
    canvas.create_text(tCenter,tHeight,text="W:",font="black")
    if "K" in canvas.data.rotisserieSettings:
        canvas.create_rectangle(rLeft,rTop+rstep,rRight,rBottom+rstep,fill="black")
    else:
        canvas.create_rectangle(rLeft,rTop+rstep,rRight,rBottom+rstep,fill="white")
    canvas.create_text(tCenter,tHeight+tstep,text="K:",font="black")
    if "ERA" in canvas.data.rotisserieSettings:
        canvas.create_rectangle(rLeft,rTop+2*rstep,rRight,rBottom+2*rstep,fill="black")
    else:
        canvas.create_rectangle(rLeft,rTop+2*rstep,rRight,rBottom+2*rstep,fill="white")
    canvas.create_text(tCenter,tHeight+2*tstep,text="ERA:",font="black")
    if "WHIP" in canvas.data.rotisserieSettings:
        canvas.create_rectangle(recLeft,rTop,recRight,rBottom,fill="black")
    else:
        canvas.create_rectangle(recLeft,rTop,recRight,rBottom,fill="white")
    canvas.create_text(textCenter,tHeight,text="WHIP:",font="black")
    if "SV" in canvas.data.rotisserieSettings:
        canvas.create_rectangle(recLeft,rTop+rstep,recRight,rBottom+rstep,fill="black")
    else:
        canvas.create_rectangle(recLeft,rTop+rstep,recRight,rBottom+rstep,fill="white")
    canvas.create_text(textCenter,tHeight+tstep,text="SV:",font="black")

#Style = done
def drawRotisserieSettings(canvas):
    bcCenter,bcHeight = 90,500
    pcCenter,pcHeight = 300,500
    canvas.create_text(bcCenter,bcHeight,text="Batting Categories:")
    drawHittingSettings(canvas)
    canvas.create_text(pcCenter,pcHeight,text="Pitching Categories:")
    drawPitchingSettings(canvas)

###############################################################################

#style = too long of lines
#Helper function for drawPointSettings
def createText(canvas):
    bcCenter,bcHeight = 90,500
    pcCenter,pcHeight = 300,500
    hrLeft,hrRight,hrTop,hrBottom,hrCenter,hrHeight = 70,515,100,535,50,525
    rLeft,rRight,rTop,rBottom,rCenter,rHeight = 70,545,100,565,50,555
    rbiLeft,rbiRight,rbiTop,rbiBottom,rbiCenter,rbiHeight = 150,515,180,535,130,525
    sbLeft,sbRight,sbTop,sbBottom,sbCenter,sbHeight = 150,545,180,565,130,555
    wLeft,wRight,wTop,wBottom,wCenter,wHeight = 270,515,300,535,250,525
    kLeft,kRight,kTop,kBottom,kCenter,kHeight = 270,545,300,565,250,555
    svLeft,svRight,svTop,svBottom,svCenter,svHeight = 360,515,390,535,340,525
    canvas.create_text(bcCenter,bcHeight,text="Batting Categories:")
    canvas.create_rectangle(hrLeft,hrRight,hrTop,hrBottom,fill="white")
    canvas.create_text(hrCenter,hrHeight,text="HR:")
    canvas.create_rectangle(rLeft,rRight,rTop,rBottom,fill="white")
    canvas.create_text(rCenter,rHeight,text="R:")
    canvas.create_rectangle(rbiLeft,rbiRight,rbiTop,rbiBottom,fill="white")
    canvas.create_text(rbiCenter,rbiHeight,text="RBI:")
    canvas.create_rectangle(sbLeft,sbRight,sbTop,sbBottom,fill="white")
    canvas.create_text(sbCenter,sbHeight,text="SB")
    canvas.create_text(pcCenter,pcHeight,text="Pitching Categories:")
    canvas.create_rectangle(wLeft,wRight,wTop,wBottom,fill="white")
    canvas.create_text(wCenter,wHeight,text="W:")
    canvas.create_rectangle(kLeft,kRight,kTop,kBottom,fill="white")
    canvas.create_text(kCenter,kHeight,text="K:")
    canvas.create_rectangle(svLeft,svRight,svTop,svBottom,fill="white")
    canvas.create_text(svCenter,svHeight,text="SV:")

#Style = too long of lines
def drawPointSettings(canvas):
    tCenter,tHeight = 85,525
    textCenter,textHeight = 165,555
    t_Center,text_Center = 285,375
    createText(canvas)
    canvas.create_text(tCenter,tHeight,text=canvas.data.pointSettings[0][1])
    canvas.create_text(tCenter,textHeight,text=canvas.data.pointSettings[1][1])
    canvas.create_text(textCenter,tHeight,text=canvas.data.pointSettings[2][1])
    canvas.create_text(textCenter,textHeight,text=canvas.data.pointSettings[3][1])
    canvas.create_text(t_Center,tHeight,text=canvas.data.pointSettings[4][1])
    canvas.create_text(t_Center,textHeight,text=canvas.data.pointSettings[5][1])
    canvas.create_text(text_Center,tHeight,text=canvas.data.pointSettings[6][1])

###############################################################################

#Style = TOo long lines
#Helper function for drawFavoriteTeamList
def drawFavoriteTextAndRectangles(canvas):
    canvas.data.favoriteTeamDisplay = True
    rLeft,rTop,rRight,rBottom,rshift = 820,415,930,445,60
    recLeft,recTop,recRight,recBottom,divHeight = 568,350,952,535,365
    textCenter,westCenter,centralCenter,eastCenter= 875,600,675,750
    teamHeight,confirmHeight,changeHeight = 380,490,430
    canvas.create_rectangle(recLeft,recTop,recRight,recBottom,fill="white")
    canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="dark grey")
    canvas.create_rectangle(rLeft,rTop+rshift,rRight,rBottom+rshift,fill="dark grey")
    canvas.create_text(textCenter,changeHeight,text="Change League")
    canvas.create_text(textCenter,confirmHeight,text="Confirm Team")
    canvas.create_text(textCenter,teamHeight,text=canvas.data.teamListDisplay,font=("Halvetica",15,"bold"))
    canvas.create_text(westCenter,divHeight,text="West")
    canvas.create_text(centralCenter,divHeight,text="Central")
    canvas.create_text(eastCenter,divHeight,text="East")

#STyle = too long of lines
#Helper function for drawFavoriteTeamList
def drawNLTeams(canvas,chosenFillColor,team):
    size,height = 75,25
    rLeft,rRight,rTop,rBottom = 580,620,380,405
    textCenter,textHeight = 600,395
    for division in xrange(len(canvas.data.NLTeams)):
        for i in xrange(len(canvas.data.NLTeams[division])):
            if canvas.data.NLTeams[division][i][0] == team:
                fillColor = chosenFillColor
            else:
                fillColor = "dark grey"
            canvas.create_rectangle(rLeft+division*size,rTop+i*height,rRight+division*size,rBottom+i*height,fill=fillColor)
            canvas.create_text(textCenter+division*size,textHeight+i*height,text=canvas.data.NLTeams[division][i][0])

#Style = Too long of Lines
#Helper functon for drawFavoriteTeamList(canvas)
def drawALTeams(canvas,chosenFillColor,team):
    size,height = 75,25
    rLeft,rRight,rTop,rBottom = 580,620,380,405
    textCenter,textHeight = 600,395
    for division in xrange(len(canvas.data.ALTeams)):
        for j in xrange(len(canvas.data.ALTeams[division])):
            if canvas.data.ALTeams[division][j][0] == team:
                fillColor = chosenFillColor
            else:
                fillColor = "dark grey"
            canvas.create_rectangle(rLeft+division*size,rTop+j*height,rRight+division*size,rBottom+j*height,fill=fillColor)
            canvas.create_text(textCenter+division*size,textHeight+j*height,text=canvas.data.ALTeams[division][j][0])

#Style = Done
def drawChosenFavoriteTeam(canvas):
    rLeft,rTop,rRight,rBottom = 580,385,740,445
    teamLeft,teamHeight,currentHeight = 660,430,400
    canvas.data.favoriteTeamDisplay = False
    if canvas.data.selectedFavoriteTeamLeague == "AL":
        team_list = canvas.data.ALTeams
    else:
        team_list = canvas.data.NLTeams
    canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="light blue")
    for teams in team_list:
        for team in teams:
            if team[0] == canvas.data.selectedFavoriteTeam:
                canvas.create_text(teamLeft,teamHeight,text=team[1])
    #Gets the actual team name from the abbreviation
    canvas.create_text(teamLeft,currentHeight,text="Current Favorite Team:")

#Style = too long of lines
def drawFavoriteTeamList(canvas):
    if canvas.data.chooseFavoriteTeam == True and canvas.data.selectedFavoriteTeam == "None":
        drawFavoriteTextAndRectangles(canvas)
        if canvas.data.teamListDisplay == "NL":
            drawNLTeams(canvas,"light blue",canvas.data.favoriteTeam)
        else:
            drawALTeams(canvas,"light blue",canvas.data.favoriteTeam)
    elif canvas.data.chooseFavoriteTeam == True and canvas.data.selectedFavoriteTeam != "None":
        if (canvas.data.chooseRivalTeam == True and canvas.data.selectedRivalTeam != "None") or canvas.data.chooseRivalTeam == False:
        #Makes sure that it isn't displayed when the user is choosing a rival team
            drawChosenFavoriteTeam(canvas)

###############################################################################

#Style = too long lines
#Helper function for drawRivalTeamList
def drawRivalTextAndRectangles(canvas):
    canvas.data.rivalTeamDisplay = True
    rLeft,rRight,rTop,rBottom,rHeight = 820,930,415,445,60
    recLeft,recTop,recRight,recBottom = 568,350,952,535
    teamCenter,teamHeight = 875,380
    wCenter,cCenter,eCenter,divHeight = 600,675,750,365
    changeCenter,changeHeight,confirmCenter,confirmHeight = 875,430,875,490
    canvas.create_rectangle(recLeft,recTop,recRight,recBottom,fill="white")
    canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="dark grey")
    canvas.create_rectangle(rLeft,rTop+rHeight,rRight,rBottom+rHeight,fill="dark grey")
    canvas.create_text(changeCenter,changeHeight,text="Change League")
    canvas.create_text(confirmCenter,confirmHeight,text="Confirm Team")
    canvas.create_text(teamCenter,teamHeight,text=canvas.data.teamListDisplay,font=("Halvetica",15,"bold"))
    canvas.create_text(wCenter,divHeight,text="West")
    canvas.create_text(cCenter,divHeight,text="Central")
    canvas.create_text(eCenter,divHeight,text="East")

#Style = too long of lines
def drawChosenRivalTeam(canvas):
    rLeft,rTop,rRight,rBottom = 775,385,925,445
    teamCenter,teamHeight = 850,430
    currentCenter,currentHeight = 850,400
    canvas.data.rivalTeamDisplay = False
    if canvas.data.selectedRivalTeamLeague == "AL":
        team_list = canvas.data.ALTeams
    else:
        team_list = canvas.data.NLTeams
    canvas.create_rectangle(rLeft,rTop,rRight,rBottom,fill="indian red")
    for teams in team_list:
        for team in teams:
            if team[0] == canvas.data.selectedRivalTeam:
                canvas.create_text(teamCenter,teamHeight,text=team[1])
    #Gets the actual team name from the abbreviation
    canvas.create_text(currentCenter,currentHeight,text="Current Rival Team:")

#STyle = too long of lines
def drawRivalTeamList(canvas):
    if canvas.data.chooseRivalTeam == True and canvas.data.selectedRivalTeam == "None":
        drawRivalTextAndRectangles(canvas)
        if canvas.data.teamListDisplay == "NL":
            drawNLTeams(canvas,"indian red",canvas.data.rivalTeam)
        else:
            drawALTeams(canvas,"indian red",canvas.data.rivalTeam)
    elif canvas.data.chooseRivalTeam == True and canvas.data.selectedRivalTeam != "None":
        if (canvas.data.chooseFavoriteTeam == True and canvas.data.selectedFavoriteTeam != "None") or canvas.data.chooseFavoriteTeam == False:
        #Makes sure it isn't displayed when the user is choosing a favorite team    
            drawChosenRivalTeam(canvas)