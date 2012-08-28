
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

    #rock sprites 
    rock_image1 = pyglet.resource.image("rock1.png")
    rock_image2 = pyglet.resource.image("rock2.png")
    rock_image3 = pyglet.resource.image("rock3.png")
    rock_sprites = [center_image(rock_image1), 
                    center_image(rock_image2),
                    center_image(rock_image3)]

    rock_image1_small = pyglet.resource.image("rock1_small.png")
    center_image(rock_image1_small)

class Labels(object):
    fps_counter = pyglet.text.Label(text="fps:", x=100, y=100,
                                    anchor_x='center', 
                                    anchor_y='center')
