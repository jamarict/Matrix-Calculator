from matrixClass import *
from cmu_graphics import *
from buttonClass import *

#Implementation of Matrix and Vector Class with graphical interface that relies
#on key and mouse presses. Inspiration for buttonCLass, screens usage, and text
#inputs taken from 15-112 TP Demo Lectures

def onAppStart(app):
    app.isPaused = True
    app.colorList = [[230,1],[240,1],[255,1]]
    app.background = rgb(*(app.colorList[item][0] for item in range(len(app.colorList))))
    makeButtons(app)

################################################################################

def start_redrawAll(app):
    drawRect(app.width/16, app.height/16, app.width*14/16, app.height*14/16, fill="snow")
    drawLabel("Matrix Calculator", app.width/2, app.height/6, size = app.width/13, font = "monospace")
    app.instructionButton.draw()
    app.matrixInputButton.draw()
    app.vectorInputButton.draw()

def start_onStep(app):
    colorChanger(app)

def start_onKeyPress(app, key):
    colorStop(app, key)
    
def start_onMousePress(app, mouseX, mouseY):
    app.instructionButton.checkForPress(app, mouseX, mouseY)
    app.matrixInputButton.checkForPress(app, mouseX, mouseY)
    app.vectorInputButton.checkForPress(app, mouseX, mouseY)

################################################################################

def instructions_redrawAll(app):
    drawRect(app.width/16, app.height/16, app.width*14/16, app.height*14/16, fill="snow")
    drawLabel("Instructions", app.width/2, app.height/6,size = app.width/13, font = "monospace")
    drawText(app)
    drawLabel("Also, to pause/unpause the background color, press s", 410, 615, size = app.width/48, font= "monospace")
    app.backButton.draw()
    

def drawText(app):
    text = text = """\
This calculator allows the user to create and analyze
matrices and vectors. 

When analyzing matrices, specify the matrix dimensions 
then input the corresponding matrix entries using key 
presses. Matrices also supports matrix addition and 
multiplication. To create new matrices, specify the 
dimensions and entries of each matrix. The calculator 
will warn you if the dimensions are not compatible. If 
the matrices are legal, a new matrix will be outputed 
and analyzed.

When analyzing vectors, specify the vector dimensions 
then input the corresponding vector entries using key 
presses. Vectors supports addition and scalar 
multiplication. To create new vectors, specify 
dimensions and entries. If the vectors are legal, a new 
vector will be outputed or information on the two 
be will given about the two."""
    textList = text.splitlines()
    for index in range(len(textList)):
        line = textList[index]
        drawLabel(line, 60, 160 + (20 * index), size = app.width/40, font = "monospace", bold = True, align = "top-left")

        
def instructions_onKeyPress(app, key):
    colorStop(app, key)

def instructions_onMousePress(app,mouseX,mouseY):
    app.backButton.checkForPress(app, mouseX, mouseY)

def instructions_onStep(app):
    colorChanger(app)

################################################################################

def matrixInput_redrawAll(app):
    drawRect(app.width/16, app.height/16, app.width*14/16, app.height*14/16, fill="snow")
    drawLabel("Matrices", app.width/2, app.height/8,size = app.width/13, font = "monospace")
    app.backButton.draw()
    app.analyzeOneMatrixButton.draw()
    app.addMatricesButton.draw()
    app.multiplyMatricesButton.draw()
    app.scaleMatrixButton.draw()
    for item in app.inputs:
        if item.canDisplay:    
            drawLabel("Matrix 1", app.width/2, 300, size = 25, font = "monospace")
            item.draw()
            if item is app.inputTwoButton:
                drawLabel("Matrix 2", app.width/2, 425, size = 25, font = "monospace")
            elif item is app.inputThreeButton:
                drawLabel("Scalar", app.width/2, 425, size = 25, font = "monospace")
    if app.resultsButton1.canDisplay:
        app.resultsButton1.draw()
    if app.showInvalid:
        drawLabel("Invalid Input", 340, 615, size = 40, font = "monospace", fill = rgb(255, 90, 90))
    

def matrixInput_onStep(app):
    colorChanger(app)

