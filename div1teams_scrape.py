#Purpose: to scrape ncsasports.org listing of womens soccer teams by division into a usable text file for data base creation
from bs4 import BeautifulSoup #python -m pip install bs4 
import sys
import requests            #NEED TO INSTALL
import lxml
from lxml import html
import unicodedata

with open('division1teams.html', 'r') as html_file:
    # Reading the file and storing in a variable
    contents = html_file.read()
  
# Creating a BeautifulSoup object and specifying the parser
soup = BeautifulSoup(contents, 'lxml')
table1 = soup.find_all('div', class_ = 'row')
listOfD1Schools = []
for row in table1:
    schoolName = row.div.div.text
    listOfD1Schools.append(schoolName)
file1 = open('Division1GirlsTeams.txt', 'a')
file1.truncate(0)
for school in listOfD1Schools:
    schoolString = unicodedata.normalize('NFKD', school).encode('ascii', 'ignore')
    file1.write(schoolString)
    file1.write("\n")