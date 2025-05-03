from primitives2 import *
from math import cos, sin, radians
import pygame

angle = 45  
velocity = 100  
g = 30 # if you want to change projectile motion's height, change that. Less = height increases
projectiles = []

barrel_base_x = -200
barrel_base_y = 0

def draw_barrel(x, y, angle, length=50):
    rad = radians(angle)
    end_x = x + length * cos(rad)
    end_y = y + length * sin(rad)
    line2D(x, y, end_x, end_y, (0, 0, 1, 0), 10)
    return end_x, end_y

def update_projectiles():
    for p in projectiles:
        t = pygame.time.get_ticks() / 1000 - p['start_time'] # milisecond to second
        x = p['x0'] + p['v'] * cos(radians(p['angle'])) * t
        y = p['y0'] + p['v'] * sin(radians(p['angle'])) * t - 0.5 * g * t**2 # projectile motion formula height
        if y >= 0:
            p['path'].append((x, y))
            for point in p['path']:
                point2D(point[0], point[1], (0, 0, 1, 1), 2)

pygame.init()
init_viewport()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle = max(0, angle - 1)
            elif event.key == pygame.K_RIGHT:
                angle = min(90, angle + 1)
            elif event.key == pygame.K_UP:
                velocity = min(1000, velocity + 10)
            elif event.key == pygame.K_DOWN:
                velocity = max(0, velocity - 10)
            elif event.key == pygame.K_SPACE:
                barrel_end = draw_barrel(barrel_base_x, barrel_base_y, angle)
                projectiles.append({
                    'x0': barrel_end[0],
                    'y0': barrel_end[1],
                    'v': velocity,
                    'angle': angle,
                    'start_time': pygame.time.get_ticks() / 1000, # milisecond to second
                    'path': []
                })

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    drawCoordinates(200, 200)
    draw_barrel(barrel_base_x, barrel_base_y, angle)
    update_projectiles()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
