import pygame
import sys
import os
import pprint

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


class Swordico(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(design_group, all_sprites)
        self.base = True
        self.images = ['Sword100.png', 'Sword100act.png']
        self.image = load_image(self.images[0])
        self.rect = self.image.get_rect().move(300, 900)

    def redraw(self):
        if self.base:
            self.image = load_image(self.images[0])
        else:
            self.image = load_image(self.images[1])
        self.base = not self.base

    def back(self):
        self.base = True
        self.redraw()

    def activate(self):
        self.base = False
        self.redraw()


class Axeico(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(design_group, all_sprites)
        self.base = True
        self.images = ['Axe100.png', 'Axe100act.png']
        self.image = load_image(self.images[0])
        self.rect = self.image.get_rect().move(400, 900)

    def redraw(self):
        if self.base:
            self.image = load_image(self.images[0])
        else:
            self.image = load_image(self.images[1])
        self.base = not self.base

    def back(self):
        self.base = True
        self.redraw()

    def activate(self):
        self.base = False
        self.redraw()


class Bowico(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(design_group, all_sprites)
        self.base = True
        self.images = ['Bow100.png', 'Bow100act.png']
        self.image = load_image(self.images[0])
        self.rect = self.image.get_rect().move(500, 900)

    def redraw(self):
        if self.base:
            self.image = load_image(self.images[0])
        else:
            self.image = load_image(self.images[1])
        self.base = not self.base

    def back(self):
        self.base = True
        self.redraw()

    def activate(self):
        self.base = False
        self.redraw()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        move = 300
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + move, tile_height * pos_y)


class Swords(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(war_group)
        self.image = load_image('Swordbig.png')
        self.rect = self.image.get_rect().move(30 * 27 + 290, 30 * 28 - 10)

    def update(self, move, speed):
        if move == 'left':
            self.rect[0] -= speed
        elif move == 'up':
            self.rect[1] -= speed
        elif move == 'right':
            self.rect[0] += speed
        elif move == 'down':
            self.rect[1] += speed

    def getrect(self):
        return (self.rect[0] - 300) // 30, self.rect[1] // 30


class Axes(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(war_group)
        self.image = load_image('Axebig.png')
        self.rect = self.image.get_rect().move(30 * 27 + 290, 30 * 28 - 10)

    def update(self, move, speed):
        if move == 'left':
            self.rect[0] -= speed
        elif move == 'up':
            self.rect[1] -= speed
        elif move == 'right':
            self.rect[0] += speed
        elif move == 'down':
            self.rect[1] += speed

    def getrect(self):
        return (self.rect[0] - 300) // 30, self.rect[1] // 30


class Bows(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(war_group)
        self.image = load_image('Bowbig.png')
        self.rect = self.image.get_rect().move(30 * 27 + 290, 30 * 28 - 10)

    def update(self, move, speed):
        if move == 'left':
            self.rect[0] -= speed
        elif move == 'up':
            self.rect[1] -= speed
        elif move == 'right':
            self.rect[0] += speed
        elif move == 'down':
            self.rect[1] += speed

    def getrect(self):
        return (self.rect[0] - 300) // 30, self.rect[1] // 30


class Units(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(design_group, all_sprites)
        self.image = load_image('Units.png')
        self.rect = self.image.get_rect().move(0, 0)


class Icons(pygame.sprite.Sprite):
    def __init__(self, number, typek):
        super().__init__(design_group, all_sprites)
        self.base = True
        self.n = number
        self.typer = typek
        self.redraw()
        self.rect = self.image.get_rect().move(0, 100 * number)
        self.multi = 100
        pygame.draw.rect(screen, (0, 255, 0), (4, 100 * number + 85, (293 * self.multi), 12), 0)

    def redraw(self):
        if self.base:
            self.image = load_image(str(self.typer) + str(self.n) + '.png')
        else:
            self.image = load_image(str(self.typer) + str(self.n) + 'active.png')

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
allow = -1
work = False
position = 0
point = ()
spawnmode = 0

moveg = []
movev = []
speedmap = []
Units()
Swordicon = Swordico()
Axeicon = Axeico()
Bowicon = Bowico()

qr = pprint.PrettyPrinter(width=41, compact=True)
qr.pprint(maps)
Sword0 = None
Sword1 = None
Sword2 = None
Sword3 = None
Sword4 = None

Axe0 = None
Axe1 = None
Axe2 = None
Axe3 = None
Axe4 = None

Bow0 = None
Bow1 = None
Bow2 = None
Bow3 = None
Bow4 = None
while running:
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    war_group.draw(screen)
    design_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if spawnmode == 0:
                    if Sword3 or Axe3 or Bow3:
                        Sword4 = Swords()
                        icon4 = Icons(5, 'Swords')
                    elif Sword2 or Axe2 and not Axe3 and not Bow3 or Bow2 and not Bow3 and not Axe3:
                        Sword3 = Swords()
                        icon3 = Icons(4, 'Swords')
                    elif Sword1 or Axe1 and not Axe2 and not Bow2 or Bow1 and not Bow2 and not Axe2:
                        Sword2 = Swords()
                        icon2 = Icons(3, 'Swords')
                    elif Sword0 or Axe0 and not Axe1 and not Bow1 or Bow0 and not Bow1 and not Axe1:
                        Sword1 = Swords()
                        icon1 = Icons(2, 'Swords')
                    elif not Axe0 and not Bow0:
                        Sword0 = Swords()
                        icon0 = Icons(1, 'Swords')

                elif spawnmode == 1:
                    if Axe3 or Sword3 or Bow3:
                        Axe4 = Axes()
                        icon4 = Icons(5, 'Axes')
                    elif Axe2 or Sword2 and not Sword3 and not Bow3 or Bow2 and not Bow3 and not Sword3:
                        Axe3 = Axes()
                        icon3 = Icons(4, 'Axes')
                    elif Axe1 or Sword1 and not Sword2 and not Bow2 or Bow1 and not Bow2 and not Sword2:
                        Axe2 = Axes()
                        icon2 = Icons(3, 'Axes')
                    elif Axe0 or Sword0 and not Sword1 and not Bow1 or Bow0 and not Bow1 and not Sword1:
                        Axe1 = Axes()
                        icon1 = Icons(2, 'Axes')
                    elif not Sword0 and not Bow0:
                        Axe0 = Axes()
                        icon0 = Icons(1, 'Axes')

                elif spawnmode == 2:
                    if Bow3 or Sword3 or Axe3:
                        Bow4 = Bows()
                        icon4 = Icons(5, 'Bows')
                    elif Bow2 or Sword2 and not Sword3 and not Axe3 or Axe2 and not Axe3 and not Sword3:
                        Bow3 = Bows()
                        icon3 = Icons(4, 'Bows')
                    elif Bow1 or Sword1 and not Sword2 and not Axe2 or Axe1 and not Axe2 and not Sword2:
                        Bow2 = Bows()
                        icon2 = Icons(3, 'Bows')
                    elif Bow0 or Sword0 and not Sword1 and not Axe1 or Axe0 and not Axe1 and not Sword1:
                        Bow1 = Bows()
                        icon1 = Icons(2, 'Bows')
                    elif not Sword0 and not Axe0:
                        Bow0 = Bows()
                        icon0 = Icons(1, 'Bows')

            elif event.key == pygame.K_l:
                already = []
                movev = []
                moveg = []
                speedmap = []
                work = False
                position = 0
                c = 0
            elif event.key == pygame.K_k:
                move = []
                for j in range(len(already)):
                    if j + 1 < len(already):
                        moveg.append(already[j][0] - already[j + 1][0])
                        movev.append(already[j][1] - already[j + 1][1])
                        point = already[j][0], already[j][1]
                        print(maps[point[1]][point[0]])
                        if maps[point[1]][point[0]] == 9:
                            speedmap.append(2)
                        elif maps[point[1]][point[0]] == 1:
                            speedmap.append(0.5)
                        elif maps[point[1]][point[0]] == 3:
                            speedmap.append(0.5)
                        else:
                            speedmap.append(1)

                work = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (100 < event.pos[1] < 199) and event.pos[0] < 200 and len(promove) >= 1:
                try:
                    icon0.change()
                    icon1.back()
                    icon2.back()
                    icon3.back()
                    icon4.back()
                except NameError:
                    pass
                allow = 0

            elif (200 < event.pos[1] < 299) and event.pos[0] < 200 and len(promove) >= 2:
                try:
                    icon1.change()
                    icon0.back()
                    icon2.back()
                    icon3.back()
                    icon4.back()
                except NameError:
                    pass
                allow = 1

            elif (300 < event.pos[1] < 399) and event.pos[0] < 200 and len(promove) >= 3:
                try:
                    icon2.change()
                    icon0.back()
                    icon1.back()
                    icon3.back()
                    icon4.back()
                except NameError:
                    pass
                allow = 2

            elif (400 < event.pos[1] < 499) and event.pos[0] < 200 and len(promove) >= 4:
                try:
                    icon3.change()
                    icon0.back()
                    icon1.back()
                    icon2.back()
                    icon4.back()
                except NameError:
                    pass
                allow = 3

            elif (500 < event.pos[1] < 599) and event.pos[0] < 200 and len(promove) >= 5:
                try:
                    icon4.change()
                    icon0.back()
                    icon1.back()
                    icon2.back()
                    icon3.back()
                except NameError:
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
                except NameError:
                    pass
            elif event.pos[1] > 900 and event.pos[0] > 500:
                spawnmode = 2
                Bowicon.activate()
                Axeicon.back()
                Swordicon.back()
            elif event.pos[1] > 900 and event.pos[0] > 400:
                spawnmode = 1
                Axeicon.activate()
                Bowicon.back()
                Swordicon.back()
            elif event.pos[1] > 900 and event.pos[0] > 300:
                spawnmode = 0
                Swordicon.activate()
                Axeicon.back()
                Bowicon.back()
    try:
        if pygame.mouse.get_pressed()[0] and (event.pos[0] > 300 and event.pos[1] < 900):
            if ((event.pos[0] - 300) // 30, event.pos[1] // 30) not in already:
                already.append(((event.pos[0] - 300) // 30, event.pos[1] // 30))
    except AttributeError:
        pass
    try:
        if work:
            if allow == 0:
                if moveg[position] != 0:
                    if moveg[position] == 1:
                        Sword0.update('left', speedmap[position])
                        c += 1
                    elif moveg[position] == -1:
                        Sword0.update('right', speedmap[position])
                        c += 1

                if movev[position] != 0:
                    if movev[position] == 1:
                        Sword0.update('up', speedmap[position])
                        c += 1
                    elif movev[position] == -1:
                        Sword0.update('down', speedmap[position])
                        c += 1
                if c == 30 // speedmap[position]:
                    c = 0
                    position += 1

    except ValueError:
        print('An error')
    except IndexError:
        pass
    for j in already:
        pygame.draw.rect(screen, (255, 255, 0), (j[0] * 30 + 300, j[1] * 30, 30, 30), 1)

    pygame.display.flip()
clock.tick(60)
pygame.quit()
