from primitives import *
import pygame
import math
from OpenGL.GL import *
from OpenGL.GLU import *

# Gradient
def enableTransparency():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def drawCircle(x, y, radius, segments, color=(1, 1, 0, 1)):
    glColor(color)
    glBegin(GL_POLYGON)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        dx = x + radius * math.cos(angle)
        dy = y + radius * math.sin(angle)
        glVertex2f(dx, dy)
    glEnd()

def filledPolygon2D(vertices, color=drawingColor):
    glColor(color)
    glBegin(GL_POLYGON)  
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

pygame.init()
init_viewport()

enableTransparency()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Sky 
    glClearColor(0.502, 0.565, 0.722, 1.0)

    # Grass 
    line2D(0, 0, 768, 0, color=(0.557, 0.635, 0.447, 1.0), lineWidth=300)
    
    # Mountains
    for i in range(4):
        x_offset = i * 4  
        filledTriangle2D([[-1 + x_offset, 2.8], [2 + x_offset, 10], [5 + x_offset, 2.8]], color=(0.427, 0.388, 0.612, 1.0))
        filledTriangle2D([[1 + x_offset, 2.8], [4 + x_offset, 7], [7 + x_offset, 2.8]], color=(0.384, 0.349, 0.551, 1.0))
    
    # Sun
    drawCircle(10, 12, 1, 50, color=(0.95, 0.75, 0.2, 0.6))  # Outer 
    drawCircle(10, 12, 0.7, 50, color=(0.9, 0.7, 0.15, 0.8))  # Middle
    drawCircle(10, 12, 0.4, 50, color=(0.85, 0.65, 0.1, 1.0))  # Inner 
    
    ray_length = 1.2
    num_rays = 8
    angle_step = 360 / num_rays
    for i in range(num_rays):
        angle = math.radians(i * angle_step)
        x_start = 10 + math.cos(angle) * 1
        y_start = 12 + math.sin(angle) * 1
        x_end = 10 + math.cos(angle) * ray_length
        y_end = 12 + math.sin(angle) * ray_length

        line2D(x_start, y_start, x_end, y_end, color=(0.95, 0.75, 0.2, 0.8), lineWidth=3)  

    # Clouds
    drawCircle(7, 10.5, 0.7, 50, color=(0.8745, 0.8039, 0.8588, 1.0))  
    drawCircle(9, 10.5, 0.7, 50, color=(0.8745, 0.8039, 0.8588, 1.0)) 
    drawCircle(8, 10.5, 1, 50, color=(0.8745, 0.8039, 0.8588, 1.0))  

    # House
    line2D(3, 4, 7, 4, color=(0.404, 0.337, 0.408, 1.0), lineWidth=200)
    filledPolygon2D([[2.5, 5.8], [7.5, 5.8], [6, 7.2], [4, 7.2]], color=(0.682, 0.506, 0.553, 1.0))
    
    # Windows
    for i in range(4, 7, 2):  
        for j in range(3, 6, int(1.8)):  
            point2D(i, j, (0.851, 0.690, 0.765, 1.0), pointSize=20)
    
    # Door
    line2D(4,2.05,4,3.4, (0.314, 0.226, 0.272, 1.0), lineWidth=50)
    
    # Trees
    line2D(2, 2.8, 2, 4, color=(0.314, 0.226, 0.272, 1.0), lineWidth=9)  
    filledTriangle2D([[1.5, 3.2], [2.5, 3.2], [2, 6]], color=(0.561, 0.584, 0.400, 1.0))  

    for i in range(3):
        x_offset = i * 2  
        line2D(8.5 + x_offset, 2.3, 8.5 + x_offset, 4, color=(0.314, 0.226, 0.272, 1.0), lineWidth=9)
        filledTriangle2D([[7.7 + x_offset, 3], [9.3 + x_offset, 3], [8.5 + x_offset, 4.5]], color=(0.561, 0.584, 0.400, 1.0))
        filledTriangle2D([[7.8 + x_offset, 3.7], [9.2 + x_offset, 3.7], [8.5 + x_offset, 5.2]], color=(0.561, 0.584, 0.400, 1.0))
        filledTriangle2D([[7.9 + x_offset, 4.4], [9.1 + x_offset, 4.4], [8.5 + x_offset, 5.9]], color=(0.561, 0.584, 0.400, 1.0))
    for i in range(2):
        x_offset = i * 2  
        line2D(9.5 + x_offset, 1.5, 9.5 + x_offset, 4, color=(0.314, 0.226, 0.272, 1.0), lineWidth=9)
        filledTriangle2D([[8.7 + x_offset, 2], [10.3 + x_offset, 2], [9.5 + x_offset, 3.5]], color=(0.345, 0.415, 0.305, 1.0))
        filledTriangle2D([[8.8 + x_offset, 2.7], [10.2 + x_offset, 2.7], [9.5 + x_offset, 4.2]], color=(0.345, 0.415, 0.305, 1.0))
        filledTriangle2D([[8.9 + x_offset, 3.4], [10.1 + x_offset, 3.4], [9.5 + x_offset, 4.9]], color=(0.345, 0.415, 0.305, 1.0))

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