def matrixInput_onMousePress(app, mouseX, mouseY):
    app.showInvalid = False
    for item in app.inputs:
        item.canEdit = False
        item.border = "black"
    app.backButton.checkForPress(app, mouseX, mouseY)
    app.analyzeOneMatrixButton.checkForPress(app, mouseX, mouseY)
    app.addMatricesButton.checkForPress(app, mouseX, mouseY)
    app.multiplyMatricesButton.checkForPress(app, mouseX, mouseY)
    app.scaleMatrixButton.checkForPress(app, mouseX, mouseY)
    for item in app.inputs:
        if item.canDisplay:
            item.checkForPress(app, mouseX, mouseY)
    num = 0
    for item in app.inputs:
        if item.canDisplay:
            num += 1
            if item.text == "":
                app.resultsButton1.canDisplay = False
                return
    if num != 0:
        app.resultsButton1.canDisplay = True
    if app.resultsButton1.canDisplay:
        app.resultsButton1.checkForPress(app, mouseX, mouseY)

def matrixInput_onKeyPress(app, key):
    colorStop(app, key)
    for item in app.inputs:
        if item.canEdit:
            if key in {",", "[", "]", "."} or key.isdigit():
                item.text += key
            elif key == "space":
                item.text += " "
            elif key == "backspace":
                item.text = item.text[:-1]
    num = 0
    for item in app.inputs:
        if item.canDisplay:
            num += 1
            if item.text == "":
                app.resultsButton1.canDisplay = False
                return
    if num != 0:
        app.resultsButton1.canDisplay = True

################################################################################

def vectorInput_redrawAll(app):
    drawRect(app.width/16, app.height/16, app.width*14/16, app.height*14/16, fill="snow")
    drawLabel("Vectors", app.width/2, app.height/8,size = app.width/13, font = "monospace")
    app.backButton.draw()
    app.analyzeOneVectorButton.draw()
    app.analyzeTwoVectorButton.draw()
    app.addVectorButton.draw()
    app.scaleVectorButton.draw()
    for item in app.inputs:
        if item.canDisplay:    
            drawLabel("Vector 1", app.width/2, 300, size = 25, font = "monospace")
            item.draw()
            if item is app.inputTwoButton:
                drawLabel("Vector 2", app.width/2, 425, size = 25, font = "monospace")
            elif item is app.inputThreeButton:
                drawLabel("Scalar", app.width/2, 425, size = 25, font = "monospace")
    if app.resultsButton.canDisplay:
        app.resultsButton.draw()
    if app.showInvalid:
        drawLabel("Invalid Input", 340, 615, size = 40, font = "monospace", fill = rgb(255, 90, 90))

def vectorInput_onStep(app):
    colorChanger(app)

def vectorInput_onMousePress(app, mouseX, mouseY):
    app.showInvalid = False
    for item in app.inputs:
        item.canEdit = False
        item.border = "black"
    app.backButton.checkForPress(app, mouseX, mouseY)
    app.analyzeOneVectorButton.checkForPress(app, mouseX, mouseY)
    app.analyzeTwoVectorButton.checkForPress(app, mouseX, mouseY)
    app.addVectorButton.checkForPress(app, mouseX, mouseY)
    app.scaleVectorButton.checkForPress(app, mouseX, mouseY)
    for item in app.inputs:
        if item.canDisplay:
            item.checkForPress(app, mouseX, mouseY)
    num = 0
    for item in app.inputs:
        if item.canDisplay:
            num += 1
            if item.text == "":
                app.resultsButton.canDisplay = False
                return
    if num != 0:
        app.resultsButton.canDisplay = True
    if app.resultsButton.canDisplay:
        app.resultsButton.checkForPress(app, mouseX, mouseY)
    

def vectorInput_onKeyPress(app, key):
    colorStop(app, key)
    for item in app.inputs:
        if item.canEdit:
            if key in {",", "[", "]", "."} or key.isdigit():
                item.text += key
            elif key == "space":
                item.text += " "
            elif key == "backspace":
                item.text = item.text[:-1]
    num = 0
    for item in app.inputs:
        if item.canDisplay:
            num += 1
            if item.text == "":
                app.resultsButton.canDisplay = False
                return
    if num != 0:
        app.resultsButton.canDisplay = True
        
################################################################################

