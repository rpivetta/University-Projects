# rescraper.py. Programming project 8 for CIS 211 (WQ 2015).


# Author: Ricardo Pivetta.

# This module fill all the requirements for project 8.

from urllib.request import urlopen
import re import findall
import sys

page = urlopen(sys.argv[1])

#read and decode the url
page_info = page.read().decode()

#creating a variable that is readable by the user
user_info = ""

#read each line of the decoded url
for line in page_info.split('\n'): 
  if '<table class="linescore' in line: #check if the line contains the score
    final_score = findall(r'"final score".*?>(.*?)</td>', line)#assign the score to a variable
    team_name = findall(r'<a.*?>(.*?)</a>', line)#assign the team name to a variable
    user_info = user_info + team_name[0] + ' ' + final_score[0] + ', ' + team_name[1] + ' ' + final_score[1]+'\n'#make a readable string for the user

print(user_info)