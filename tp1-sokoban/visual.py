import pygame, sys
from pygame.locals import *

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Config
BOX_COLOR = (191, 161, 134)
TARGET_COLOR = (64, 201, 255)
PLAYER_COLOR = (249, 64, 255)
WALL_COLOR = (150, 5, 5)
BACKGROUND_COLOR = BLACK
PLAYER_IMAGE_PATH = "player3.png"
BOX_SIZE_RATIO = 1.5
PLAYER_SIZE_RATIO = 1.1

AUTO_PLAY_DELAY = 500
WINNING_FPS = 25

last_direction = "left"


def draw_square(d, x, y, block_size, color):
    pygame.draw.rect(d, color, (x * block_size, y * block_size, block_size, block_size))


def draw_wall(d, x, y, block_size, size, color):
    pygame.draw.rect(d, color, (x * block_size, y * block_size, size, size))

def draw_objective(d, x, y, block_size, size, color):
    pygame.draw.rect(d, color, (x * block_size, y * block_size, size, size))

'''
def draw_player(d, x, y, block_size, size, color):
    pygame.draw.rect(d, color, (x * block_size, y * block_size, size, size))

'''
def draw_player(d, x, y, block_size, size, direction=None, degree=None):
    player_pic = pygame.image.load(PLAYER_IMAGE_PATH)
    (image_width, image_height) = player_pic.get_rect().size

    bigger = image_height if image_height > image_width else image_width
    lower = image_width if image_height > image_width else image_height

    ratio = 1.0 * lower / bigger

    if bigger == image_width:
        image_width = int(size)
        image_height = int(size * ratio)
    else:
        image_height = int(size)
        image_width = int(size * ratio)

    # Transformations
    player_pic = pygame.transform.scale(player_pic, (image_width, image_height))

    global last_direction

    if direction == "right" or direction == "left":
        last_direction = direction

    if last_direction == 'right':
        player_pic = pygame.transform.flip(player_pic, True, False)

    if degree is None:
        degree = 0

        if (direction == "up" and last_direction == "right") or (direction == "down" and last_direction == "left"):
            degree = 30
        elif (direction == "up" and last_direction == "left") or (direction == "down" and last_direction == "right"):
            degree = -30
    
    player_pic = pygame.transform.rotate(player_pic, degree)

    # Drawing
    margin = (block_size - size) / 2

    d.blit(player_pic, (x * block_size + margin, y * block_size + margin))

def draw_box(d, x, y, block_size, size, color):
    margin = (block_size - size) / 2
    pygame.draw.rect(d, color, (x * block_size + margin, y * block_size + margin, size, size))


def draw_scene(d, block_size, a_map, scene):
    d.fill(BACKGROUND_COLOR)

    # Draw targets
    # for target in map['targets']:
    #     draw_square(d, x, y, block_size, TARGET_COLOR)

    # Draw boxes

    for(x,y) in a_map.objectives:
        draw_wall(d, y, x, block_size, block_size, TARGET_COLOR)

    for (x, y) in scene.boxes:
        draw_box(d, y, x, block_size, int(block_size / BOX_SIZE_RATIO), BOX_COLOR)

    for (x, y) in a_map.walls:
        draw_wall(d, y, x, block_size, block_size, WALL_COLOR)

    # Draw player
    (x, y) = scene.player
    #draw_player(d, y, x, block_size, block_size, PLAYER_COLOR)
    draw_player(d, y, x, block_size, int(block_size / BOX_SIZE_RATIO), scene.direction)

