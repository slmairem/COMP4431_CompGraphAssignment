import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


width, height = 1024, 768
backgroundColor, drawingColor, pointSize, drawingWidth \
    = (0,0,0,1), (1,1,0,0), 1, 1

def point2D(x,y,color=drawingColor,pointSize=pointSize):
    glPointSize(pointSize)
    glColor(color)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def line2D(x0,y0,x1,y1,color=drawingColor,lineWidth=drawingWidth):
    glLineWidth(lineWidth)
    glColor(color)
    glBegin(GL_LINES)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()

def polygon2D(vertices,color=drawingColor,lineWidth=drawingWidth):
    glLineWidth(lineWidth)
    glColor(color)
    glBegin(GL_LINE_LOOP)
    for i in range(len(vertices)):
        glVertex2f(vertices[i][0],vertices[i][1])
    glEnd()

def filledTriangle2D(vertices,color=drawingColor):
    glColor(color)
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(vertex[0],vertex[1])
    glEnd()

def filledColorfulTriangle2D(vertices):
    color = [[1,0,0,1],[0,1,0,1],[0,0,1,1]]
    glBegin(GL_TRIANGLES)
    for i in range(len(vertices)):
        glColor(color[i])
        glVertex2f(vertices[i][0],vertices[i][1])
    glEnd()

def triangleFan2D(vertices,color=drawingColor):
    glColor(color)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(len(vertices)):
        glVertex2f(vertices[i][0],vertices[i][1])
    glEnd()

def init_viewport():
    global width, height, drawing_color

    # Setting and Displaying the Screen
    screen = pygame.display.set_mode((width, height),
                                     DOUBLEBUF | OPENGL | RESIZABLE)
    pygame.display.set_caption("OpenGL in Python")

    glClearColor(backgroundColor[0], backgroundColor[1],
                 backgroundColor[2], backgroundColor[3])

    # Setting the Projection and Clipping
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 15, 0, 15)