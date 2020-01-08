class bookNode:
    def __init__(self, bkId , availCount):
        self.bookId = bkId
        self.availCount = availCount
        self.checkoutCount = 0
        self.left = None
        self.right = None
    
    def _readBookList(self, bkId , availCount):
        if self.bookId:
            if bkId < self.bookId:
                if self.left is None:
                    self.left = bookNode(bkId , availCount)
                else:
                    self.left._readBookList(bkId , availCount)
            elif bkId > self.bookId:
                if self.right is None:
                    self.right = bookNode(bkId , availCount)
                else:
                    self.right._readBookList(bkId , availCount)
        else:
            self.bookId = bkId
            self.availCount = availCount
        return None
   
   #TODO -- this method id just for testing , will remove later on .
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.bookId +' -- ' + self.availCount)
        if self.right:
            self.right.PrintTree()     
    
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
