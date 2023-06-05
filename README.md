# Matrix-Calculator
This matrix calculator functions entirely in Python and makes use of the list data type to create matrices and vectors.
The calculator uses object-oriented programming to specify all of the matrix and vector properties that are commonly associated with each (transposes, inverses, onto, 1-1, norm, projections, etc...)

There is currently an unfinished portion that implements all of the code into a graphical interface using CMU Graphics. This interface will only rely on keys, mouses presses, and background matrices knowledge to use.

## Instructions to use the calculator (non-graphical)
To use the calculator built directly into the code, create a 2d list to represent a matrix. With this, specify a new variable, and set it equal to Matrix(x), where x is the 2d list you specified. Finally, call the .getProperties() method on the matrix you created and that will define all of the characteristics of that matrix. Make sure your 2d list is rectangular (each row has the same number of cols) so the calculator does not throw an error. To actually see what a specific property is: create a new variable and use the method corresponding to that property, or just print it in the terminal.

For the vectors it is the same thing, but instead of using a 2d list, replace it with a 1d list. Then you can directly call the methods to get specific properties. Some methods may require an input of another matrix or vector, so be careful of this as well. FInally, make sure you run any additional code you have in the MatrixClass.py file, as it calls from subsequent files.


