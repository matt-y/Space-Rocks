import pyglet 
import math 
import constants
from ship import Ship
from rocks import Rock_List, Rock
from vector import Vector
from resources import Resources
from gameobject import GameObject
from pyglet.window import key

def update(dt):
    '''
    update function (empty atm). Docs reccommend to give pyglet something to do 
    as to keep the fps at a stable level 
    
    '''
    pass

def init_clock(interval_func, interval):
    '''
    Function configures a couple clock settings for the game. 
    Returns a handle on a ClockDisplay that is drawn after all game logic 

    '''
    pyglet.clock.schedule_interval(interval_func, interval)
    return pyglet.clock.ClockDisplay()
    

# Initial Application Setup. 
# Player ship, asteroids, window, resources, etc.
window = pyglet.window.Window(constants.window_width, constants.window_height)
game_resources = Resources()
ship_start = constants.player_start
ship = Ship(ship_start)
#python! :<
object_list = Rock_List(constants.number_of_rocks, ship.position).rock_list
#object_list.append(ship)
fps_display = init_clock(update, constants.clock_interval)

#Below are the game's window events. 
@window.event
def on_draw():
    window.clear()
    for obj in object_list:
        #rock logic handled in rock's draw function, likewise for ship
        obj.draw()
    rock2obj_collision_check(object_list, object_list)
    fps_display.draw()
    
@window.event 
def on_key_press(symbol, mods):
    if symbol == key.LEFT:
        print "left key"
        ship.rotate_left()
    elif symbol == key.RIGHT:
        print "right key"
        ship.rotate_right()


def rock2obj_collision_check(list1, list2):
    '''
    naiive collision algorithm to compute collisions between rocks or ships or both 

    '''
    for obj in list1:
        for other_obj in list2:
            if obj == other_obj:
                continue
            else:
                if(GameObject.will_collide_with(obj, other_obj)):
                       GameObject.handle_collision(obj, other_obj)




if __name__ == '__main__':
    pyglet.app.run()