def vectorResult_redrawAll(app):
    drawRect(app.width/16, app.height/16, app.width*14/16, app.height*14/16, fill="snow")
    drawLabel("Results", app.width/2, app.height/8,size = app.width/13, font = "monospace")
    app.backButton.draw()
    app.showInputButton.draw()
    app.showOutputButton.draw()
    if app.showInput:
        drawLabel(f"Vector 1: {app.input1.dims} x 1 Vector", app.width/2, 250, size = 25, font = "monospace", bold = True)
        drawLabel(app.input1, app.width/2, 325, size = 25 - int(app.input1.dims/2), font = "monospace", bold = True)
        if app.input2 == None:
            pass
        elif type(app.input2) == Vector:
            drawLabel(f"Vector 2: {app.input2.dims} x 1 Vector", app.width/2, 400, size = 25, font = "monospace", bold = True)
            drawLabel(app.input2, app.width/2, 475, size = 25 - int(app.input2.dims/2), font = "monospace", bold = True)
        else:
            drawLabel("Scalar", app.width/2, 400, size = 25, font = "monospace", bold = True)
            drawLabel(app.input2, app.width/2, 475, size = 25, font = "monospace", bold = True)
    else:
        if app.input2 == None:
            display1Vector(app, 0)
        elif type(app.input2) in {float, int}:
            display1Vector(app, 1)
        else:
            if app.addVectorButton.border == "silver":
                display1Vector(app, 2)
            else:
                display2Vector(app)


def display1Vector(app, param):
    if param == 0:
        drawLabel("Vector Analysis", app.width/2, 250, size = 25, font = "monospace", bold = True)
        drawLabel(app.input1, app.width/2, 300, size = 25 - int(app.input1.dims/2), font = "monosapce", bold = True)
        drawLabel(f"Dimension: {app.input1.dims} x 1 Vector", app.width/2, 390, size = 25, font = "monosapce", bold = True)
        drawLabel(f"Norm/Distance: {int((app.input1.norm*1000))/1000}", app.width/2, 475, size = 25, font = "monosapce", bold = True)
    elif param == 1:
        newVector = app.input1.scaleVector(app.input2)
        drawLabel("New Vector", app.width/2, 250, size = 25, font = "monospace", bold = True)
        drawLabel(newVector, app.width/2, 300, size = 25 - int(newVector.dims/2), font = "monosapce", bold = True)
        drawLabel(f"Dimension: {newVector.dims} x 1 Vector", app.width/2, 390, size = 25, font = "monosapce", bold = True)
        drawLabel(f"Norm/Distance: {int((newVector.norm*1000))/1000}", app.width/2, 475, size = 25, font = "monosapce", bold = True)
    elif param == 2:
        newVector = app.input1.addVectors(app.input2)
        drawLabel("New Vector", app.width/2, 250, size = 25, font = "monospace", bold = True)
        drawLabel(newVector, app.width/2, 300, size = 25 - int(newVector.dims/2), font = "monosapce", bold = True)
        drawLabel(f"Dimension: {newVector.dims} x 1 Vector", app.width/2, 390, size = 25, font = "monosapce", bold = True)
        drawLabel(f"Norm/Distance: {int((newVector.norm*1000))/1000}", app.width/2, 475, size = 25, font = "monosapce", bold = True)



def display2Vector(app):
    drawLabel("Vector Analysis", app.width/2, 250, size = 25, font = "monospace", bold = True)
    drawLabel(f"Dot Product: {int(app.input1.dotProduct(app.input2)*1000)/1000}", app.width/2, 325, size = 25, font = "monosapce", bold = True)
    drawLabel(f"Distance: {int(app.input1.vectorDistance(app.input2)*1000)/1000}", app.width/2, 375, size = 25, font = "monosapce", bold = True)
    angle = app.input1.vectorAngle(app.input2)
    if angle == None:
        drawLabel(f"Angle: No Angle (Zero Vector)", app.width/2, 425, size = 25, font = "monosapce", bold = True)
        drawLabel(f"Parallel Proj: No Projection", app.width/2, 475, size = 25, font = "monospace", bold = True)
        drawLabel(f"Perpendicular Proj: No Projection", app.width/2, 525, size = 25, font = "monospace", bold = True)
    else:
        ortho = app.input1.orthoProj(app.input2)
        for item in range(len(ortho.vector)):
            ortho.vector[item] = int(ortho.vector[item]*1000)/1000
        perp = app.input1.perpProj(app.input2)
        for item in range(len(perp.vector)):
            perp.vector[item] = int(perp.vector[item]*1000)/1000
        drawLabel(f"Angle: {int(angle*1000)/1000}", app.width/2, 425, size = 25, font = "monospace", bold = True)
        drawLabel(f"Parallel Proj: {ortho}", app.width/2, 475, size = 20 - int(ortho.dims), font = "monospace", bold = True)
        drawLabel(f"Perpendicular Proj: {perp}", app.width/2, 525, size = 20 - int(perp.dims), font = "monospace", bold = True)


