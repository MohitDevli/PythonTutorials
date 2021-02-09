#print_options = pymunk.SpaceDebugDrawOptions() # For easy printing
#while True:                 # Infinite loop simulation
    #space.step(0.02)        # Step the simulation one step forward
    #space.debug_draw(print_options) # Print the state of the simulation
    

import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
import time


#seting up pyglet
window=pyglet.window.Window(1280,720,"MyMunk",resizable=True)
option=DrawOptions()

space=pymunk.Space()
space.gravity=0,-1000

body=pymunk.Body(1,1666)
body.position=600,700


poly=pymunk.Poly.create_box_bb(body,bb,radius=25)
space.add(body,poly)

@window.event
def on_draw():
    window.clear()
    space.debug_draw(option)

def update(dt): #dt==date_time
    space.step(dt)
    

if __name__=='__main__':
    pyglet.clock.schedule_interval(update,1.0/60)   #this will call update method once in every 1/60 sec
    pyglet.app.run()