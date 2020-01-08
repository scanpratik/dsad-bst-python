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
   
   #Retrieving book details from this libraray system as IN-ORDER traversal and write to outputPS6.txt,
    def _printBooks(self):
        outFile = open('outputPS6.txt', 'w')
        outFile = open('outputPS6.txt', 'a')
        if self.left:
            self.left._printBooks()
            
        if self.bookId:
            outFile.write(self.bookId+', '+ self.availCount +'\n')
        
        if self.right:
            self.right._printBooks()  
        outFile.close()    
    
    def _notIssued(self, bkNode):
        outFile = open('outputPS6.txt', 'w')
        outFile = open('outputPS6.txt', 'a')
        if self.bookId:
            if (self.checkoutCount == 0):
                outFile.write(self.bookId +', '+ self.availCount)
        if self.left:
            self.left._notIssued('')
        if self.right:
            self.right._notIssued('')
        outFile.close()
    
    def _chkInChkOut(self, bkID, inOut):
        if (inOut == "checkOut"):
            self._traverseTreeAndUpdate(bkID, inOut)
        else:
            self._traverseTreeAndUpdate(bkID, inOut)

    
    def _traverseTreeAndUpdate(self, bkID, inOut):

        if self.bookId == bkID:
            if (inOut == "checkOut"):
                if (self.availCount == 0):
                    raise InvalidOperationException("Can Not checkOut when availCount is 0")
                else:
                    self.availCount -= 1
                    self.checkoutCount +=1
                    return
            elif (inOut == "checkIn"):
                self.availCount += 1
                return
        if self.left:
            self.left._traverseTreeAndUpdate(bkID, inOut)
        if self.right:
            self.right._traverseTreeAndUpdate(bkID, inOut)
          
    
    def getTopBooks(self, bkNode):
        pass
    
    def notIssued(self, bkNode):
        pass
    
    def findBook(self, eNode, bkID):
        pass
    
    def stockOut(self, eNode):
        pass


class InvalidOperationException(Exception): pass
