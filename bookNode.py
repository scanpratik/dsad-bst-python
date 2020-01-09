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
        print( str(self.bookId) +' -- ' + str(self.availCount))
        if self.right:
            self.right.PrintTree()     
    
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
          
    
    def _getTopBooks(self, bkNode):
        pass
    
    def _notIssued(self, bkNode):
        pass
    
    def _findBook(self, eNode, bkID):
        pass
    
    def _stockOut(self, eNode):
        pass
    
    def _printBooks(self, bkNode):
        pass

class InvalidOperationException(Exception): pass