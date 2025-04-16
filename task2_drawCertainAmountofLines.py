from primitives import *
import pygame
from OpenGL.GL import *
import math

def draw_circle(num_lines, radius=2, center_x=7, center_y=7):
    if num_lines < 3:
        print("Number of lines must be at least 3.")
        return
    
    angle_step = 2 * math.pi / num_lines
    glBegin(GL_LINES)
    for i in range(num_lines):
        angle1 = i * angle_step
        angle2 = (i + 1) * angle_step
        
        x1, y1 = center_x + radius * math.cos(angle1), center_y + radius * math.sin(angle1)
        x2, y2 = center_x + radius * math.cos(angle2), center_y + radius * math.sin(angle2)
        
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
    glEnd()

pygame.init()
init_viewport()

num_lines = int(input("Enter the number of lines (at least 3): "))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Setting the ModelView State
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_circle(num_lines)

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
