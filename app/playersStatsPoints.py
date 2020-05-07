from BeautifulSoup import BeautifulSoup
import urllib
import re 
import os

hitter_pageFile = urllib.urlopen("http://fantasyknuckleheads.com/projected-2011-fantasy-baseball-statistics-batters/")
hitter_pageHtml = hitter_pageFile.read()
hitter_pageFile.close()

pitcher_pageFile = urllib.urlopen("http://fantasyknuckleheads.com/projected-2011-fantasy-baseball-stats-pitchers/")
pitcher_pageHtml = pitcher_pageFile.read()
pitcher_pageFile.close()       

hitter_soup = BeautifulSoup("".join(hitter_pageHtml))
pitcher_soup = BeautifulSoup("".join(pitcher_pageHtml))

def makePlayersList(new_list,type_of_player):
    max_number_of_letters,index_of_chris_johnson,index_of_josh_johnson = 4,1305,64
    index_of_mike_adams = 576
    if type_of_player == "Hitter":
        len_of_tags = 2000
    else:
        len_of_tags = 1130
    for i in xrange(0,len_of_tags):
        letter_count = 0
        if type_of_player == "Hitter":
            contents = hitter_soup.findAll("td")[i].contents 
        else:
            contents = pitcher_soup.findAll("td")[i].contents
        string = ''
        for word in contents:
            if type_of_player == "Hitter":
                if i == index_of_chris_johnson:
                    word = "Chris Johnson"
            else:
                if i == index_of_josh_johnson:
                    word = "Josh Johnson"
                elif i == index_of_mike_adams:
                    word = "Mike Adams"
            #These three players are links, instead of just strings for whatever reason
            string += str(word)
            for letter in string:
                if (letter.isalpha() == True):
                    letter_count += 1
        if letter_count > max_number_of_letters:
            new_list += [str(string)]
#List of players, i.e. [Hanley Ramirez, Albert Pujols, Ryan Braun]

def makeStatList(players,new_list,type_of_player):
    index_of_chris_johnson = 1305
    index_of_josh_johnson = 64
    index_of_mike_adams = 576
    max_number_of_letters = 4
    for row in xrange(len(players)):
        new_list += [[]]
    j = -1
    if type_of_player == "Hitter":
        len_of_tags = 2007
    else:
        len_of_tags = 1135
    for i in xrange(0,len_of_tags):
        letter_count = 0
        if type_of_player == "Hitter":
            contents = hitter_soup.findAll("td")[i].contents
        else:
            contents = pitcher_soup.findAll("td")[i].contents
        string = ''
        for word in contents:
            if type_of_player == "Hitter":
                if i == index_of_chris_johnson:
                    word = "Chris Johnson"
            else:
                if i == index_of_josh_johnson:
                    word = "Josh Johnson"
                elif i == index_of_mike_adams:
                    word = "Mike Adams"
            string += word
            for letter in word:
                if (letter.isalpha() == True):
                    letter_count += 1
        if letter_count > max_number_of_letters:
            j += 1
        else:
            new_list[j] += [str(string)]
#List of stats sorted by index, i.e. [[Team,Position,BA,RBI,HR,R,SB]]