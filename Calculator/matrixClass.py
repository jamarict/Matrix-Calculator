from vectorClass import*

#Main Matrix Class
#Inspired from CMU 15-112 2023 Midterm 2 & CMU 21-241 2023 Content
class Matrix(object):         
    
    #Initials properties of a matrix that don't rely on other matrices
    def __init__(self,L):
        self.matrix = L
        self.rows, self.cols = self.getDims()
        self.vectorSet = self.getVectors()
        self.isSquare = self.checkSquare()
        self.isTriangular, self.isDiagonal = self.checkTriangular()
        self.determinant = self.findDeterminant()
        self.properties = 0

    #Gets further properties of the matrix that relies on other properties
    #(Done to prevent infinite recursive calls)
    def getProperties(self):
        self.ref = self.getREF()
        self.rref = self.getRREF()
        self.inverse = self.getInverse()
        self.transpose = self.getTranspose() 
        self.pivotLocations = self.findPivots() # Don't Include
        self.freeLocations = self.getFree() #Don't Include
        self.isOnto, self.is1to1 = self.checkConditions()
        self.basis = self.getBasis()
        self.rank = len(self.basis)
        self.nullity = self.cols - self.rank
        self.nullSpace = self.getNullSpace()
        self.isIdempotent = self.checkIdempotent()
        self.isNilpotent = self.checkNilpotent() 
        self.orthogonalBasis = self.getOrthogonalBasis()
        self.orthonormalBasis = self.getOrthonormalBasis()
        self.isOrthogonal = self.checkOrthogonal()
        self.isSymmetric = self.checkSymmetric()
        self.isSkewSymmetric = self.checkSkewSymmetric()
        self.approxEigenValues = self.getEigenValues()

    #Gets row and column length
    def getDims(self):
        return len(self.matrix), len(self.matrix[0])  
    
    #Gets row at specific index
    def getRow(self, row):
        if 0 <= row < self.rows:
            return self.matrix[row]
        return None
    
    #Gets column at specific index
    def getCol(self, col):
        if 0  <= col < self.cols:
            return [self.matrix[row][col] for row in range(self.rows)]
        return None
    
    #Check other is a matrix that shares the same 2d List
    def __eq__(self, other):
        return isinstance(other, Matrix) and checkMatrix(self,other)
    
    #Checks that two items are matrices with same dimensions
    #then adds the corresponding entries into a new matrix.
    #Initializes result as a new Matrix
    def addMatrix(self, other):
        if isinstance(other, Matrix) and self.getDims() == other.getDims():
            finalList = ([[self.matrix[row][col] + other.matrix[row][col] for 
                        col in range(self.cols)] for row in range(self.rows)])
            return Matrix(finalList)
        return None
    
    #Prints rows, cols, and the 2d List representation of the matrix
    def __repr__(self):
        return f"{self.rows} x {self.cols} Matrix\n{self.matrix}"
    
    #Converts Matrix into list of column vectors
    def getVectors(self):
        return [Vector(self.getCol(i)) for i in range(self.cols)]
    
    #Gets value at specified entry
    def getEntry(self,i,j):
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols: return None
        return self.matrix[i][j]
    
    #Creates Row Echelon Form of given Matrix
    def getREF(self):
        return Matrix(makeREF(self.matrix))
    
    #Creates Reduced Row Echelon Form of a given Matrix
    def getRREF(self):
        return Matrix(makeRREF(self.matrix))

    #Creates transpose matrix by swapping row & col entries
    def getTranspose(self):
        return Matrix([[self.matrix[row][col] for row in 
                    range(self.rows)] for col in range(self.cols)])
    
    #Check that the matrix and vector have compatible dimensions
    #Perform dotProduct using row vectors of matrix and input vector
    #Returns result as new Vector
    def MatrixVectorProduct(self,vector):
        if isinstance(vector,Vector) and vector.dims == self.cols:
            result = [0 for val in range(self.rows)] 
            for row in range(self.rows):
                rowVector = Vector(self.getRow(row))
                result[row] = vector.dotProduct(rowVector)
            return Vector(result)
        return None
    
    #Checks square through dims
    def checkSquare(self):
        return self.rows == self.cols

    #Checks the upper and lower triangles
    #If both cases, then diagonal
    def checkTriangular(self):
        if not(self.isSquare):
            return False, False
        if (self.checkUpperTriangle() or 
            self.checkLowerTriangle()):
            if (self.checkUpperTriangle() and 
                self.checkLowerTriangle()):
                return True, True
            else:
                return True, False
        return False, False
    
    #Checks upper triangle for any nonzeros
    def checkUpperTriangle(self):
        for row in range(self.rows):
            #skips over diagonals and ensures upper triangle entries
            for col in range(row+1, self.cols):
                if self.matrix[row][col] != 0:
                    return False
        return True
    
    #Checks lower triangle for any nonzeros
    def checkLowerTriangle(self):    
        for row in range(self.rows):
            #skips over diagonal and ensures lower triangle entires
            for col in range(self.cols - (self.cols - row)):
                if self.matrix[row][col] != 0:
                    return False
        return True

    #Find the pivots locations using RREF matrix
    def findPivots(self):
        L = copy.deepcopy(self.rref.matrix)
        return findPivotsHelper(L)
    
    #Checks that a matrix is Onto and 1to1 by the number of pivots in the matrix
    def checkConditions(self):
        isOnto = len(self.pivotLocations) == self.rows
        is1to1 = len(self.pivotLocations) == self.cols
        return isOnto, is1to1
    
    #Returns list of vectors that correspond to pivot columns, also the ColSpace
    def getBasis(self):
        return [Vector(self.getCol(pivot)) for pivot in self.pivotLocations]
    
    #Returns matrixProduct, order matters
    def matrixProduct(self, other):
        #Compatibility check
        if not(isinstance(other, Matrix)) or self.cols != other.rows:
            return None
        #Initialize new list for matrix
        result = [[0 for col in range(other.cols)] for row in range(self.rows)]
        for index in range(len(other.vectorSet)):
            #Perform MatrixVectorProduct with self and other vectors
            x = self.MatrixVectorProduct(other.vectorSet[index])
            #Insert entries in result
            for entry in range(len(x.vector)):
                result[entry][index] = x.vector[entry]
        #Return as a new matrix instance
        return Matrix(result)
    
    #Checks if a matrix is idempotent, that is,
    #if the matrix product with itself is equal to the original matrix
    def checkIdempotent(self):
        return self.isSquare and checkMatrix(self.matrixProduct(self), self)
    
    #Checks if a matrix is nilpotent, that is,
    #if there is some power k so that A ** k is equal ot the zero matrix
    def checkNilpotent(self):
        return self.isSquare and checkNilpotentHelper(self, self)
    
    #Scales all entires in a matrix by factor c
    def scaleMatrix(self, c):
        if type(c) in {int, float}:
            return Matrix([[c * self.matrix[row][col] for col in range(self.cols)] 
                                               for row in range(self.rows)])
        return None

    #Chekcs that a matrix is square then calculates the determinant
    #Uses diagonal product when diagonal matrix
    def findDeterminant(self):
        if self.isTriangular:
            total = 1
            for row in range(self.rows):
                total *= self.matrix[row][row]
            return total
        if self.isSquare == False:
            return None
        return findDeterminantHelper(self.matrix)
    
    #Finds free columns based on what's not a pivot columns
    def getFree(self):
        result = []
        for item in range(self.cols):
            if item not in (self.pivotLocations):
                result.append(item)
        return result

    #Returns the Null Space of a matrix
    def getNullSpace(self):
        #Return zero vector if nullity is 0
        if self.nullity == 0:
            return [Vector([0 for length in range(self.rows)])]
        #Create n many vectors where n is the nullity of the matrix
        else:
            result = [[0 for num in range(self.cols)] for item in range(self.nullity)]
            #If we have a free variable, place 1 in separate vector
            for number in range(len(self.freeLocations)):
                result[number][self.freeLocations[number]] = 1
            #If we have a pivot variable, place correct weight corresponding to
            #each free column
            for row in range(len(self.pivotLocations)):
                for col in range(len(self.freeLocations)):
                    r = self.pivotLocations[row]
                    c = self.freeLocations[col]
                    result[col][r] = -self.rref.matrix[row][c]
        #Converts items into vectors and return as a list
        for item in range(len(result)):
            result[item] = Vector(result[item])
        return result
    
    #Gets the inverse of a matrix given it is invertible
    def getInverse(self):
        if self.isSquare != True or self.determinant in {0,None}:
            return None
        return getInverseHelper(self)

    #Returns the orthogonal basis of the matrix, where the dot product of each
    #vector in the basis is 0 (they are orthogonal or perpendicular)
    def getOrthogonalBasis(self):
        return getOrthogonalBasisHelper(self.basis, list())
    
    #Takes Orthogonal basis and norms each vector, or divides them by their 
    #length to make a basis of orthogonal unit vectors
    def getOrthonormalBasis(self):
        result = []
        for item in range(len(self.orthogonalBasis)):
            vector = self.orthogonalBasis[item]
            newVector = vector.scaleVector(1/vector.norm)
            result.append(newVector)
        return result
    
    #Checks if a matrix is orthogonal, which is that its transpose must equal
    #its inverse
    def checkOrthogonal(self):
        if self.isSquare == False or self.determinant in  {0, None}:
            return False
        return checkMatrix(self.transpose, self.inverse)
    
    #checks if a matrix is symmetrix, which is that its transpose is equal
    #to itself
    def checkSymmetric(self):
        if not(self.isSquare):
            return False
        return checkMatrix(self, self.transpose)
    
    #checks if a matrix is skew-symmetric, which is that its tranpose it equal
    #to the negative of itself
    def checkSkewSymmetric(self):
        if not(self.isSquare):
            return False
        return checkMatrix(self.transpose, self.scaleMatrix(-1))
    
    #Experimental feature
    #Approximates the eigenvalues of a square matrix that is full rank
    #using the QR algorithm. Idea taken from Wikipedia
    #https://en.wikipedia.org/wiki/QR_algorithm
    def getEigenValues(self):
        if False in {self.is1to1, self.isSquare}:
            return None
        A = convertVectorToMatrix(self.basis)
        Q = convertVectorToMatrix(self.orthonormalBasis)
        Q.transpose = Q.getTranspose()
        R = Q.transpose.matrixProduct(A)
        newA = R.matrixProduct(Q)
        for iteration in range(500):
            A = newA
            A.rref = A.getRREF()
            A.pivotLocations = A.findPivots()
            A.basis = A.getBasis()
            A.orthogonalBasis = A.getOrthogonalBasis()
            A.orthonormalBasis = A.getOrthonormalBasis()
            Q = convertVectorToMatrix(A.orthonormalBasis)
            Q.transpose = Q.getTranspose()
            R = Q.transpose.matrixProduct(A)
            newA = R.matrixProduct(Q)
        return newA

