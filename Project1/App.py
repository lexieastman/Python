
from Line import Line
from Table import Table

lines=[]
player1= ""
player2= ""
turn = player1
lines=[]

def createTable():
    t=Table(4,4)
    t.constructTable()
    print("reference coordinates: ")
    t.printCoordinates()
    return t


def newLine():
    print ("Enter verticle coordinate for line start: ")
    x=int(input())
    print("Enter horizontal coordinate for line start point: ")
    y=int(input())
    print ("Enter verticle coordinate for line end point: ")
    a=int(input())
    print("Enter horizontal coordinate for line end point: ")
    b=int(input())
    line=Line([x,y],[a,b])
    lines.append ([x,y])
    lines.append ([a,b])
    
    return line



def updateTable(line,table): 
    for i in range(table.getSize()):
        if line.getStart()[0]==table.getValue(i)[0] and line.getStart()[1]==table.getValue(i)[1]:
            table.changeSymbol(i,"X")
        if line.getEnd()[0]==table.getValue(i)[0] and line.getEnd()[1]==table.getValue(i)[1]:
            table.changeSymbol(i,"X")

##def square(l):

##def turn():


def main():
    table= createTable()
    table.printTable()
    line=newLine()
    updateTable(line,table)
    table.printTable()
    print(lines)
    




main()
