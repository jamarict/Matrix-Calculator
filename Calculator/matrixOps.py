import math
import copy

#From CMU 15-112: http://www.cs.cmu.edu/~112-f22/notes/notes-variables-and-functions.html#HelperFunctions
#Verifies if two values are equal to the 10th decimal place
def almostEqual(d1, d2):
    epsilon = 10**-10
    return (abs(d2 - d1) < epsilon)

#Adds row j multiplied by scalar s to row i
def scalarSumRowsMutating(L, i, j, s):
    L[i] = [L[i][k] + (L[j][k] * s) for k in range(len(L[i]))]  

#Multiplies row i by scalar s
def scalarRowMutating(L, i, s):
    L[i] = [L[i][j] * s for j in range(len(L[i]))]
 
#Changes positions of row i and j
def interchangeRowsMutating(L, i, j):
    L[i], L[j] = L[j], L[i]

#Counts rows of zeros and pops them, then appends them to the end of the list
def interchangeZeroesRowsMutating(L):
    col = len(L[0])
    i = 0
    count = 0
    while i < len(L):
        count1 = 0
        for item in L[i]:
            if almostEqual(item, 0):
                count1 += 1
        if count1 == len(L[i]):
            L.pop(i)
            count += 1
        else:
            i += 1
    for j in range(count):
        L.append([0] * col)

#Moves zero rows to the bottom, then finds the pivot indices. Makes sure they
#are in order descending + left to right order   
def isREF(L):
    interchangeZeroesRowsMutating(L)
    rows = len(L)
    cols = len(L[0])
    indices = []
    for row in range(rows):
        for col in range(cols):
            if not(almostEqual(L[row][col],0)):
                if (col) in indices:
                    return False
                else:
                    indices.append(col)
                    break
    return indices == sorted(indices)
