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


maps = []


def generate_level(level):
    # 0 - поле, 1 - горы, 2 - лес, 3 - река, 4 - база игрока1, \
    # 5 - база игрока2, 6 - нейтр. город, 7 - крепость, 8 - рудник, 9 - дорога
    global maps
    temp = []
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
                temp.append(0)
            elif level[y][x] == '#':
                Tile('wall', x, y)
                temp.append(1)
            elif level[y][x] == '%':
                Tile('bigtown', x, y)
                temp.append(7)
            elif level[y][x] == '$':
                Tile('coin', x, y)
                temp.append(8)
            elif level[y][x] == '+':
                Tile('road', x, y)
                temp.append(9)
            elif level[y][x] == '-':
                Tile('groad', x, y)
                temp.append(9)
            elif level[y][x] == '[':
                Tile('lbroad', x, y)
                temp.append(9)
            elif level[y][x] == 'T':
                Tile('troad', x, y)
                temp.append(9)
            elif level[y][x] == 'r':
                Tile('rtroad', x, y)
                temp.append(9)
            elif level[y][x] == 'e':
                Tile('retroad', x, y)
                temp.append(9)
            elif level[y][x] == ']':
                Tile('rbroad', x, y)
                temp.append(9)
            elif level[y][x] == 'o':
                Tile('luroad', x, y)
                temp.append(9)
            elif level[y][x] == 'p':
                Tile('ruroad', x, y)
                temp.append(9)
            elif level[y][x] == 'c':
                Tile('croad', x, y)
                temp.append(9)
            elif level[y][x] == 'u':
                Tile('ltroad', x, y)
                temp.append(9)
            elif level[y][x] == 't':
                Tile('tree', x, y)
                temp.append(2)
            elif level[y][x] == '8':
                Tile('river', x, y)
                temp.append(3)
            elif level[y][x] == '6':
                Tile('griver', x, y)
                temp.append(3)
            elif level[y][x] == '3':
                Tile('rbriver', x, y)
                temp.append(3)
            elif level[y][x] == '7':
                Tile('luriver', x, y)
                temp.append(3)
            elif level[y][x] == '9':
                Tile('ruriver', x, y)
                temp.append(3)
            elif level[y][x] == '1':
                Tile('lbriver', x, y)
                temp.append(3)
            elif level[y][x] == 'b':
                Tile('griverb', x, y)
                temp.append(3)
            elif level[y][x] == 'd':
                Tile('riverb', x, y)
                temp.append(3)
            elif level[y][x] == 'n':
                Tile('smalltown', x, y)
                temp.append(6)
            elif level[y][x] == 'x':
                Tile('smalltowna', x, y)
                temp.append(4)
            elif level[y][x] == 'y':
                Tile('smalltownb', x, y)
                temp.append(5)
        if temp:
            maps.append(temp)
            temp = []
    return x, y


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
    'troad': pygame.transform.scale(load_image('troad.png'), (30, 30)),
    'rtroad': pygame.transform.scale(load_image('rtroad.png'), (30, 30)),
    'retroad': pygame.transform.scale(load_image('retroad.png'), (30, 30)),
    'croad': pygame.transform.scale(load_image('croad.png'), (30, 30)),
    'ltroad': pygame.transform.scale(load_image('ltroad.png'), (30, 30)),

    'griver': pygame.transform.scale(load_image('griver.png'), (30, 30)),
    'river': pygame.transform.scale(load_image('river.png'), (30, 30)),
    'lbriver': pygame.transform.scale(load_image('lbriver.png'), (30, 30)),
    'rbriver': pygame.transform.scale(load_image('rbriver.png'), (30, 30)),
    'luriver': pygame.transform.scale(load_image('luriver.png'), (30, 30)),
    'ruriver': pygame.transform.scale(load_image('ruriver.png'), (30, 30)),
    'griverb': pygame.transform.scale(load_image('griverb.png'), (30, 30)),
    'riverb': pygame.transform.scale(load_image('riverb.png'), (30, 30)),
    'smalltown': pygame.transform.scale(load_image('smalltown.png'), (30, 30)),
    'smalltowna': pygame.transform.scale(load_image('smalltowna.png'), (30, 30)),
    'smalltownb': pygame.transform.scale(load_image('smalltownb.png'), (30, 30)),
    'bigtown': pygame.transform.scale(load_image('castle.png'), (30, 30)),
    'coin': pygame.transform.scale(load_image('coin.png'), (30, 30)),
    'coina': pygame.transform.scale(load_image('coina.png'), (30, 30)),
    'coinb': pygame.transform.scale(load_image('coinb.png'), (30, 30)),

}

tile_width = tile_height = 30


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        move = 300
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + move, tile_height * pos_y)


