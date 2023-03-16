class Line: 

    __start=None
    __end=None

    def __init__(self, start, end):
        self.__start=start
        self.__end=end

    def validLine(self): 
        if self.__start[0]!=self.__end[0] and self.__start[1]!=self.__end[1]:
            return False
        else:
            return True
    
    def getStart(self):
        return self.__start
    
    def getEnd(self):
        return self.__end
    
    def printLine(self):
        print(self.__start,self.__end)

    def equals(self,l2):
        if self.__start==l2.__start & self.__end==l2.__end:
            return True
        else:
            return False
    
    def list(self):
        return [self.__start[0],self.__start[1],self.__end[0],self.__end[1]]

