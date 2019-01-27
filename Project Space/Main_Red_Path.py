import pygame
# import Adventurer_Red_Path
# import Enemy_Red_Path

# __________________________________________________________________
# Initializes pygame module

pygame.init()

# __________________________________________________________________
# Universal Constants

window_width = 1000
window_height = 600

adventurer_IMG = pygame.image.load('Hero_Red_Path_IMG.png')
red_path_IMG = pygame.image.load('Red_Path_Logo_IMG.png')

black = (0, 0, 0)
white = (0, 0, 0)

# __________________________________________________________________

gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Red_Path')
clock = pygame.time.Clock()

# __________________________________________________________________
# Event processing


def process_key_down(delta_vector, event):
    adventurer_delta_x = delta_vector[0]
    adventurer_delta_y = delta_vector[1]

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            adventurer_delta_x = -5
        elif event.key == pygame.K_RIGHT:
            adventurer_delta_x = 5

        if event.key == pygame.K_UP:
            adventurer_delta_y = -5
        elif event.key == pygame.K_DOWN:
            adventurer_delta_y = 5

    return [adventurer_delta_x, adventurer_delta_y]


def process_key_up(delta_vector, event):
    adventurer_x_delta = delta_vector[0]
    adventurer_y_delta = delta_vector[1]

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or pygame.K_RIGHT:
            adventurer_x_delta = 0

        if event.key == pygame.K_UP or pygame.K_DOWN:
            adventurer_y_delta = 0

    return [adventurer_x_delta, adventurer_y_delta]

# _________________________________________________________________
# Graphics Functions


def display_graphics(adventurer_pos, color=white):
    gameDisplay.fill(color)
    red_path_display()
    adventurer_display(adventurer_pos)


def adventurer_display(position):
    gameDisplay.blit(adventurer_IMG, (position[0], position[1]))


def red_path_display():
    gameDisplay.blit(red_path_IMG, (0, 0))


def update_adventurer_pos(current_pos, current_delta):
    updated_x_pos = current_pos[0] + current_delta[0]
    updated_y_pos = current_pos[1] + current_delta[1]
    return [updated_x_pos, updated_y_pos]


# __________________________________________________________________
# Game play loop

def game_loop():

    game_play = True
    adventurer_pos = [400, 400]
    adventurer_movement_vector = [0, 0]

    while game_play:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_play = False

            adventurer_movement_vector = process_key_down(adventurer_movement_vector, event)
            adventurer_movement_vector = process_key_up(adventurer_movement_vector, event)

        adventurer_pos = update_adventurer_pos(adventurer_pos, adventurer_movement_vector)

        display_graphics(adventurer_pos, white)

        pygame.display.update()

        clock.tick(60)


game_loop()
pygame.quit()
quit()


