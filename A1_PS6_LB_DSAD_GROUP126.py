from bookNode import bookNode

def readBookList(path):
    inputFile = open(path,'r')
    lines = inputFile.readlines()
    inputFile.close()
    for line in lines:
        bookEntry = line.split(', ')
        bookId = int(bookEntry[0])
        count = int(bookEntry[1])
        books._readBookList(bookId , count)
    return None


books = bookNode(0,0)
readBookList("inputPS6.txt")
books.PrintTree()


"""
Perform Operations based on promptsPS6.txt
"""

def readPrompts(path):
    with open(path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if (line.trim() == "ListTopBooks"):
            books._getTopBooks(books)
        elif (line.trim() == "BooksNotIssued"):
            books._notIssued(books)
        elif (line.trim() == "ListStockOut"):
            books._stockOut(books)
        elif (line.trim() == "printInventory"):
            books._printBooks(books)
        else:
            command, bookId = line.split(": ")
            if (command == "findBook"):
                books._findBook(books, bookId)
            else:
                books._chkInChkOut(int(bookId), command)

readPrompts("promptsPS6.txt")

print("\n Post checkInCheckOut \n")
books.PrintTree()