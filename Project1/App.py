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
            table.changeSymbol(i,"x")
        if line.getEnd()[0]==table.getValue(i)[0] and line.getEnd()[1]==table.getValue(i)[1]:
            table.changeSymbol(i,"x")


    
def used(line): ##returning None
    flag=False
    for i in range (len(lines)):
        if line.list()==lines[i]:
            return True
        else: 
            
            return False

def turn(table,t):
     
    x=newLine() ##Good 
    print(x.validLine()) ##Returning a value but not the right one
    print (used(x)) ##returning None
    while used(x)==True:
        print("Enter a valid unused line ")
        x=newLine()
        print(x.printLine())
        
    lines.append(x.list())
    updateTable(x,table) ##Good
    print("lines: ",lines)
    print("used",used(x))
    player+=1
    if square(x): ##Returning None
        if t%2==0:
            player1+=1
        else:
            player2+=1
        
    
    print ("square", square(x), "score", player)
    table.printTable()
    
def square(l): 
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
    size=table.getSize()-1
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
      
        turn(table,t)
        t+=1
        print(t)
        print(end)
        
        end=endGame(table)
   

    print("Score: ")
    print("Player 1: "+str(player1))
    print ("Player 2: "+str(player2))
        

    
    
    




main()
