import random
from queue import LifoQueue
class node:
    def __init__(self, value, index):
        self.value = value
        self.index=index
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
    '''lane = 0
    for i in range(n*n):
        lane+=1
        print(arr[i].index,"\t",end="")
        if lane % 9 == 0:
            print()'''
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
#def CSP() 

#--------------------------------
##############################################################################################
read_file()
heuristic()
