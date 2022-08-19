#Purpose: Convert Total Global Sports data to file that can then be converted to XL sheet
        # to create own data base of commited youth soccer players by level of school commited to
        
from bs4 import BeautifulSoup #python -m pip install bs4 
import sys
import requests            #NEED TO INSTALL
import lxml
from lxml import html

            #  ******* 04 GIRLS TGS TABLE *******  #

#Gather list of all D1 Girls teams:
d1GirlsFile = open('Division1GirlsTeams.txt', 'r')
d1TeamsList1 = d1GirlsFile.readlines()
d1TeamsList = []
for team in d1TeamsList1:
    d1TeamsList.append(team.strip())#team.replace('\n', '')
#print(d1TeamsList)

#Gather list of all D2 Girls Teams:
d2GirlsFile = open('Division2GirlsTeams.txt', 'r')
d2TeamsList1 = d2GirlsFile.readlines()
d2TeamsList = []
for team in d2TeamsList1:
    d2TeamsList.append(team.strip())#team.replace('\n', '')
#print(d2TeamsList)

#Gather list of all D2 Girls Teams:
d3GirlsFile = open('Division3GirlsTeams.txt', 'r')
d3TeamsList1 = d3GirlsFile.readlines()
d3TeamsList = []
for team in d3TeamsList1:
    d3TeamsList.append(team.strip())#team.replace('\n', '')
# print(d3TeamsList)

#start by reading in the html file
with open('01Girls.html', 'r') as html_file:
    # Reading the file and storing in a variable
    contents = html_file.read()
  
# Creating a BeautifulSoup object and specifying the parser
soup = BeautifulSoup(contents, 'lxml')

#create a list of the html code that represents each player
players  = soup.find_all('tr')
players.remove(players[0])

#run through each block of html code belonging to each player, adding necessary info to row in 2d array
playerInfoTable = []
for player in players:
    playerInfo1 = player.find_all('td')
    playerName = player.find_all('div')
    playerInfo =[]
    # print("Player Name: ")
    for row in playerName:  #adds name, club, and gender to 
        playerInfo.append(row.text)
    for i in range(1, len(playerInfo1)):
        if i == 5 or i == 3: #adds school and commitment status
            playerInfo.append(playerInfo1[i].get_text())
    #playerInfoTable.append(playerInfo)
    SchoolName1 = playerInfo[4].replace("- ", " ")
    SchoolName = SchoolName1.replace(" and ", " & ")
    #print(SchoolName)
    if SchoolName in d1TeamsList:    #adds division
        playerInfo.append(u'D1')
    elif SchoolName in d2TeamsList:
        playerInfo.append(u'D2')
    elif SchoolName in d3TeamsList:
        playerInfo.append(u'D3')
    else:
        playerInfo.append(u'NAIA')
    playerInfoTable.append(playerInfo)
#print(playerInfoTable)
file1 = open('01Girls.txt', 'w')
file1.truncate(0)

for row in playerInfoTable:
    name = str(row[0].encode('ascii', 'ignore').decode('ascii'))
    name1 = name.encode("utf-8")
    names = name1.replace(" ", "").split(",")
    firstLast = names[1] +" " +names[0]
    file1.write(firstLast)
    file1.write("\n")

# #To get one piece of info at a time:
# for row in playerInfoTable:
#     # print(row[3])
#     file1.write(row[5].encode('ascii', 'ignore').decode('ascii'))
#     file1.write('\n')

# for row in playerInfoTable:
#     playerIDOne = row[0]+'.'+row[1]
#     playerID2 = playerIDOne.replace(" ", "")
#     playerID = playerID2.replace(",", ".")
#     print(playerID)

#To write in table format:
# file1.write('\n'.join([''.join(['{:30}'.format(item) for item in row]) 
#      for row in playerInfoTable]))

#print(playerInfoTable[1][4])
#print(playerInfoTable)


# for r in range(0,len(playerInfoTable)):
#     for c in range(0,r):
#         file1.write(playerInfo1[r][c])
# 
    
    