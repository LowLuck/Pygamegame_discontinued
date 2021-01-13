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

    def update(self, move):
        if move == '1':
            self.rect[0] -= 1
        elif move == '2':
            self.rect[1] -= 1
        elif move == '3':
            self.rect[0] += 1
        elif move == '4':
            self.rect[1] += 1


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
superlist = []
betterlist = []
mover = []
last1 = 27
last2 = 28
movek = 0
moverv = [0, 0]
moverg = [0, 0]
c = -1
n = 0
chosen = 0
name = 0
made = False
drawer = False
fixer = False
FIX = False
moved = False
allow = -1
promove = []

unitcount = 0

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
                except Exception:
                    pass
                if allow != -1:
                    allow = -1
                else:
                    allow = 0

            elif (200 < event.pos[1] < 299) and event.pos[0] < 200 and len(promove) >= 2:
                try:
                    icon1.change()
                except Exception:
                    pass
                if allow != -1:
                    allow = -1
                else:
                    allow = 1

            elif (300 < event.pos[1] < 399) and event.pos[0] < 200 and len(promove) >= 3:
                try:
                    icon2.change()
                except Exception:
                    pass
                if allow != -1:
                    allow = -1
                else:
                    allow = 2

            elif (400 < event.pos[1] < 499) and event.pos[0] < 200 and len(promove) >= 4:
                try:
                    icon3.change()
                except Exception:
                    pass
                if allow != -1:
                    allow = -1
                else:
                    allow = 3

            elif (500 < event.pos[1] < 599) and event.pos[0] < 200 and len(promove) >= 5:
                try:
                    icon4.change()
                except Exception:
                    pass
                if allow != -1:
                    allow = -1
                else:
                    allow = 4

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2 and allow != -1:
            first = (event.pos[0] - 300) // 30
            second = event.pos[1] // 30
            if warmap[first][second] != 0:
                drawer = True
                print(allow)
                saver = (first, second)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            drawer = False
        if event.type == pygame.MOUSEMOTION and drawer:
            if event.pos[0] > 300:
                first = (event.pos[0] - 300) // 30
                second = event.pos[1] // 30
                if (first * 30 + 300, second * 30) not in superlist and second <= 29:
                    superlist.append((first * 30 + 300, second * 30))
                    betterlist.append((first, second))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                superlist = []
            elif event.key == pygame.K_k and len(promove) >= 1:
                drawer = False
                superlist = []
                f = True
                moverv = []
                moverg = []
                try:
                    newgen = saver[0]
                    newestgen = saver[1]
                except BaseException:
                    pass
                FIX = False
                i = []
                for j in betterlist:
                    if f:
                        i = j
                        f = False
                    else:
                        dif1 = i[0] - j[0]
                        dif2 = i[1] - j[1]
                        i = j
                        moverg.append(dif1)
                        moverv.append(dif2)

                fixer = True

    if fixer and moverg and moverv:
        if moverg[n] == 1:
            if not moved:
                warmap[newgen][newestgen] = 0
                warmap[newgen - 1][newestgen] = 1
                newgen -= 1
                print('left')
                moved = True
            movek = 1
            if not made:
                c = 30
                made = True
        elif moverg[n] == -1:
            movek = 2
            if not moved:
                warmap[newgen][newestgen] = 0
                warmap[newgen + 1][newestgen] = 1
                newgen += 1
                print('right')
                moved = True
            if not made:
                c = 30
                made = True

        if moverv[n] == 1:
            movek = 3
            if not moved:
                warmap[newgen][newestgen] = 0
                warmap[newgen][newestgen - 1] = 1
                newestgen -= 1
                print('up')
                moved = True
            if not made:
                c = 30
                made = True
        elif moverv[n] == -1:
            if not moved:
                warmap[newgen][newestgen] = 0
                warmap[newgen][newestgen + 1] = 1
                newestgen += 1
                print('duwn')
                moved = True
            movek = 4
            if not made:
                c = 30
                made = True

        if movek == 1 and c != 0 and allow == 0:
            Sword0.update('1')
            c -= 1
        if movek == 2 and c != 0 and allow == 0:
            Sword0.update('3')
            c -= 1
        if movek == 3 and c != 0 and allow == 0:
            Sword0.update('2')
            c -= 1
        if movek == 4 and c != 0 and allow == 0:
            Sword0.update('4')
            c -= 1

        if movek == 1 and c != 0 and allow == 1:
            Sword1.update('1')
            c -= 1
        if movek == 2 and c != 0 and allow == 1:
            Sword1.update('3')
            c -= 1
        if movek == 3 and c != 0 and allow == 1:
            Sword1.update('2')
            c -= 1
        if movek == 4 and c != 0 and allow == 1:
            Sword1.update('4')
            c -= 1

        if movek == 1 and c != 0 and allow == 2:
            Sword2.update('1')
            c -= 1
        if movek == 2 and c != 0 and allow == 2:
            Sword2.update('3')
            c -= 1
        if movek == 3 and c != 0 and allow == 2:
            Sword2.update('2')
            c -= 1
        if movek == 4 and c != 0 and allow == 2:
            Sword2.update('4')
            c -= 1

        if movek == 1 and c != 0 and allow == 3:
            Sword3.update('1')
            c -= 1
        if movek == 2 and c != 0 and allow == 3:
            Sword3.update('3')
            c -= 1
        if movek == 3 and c != 0 and allow == 3:
            Sword3.update('2')
            c -= 1
        if movek == 4 and c != 0 and allow == 3:
            Sword3.update('4')
            c -= 1

        if movek == 1 and c != 0 and allow == 4:
            Sword4.update('1')
            c -= 1
        if movek == 2 and c != 0 and allow == 4:
            Sword4.update('3')
            c -= 1
        if movek == 3 and c != 0 and allow == 4:
            Sword4.update('2')
            c -= 1
        if movek == 4 and c != 0 and allow == 4:
            Sword4.update('4')
            c -= 1

        elif c == 0:
            made = False
            moved = False
            movek = 0
            betterlist = []
            if n + 1 < len(moverg):
                n += 1
            else:
                moverg = [0, 0]
                moverv = [0, 0]
                n = 0

                fixer = False

    try:
        for j in superlist:
            firsts = j[0]
            seconds = j[1]
            pygame.draw.rect(screen, (255, 255, 0), (firsts, seconds, 30, 30), 1)
    except Exception:
        pass
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
