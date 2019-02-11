#!/usr/bin/env python

import menu
import cropimage

choice = ''
choice = menu.showMenu()
cropimage.crop()

if (choice == 'bubble'):
    import bubblesort
    bubblesort.init()