def vectorResult_onStep(app):
    colorChanger(app)

def vectorResult_onKeyPress(app, key):
    colorStop(app, key)

def vectorResult_onMousePress(app, mouseX, mouseY):
    app.backButton.checkForPress(app, mouseX, mouseY)
    app.showInputButton.checkForPress(app, mouseX, mouseY)
    app.showOutputButton.checkForPress(app, mouseX, mouseY)


################################################################################

def matrixResult_redrawAll(app):
    drawRect(app.width/16, app.height/16, app.width*14/16, app.height*14/16, fill="snow")
    drawLabel("Results", app.width/2, app.height/8,size = app.width/13, font = "monospace")
    app.backButton.draw()
    app.showInputButton.draw()
    if app.showInput:
        drawLabel(f"Matrix 1: {app.input1.rows} x {app.input1.cols } Matrix", app.width/2, 225, size = 25, font = "monospace", bold = True)
        for item in range(len(app.input1.matrix)):
            drawLabel(app.input1.matrix[item], app.width/2, 250 + (item * (30 - app.input1.rows)),size = 25 - int(app.input1.cols/2), font = "monospace", bold = True)

def matrixResult_onStep(app):
    colorChanger(app)

def matrixResult_onKeyPress(app, key):
    colorStop(app, key)

def matrixResult_onMousePress(app, mouseX, mouseY):
    app.backButton.checkForPress(app, mouseX, mouseY)
    app.showInputButton.checkForPress(app, mouseX, mouseY)


################################################################################

def makeButtons(app):
    app.instructionButton = RectangleButton(app.width/2,225,300,70, 35, "Instructions",instructFun,"white")
    app.backButton = RectangleButton(110, 615, 100, 50, 25, "Back", startFun, "white")
    app.matrixInputButton = RectangleButton(app.width/2, 375, 350,100,60, "Matrices", matrixInputFun, "white")
    app.vectorInputButton = RectangleButton(app.width/2, 525, 350,100,60, "Vectors", vectorInputFun, "white")
    app.analyzeOneMatrixButton = RectangleButton(200, 155, 200, 50, 18, "Analyze 1 Matrix", analyze1MatrixFun, "white")
    app.addMatricesButton = RectangleButton(500,155,200,50,18, "Add Matrices", addMatricesFun, "white")
    app.multiplyMatricesButton = RectangleButton(200,215,200,50,18,"Multiply Matrices",multiplyMatricesFun, "white")
    app.scaleMatrixButton = RectangleButton(500,215,200,50,18, "Scale Matrix", scaleMatrixFun, "white")
    app.matrixButtons = [app.analyzeOneMatrixButton, app.addMatricesButton,app.multiplyMatricesButton, app.scaleMatrixButton]
    app.analyzeOneVectorButton = RectangleButton(200, 155, 200, 50, 18, "Analyze 1 Vector", analyze1VectorFun, "white")
    app.analyzeTwoVectorButton = RectangleButton(500, 155, 200, 50, 18, "Analyze 2 Vectors", analyze2VectorFun, "white" )
    app.addVectorButton = RectangleButton(200, 215, 200, 50, 18, "Add Vectors", addVectorFun, "white")
    app.scaleVectorButton = RectangleButton(500, 215, 200, 50, 18, "Scale Vector", scaleVectorFun, "white")
    app.vectorButtons = [app.analyzeOneVectorButton, app.analyzeTwoVectorButton, app.addVectorButton, app.scaleVectorButton]
    app.inputOneButton = RectangleButton(350, 350, 550, 50, 20, "", inputText1, "white")
    app.inputTwoButton = RectangleButton(350, 475, 550, 50, 20, "", inputText2, "white")
    app.inputThreeButton = RectangleButton(350, 475, 550, 50, 20, "", inputText3, "white")
    app.resultsButton1 = RectangleButton(580,615,125,50,25, "Results", getResults1, rgb(110,255,110))
    app.resultsButton = RectangleButton(580, 615, 125, 50, 25, "Results", getResults, rgb(110, 255, 110))
    app.inputs = [app.inputOneButton, app.inputTwoButton, app.inputThreeButton]
    app.showInvalid = False
    app.input1, app.input2 = None, None
    app.showInput = True
    app.showInputButton = RectangleButton(app.width/4, 155, 200, 50, 20, "Show Inputs", showInputs, "white")
    app.showOutputButton = RectangleButton(app.width*(3/4),155,200,50,20,"Show Outputs", showOutputs, "white")

