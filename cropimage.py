#!/usr/bin/env python

from PIL import Image

def crop():
    im = Image.open("monalisa.jpg")
    im = im.resize((800, 800))
    img_width, img_height = im.size
#    print("IMG SIZE:", img_width, img_height)
    
    max_size = 800
    pixels = 100

    left = 0
    top = 0
    right = pixels
    bottom = pixels
    
    path = ''
    iteration = 0

    not_done = True
    
    while not_done:
        for i in range(0, max_size, pixels):
            path = 'imgs/' + '[' + str(iteration) + ', ' + str(int(i/pixels)) + ']' + '.jpg'
#            print (i)
#            print('IMG ATTRIBUTES:', left+i, top, right, bottom)
            cropped_example = im.crop((left+i, top, right+i, bottom))
            cropped_example.save(path, 'jpeg')
        top += pixels
        bottom += pixels
        iteration += 1
        if iteration == 8:  # change this for something better
            not_done = False
    