################################################################################
# Matrix Helper Function

#checks if two matrices are equal by making sure each entry is almost equal
#to avoid buggy floating point errors
def checkMatrix(m1,m2):
    if m1.getDims() != m2.getDims():
        return False
    for row in range(m1.rows):
        for col in range(m1.cols):
            if not(almostEqual(m1.matrix[row][col],m2.matrix[row][col])):
                return False
    return True

#Takes a list of vectors and converts them into a matrix instance
def convertVectorToMatrix(L):
    cols = len(L)
    rows = L[0].dims
    result = [[0 for col in range(cols)] for row in range(rows)]
    for col in range(cols):
        vector = L[col]
        for row in range(rows):
            entry = vector.vector[row]
            result[row][col] = entry
    return Matrix(result)
    
#Recursively creates basis using Gram-Schidmt process. Idea from Lin Alg Textbook
#https://scholarworks.gvsu.edu/cgi/viewcontent.cgi?article=1021&context=books
def getOrthogonalBasisHelper(vectors, L, depth = 0):
    if len(L) == len(vectors):
        return L
    else:
        final = vectors[depth]
        v = vectors[depth]
        for index in range(depth):
            w = L[index]
            subtractVector = w.scaleVector(-(w.dotProduct(v))/(w.dotProduct(w)))
            final = final.addVectors(subtractVector)
        L.append(final)
        return getOrthogonalBasisHelper(vectors,L,depth+1)

