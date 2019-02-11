#!/usr/bin/env python

import sys, pygame
from random import shuffle

def init():
    pygame.init()

    size = width, height = 800, 800

    screen = pygame.display.set_mode(size)
    imgs = []

    for i in range(8):
        for j in range(8):
            imgs.append(pygame.image.load('imgs/[' + str(i) + ', ' + str(j) + '].jpg'))

    x = [i for i in range (0, 800, 100)]
    print(x)
    shuffle(x)
    print(x)
    print(len(imgs))
    print(len(x))
    img_size = 100
    img_pos_x = 0
    img_pos_y = 0
    i = 0
    j = 0
    z = 0
    img_unsorted_positions = []

    min_range = 0
    max_range = 8

# unsort image
    while True:
        index = 0

        for n in range(min_range, max_range):
            screen.blit(imgs[n], (x[index], img_pos_y))
            img_pos_x += img_size
            img_unsorted_positions.append(x[index])
            index += 1

        index = 0
        shuffle(x)
        min_range += 8
        max_range += 8
        if img_pos_x >= 800:
            img_pos_x = 0
            img_pos_y += img_size
        if img_pos_y >= 800:
            break

    min_range = 0
    max_range = 8
    img_pos_x = 0
    img_pos_y = 0
    placeholder = 0

    # sort image
    while True:

        for i in range(7):
            for j in range(7):
                if img_unsorted_positions[j] > img_unsorted_positions[j+1]:
                    placeholder = img_unsorted_positions[j]
                    img_unsorted_positions[j] = img_unsorted_positions[j+1]
                    img_unsorted_positions[j+1] = placeholder
                    print(img_unsorted_positions)
        if img_pos_y == 0:
            index = 0
        for n in range(min_range, max_range):
            screen.blit(imgs[n], (img_unsorted_positions[n], img_pos_y))
            img_pos_x += img_size
            img_unsorted_positions.append(x[index])
            index += 1 
    
            pygame.display.update()
            pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

