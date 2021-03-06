import random
import turtle
class node:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.row = index // n
        self.column = index % n
        self.deleted = False
        self.domain = [True, False]
        self.degree = float('inf')
##############################################################################################
def read_file():
    infile = open("sample1.txt","r")
    global n,arr
    a = infile.readline()
    a = a.split(" ")
    n = int(len(a))
    infile.close()
    infile = open("sample1.txt","r")
    arr = []
    index = 0
    for i in range(n):
        temp = infile.readline().split(' ')
        for j in range(n):
            TempNode = node(int(temp[j]),index)
            arr.append(TempNode)
            index += 1
##############################################################################################
def heuristic():
    for i in range(len(arr)):
        if (arr[i].row == 0 and arr[i].column == 0) or (arr[i].row == 0 and arr[i].column == n-1) or (arr[i].row == n-1 and arr[i].column == 0) or (arr[i].row == n-1 and arr[i].column == n-1):
            arr[i].degree = 2
        elif arr[i].row == 0 or arr[i].row == n-1 or arr[i].column == 0 or arr[i].column == n-1:
            arr[i].degree = 3
        else:
            arr[i].degree = 4
##############################################################################################
def find_max_degree():
    maxi = float('-inf')
    for i in range(len(arr)):
        if arr[i].degree > maxi:
            maxi = arr[i].degree
    return maxi
##############################################################################################
def forward_checking(Node):
    for i in range(n*n):
        if arr[i].index == Node.index - 1 and arr[i].deleted != True:
            arr[i].degree -= 1
            arr[i].domain.remove(True)
        if arr[i].index == Node.index + 1 and arr[i].deleted != True:
            arr[i].degree -= 1
            arr[i].domain.remove(True)
        if arr[i].index == Node.index + n and arr[i].deleted != True:
            arr[i].degree -= 1
            arr[i].domain.remove(True)
        if arr[i].index == Node.index - n and arr[i].deleted != True:
            arr[i].degree -= 1
            arr[i].domain.remove(True)
##############################################################################################
def random_pick():
    max_deg = find_max_degree()
    pick_arr = []
    for i in range(n*n):
        if arr[i].degree == max_deg:
            pick_arr.append(arr[i])
    random.shuffle(pick_arr)
    return pick_arr[1]
##############################################################################################
def drawHitori():
    y = n * 20
    turtle.color("light gray")
    turtle.speed(0)
    for i in range (n):
        x = -n * 20
        for i in range(n):
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            turtle.goto(x+40,y)
            turtle.goto(x+40,y-40)
            turtle.goto(x,y-40)
            turtle.goto(x,y)
            turtle.penup()
            x += 40
        y -= 40
    for i in range(len(arr)):
        YPos = (n * 20) - (arr[i].row * 40)
        XPos = (-n *20) + (arr[i].column * 40)
        turtle.goto(XPos+20,YPos-40)
        turtle.color("black")
        style = ('Courier', 20, 'italic')
        turtle.write(arr[i].value, font=style, align='center')
##############################################################################################
#def CSP():
        
##############################################################################################
read_file()
heuristic()
drawHitori()
