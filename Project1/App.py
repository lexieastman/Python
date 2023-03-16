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


    
def used(line): ##returning None
    flag=False
    for i in range (len(lines)):
        if line.list()==lines[i]:
            return True
        else: 
            
            return False

def turn(player,table):
    x=newLine() ##Good 
    print(x.validLine()) ##Returning a value but not the right one
    print (used(x)) ##returning None
    while used(x)==True:
        x=newLine()
        print(x.printLine())
        print("Enter a valid line ")
    lines.append(x.list())
    updateTable(x,table) ##Good
    print("lines: ",lines)
    print("used",used(x))
    if square(x): ##Returning None
        player+=1
    
    print ("square", square(x), "score", player)
    table.printTable()
    
def square(l): ##Returning None
    for i in range (len(lines)): 
        if lines[i]==[l.list()[0],l.list()[1],l.list()[2],l.list()[3]-1] and lines[i]==[l.list()[0],l.list()[1],l.list()[2]+1,l.list()[3]] and lines()[i]==[l.list()[0],l.list()[1]+1,l.list()[2]+1,l.list()[3]]:
                    return True
        elif lines[i]==[l.list()[0],l.list()[1],l.list()[2]-1,l.list()[3]+1] and lines[i]==[l.list()[0]+1,l.list()[1],l.list()[2],l.list()[3]+1] and lines[i]==[l.list()[0],l.list()[1]+1,l.list()[2],l.list()[3]+1]:
                    return True
        elif lines[i]==[l.list()[0]-1,l.list()[1],l.list()[2]-1,l.list()[3]] and lines[i]==[l.list()[0]-1,l.list()[1],l.list()[2],l.list()[3]-1] and lines[i]==[l.list()[0]-1,l.list()[1]+1,l.list()[2],l.list()[3]]:
                    return True
        elif lines[i]==[l.list()[0],l.list()[1]-1,l.list()[2]-1,l.list()[3]] and lines[i]==[l.list()[0],l.list()[1]-1,l.list()[2],l.list()[3]-1] and lines[i]==[l.list()[0]+1,l.list()[1]-1,l.list()[2],l.list()[3]]:
                    return True
        else:
             return False
   
def endGame(table): ##Returning None
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
    
    while (end==False):
        if t%2==0:
            p=player1
            print("Player 1 turn: ")
        else:
            p=player2
            print("player 2 turn: ")
        
        turn(p,table)
        t+=1
        print(t)
        
        end=endGame(table)
   

    print("Score: ")
    print("Player 1: "+str(player1))
    print ("Player 2: "+str(player2))
        

    
    
    




main()
