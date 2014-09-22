'''
  @Description: 
      Given an input matrix, duplicates and rotates image 180 degrees.
      Thereby enabling the encoding of an image twice for a more robust,
      AprilTag.

  @Author: Austin Walters
  @Creation Date: 9/21/2014
  @Last Modified: 9/21/2014
  @Written in Python 2.7
'''

import numpy as np

# (1, 1), (1, 0), (0, 1), (0, 0)
colors = [0, 1, 2, 3]

'''
Flips and encodes!
Could use http://stackoverflow.com/questions/16265673/rotate-image-by-90-180-or-270-degrees
for OpenCV implementation
'''
def encode(matrix):

    encodedMatrix = []
    
    # NEED TO ADD VALIDATION
    height = len(matrix) 
    width = len(matrix[0])

    for i in range(height):
        newRow = []
        for j in range(width):
            tup = (matrix[i][j], matrix[height - i - 1][width - j - 1])
            newRow.append(tup)
        encodedMatrix.append(newRow)
    return encodedMatrix

'''
Decodes encoded matrix from image
'''
def image2Matrix(imageMatrix):
    
    matrix = []

    # NEED TO ADD VALIDATION                                                    
    height = len(imageMatrix)
    width = len(imageMatrix[0])

    for i in range(height):
        row = []
        for j in range(width):
            if imageMatrix[i][j] is colors[0]:
                row.append((1, 1))
            elif imageMatrix[i][j] is colors[1]:
                row.append((1, 0))
            elif imageMatrix[i][j] is colors[2]:
                row.append((0, 1))
            elif imageMatrix[i][j] is colors[3]:
                row.append((0, 0))
        matrix.append(row)
    return matrix



'''
Converts the tuples into pixel matrix
'''
def generateImage(matrix):
    
    imageMatrix = []
    i = 0

    for row in matrix:
        imageMatrix.append([])
        for entry in row:
            if entry[0] is 1:
                if entry[1] is 1: 
                    imageMatrix[i].append(colors[0])
                else:
                    imageMatrix[i].append(colors[1])
            else:
                if entry[1] is 1:
                    imageMatrix[i].append(colors[2])
                else:
                    imageMatrix[i].append(colors[3])
        i += 1

    return imageMatrix


def printMatrix(matrix):

    for i in range(len(matrix)):
        print '\t[',
        for j in range(len(matrix[i])):
            print matrix[i][j], 
        print ']'

'''
  Simple test, checks to see if input == output
'''
def runTest(name, test):

    print '\n-- Beginning Test %s! --\n' % (name)
    print 'input matrix:'
    printMatrix(test)
    print 'tuple matrix:'
    printMatrix(encode(test))
    print 'coded matrix:'
    printMatrix(generateImage(encode(test)))
    print 'tuple matrix:'
    printMatrix(image2Matrix(generateImage(encode(test))))
    if encode(test) == image2Matrix(generateImage(encode(test))):
        print '\nOutput == Input!'
        print 'Successfully, Completed Test %s!\n\n' % (name)
    else:
        print '\nOutput != Input!'
        print 'Failed Test %s!\n\n' % (name)


print '\n\n---- TESTING CODE -----\n\n'
test = [[1, 0],[0, 1]]
runTest('#1', test) 

test2 = [[0, 1, 1], [1, 1, 1], [0, 1, 0]]
runTest('#2', test2)

test3 = [[0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 0, 1],\
         [1, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0],\
         [0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 1, 0]]
runTest('#3', test3)
