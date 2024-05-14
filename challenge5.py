class InputOutString:
    def __init__(self):
        self.s = ''
    
    def getstring(self):
        self.s = input()
        
    def printstring(self):
        return self.s.upper()
    
    def test(self):
        return self.s
    
    
strObj = InputOutString()
strObj.getstring()
print(strObj.test())
print(strObj.printstring())