def showInputs(app):
    app.showInput = True

def showOutputs(app):
    app.showInput = False

def colorChanger(app):
    if app.isPaused:
        return
    for item in range(len(app.colorList)):
        if app.colorList[item][0] == 255:
            app.colorList[item][1] = -1
        elif app.colorList[item][0] == 220:
            app.colorList[item][1] = 1
        app.colorList[item][0] = (app.colorList[item][0] + (1 * app.colorList[item][1]))
    app.background = rgb(*(app.colorList[item][0] for item in range(len(app.colorList))))

def colorStop(app, key):
    if key == "s":
        app.isPaused = not(app.isPaused)

def instructFun(app):
    setActiveScreen("instructions")

def startFun(app):
    app.input1, app.input2 = None, None
    app.resultsButton.canDisplay = False
    for item in app.matrixButtons:
        item.border = "black"
    for item in app.vectorButtons:
        item.border = "black"
    for item in app.inputs:
        item.border = "black"
        item.canDisplay = False
        item.text = ""
    app.showInput = True
    setActiveScreen("start")

def matrixInputFun(app):
    setActiveScreen("matrixInput")

def vectorInputFun(app):
    setActiveScreen("vectorInput")

def analyze1MatrixFun(app):
    outlineColor1(app,0)
    changeStatus(app, [0])

def addMatricesFun(app):
    outlineColor1(app, 1)
    changeStatus(app, [0,1])

def multiplyMatricesFun(app):
    outlineColor1(app, 2)
    changeStatus(app, [0,1])

def scaleMatrixFun(app):
    outlineColor1(app, 3)
    changeStatus(app, [0,2])


def outlineColor1(app, num):
    for item in app.matrixButtons:
        item.border = "black"
        app.matrixButtons[num].border = "silver"

def outlineColor(app, num):
    for item in app.vectorButtons:
        item.border = "black"
    app.vectorButtons[num].border = "silver"


def changeStatus(app, L):
    for index in range(len(app.inputs)):
        if index not in L:
            app.inputs[index].canDisplay = False
            app.inputs[index].text = ""
        else:
            app.inputs[index].canDisplay = True


def analyze1VectorFun(app):
    outlineColor(app, 0)
    changeStatus(app, [0])

def analyze2VectorFun(app):
    outlineColor(app, 1)
    changeStatus(app, [0,1])

def addVectorFun(app):
    outlineColor(app, 2)
    changeStatus(app, [0,1])

def scaleVectorFun(app):
    outlineColor(app, 3)
    changeStatus(app, [0,2])

def inputText1(app):
    app.inputOneButton.border = rgb(255, 200, 100)
    app.inputOneButton.canEdit = True

def inputText2(app):
    app.inputTwoButton.border = rgb(255, 200, 100)
    app.inputTwoButton.canEdit = True

def inputText3(app):
    app.inputThreeButton.border = rgb(255, 200, 100)
    app.inputThreeButton.canEdit = True

def getResults(app):
    if validateInputs(app):
        setActiveScreen("vectorResult")
    else:
        return "Invalid Input"
    
def getResults1(app):
    if validateInputs1(app):
        setActiveScreen("matrixResult")
    else:
        return "Invalid Input"

