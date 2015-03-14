# scraper.py. Programming project 8 for CIS 211 (WQ 2015).

# Author: Ricardo Pivetta.

# This module fill all the requirements for project 8.

from html.parser import HTMLParser
from urllib.request import urlopen
import sys
import copy

class Scraper(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self._games = []
    self._flag = False
    self._aux_list = []

  def handle_starttag(self, tag, attrs):
    if tag == 'td' and attrs == [('class','final score')] or tag == 'div' and attrs == [('class','team')]:
      self._flag = True #changing the flag when data is found

  def handle_data(self, text):
    if self._flag:
      self._aux_list.append(text.strip()) #appeding the text to the aux list
      self._flag = False
    if len(self._aux_list) == 4: #checking if the aux_list has all the four elements
      self._games.append(copy.copy(self._aux_list)) #appending the aux_list to the games
      self._aux_list.clear() #cleaning the aux_list

  def print_games(self):#auxiliar function
    for score in self._games:
      print(score[0] + ' ' + score[1] + ', ' + score[2] + ' ' + score[3]) #concatenating the results to make them readable for the user
parser = Scraper()

parser.feed(urlopen(sys.argv[1]).read().decode())

#printing the results
parser.print_games()