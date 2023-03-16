
from Line import Line
from Table import Table

lines=[]
player1= 0
player2= 0
turn = player1
lines=[]


def createTable(x,y):
    t=Table(x,y)
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
    
    
    return line



def updateTable(line,table): 
    for i in range(table.getSize()):
        if line.getStart()[0]==table.getValue(i)[0] and line.getStart()[1]==table.getValue(i)[1]:
            table.changeSymbol(i,"X")
        if line.getEnd()[0]==table.getValue(i)[0] and line.getEnd()[1]==table.getValue(i)[1]:
            table.changeSymbol(i,"X")


    
def used(line):
    for i in range (len(lines)):
        if line.list()==lines[i]:
            flag= True
        else: 
            lines.append(line)
            flag=False
        return flag

def turn(player,table):
    x=newLine()
    print(x.validLine())
    
    while used(x)==True:
        x=newLine()
        print(x.printLine())
        print("Enter a valid line ")
    
    updateTable(x,table)
    
    table.printTable()

   
def endGame(table):
    count=0
    end=False
    size=table.getSize()
    for i in range (size):
        if table.getValue(i)=="X":
            count+=1

    if count==size:
        end=True

    return end


            

def main():
    print("hello")
    table=createTable(4,4)
    print(table.getSize())
    t =0
    end=False
   
   

    while (endGame(table)==False):
        if t%2==0:
            p=player1
            print("Player 1 turn: ")
        else:
            p=player2
            print("player 2 turn: ")
        
        turn(p,table)
        t+=1
   

    print("Score: ")
    print("Player 1: "+str(player1))
    print ("Player 2: "+str(player2))
        

    
    
    




main()
