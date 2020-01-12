"""This class is for ADT of BST and contains all Library related operations and supporting methods."""


class bookNode:
    count = 0


    def __init__(self, bkId, availCount):
        self.bookId = bkId
        self.availCount = availCount
        self.checkoutCount = 0
        self.left = None
        self.right = None


    """
        This function reads the book ids and the number of copies available from the inputPS6.txt file. 
        One book id should be populated per line (in the input text file) along with the number of copies separated by a comma. 
        The input data is used to populate the tree. Use a trigger function to call this recursive function from the root node.
    """


    def _readBookList(self, bkId, availCount):
        if self.bookId:
            if bkId < self.bookId:
                if self.left is None:
                    self.left = bookNode(bkId, availCount)
                else:
                    self.left._readBookList(bkId, availCount)
            elif bkId > self.bookId:
                if self.right is None:
                    self.right = bookNode(bkId, availCount)
                else:
                    self.right._readBookList(bkId, availCount)
        else:
            self.bookId = bkId
            self.availCount = availCount
        return None


    # Retrieving book details from this library system as IN-ORDER traversal and write to outputPS6.txt,
    """
    The input should be read from the promptsPS6.txt file where the range is mentioned with the tag as shown below.
    printInventory
    This function prints the list of book ids and the available number of copies in the file outputPS6.txt.
    The output file should show:
    There are a total of xx book titles in the library. 100001, 0
    100002, 5
    100003, 13
    Ensure that you use a traversal method that displays the sequence of books in ascending order of book id.
    """


    def _printBooks(self, bkNode):
        listOfBook = []
        self._inOrder(listOfBook)
        with open('outputPS6.txt', 'a') as outFile:
            outFile.write(str("There are a total of " + str(len(listOfBook)) + " book titles in the library:") + "\n")
            for book in listOfBook:
                outFile.write(str(book.bookId) + ', ' + str(book.availCount) + "\n")


    def _inOrder(self, listOfBook):
        if self.left:
            self.left._inOrder(listOfBook)

        if self.bookId:
            listOfBook.append(self)

        if self.right:
            self.right._inOrder(listOfBook)


    """
    This function is triggered when the following tag is encountered in the promptsPS6.txt file
    BooksNotIssued
    The function searches the list of books in the system and generates a list of books which have never been checked out.
    The output of this list is put into the outputPS6.txt file as shown below.
    """


    def _notIssued(self, bkNode):
        listOfBook = []
        self._inOrder(listOfBook)
        with open('outputPS6.txt', 'a') as outFile:
            outFile.write(str("List of books not issued:") + "\n")
            for book in listOfBook:
                if book.checkoutCount == 0:
                    outFile.write(str(book.bookId) + "\n")


    """
    This function updates the check in / check out status of a book based on the book id. The function reads the input from the promptsPS6.txt file. 
    The below sample lines should be part of the promptsPS6 file to indicate if a book is checked in or checked out. If a book is checked out, the available count is reduced by one and the checkout counter is incremented by one. 
    If a book is checked in, the available counter is incremented and the checkout counter is not altered.
    """


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
                    self.checkoutCount += 1
                    return
            elif (inOut == "checkIn"):
                self.availCount += 1
                return
        if self.left:
            self.left._traverseTreeAndUpdate(bkID, inOut)
        if self.right:
            self.right._traverseTreeAndUpdate(bkID, inOut)


    """
    This function is triggered when the - ListTopBooks   tag is encountered in the promptsPS6.txt file
    The function searches through the list of books and the checkout counter and determines which are the top three books 
    that have been checked out the most and lists those books and the number of times 
    they have been checked out into the outputPS6.txt file as shown below.
    """


    def _getTopBooks(self, bkNode):
        bookIdCheckOutTuple = []
        self._calculateBookIdCheckOutTuple(bookIdCheckOutTuple)

        # print(bookIdCheckOutTuple)
        self._fetchTopThree(bookIdCheckOutTuple, 3)
        # print(bookIdCheckOutTuple)

        with open('outputPS6.txt', 'a') as file:
            last = len(bookIdCheckOutTuple) - 1
            for k in range(min(len(bookIdCheckOutTuple), 3)):
                file.write(f"Top Books {k + 1}: {bookIdCheckOutTuple[last][0]}, {bookIdCheckOutTuple[last][1]} \n")
                last -= 1


    def _fetchTopThree(self, books, top):
        n = len(books)

        calc_top = min(n, top)
        for i in range(calc_top):
            for j in range(0, n - i - 1):
                if books[j][1] > books[j + 1][1]:
                    books[j], books[j + 1] = books[j + 1], books[j]


    def _calculateBookIdCheckOutTuple(self, bookIdCheckOutTuple):
        if self.bookId:
            bookIdCheckOutTuple.append((self.bookId, self.checkoutCount))
        if self.left:
            self.left._calculateBookIdCheckOutTuple(bookIdCheckOutTuple)
        if self.right:
            self.right._calculateBookIdCheckOutTuple(bookIdCheckOutTuple)


    """
    his function reads the promptsPS6.txt file to get the book id that needs to be searched for availability in the system.
    The function reads the id from the file promptsPS6.txt where the search id is mentioned with the tag as shown below.
    findBook: 100005  -- example 
    The search function is called for every findBook tag the program finds in the promptsPS6.txt file.
    If the book id is found, the below string is appended to the into the outputPS6.txt file Book id xx is available for checkout
    If the book id is found but all the copies have been checked out, the below string is output into the outputPS6.txt file
    All copies of book id xx have been checked out
    If the book id is not found it outputs the below string into the outputPS6.txt file Book id xx does not exist.
    """


    def _findBook(self, eNode, bkID):
        found = {"status": False}

        self._findBookNode(bkID, found)

        if (found["status"] == False):
            with open('outputPS6.txt', 'a') as file:
                file.write("Book id " + str(bkID) + " does not exist\n")


    def _findBookNode(self, bkID, found):
        if self.bookId == bkID:
            found["status"] = True
            with open('outputPS6.txt', 'a') as file:
                if (self.availCount == 0):
                    file.write("All copies of book id " + str(bkID) + " have been checked out\n")
                else:
                    file.write("Book id " + str(bkID) + " is available for checkout\n")
            return
        else:
            if (bkID < self.bookId):
                if self.left:
                    self.left._findBookNode(bkID, found)
            else:
                if self.right:
                    self.right._findBookNode(bkID, found)


    """
    This function is triggered when the following tag is encountered in
    the promptsPS6.txt file
    ListStockOut
    This function searches for books for which all the available copies have been checked out and outputs the list into the outputPS6.txt file.
    All available copies of the below books have been checked out:
    100001
    """


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
