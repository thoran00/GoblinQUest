from PIL import Image
import requests
from io import BytesIO
import turtle
import sys
import time

# Test image: 10x10
Maze1 = "https://i.ibb.co/kJMFzHx/10-by-10-orthogonal-maze.png"

# Test image: 15x15
Maze2 = "https://i.ibb.co/Xt2NTGn/15-by-15-orthogonal-maze.png"

# Test image: 20x20
Maze3 = "https://i.ibb.co/C5mQQCZ/20-by-20-orthogonal-maze.png"

# Test image 30x30
Maze4 = "https://i.ibb.co/bKSLyLk/30-by-30-orthogonal-maze.png"


# Define functions
def defaultmaze():
  userchoice=input("Would you like to create your own maze or select from some default choices?\n(Press 1 for the former, 2 for the latter)")
  if userchoice=='2':
    x=0
    mazechoice=input("We have Maze 1, Maze 2, Maze 3, and Maze 4. Which maze would you like to solve?")
    while x==0:
       if mazechoice=='Maze 1':
          print("The url of Maze 1 is", Maze1)
          x=1
          return
       elif mazechoice=='Maze 2':
          print("The url of Maze 2 is", Maze2)
          x=1
          return
       elif mazechoice=='Maze 3':
          print("The url of Maze 3 is", Maze3)
          x=1
          return
       elif mazechoice=='Maze 4':
          print("The url of Maze 4 is", Maze4)
          x=1
          return
       else:
          print("Error: The choice wasn't one of the mazes (Type the name of the maze exactly how it appears in the instructions).")
          return defaultmaze()
  elif userchoice=='1':
    pass
  else:
    print("Follow instructions: Input either 1 or 2")
    return defaultmaze()

def timer():
   challengemode=input("Press the c key to initiate a timer countdown of your choosing to challenge yourself to solve the maze. Press any other button to solve the maze normally.")
   if challengemode!="c":
      print("Chicken! Go ahead and solve the maze!")
      #right here a block of code will go for the user to solve the maze normally, without a time limit
   else:
      #same as above, except constrained by a time limit
      _input=int(input("How much time do you think you need to solve the maze (in seconds)?"))
      for i in range(_input, 0, -1):
         print(i)
         time.sleep(1)
      print("You ran out of time!")
      sys.exit()



def loadimage():
    try:
      if defaultmaze()==True:
        return Image.open(Bytes.IO(requests.get(url)).content).convert('RGB')
      else:
        return Image.open(BytesIO(requests.get(input("Enter image URL:")).content)).convert('RGB')
    except requests.exceptions.MissingSchema:
        print("ERROR: The image URL you entered is invalid. Try another one.")
    except requests.exceptions.ConnectionError:
        print("ERROR: The image URL you entered is invalid. Try another one.")
    except OSError:
        print("ERROR: The image URL you entered is invalid. Try another one.")
    return loadimage()


def getpixels(image):
    coords = []
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.getpixel((x, y)) == (0, 0, 0):
                coords.append([x, y])
    return coords


def optimizeX(lofcrds, singlelist):
    counter = 0
    crdflag = False
    ogcrds = []
    xfinal = []
    for coordset in lofcrds:
        try:
            clindex = lofcrds.index(coordset)
            if coordset[1] + 1 == lofcrds[clindex + 1][1]:
                if crdflag is False:
                    crdflag = True
                    ogcrds = coordset
                counter += 1
            elif crdflag:
                if counter <= 2:
                    singlelist.append([ogcrds[0], ogcrds[1]])
                    singlelist.append([lofcrds[clindex][0], lofcrds[clindex][1]])
                else:
                    xfinal.append([[ogcrds[0], -ogcrds[1]], [lofcrds[clindex][0], -lofcrds[clindex][1]]])
                crdflag = False
                ogcrds = []
                counter = 0
        except IndexError:
            continue
    return xfinal


def optimizeY(singlelist):
    crdflag = False
    ogcrds = []
    yfinal = []
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if [x, y] in singlelist:
                if crdflag is False:
                    crdflag = True
                    ogcrds = [x, -y]
            elif crdflag:
                yfinal.append([ogcrds, [x - 1, -y]])
                crdflag = False
                ogcrds = []
    return yfinal


def centercoords(xlist, ylist, image):
    xsize = image.size[0] / 2
    ysize = image.size[1] / 2
    for xcoordset in xlist:
        for coord in xcoordset:
            coord[0] = coord[0] - xsize
            coord[1] = coord[1] + ysize

    for ycoordset in ylist:
        for coord in ycoordset:
            coord[0] = coord[0] - xsize
            coord[1] = coord[1] + ysize


def drawmaze(turt, turtcolor, xlist, ylist):
    try:
        if turtcolor.upper() == 'B':
            turtcolor = "Black"
        turt.color(turtcolor)
    except turtle.TurtleGraphicsError:
        print("ERROR: The color \"" + turtcolor + "\" is invalid. Try a different one.")
        drawmaze(turt, input("What color would you like your maze to be:"), xlist, ylist)

    turt.speed(0)
    turt.pensize(2)
    for coords in xlist:
        turt.penup()
        turt.goto(coords[0])
        turt.pendown()
        turt.goto(coords[1])

    for coords in ylist:
        turt.penup()
        turt.goto(coords[0])
        turt.pendown()
        turt.goto(coords[1])
    turt.hideturtle()


# Main program
img = loadimage()
ogcoordlist = getpixels(img)
revcoordlist = []
optxcoords = optimizeX(ogcoordlist, revcoordlist)
optycoords = optimizeY(revcoordlist)
centercoords(optxcoords, optycoords, img)

wn = turtle.Screen()
wn.setup(600, 600)
draw = turtle.Turtle()
drawmaze(draw, input("What color would you like your maze to be?\n(Enter 'b' for black default):"), optxcoords, optycoords)
timer()
wn.exitonclick()
