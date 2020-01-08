from bookNode import bookNode

def readBookList(path):
    inputFile = open(path,'r')
    lines = inputFile.readlines()
    for line in lines:
        bookEntry = line.trim().split(', ')
        bookId = bookEntry[0]
        count = bookEntry[1]
        books._readBookList(bookId , count)
    return None


books = bookNode(0,0)
readBookList("inputPS6.txt")