#Appends the identity matrix to the original matrix, then puts it into RREF
#Extracts and converts new matrix
def getInverseHelper(matrix):
    L = copy.deepcopy(matrix.matrix)
    ite = range(len(L))
    for rows in ite:
        newList = [0 for row in ite]
        newList[rows] = 1
        L[rows].extend(newList)
    newL = makeRREF(L)
    finalL = [newL[row][len(L):] for row in ite]
    return Matrix(finalL)

#Cofactor expansion formula and lower dimension determinant forumla
#Uses recursion to cut down higher dimension determinants
#Formulaes from: https://en.wikipedia.org/wiki/Determinant
def findDeterminantHelper(L):
    if L == []:
        return 0
    elif len(L) == 1:
        return L[0][0]
    elif len(L) == 2:
        return (L[0][0] * L[1][1]) - (L[0][1] * L[1][0])
    else:
        total = 0
        for col in range(len(L[0])):
            total += L[0][col] * ((-1) ** (col % 2)) * findDeterminantHelper(removeRowCol(L,0,col))
        return total
    
#Performs n many matrix products to see if the matrix ever becomes the zero matrix
#where n is the number of rows/cols in the square matrix
#Idea from Wikipedia: https://en.wikipedia.org/wiki/Nilpotent_matrix
def checkNilpotentHelper(matrix, original):
    zeroMatrix = Matrix([[0 for col in range(original.cols)] for row in range(original.rows)])
    if checkMatrix(original, zeroMatrix):
        return True
    for i in range(original.rows-1):
        matrix = matrix.matrixProduct(original)
        if checkMatrix(matrix, zeroMatrix):
            return True
    return False
        

#Find pivots by looking through cols fowards and rows backwards
def findPivotsHelper(L):
    result = []
    for row in range(len(L)-1, -1, -1):
        for col in range(len(L[0])):
            if almostEqual(L[row][col],1):
                result = [col] + result
                break
    return result

#Removes specified row and column nonmutatingingly, or stays same with None input
#Modified from CMU CSAcademy: https://cs3-112-f22.academy.cs.cmu.edu/exercise/4729
def removeRowCol(L, row, col):
    N = copy.deepcopy(L)
    if row != None:
        N.pop(row)
    if col != None:
        for rowIndex in range(len(N)):
            N[rowIndex].pop(col)
    return N

