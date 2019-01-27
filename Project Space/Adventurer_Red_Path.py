import GameCharacter


class Adventurer(GameCharacter):

    player_img = 'Hero_Red_Path_IMG_v2.png'
    position = [400, 400]
    movement_vector = [0, 0]
    health = 10

    def __init__(self):
        pass

# GETTERS
# ________________________________________________

    def get_position(self):
        return self.position

    def get_movement_vector(self):
        return self.movement_vector

    def get_player_img(self):
        return self.player_img

    def get_player_health(self):
        return self.health

# SETTERS
# ________________________________________________

    def set_position(self, new_pos):
        self.position[0] = new_pos[0]
        self.position[1] = new_pos[1]

    def set_movement_vector(self, mov_vector):
        self.movement_vector[0] = mov_vector[0]
        self.movement_vector[1] = mov_vector[1]

# ___________________________________________________
# BEHAVIORAL FUNCTIONS

    def apply_movement(self):
        self.movement_vector[0] += self.movement_vector[0]
        self.movement_vector[1] += self.movement_vector[1]
