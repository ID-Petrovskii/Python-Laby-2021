import pygame
import random
import yaml
from yaml.loader import SafeLoader
pygame.init()

FPS = 10
brdrx = 512
brdry = 512
R = 50
V = 10
screen = pygame.display.set_mode((brdrx + 2*R, brdry + 3*R))
N_All = 1024 #Число шаров
N = 13 #Число шаров на экране
Time = 500
TimeN = Time #неизменяемое время
Score = 0
ballform = True
Yes = 0
Name = ''
j = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
COLORS = (RED, GREEN, BLUE, YELLOW, PINK)
ALPHABET = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "_", "#")
            


def randomcolors():
    '''
    Функция возвращает случайный цвет, причем такой, что он
    не слишком близок к черному и не слишком близок к белому
    '''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    if r + g + b < 255 or r + g + b > 510:
        r = (r + 255)//3
        g = (g + 255)//3
        b = (b + 255)//3
    col = (r, g, b)
    return col

class Ball:
    '''
    Класс шариков - основных объектов в игре
    '''
    def __init__(self):
        '''
        Функция определяет основные характеристика шарика
        self.x - координата шарика по оси абсцисс
        self.y - координата шарика по оси ординат
        self.vx - скорость шарика по оси абсцисс
        self.vy - скорость шарика по оси ординат
        self.r - радиус шарика
        self.color - цвет шарика
        '''
        self.x = random.randint(2*R, brdrx - R)
        self.y = random.randint(2*R, brdry - R)
        self.vx = random.randint(-V, V)
        self.vy = random.randint(-V, V)
        self.r = random.randint(R//3, R)
        self.color = randomcolors()

    def form(self):
        '''
        Возращает истину, подтверждая шарообразную форму шарика (очев)
        '''
        ballform = True
        return ballform

    def draw(self, surface):
        '''
        Отрисовывает шарик
        '''
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)

    def move(self):
        '''
        Перемещает шарик, увеличивая его координату на величину скорости
        '''
        self.x += self.vx
        self.y += self.vy

    def collision(self):
        '''
        Проверяет не вышел ли шарик за границы поля
        Если да - отражает его от границы
        '''
        ch = 0
        if self.x - self.r < R or self.x + self.r > brdrx + R:
            self.vx = -self.vx
            ch = 1
        elif self.y - self.r < R or self.y + self.r > brdry + R:
            self.vy = -self.vy
            ch = 1
        if ch == 1:
            Ball.move(self)
            Ball.move(self)

    def peresechenie(self, x, y):
        '''
        Проверяет принадлежит ли точка с координатами х, у
        данному объекту. В зависимости от этого возвращает правду или ложь
        х - координата точки по оси абсцисс
        у - координата точки по оси ординат
        '''
        rast2 = (self.x - x)**2 + (self.y - y)**2
        if rast2 < (self.r)**2:
            peresechenie = True
        else:
            peresechenie = False
        return peresechenie

