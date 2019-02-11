#!/usr/bin/env python

user_choice = "1"
amount_of_choices = 1

def showMenu():
    while True:
        print("What sorting algorithm do you want to use?")
        print("[1] Bubble Sort")
#        user_choice = input()
        if (user_choice == "1"):
            return "bubble"
            break

