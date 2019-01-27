class GameCharacter:
    character_img = 'Hero_Red_Path_IMG_v2.png'
    character_position = [400, 400]
    character_movement_vector = [0, 0]

    def __init__(self):
        pass

    # GETTERS
    # ________________________________________________

    def get_position(self):
        return self.character_position

    def get_movement_vector(self):
        return self.character_movement_vector

    def get_player_img(self):
        return self.character_img

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
