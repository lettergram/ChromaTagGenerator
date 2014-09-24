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

import sys
from PIL import Image


# TODO: ENSURE COLORS ARE OPTIMAL
# AprilTag - (a, b) - colors

# (1, 1) - (a+, b+) - Orange (255, 180,   0)
# (1, 0) - (a+, b-) - purple (255,   0, 255)
# (0, 1) - (a-, b+) - lime   (120, 255,   0)
# (0, 0) - (a-, b-) - teal   (  0, 255, 255)

orange = (255, 180,   0)
purple = (255,   0, 255)
lime   = (120, 255,   0)
teal   = (  0, 255, 255)

black = (0, 0, 0)
white = (255, 255, 255)

colors = [orange, purple, lime, teal]

'''
Flips and encodes!
Could use http://stackoverflow.com/questions/16265673/rotate-image-by-90-180-or-270-degrees
for OpenCV implementation
'''
def encode(matrix):
    encodedMatrix = []
    try:
        height = len(matrix) 
        width = len(matrix[0])
    except:
        return [[]]
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
    try:
        height = len(imageMatrix)
        width = len(imageMatrix[0])
    except:
        return [[]]
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
pCreates an image from a matrix
'''
def generateImage(name, matrix):
    scale = 100
    size = len(matrix) * scale
    img = Image.new("RGB", (size, size), (255, 255, 255))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(scale):
                for t in range(scale):
                    img.putpixel((i*scale + t, j*scale + k), matrix[i][j])
    img.save(name, "PNG")


'''
Creates a black and white image
'''
def generateBWMatrix(matrix):
    imageMatrix = []
    i = 0
    for row in matrix:
        imageMatrix.append([])
        for entry in row:
            if entry is 1:
                imageMatrix[i].append(black)
            else:
                imageMatrix[i].append(white)
        i += 1
    return imageMatrix

'''
Converts the tuples into pixel matrix
'''
def generateColorMatrix(matrix):    
    imageMatrix = []
    aMatrix = []
    bMatrix = []
    i = 0
    for row in matrix:
        imageMatrix.append([])
        aMatrix.append([])
        bMatrix.append([])
        for entry in row:
            if entry[0] is 1:
                aMatrix[i].append(black)
                if entry[1] is 1: 
                    bMatrix[i].append(black)
                    imageMatrix[i].append(colors[0])
                else:
                    bMatrix[i].append(white)
                    imageMatrix[i].append(colors[1])
            else:
                aMatrix[i].append(white)
                if entry[1] is 1:
                    bMatrix[i].append(black)
                    imageMatrix[i].append(colors[2])
                else:
                    bMatrix[i].append(white)
                    imageMatrix[i].append(colors[3])
        i += 1
    generateImage("a-channel", aMatrix)
    generateImage("b-channel", bMatrix)
    return imageMatrix


'''
Prints a matrix in a decent format
'''
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
    print 'Genearting Input Image...'
    generateImage(name + '-input', generateBWMatrix(test))
    print 'tuple matrix:'
    printMatrix(encode(test))
    print 'coded matrix:'
    printMatrix(generateColorMatrix(encode(test)))
    print 'tuple matrix:'
    printMatrix(image2Matrix(generateColorMatrix(encode(test))))
    print 'Generating Output Image...'
    generateImage(name + '-output', generateColorMatrix(encode(test)))

    if encode(test) == image2Matrix(generateColorMatrix(encode(test))):
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

test4 = []
print 'Enter 6 rows, each row MUST contain 6 entries of 1s and 0s ONLY!'
print 'EXAMPLE: 1 0 1 0 1 0'
'''
for i in range(6):
    row = input('Row #%s: ' % (i))
    row = row.split()
    test4.append(row)
runTest('#4', test4)
'''
