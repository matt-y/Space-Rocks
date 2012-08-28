from vector import Vector
from rock_list import Rock_List 

window_width = 800
window_height = 600
v_window_center = Vector(window_width/2, window_height/2)
clock_interval = 1/60.0

#for your health, don't make a humongous amount 
number_of_rocks = 10
player_start = Vector(window_width/2, window_height/2)

object_list = Rock_List(number_of_rocks, player_start).rock_list


debug = True 
