
     class Table: 

    __size=0
    __veticle=None
    __horizontal=None
    __list=[]

    def __init__(self, vert, horiz):
        self.__verticle=vert
        self.__horizontal=horiz
    
    def constructTable(self):
        
        for i in range (self.__verticle):
            for j in range (self.__horizontal):
                self.__list.append([i,j,"*"])
                self.__size+=1

    
    def printTable(self):
        count=0;
        
        for i in range (len(self.__list)):
            count+=1
            if count%self.__horizontal==0:
                x='\n'
            else:
                x=""
            
            print (self.__list[i][2]," ",end=x)

    def printCoordinates(self):
        count =0
        for i in range (len(self.__list)):
            count+=1
            if count%self.__horizontal==0:
                x='\n'
            else:
                x=""
            
            print ("[",self.__list[i][0],",", self.__list[i][1],"]",end=x)


    def changeSymbol(self, i, x):
        self.__list[i][2]=x


    def getSize(self):
        return self.__size
    
    def getValue(self, i):
        return self.__list[i]
    
    def getWidth(self):
        return self.__horizontal


            





            