def validateInputs1(app):
    for index in range(len(app.inputs)):
        if app.inputs[index].canDisplay:
            if index in {0,1}:
                if not(verifyMatrix(app.inputs[index].text)):
                    app.inputs[index].border = rgb(255, 90, 90)
                    app.showInvalid = True
                    return False
                else:
                    result = convertMatrix(app.inputs[index].text)
                    if result == False:
                        print(1)
                        app.inputs[index].border = rgb(255, 90, 90)
                        app.showInvalid = True
                        return False
                    else:
                        if index == 0:
                            app.input1 = result
                        else: 
                            app.input2 = result
            elif index == 2:
                if not(verifyScalar(app.inputs[index].text)):
                    app.inputs[index].border = rgb(255, 90, 90)
                    app.showInvalid = True
                    return False
                else:
                    app.input2 = convertScalar(app.inputs[index].text)
    if app.addMatricesButton.border == "silver":
        if app.input1.getDims() != app.input2.getDims():
            app.inputs[0].border = rgb(255, 90, 90)
            app.inputs[1].border = rgb(255, 90, 90)
            app.showInvalid = True
            return False
    elif app.multiplyMatricesButton.border == "silver":
        if app.input1.cols != app.input2.rows:
            app.inputs[0].border = rgb(255, 90, 90)
            app.inputs[1].border = rgb(255, 90, 90)
            app.showInvalid = True
            return False
    return True



def validateInputs(app):
    for index in range(len(app.inputs)):
        if app.inputs[index].canDisplay:
            if index in {0,1}:
                if not(verifyVector(app.inputs[index].text)):
                    app.inputs[index].border = rgb(255, 90, 90)
                    app.showInvalid = True
                    return False
                else:
                    if index == 0:
                        app.input1 = convertVector(app.inputs[index].text)
                    else:
                        app.input2 = convertVector(app.inputs[index].text)
            elif index == 2:
                if not(verifyScalar(app.inputs[index].text)):
                    app.inputs[index].border = rgb(255, 90, 90)
                    app.showInvalid = True
                    return False
                else:
                    app.input2 = convertScalar(app.inputs[index].text)
    if type(app.input1) == type(app.input2):
        if app.input1.dims != app.input2.dims:
            app.inputs[0].border, app.inputs[1].border = rgb(255, 90, 90), rgb(255, 90, 90)
            app.showInvalid = True
            return False
    return True
    

def convertMatrix(s):
    M = []
    s = s.strip()
    s = s[1:-1].strip()
    first = True
    while len(s) != 0:
        if first:
            first = False
        else:
            s = s[1:].strip()
        rightBrackIndex = s.find("]")
        rowVector = getRowVector(s[0:rightBrackIndex+1])
        M.append(rowVector)
        s = s[rightBrackIndex+1:].strip()
    try:
        finalMatrix = Matrix(M)
        finalMatrix.getProperties()
        return finalMatrix
    except:
        return False

    

def getRowVector(s):
    L = []
    s = s.strip()
    s = s[1:-1]
    entries = s.split(",") 
    for item in entries:
        item = item.strip()
        number  = float(item)
        integer = int(number)
        if almostEqual(number,integer):
            L.append(integer)
        else:
            L.append(number)
    return L

def convertVector(s):
    L = []
    s = s.strip()
    s = s[1:-1]
    entries = s.split(",") 
    for item in entries:
        item = item.strip()
        number  = float(item)
        integer = int(number)
        if almostEqual(number,integer):
            L.append(integer)
        else:
            L.append(number)
    return Vector(L)

def convertScalar(s):
    s = s.strip()
    number = float(s)
    integer = int(number)
    if almostEqual(number, integer):
        return integer
    else:
        return number
    
def verifyMatrix(matrix):
    matrix = matrix.strip()
    if matrix[0] != "[" or matrix[-1] != "]":
        return False
    if matrix.count("[") != matrix.count("]"):
        return False
    matrix = matrix[1:-1].strip()
    first = True
    while len(matrix) != 0:
        if first:
            first = False
        else:
            if matrix[0] != ",":
                return False
            matrix = matrix[1:].strip()
        if matrix[0] != "[":
            return False
        rightBrackIndex = matrix.find("]")
        vector = matrix[0:rightBrackIndex+1]
        if not(verifyVector(vector)):
            return False
        matrix = matrix[rightBrackIndex+1:].strip()
    return True
        
def verifyVector(vector):
    vector = vector.strip()
    if vector[0] != "[" or vector[-1] != "]":
        return False
    entries = vector[1:-1].split(",")
    for item in entries:
        item = item.strip()
        try:
            float(item)
        except:
            return False
    return True

def verifyScalar(scalar):
    scalar = scalar.strip()
    try:
        float(scalar)
    except:
        return False
    return True

def main():
    runAppWithScreens(width = 700, height = 700, initialScreen="start")

main()