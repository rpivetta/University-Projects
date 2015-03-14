# fp.py. Sixth programming project for CIS 211 (WQ 2015).


# Author: Ricardo Pivetta.

# This module fill all the requirements for project six.


'''Import string punctuation for later use'''
from string import punctuation

'''function for exercise number 1'''
def codes(ch):
  return list(map(ord, ch))

'''function for exercise number 2'''
def vowels(ch):

  '''Helper function that checks if the char is a vowel'''
  def isVowel(char):
    if char in 'aeiouAEIOU':
      return True
    else:
      return False
  
  '''returning the string with only vowels'''
  return ''.join(filter(isVowel, ch))

'''function for exercise number 3'''
def tokens(ch):
  
  '''Helper function that split strings by punctuation'''
  def strip_punctuation(s):
    return s.strip(punctuation)
  
  '''returning the list'''
  return  map(strip_punctuation, ch.split())

'''function for exercise number 4'''
def numbers(ch):
  '''returning the list using the function isdigit'''
  return list(filter(str.isdigit, tokens(ch)))

'''Creating the class Room for exercise number 5'''
class Room:
  def __init__(self, params):
    '''Spliting the string by punctuation'''
    content = list(tokens(params))
    '''Initializing the class atributes'''
    self.room = content[0]
    self.width = float(content[1])
    self.depth = float(content[2]) 
  '''function that returns the room area'''
  def area(self):
  	return self.width * self.depth
'''function for exercise number 5'''
def sq_ft(textFile):
  '''opening the file'''
  with open (textFile, 'r') as room_list:
    rooms = room_list.readlines()
  '''return the sum of the areas of each room'''
  return sum(map(Room.area, list(map(Room, rooms))))