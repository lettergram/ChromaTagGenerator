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
# from PIL import Image


# TODO: CHECK COLORS
# AprilTag - (a, b) - colors

# (1, 1) - (a+, b+) - Orange (100, 255, 160)
# (1, 0) - (a+, b-) - purple (255,   0, 255)
# (0, 1) - (a-, b+) - lime   (  0, 255,   0)
# (0, 0) - (a-, b-) - teal   (  0, 255, 255)

o = (100, 255, 160)
p = (255, 0, 255)
l = (0, 255, 0)
t = (0, 255, 255)
colors = [o, p, l, t]

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
def generateImage(name, matrix):

    img = Image.new("RGB", (len(matrix), len(matrix)), (255, 255, 255))
    scale = 10
    for i in len(matrix):
        for j in len(matrix):
            for k in len(size):
                # TODO, check works
                img.putpixel((i*scale + k, j*scale + k), colors[matrix[i][j]])
    img.save(name, "PNG")
'''

'''
Converts the tuples into pixel matrix
'''
def generateImageMatrix(matrix):
    
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
    printMatrix(generateImageMatrix(encode(test)))
    print 'tuple matrix:'
    printMatrix(image2Matrix(generateImageMatrix(encode(test))))
    if encode(test) == image2Matrix(generateImageMatrix(encode(test))):
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
