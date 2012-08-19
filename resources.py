import pyglet

def center_image(image):
      """ 
      Sets the anchor point of an image to its center
      """
      image.anchor_x = image.width/2
      image.anchor_y = image.height/2
      return image
      

class Resources(object):
    pyglet.resource.path = ['images']
    pyglet.resource.reindex()

    #load image files 
    ship_image = pyglet.resource.image("ship.png")
    center_image(ship_image)

    rock_image = pyglet.resource.image("rock.png")
    center_image(rock_image)

class Labels(object):
    fps_counter = pyglet.text.Label(text="fps:", x=100, y=100,
                                    anchor_x='center', 
                                    anchor_y='center')
