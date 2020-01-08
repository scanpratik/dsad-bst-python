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
Perform Check In Check Out based on promptsPS6.txt
"""

def checkInCheckOut(path):
    with open(path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        command, bookId = line.split(": ")
        books._chkInChkOut(int(bookId), command)

checkInCheckOut("promptsPS6.txt")

print("\n Post checkInCheckOut \n")
books.PrintTree()