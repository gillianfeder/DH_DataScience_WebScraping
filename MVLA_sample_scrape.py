from bs4 import BeautifulSoup #python -m pip install bs4 
import sys
import requests            
import lxml
from lxml import html
""" Purpose: A sample web scraping script meant to demonstrate how webscraping 
works with the BeautifulSoup module. Gathers all team names and coaches from
the MVLA website and organizes into a file called MVLA_Girls_Teams.txt"""
#Make sure you have all necessary packages installed using pip
    #ex: python -m pip install lxml  or pip3 install requests       


def getTeamInfo():
    #Step 1: find your website and convert it into a beautiful soup object for parsing
    html_text = requests.get('https://mvlasc.org/girls-teams/').text
    soup = BeautifulSoup(html_text, 'lxml')
    
    #Step 2: determine what tags are affiliated with the data you want to gather.
            # find_all adds all sections of HTML with this tag to a list 
    teams = soup.find_all('tr') 
    
    #Step 3: open and clear the file you will be writing to; can use append or write mode
    file1 = open('MVLA_Girls_Teams.txt', 'a')
    file1.truncate(0)
    
    #Step 4: Go through all data points and gather the necessary information about them 
            # Write to the file as a formatted string to make as readable as possible
    for i in (range(1, len(teams))): #started at 1 because the first tr is the header of the table, not a real team 
        teamName = teams[i].find('td', class_ = 'column-1').text
        coachName = teams[i].find('td', class_='column-2').text
        file1.write(f'Team Name: {teamName.strip()} with coach: {coachName.strip()}')
        file1.write("\n")

if __name__ == '__main__':
    getTeamInfo()
    print("complete")