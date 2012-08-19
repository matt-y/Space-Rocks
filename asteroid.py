import pyglet 
from ship import Ship
from rocks import Rock_List, Rock
from vector import Vector
from resources import Resources

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
window = pyglet.window.Window(800, 600)
game_resources = Resources()
ship_start = Vector(400,300)
ship = Ship(ship_start)
rock_list = Rock_List(6, ship.ship_position)
fps_display = init_clock(update, 1/60.0)

#Below are the game's window events. 
@window.event
def on_draw():
    window.clear()
    ship.draw()
    for rock in rock_list.rock_list:
        rock.draw() #rock logic handled in rock's draw function 
    fps_display.draw()


if __name__ == '__main__':
    pyglet.app.run()