WINNING_SCENE = [
    {
        'direction': 'right',
        'degree': 0
    },
    {
        'direction': 'right',
        'degree': 10
    },
    {
        'direction': 'right',
        'degree': 20
    },
    {
        'direction': 'right',
        'degree': 30
    },
    {
        'direction': 'right',
        'degree': 50
    },
    {
        'direction': 'right',
        'degree': 70
    },
    {
        'direction': 'right',
        'degree': 80
    },
    {
        'direction': 'right',
        'degree': 90
    },
    {
        'direction': 'right',
        'degree': 110
    },
    {
        'direction': 'right',
        'degree': 130
    },
    {
        'direction': 'right',
        'degree': 150
    },
    {
        'direction': 'right',
        'degree': 170
    },
    {
        'direction': 'right',
        'degree': 180
    },
    {
        'direction': 'right',
        'degree': 180
    },
    {
        'direction': 'right',
        'degree': 180
    },
    {
        'direction': 'right',
        'degree': 200
    },
    {
        'direction': 'right',
        'degree': 230
    },
    {
        'direction': 'right',
        'degree': 250
    },
    {
        'direction': 'right',
        'degree': 270
    },
    {
        'direction': 'right',
        'degree': 300
    },
    {
        'direction': 'right',
        'degree': 330
    },
    {
        'direction': 'right',
        'degree': 350
    },
    {
        'direction': 'right',
        'degree': 360
    },
    {
        'direction': 'right',
        'degree': 360
    },
    {
        'direction': 'right',
        'degree': 360
    },
    {
        'direction': 'right',
        'degree': 360
    }
]

def draw_winning(d, block_size, player, win_idx):
    # Draw player
    (x, y) = player
    #draw_player(d, y, x, block_size, block_size, PLAYER_COLOR)
    cfg = WINNING_SCENE[win_idx % len(WINNING_SCENE)]

    draw_square(d, y, x, block_size, BACKGROUND_COLOR)
    draw_player(d, y, x, block_size, int(block_size / BOX_SIZE_RATIO), cfg['direction'], cfg['degree'])


def visual_play(game_map, nodes):
    pygame.init()
    pygame.display.set_caption('Sokoban')

    # LOAD DATA
    scenes=nodes
    a_map=game_map

    # SETUP
    map_size = (a_map.cantFilas, a_map.cantColumnas)

    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 600

    block_width = int(WINDOW_WIDTH / a_map.cantColumnas)
    block_height = int(WINDOW_HEIGHT / a_map.cantFilas)

    block_size = block_width if (block_width < block_height) else block_height

    WINDOW_WIDTH = block_size * a_map.cantColumnas+1
    WINDOW_HEIGHT = block_size * a_map.cantFilas+1

    d = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    current_scene_idx = 0
    auto_play = False
    last_time = None
    winning_idx = 0

    draw_scene(d, block_size, a_map, nodes[current_scene_idx])

    while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    auto_play = False
                    winning_idx = 0
                    current_scene_idx = (current_scene_idx - 1) if (current_scene_idx > 0) else 0
                elif event.key == K_RIGHT:
                    auto_play = False
                    winning_idx = 0
                    current_scene_idx = (current_scene_idx + 1) if (current_scene_idx < len(scenes) - 1) else (len(scenes) - 1)
                elif event.key == K_p:
                    auto_play = not auto_play
                    if auto_play:
                        last_time = pygame.time.get_ticks()
                elif event.key == K_r:
                    auto_play = False
                    winning_idx = 0
                    current_scene_idx = 0

                draw_scene(d, block_size, a_map, scenes[current_scene_idx])

        if auto_play:
            curr_time = pygame.time.get_ticks()
            if (curr_time - last_time) > AUTO_PLAY_DELAY:
                current_scene_idx = (current_scene_idx + 1) if (current_scene_idx < len(scenes) - 1) else (
                            len(scenes) - 1)
                draw_scene(d, block_size, a_map, scenes[current_scene_idx])
                last_time = curr_time

            if current_scene_idx == (len(scenes) - 1) and ((curr_time - last_time) % WINNING_FPS) == 0:
                draw_winning(d, block_size, scenes[current_scene_idx].player, winning_idx)
                winning_idx += 1

        pygame.display.update()
