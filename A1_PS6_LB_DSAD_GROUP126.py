class bookNode:
    def __init__(self, bkId , availCount):
        self.bookId = bkId
        self.availCount = availCount
        self.checkoutCount = 0
        self.left = None
        self.right = None
    
    def readBookList(self, bkID, availCount):
        pass
    
    def chkInChkOut(self, bkID, inOut):
        pass
    
    def getTopBooks(self, bkNode):
        pass
    
    def notIssued(self, bkNode):
        pass
    
    def findBook(self, eNode, bkID):
        pass
    
    def stockOut(self, eNode):
        pass
    
    def printBooks(self, bkNode):
        pass