class Square:
    '''
    Класс квадратиков - дополнительных, редких объектов
    '''
    def __init__(self):
        '''
        Функция определяет основные характеристика квадратика
        self.x - координата квадратика по оси абсцисс
        self.y - координата квадратика по оси ординат
        self.vx - скорость квадратика по оси абсцисс
        self.vy - скорость квадратика по оси ординат
        self.r - радиус квадратика
        self.color - цвет квадратика
        self.time - счётчик времени жизни квадратика
        '''
        self.x = random.randint(2*R, brdrx - R)
        self.y = random.randint(2*R, brdry - R)
        self.vx = random.randint(-V, V)
        self.vy = random.randint(-V, V)
        self.r = random.randint(R//3, R)
        self.color = randomcolors()
        self.time = 0

    def form(self):
        '''
        Возращает ложь, так как квадратик не шарообразной формы (очев)
        '''
        ballform = False
        return ballform

    def draw(self, surface):
        '''
        Отрисовывает квадратик
        '''
        self.ancolor = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        pygame.draw.line(surface, BLACK, (self.x, self.y), (R, R))
        pygame.draw.line(surface, BLACK, (self.x, self.y), (R, R + brdry))
        pygame.draw.line(surface, BLACK, (self.x, self.y), (R + brdrx, R))
        pygame.draw.line(surface, BLACK, (self.x, self.y), (R + brdrx, R + brdry))
        pygame.draw.rect(surface, self.color, (self.x - self.r, self.y - self.r, 2*self.r, 2*self.r))
        pygame.draw.rect(surface, self.ancolor, (self.x - 3/4*self.r, self.y - 3/4*self.r, 3/2*self.r, 3/2*self.r))
        pygame.draw.rect(surface, self.color, (self.x - 1/2*self.r, self.y - 1/2*self.r, self.r, self.r))
        pygame.draw.rect(surface, self.ancolor, (self.x - 1/4*self.r, self.y - 1/4*self.r, 1/2*self.r, 1/2*self.r))
        

    def move(self):
        '''
        Перемещает квадратик, увеличивая его координату на величину скорости
        Так же увеличивает значение счётчика времени и если он достигает
        достаточно больших значени - обнуляется и квадратик телепортируется,
        меняя скорость
        '''
        self.x += self.vx
        self.y += self.vy
        self.time += 1
        if self.time > 7:
            self.time = 0
            self.x = random.randint(2*R, brdrx - R)
            self.y = random.randint(2*R, brdry - R)
            self.vx = random.randint(-V, V)
            self.vy = random.randint(-V, V)
            
        

    def collision(self):
        '''
        Проверяет не вышел ли квадратик за границы поля
        Если да - отражает его от границы
        '''
        ch = 0
        if self.x - self.r < R or self.x + self.r > brdrx + R:
            self.vx = -self.vx
            ch = 1
        elif self.y - self.r < R or self.y + self.r > brdry + R:
            self.vy = -self.vy
            ch = 1
        if ch == 1:
            Square.move(self)

    def peresechenie(self, x, y):
        '''
        Проверяет принадлежит ли точка с координатами х, у
        данному объекту. В зависимости от этого возвращает правду или ложь
        х - координата точки по оси абсцисс
        у - координата точки по оси ординат
        '''
        if -self.r < x - self.x < self.r and -self.r < y - self.y < self.r:
            peresechenie = True
        else:
            peresechenie = False
        return peresechenie

def update_records(recordlist):
    '''
    Обновляет переданный в функцию список, сортируя его по уменьшению
    значений очков в данном элементе списка
    recordlist - сортируемый список
    '''
    for i in range(len(recordlist)):
        for j in range(len(recordlist) - 1):
            if recordlist[j]['points'] < recordlist[j + 1]['points']:
                   table = recordlist[j]
                   recordlist[j] = recordlist[j + 1]
                   recordlist[j + 1] = table
    

pool_All = []
for j in range(N_All):
    if j%20 == 20 - 1:
        pool_All.append(Square())
    else:
        pool_All.append(Ball())

pool = []
for j in range(N):
    pool.append(pool_All[0])
    pool_All.pop(0)

with open("data.yaml", 'r') as f:
    loaded = yaml.load(f, Loader = SafeLoader)


clock = pygame.time.Clock()
finished = False
Start = False
Finish = False

while not Start:
    pygame.draw.rect(screen, WHITE, (0, 0, brdrx + 2*R, brdry + 3*R))
    pygame.draw.rect(screen, BLACK, (R, R, brdrx, brdry), 1)
    f3 = pygame.font.Font(None, 70)
    text3 = f3.render('Enter your name:', True,(0, 0, 0))
    f4 = pygame.font.Font(None, 70)
    text4 = f4.render(Name, True,(0, 0, 0))
    screen.blit(text3, (R + 0.1*brdrx, R + 0.25*brdry))
    screen.blit(text4, (R + 0.1*brdrx, R + 0.25*brdry + 70*2))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and len(Name) > 2:
                Start = True
            elif event.key == pygame.K_BACKSPACE:
                Name = Name[:-1]
            elif len(Name) < 14 and (event.unicode in ALPHABET):
                Name += event.unicode

while not Finish:
    pygame.draw.rect(screen, WHITE, (0, 0, brdrx + 2*R, brdry + 3*R))
    pygame.draw.rect(screen, BLACK, (R, R, brdrx, brdry), 1)
    if Time < 1:
        Finish = True
    elif len(pool) < 1:
        Finish = True
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in pool:
                    if i.peresechenie(event.pos[0], event.pos[1]) == True:
                        if i.form():
                            Score += 1
                        else:
                            Score += 33
                            Yes = 5
                            Yesx = event.pos[0]
                            Yesy = event.pos[1]
                        pool.remove(i)
                        if len(pool_All) > 0:
                            pool.append(pool_All[0])
                            pool_All.pop(0)
                        
    pygame.draw.rect(screen, BLUE, (R, R/4, brdrx * Time / TimeN, R/2))
    f1 = pygame.font.Font(None, R)
    text1 = f1.render('Score: ' + str(Score), True,(0, 0, 0))
    screen.blit(text1, (R, 1.5*R + brdry))
    for i in pool:
        i.draw(screen)
        i.collision()
        i.move()
    if Yes > 0:
        f3 = pygame.font.Font(None, R)
        text3 = f3.render('Yes!', True,(0, 0, 0))
        screen.blit(text3, (Yesx - R/2, Yesy - R/2))
    Time -= 1
    Yes -= 1
    pygame.display.update()


loaded['results'].append({'name': Name, 'points': Score})
update_records(loaded['results'])

with open("data.yaml", 'w') as f:
    yaml.dump(loaded, f)

while not finished:
    pygame.draw.rect(screen, WHITE, (0, 0, brdrx + 2*R, brdry + 3*R))
    pygame.draw.rect(screen, BLACK, (R, R, brdrx, brdry), 1)
    pygame.draw.circle(screen, RED, (0.5*R + brdrx, 0.5*R), 0.25*R)

                   
    f2 = pygame.font.Font(None, 50)
    text2 = f2.render('Your Score: ' + str(Score), True,(0, 0, 0))
    screen.blit(text2, (R + 0.25*brdrx, R + 0.1*brdry))
    text3 = f2.render('Top-5 records:', True,(0, 0, 0))
    screen.blit(text3, (R + 0.25*brdrx, R + 0.1*brdry + 80))
    for i in range(5):
        fresult = pygame.font.Font(None, 40)
        textresult = fresult.render(str(loaded['results'][i]['name']) + ': ' + str(loaded['results'][i]['points']), True, (0, 0, 0))
        screen.blit(textresult, (R + 0.25*brdrx, R + 0.1*brdry + 130 + 50*i))
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 0.25*R + brdrx < event.pos[0] < 0.75*R + brdrx and 0.25*R < event.pos[1] < 0.75*R:
                    finished = True

pygame.quit()
