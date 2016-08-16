"""
Integractive ping pong game for 2 players developed as part of Coursera course on Interactive python programming from Rice university
"""
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,0]
paddle1_pos=0
paddle2_pos=0
paddle1_vel=0
paddle2_vel=0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    """
    Function to spawn a new ball
    """
    global ball_pos, ball_vel
    ball_pos[0]=WIDTH/2
    ball_pos[1]=HEIGHT/2
    ball_vel=[random.randrange(5, 13),random.randrange(-10, -6)] #ranges arrived through multiple iterations
    if(direction==LEFT):
        ball_vel[0]= -ball_vel[0]
        
# define event handlers
def new_game():
    """
    Function to reset and start a new game: reset scores, paddle positions and velocities
    """
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
    global score1, score2  
    spawn_ball(RIGHT)
    score1=0
    score2=0
    paddle1_pos=0
    paddle2_pos=0
    paddle1_vel=0
    paddle2_vel=0
    
def draw(canvas):
    """
    Function to create canvas: draw edges, paddles, midlines and gutters
    """
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White") 
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1),(150,50),30,"white") 
    canvas.draw_text(str(score2),(450,50),30,"white")
    # update ball
    ball_pos[0]+= ball_vel[0]
    ball_pos[1]+= ball_vel[1]
    canvas.draw_circle((ball_pos[0], ball_pos[1]), BALL_RADIUS-5, 5, 'Red', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    if(paddle1_pos+paddle1_vel<=0)or (paddle1_pos+paddle1_vel+PAD_HEIGHT >=HEIGHT):
        paddle1_vel=0
    if(paddle2_pos+paddle2_vel<=0)or (paddle2_pos+paddle2_vel+PAD_HEIGHT >=HEIGHT):
        paddle2_vel=0
    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos], [PAD_WIDTH, paddle1_pos], [PAD_WIDTH,paddle1_pos+PAD_HEIGHT], [0,paddle1_pos+PAD_HEIGHT]], 0.1, 'Black','Yellow')
    canvas.draw_polygon([[WIDTH-PAD_WIDTH-1,paddle2_pos], [WIDTH, paddle2_pos], [WIDTH,paddle2_pos+PAD_HEIGHT], [WIDTH-PAD_WIDTH-1,paddle2_pos+PAD_HEIGHT]], 0.1, 'Black','Yellow')
    
    # determine whether paddle and ball collide    
    #LEFT
    if((ball_pos[0]-BALL_RADIUS<=PAD_WIDTH+1)):
        if(ball_pos[1]>= paddle1_pos and ball_pos[1] <= paddle1_pos+PAD_HEIGHT ):
            ball_vel[0]=-ball_vel[0]
        else:
            score2+=1
            spawn_ball(RIGHT)
    #RIGHT        
    if((ball_pos[0]+BALL_RADIUS>=WIDTH-PAD_WIDTH+1)):
        if(ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos+PAD_HEIGHT ):
            ball_vel[0]=-ball_vel[0]
        else:
            score1+=1
            spawn_ball(LEFT)           
    #if ball hits the edges, reverse its direction
    if((ball_pos[1]-BALL_RADIUS<=0) or (ball_pos[1]+BALL_RADIUS>=HEIGHT)):
        ball_vel[1]=-ball_vel[1]
        
     
def keydown(key):
    """
    Function to map keys for playing: 
    w and s : when pressed down help to move paddle up/down for player on left
    up and down arrows: when pressed down help to move paddle up/down for player on right
    """
    global paddle1_vel, paddle2_vel
    acc = 9
    dec = 9
    if(key==simplegui.KEY_MAP['w']):
        paddle1_vel -= acc
    elif(key==simplegui.KEY_MAP['s']):        
        paddle1_vel +=dec
    elif(key==simplegui.KEY_MAP["up"]):
        paddle2_vel -= acc
    elif(key==simplegui.KEY_MAP["down"]):        
        paddle2_vel += dec
        
   
def keyup(key):
    """
    Function to handle transition from key press to release
    """
    global paddle1_vel, paddle2_vel
    paddle1_vel=0
    paddle2_vel=0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1=frame.add_button("Reset",new_game,200)


# start frame
new_game()
frame.start()
