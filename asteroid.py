import pyglet 
from ship import Ship
from rocks import Rock_List, Rock
from vector import Vector
from resources import Labels, Resources


window = pyglet.window.Window(800, 600)
game_resources = Resources()
ship_start = Vector(400,400)
ship = Ship(ship_start)
rock_list = Rock_List(12, ship.ship_position)


@window.event
def on_draw():
    window.clear()
    ship.draw()
    for rock in rock_list.rock_list:
        rock.draw()
    Labels.fps_counter.draw()
    


if __name__ == '__main__':
    pyglet.app.run()