class Swords(pygame.sprite.Sprite):
    global warmap

    def __init__(self, typer):
        super().__init__(war_group)
        self.image = load_image('Swordbig.png')
        if typer == 'me':
            self.rect = self.image.get_rect().move(30 * 27 + 290, 30 * 28 - 10)
            warmap[27][28] = 1

    def update(self, move, speed):
        if move == '1':
            self.rect[0] -= speed
        elif move == '2':
            self.rect[1] -= speed
        elif move == '3':
            self.rect[0] += speed
        elif move == '4':
            self.rect[1] += speed


class Units(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(design_group, all_sprites)
        self.image = load_image('Units.png')
        self.rect = self.image.get_rect().move(0, 0)


class Icons(pygame.sprite.Sprite):
    def __init__(self, number):
        super().__init__(design_group, all_sprites)
        self.base = True
        self.n = number
        self.redraw()
        self.rect = self.image.get_rect().move(0, 100 * number)
        self.multi = 100
        pygame.draw.rect(screen, (0, 255, 0), (4, 100 * number + 85, (293 * self.multi), 12), 0)

    def redraw(self):
        if self.base:
            self.image = load_image('Swords' + str(self.n) + '.png')
        else:
            self.image = load_image('Swords' + str(self.n) + 'active.png')

    def change(self):
        self.base = not self.base
        self.redraw()

    def back(self):
        self.base = True
        self.redraw()

    def reheal(self, into):
        self.multi += into


design_group = pygame.sprite.Group()
war_group = pygame.sprite.Group()
end_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
level_x, level_y = generate_level(load_level('map.txt'))

warmap = [[0 for j in range(30)] for i in range(30)]
# 1 - мечники

clock = pygame.time.Clock()
running = True
c = -1
name = 0
promove = []
already = []
drown = []
allow = -1


Units()
while running:
    tiles_group.draw(screen)
    war_group.draw(screen)
    design_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                if name == 0:
                    Sword0 = Swords('me')
                    name += 1
                    icon0 = Icons(1)
                    promove.append(0)
                elif name == 1:
                    Sword1 = Swords('me')
                    name += 1
                    icon1 = Icons(2)
                    promove.append(0)
                elif name == 2:
                    Sword2 = Swords('me')
                    name += 1
                    icon2 = Icons(3)
                    promove.append(0)
                elif name == 3:
                    Sword3 = Swords('me')
                    name += 1
                    icon3 = Icons(4)
                    promove.append(0)
                elif name == 4:
                    Sword4 = Swords('me')
                    name += 1
                    icon4 = Icons(5)
                    promove.append(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > 300:
                first = (event.pos[0] - 300) // 30
                second = event.pos[1] // 30
                # if second <= 29:
                # print(first)
                # print(second)
                # print(maps[second][first])
            if (100 < event.pos[1] < 199) and event.pos[0] < 200 and len(promove) >= 1:
                try:
                    icon0.change()
                    icon1.back()
                    icon2.back()
                    icon3.back()
                    icon4.back()
                except Exception:
                    pass
                allow = 0

            elif (200 < event.pos[1] < 299) and event.pos[0] < 200 and len(promove) >= 2:
                try:
                    icon1.change()
                    icon0.back()
                    icon2.back()
                    icon3.back()
                    icon4.back()
                except Exception:
                    pass
                allow = 1

            elif (300 < event.pos[1] < 399) and event.pos[0] < 200 and len(promove) >= 3:
                try:
                    icon2.change()
                    icon0.back()
                    icon1.back()
                    icon3.back()
                    icon4.back()
                except Exception:
                    pass
                allow = 2

            elif (400 < event.pos[1] < 499) and event.pos[0] < 200 and len(promove) >= 4:
                try:
                    icon3.change()
                    icon0.back()
                    icon1.back()
                    icon2.back()
                    icon4.back()
                except Exception:
                    pass
                allow = 3

            elif (500 < event.pos[1] < 599) and event.pos[0] < 200 and len(promove) >= 5:
                try:
                    icon4.change()
                    icon0.back()
                    icon1.back()
                    icon2.back()
                    icon3.back()
                except Exception:
                    pass
                allow = 4
            elif event.pos[1] > 599 and event.pos[0] < 200:
                try:
                    allow = -1
                    icon0.back()
                    icon1.back()
                    icon2.back()
                    icon3.back()
                    icon4.back()
                except Exception:
                    pass

        if pygame.mouse.get_pressed()[0]:
            if event.pos[0] > 300 and event.pos[1] < 900:
                if ((event.pos[0] - 300) // 30, event.pos[1] // 30) not in already:
                    already.append(((event.pos[0] - 300) // 30, event.pos[1] // 30))
                    print(already)

    for j in already:
        pygame.draw.rect(screen, (255, 255, 0), (j[0] * 30 + 300, j[1] * 30, 30, 30), 1)
        drown.append(j)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
