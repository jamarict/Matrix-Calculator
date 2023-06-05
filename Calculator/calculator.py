from matrixOps import *

#Checks if the current column is full of zeros
#If not, returns the current row
def zeroColCheck(L, currRow, currCol):
    rows = len(L)
    for row in range(currRow, rows):
        if not(almostEqual(L[row][currCol],0)):
            return False, row
    return True, None

#Keeps the pivot at currRow and removes it from all rows below it
#Creates additive inverse with scalar
def createPivots(L, currRow, currCol):
    rows = len(L)
    for row in range(currRow + 1, rows):
        scalarSumRowsMutating(L, row, currRow, -(L[row][currCol]/L[currRow][currCol]))

#Main function to make Row Echelon Form. Returns as new list
def makeREF(L):
    M = copy.deepcopy(L)
    makeREFHelper(M)
    return M

#Mutating helper function to make a list REF
def makeREFHelper(L, currRow = 0, currCol = 0):
    #BC: Already in REF
    if isREF(L):
        return
    else:
        isZeroCol, rowIndex = zeroColCheck(L, currRow, currCol)
        #Zero Col, go over to the next column
        if isZeroCol:
            currCol += 1
            return makeREFHelper(L, currRow, currCol)
        #Not a zero col but zero entry, switch whatever row is not zero
        elif almostEqual(L[currRow][currCol],0):
            interchangeRowsMutating(L, currRow, rowIndex)
        #Makes pivots below and move to the next row and column
        createPivots(L, currRow, currCol)
        currRow += 1
        currCol += 1
        return makeREFHelper(L, currRow, currCol)

#Main function to make a list into Reduced Row Echelon Form. Uses REF and returns a new list
def makeRREF(L):
    M = makeREF(L)
    makeRREFHelper(M)
    return M

#Mutating helper that makes a list RREF
def makeRREFHelper(L):
    rows = len(L)
    #For each row, find the pivot, scale it to 1, then remove all entries above it
    for row in range(rows-1, -1, -1):
        colIndex = findPivotIndex(L, row)
        #No pivots, move to the next row above
        if colIndex == None:
            continue
        scalePivot(L, row, colIndex)
        removeAbovePivots(L, row, colIndex)
    return

#Finds pivot location at the specified row, returns None if there is no pivot (all zeros)
#otherwise returns column index
def findPivotIndex(L, row):
    for i in range(len(L[0])):
        if not(almostEqual(L[row][i],0)):
            return i
    return None

#Gets the pivot location, then scales the row by its multiplicative inverse
def scalePivot(L, row, col):
    pivot = L[row][col]
    scalarRowMutating(L, row, (1/pivot))
   
#Removes entries above the pivor by creating additive inverse
def removeAbovePivots(L, currRow, currCol):
    for row in range(currRow):
        scalarSumRowsMutating(L, row, currRow, -(L[row][currCol]/L[currRow][currCol]))


