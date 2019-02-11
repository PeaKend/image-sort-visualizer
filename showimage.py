#!/usr/bin/env python

import sys, pygame

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
img = pygame.image.load('monalisa.jpg')

while True:
    screen.blit(img, (0, 0))
    pygame.display.update()
