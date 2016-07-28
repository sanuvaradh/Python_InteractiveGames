# "Guess the number" mini-project developed for Coursera course on Integractive programming in python from Rice university
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math
# helper function to start and restart the game
low=0
high=100
num_guesses=7
secret_num=0
def new_game():
    global num_guesses,high,secret_num
    # initialize global variables used in your code here
    print "New game! Range is from 0 to "+str(high)
    secret_num=random.randrange(0, high)
    num_guesses= int(math.ceil((math.log(high+1))/(math.log (2))))
    print "Number of remaining guesses: "+ str(num_guesses)
    print "    "


# define event handlers for control panel
def range100():
    global high
    # button that changes the range to [0,100) and starts a new game 
    high=100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global high
    high=1000
    new_game()
    
def input_guess(guess):
    global num_guesses
    print "Your Guess was " +str(guess)
    num_guesses=num_guesses-1    
    if(int(guess)>high):
        print " number out of range"
    elif( secret_num==int(guess)):
        print "Correct!\n"
        new_game()
        return
    elif ( secret_num>int(guess)):
        print "Higher"
    else:
        print "Lower"
    print "Number of remaining guesses: "+ str(num_guesses)+"\n"
    if(num_guesses==0):
        print "You ran out of guesses!"
        print "The number was: "+str(secret_num)
        new_game()
   
# create frame
frame=simplegui.create_frame('Guess the Number!',200,200)

# register event handlers for control elements and start frame
frame.add_input('Guess',input_guess,50)
frame.add_button('Range 0 to 100',range100,200)
frame.add_button('Range 0 to 1000',range1000,200)
frame.start()

# call new_game 
new_game()



