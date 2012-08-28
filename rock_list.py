from rocks import Rock
from vector import Vector

class Rock_List(object):
    def __init__(self, number, player_pos):
        self.number = number 
        self.rock_list = [Rock.create_rock_from_other_pos(player_pos)]
        for i in range(self.number):
         
            #create a rock. If the rock is in range of the player OR any rock in the rock list - try again 
            is_rock_valid = False 
           
            while(is_rock_valid == False):
                broken = False 
                #try to get a valid rock 
                rock = Rock.create_rock_from_other_pos(player_pos)
                for r in self.rock_list:
                    if(self.do_objects_overlap(r, rock)):
                        #conflict with current rock 
                        broken = True
                        break
                    else:
                        continue
                if(broken): 
                    continue
                else: 
                    is_rock_valid = True

            #outside while loop:
            self.rock_list.append(rock)

    def do_objects_overlap(self, one, other):
        if(one.position.v_distance_between(other.position) < 100):
            return True
        else:
            return False
