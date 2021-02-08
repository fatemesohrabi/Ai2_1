#csp

class node:
    def __init__(self, value, index):
        self.value = value
        self.index=index
        self.row = index // n
        self.column = index % n
        self.deleted = False
def read_file():
    infile = open("sample1.txt","r")
    global n,start,goals,arr
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
read_file()