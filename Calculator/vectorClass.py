from calculator import *

#Main Vector Class
class Vector(object):
    
    #Major properties for a singular vector
    def __init__(self,L):
        self.vector = L
        self.dims = len(L)
        self.norm = self.getNorm()

    #gets the Norm or distance of vector
    def getNorm(self):
        return math.sqrt(self.dotProduct(self))
    
    #Prints vector
    def __repr__(self):
        return f"{self.vector}"
    
    #Checks two vector instances have same list
    def __eq__(self, other):
        return isinstance(other,Vector) and checkVector(self, other)
    
    #Adds corresponding entries of two vector instances
    def addVectors(self,other):
        if not(isinstance(other, Vector)) or self.dims != other.dims:
            return None
        return Vector([self.vector[i] + other.vector[i] for i in 
                                                        range(self.dims)])
    
    #Scales values in the vector by scalar c
    def scaleVector(self,c):  
        if type(c) in {int, float}: 
            return Vector([c * self.vector[i] for i in range(self.dims)])
        return None

    #Calculates the angle between two vectors using the laws of cosines
    #Returns angle in degrees, idea from Lin Alg textbook, from:
    #https://scholarworks.gvsu.edu/cgi/viewcontent.cgi?article=1021&context=books 
    def vectorAngle(self,vec):
        if not(isinstance(vec, Vector)):
            return None
        if 0 in {self.norm, vec.norm}:
            return None
        return math.degrees(math.acos((self.dotProduct(vec)/(self.norm * vec.norm))))
        
    #Takes two vector instances and performs the dotProduct
    def dotProduct(self, v2):
        if not(isinstance(v2, Vector)) or self.dims != v2.dims:
            return None
        return sum([self.vector[i] * v2.vector[i] for i in range(self.dims)])
    
    #Calculates the distance between two vectors using vector norm forumla
    #Idea from Lin Alg textbook, from:
    #https://scholarworks.gvsu.edu/cgi/viewcontent.cgi?article=1021&context=books
    def vectorDistance(self, v2):
        if not(isinstance(v2, Vector)) or self.dims != v2.dims:
            return None
        newVector = self.addVectors(v2.scaleVector(-1))
        return newVector.norm
    
    #Calculates projection of self onto v2 Idea from Lin Alg textbook, from:
    #https://scholarworks.gvsu.edu/cgi/viewcontent.cgi?article=1021&context=books
    def orthoProj(self, v2):
        if not(isinstance(v2,Vector)) or self.dims != v2.dims:
            return None
        if almostEqual(v2.norm, 0):
            return None
        scalar = self.dotProduct(v2)/(v2.norm ** 2)
        return v2.scaleVector(scalar)
    #Calculates perpendicular component of self onto v2. Idea from Lin Alg textbook, from:
    #https://scholarworks.gvsu.edu/cgi/viewcontent.cgi?article=1021&context=books 
    def perpProj(self,v2):
        if not(isinstance(v2,Vector)) or self.dims != v2.dims:
            return None
        ortho = self.orthoProj(v2)
        return self.addVectors(ortho.scaleVector(-1))

################################################################################
# Vector Helper Function

#Checks that two vectors are equal by comparing each entry and seeing if they 
#are close to equal
def checkVector(v1, v2):
    if v1.dims != v2.dims:
        return False
    for row in range(v1.dims):
        if not(almostEqual(v1.vector[row], v2.vector[row])):
            return False
    return True


