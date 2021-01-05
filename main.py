import pygame
import sys
import os

WIDTH = 1200
HEIGHT = 1000
pygame.init()
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
pygame.display.set_caption('P2C1 WIP')
fps = 50

walls = []


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def terminate():
    pygame.quit()
    sys.exit()


def generate_level(level):
    global walls
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
                walls.append([x, y])
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == '+':
                Tile('road', x, y)
            elif level[y][x] == '-':
                Tile('groad', x, y)
            elif level[y][x] == '[':
                Tile('lbroad', x, y)
            elif level[y][x] == ']':
                Tile('rbroad', x, y)
            elif level[y][x] == 'o':
                Tile('luroad', x, y)
            elif level[y][x] == 'p':
                Tile('ruroad', x, y)
            elif level[y][x] == 't':
                Tile('tree', x, y)
            elif level[y][x] == '8':
                Tile('river', x, y)
            elif level[y][x] == '6':
                Tile('griver', x, y)
            elif level[y][x] == '3':
                Tile('rbriver', x, y)
            elif level[y][x] == '7':
                Tile('luriver', x, y)
            elif level[y][x] == '9':
                Tile('ruriver', x, y)
            elif level[y][x] == '1':
                Tile('lbriver', x, y)
            elif level[y][x] == 'b':
                Tile('griverb', x, y)
    return new_player, x, y


tile_images = {
    'wall': pygame.transform.scale(load_image('mgrass.png'), (30, 30)),
    'empty': pygame.transform.scale(load_image('grass.png'), (30, 30)),
    'road': pygame.transform.scale(load_image('road.png'), (30, 30)),
    'lbroad': pygame.transform.scale(load_image('lbroad.png'), (30, 30)),
    'rbroad': pygame.transform.scale(load_image('rbroad.png'), (30, 30)),
    'luroad': pygame.transform.scale(load_image('luroad.png'), (30, 30)),
    'ruroad': pygame.transform.scale(load_image('ruroad.png'), (30, 30)),
    'tree': pygame.transform.scale(load_image('tgrass.png'), (30, 30)),
    'groad': pygame.transform.scale(load_image('groad.png'), (30, 30)),

    'griver': pygame.transform.scale(load_image('griver.png'), (30, 30)),
    'river': pygame.transform.scale(load_image('river.png'), (30, 30)),
    'lbriver': pygame.transform.scale(load_image('lbriver.png'), (30, 30)),
    'rbriver': pygame.transform.scale(load_image('rbriver.png'), (30, 30)),
    'luriver': pygame.transform.scale(load_image('luriver.png'), (30, 30)),
    'ruriver': pygame.transform.scale(load_image('ruriver.png'), (30, 30)),
    'griverb': pygame.transform.scale(load_image('griverb.png'), (30, 30))
}
player_image = None

tile_width = tile_height = 30


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        move = 300
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + move, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.px = pos_x
        self.py = pos_y
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * self.px + 15, tile_height * self.py + 5)
        self.post = [4, 4]


class Bomb(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = 0


end_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

player, level_x, level_y = generate_level(load_level('map.txt'))

clock = pygame.time.Clock()
running = True

while running:
    tiles_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()