#
#  Example program for Targil 1
#
import math
from myboolfuncs import *
#
# Area calculation program
def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return math.pi * r**2
#
# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return
#
# main program
#
print ("Welcome to the Area calculation program")
print ("---------------------------------------\n")
# Print out the menu
shapes = ("Rectangle", "Circle")
while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes)
    # Get the user's choice:
    shape = input("> ")
    # Calculate the area:
    if shape == "1":
         height = getNumber("Please enter the height: ")
         width  = getNumber("Please enter the width: ")
         area = rectangleArea(width, height)
         print ("The area is", area)
         continue
    elif shape == "2":
         radius = getNumber("Please enter the radius: ")
         area   = circleArea(radius)
         print ("The area is", area)
         continue
    elif shape == "0":
         print ("Bye!")
         break
    else:
         print ("Invalid shape")
