class bookNode:
    count = 0
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
    def _printBooks(self, bkNode):

        outFile = open('outputPS6.txt', 'a')


        if self.left:
            self.left._printBooks(self.right)

        if self.bookId:
            outFile.write(str(self.bookId) + '\n')

        if self.right:
            self.right._printBooks(self.left)


        outFile.close()    
    
    def _notIssued(self, bkNode):

        outFile = open('outputPS6.txt', 'a')
        if self.bookId:
            if (self.checkoutCount == 0):
                outFile.write(str(self.bookId)+'\n')
        if self.left:
            self.left._notIssued(bkNode)
        if self.right:
            self.right._notIssued(bkNode)
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
          
    
    def _getTopBooks(self, bkNode):
        bookIdCheckOutTuple = []
        self._calculateBookIdCheckOutTuple(bookIdCheckOutTuple)

        print(bookIdCheckOutTuple)
        # TODO Do bubble sort 3 times and print

    
    def _calculateBookIdCheckOutTuple(self, bookIdCheckOutTuple):
        if self.bookId:
            bookIdCheckOutTuple.append((self.bookId, self.checkoutCount))
        if self.left:
            self.left._calculateBookIdCheckOutTuple(bookIdCheckOutTuple)
        if self.right:
            self.right._calculateBookIdCheckOutTuple(bookIdCheckOutTuple)
    
    def _findBook(self, eNode, bkID):
        pass
    
    def _stockOut(self, eNode):
        stockOut = []
        self._fetchStockOutBooks(stockOut)
        
        if (len(stockOut) != 0):
            with open('outputPS6.txt', 'a') as file:
                file.write("All available copies of the below books have been checked out:\n")
                for id in stockOut:
                    file.write(str(id) + "\n")

    def _fetchStockOutBooks(self, stockOut):
        if self.bookId:
            if (self.availCount == 0):
                stockOut.append(self.bookId)
        if self.left:
            self.left._fetchStockOutBooks(stockOut)
        if self.right:
            self.right._fetchStockOutBooks(stockOut)
            


class InvalidOperationException(Exception): pass
