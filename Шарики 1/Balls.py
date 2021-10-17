import pygame
import random
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

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
COLORS = [RED, GREEN, BLUE, YELLOW, PINK]

def randomcolors():
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
    def __init__(self):
        self.x = random.randint(2*R, brdrx - R)
        self.y = random.randint(2*R, brdry - R)
        self.vx = random.randint(-V, V)
        self.vy = random.randint(-V, V)
        self.r = random.randint(R//3, R)
        self.color = randomcolors()

    def form(self):
        ballform = True
        return ballform

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def collision(self):
        ch = 0
        if self.x - self.r < R or self.x + self.r > brdrx + R:
            self.vx = -self.vx
            ch = 1
        elif self.y - self.r < R or self.y + self.r > brdry + R:
            self.vy = -self.vy
            ch = 1
        if ch == 1:
            Ball.move(self)

    def peresechenie(self, x, y):
        rast2 = (self.x - x)**2 + (self.y - y)**2
        if rast2 < (self.r)**2:
            peresechenie = True
        else:
            peresechenie = False
        return peresechenie

class Square:
    def __init__(self):
        self.x = random.randint(2*R, brdrx - R)
        self.y = random.randint(2*R, brdry - R)
        self.vx = random.randint(-V, V)
        self.vy = random.randint(-V, V)
        self.r = random.randint(R//3, R)
        self.color = randomcolors()
        self.time = 0

    def form(self):
        ballform = False
        return ballform

    def draw(self, surface):
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
        if -self.r < x - self.x < self.r and -self.r < y - self.y < self.r:
            peresechenie = True
        else:
            peresechenie = False
        return peresechenie

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


clock = pygame.time.Clock()
finished = False
Start = False
Finish = False

while not Start:
    pygame.draw.rect(screen, WHITE, (0, 0, brdrx + 2*R, brdry + 3*R))
    pygame.draw.rect(screen, BLACK, (R, R, brdrx, brdry), 1)
    pygame.draw.polygon(screen, BLACK, ((R + 1.211*brdrx/3, R + brdry/3), (R + 1.211*brdrx/3, R + 2*brdry/3), (R + 1.943*brdrx/3, R + brdry/2)))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if R < event.pos[0] < R + brdrx and R < event.pos[1] < R + brdry:
                    Start = True

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

while not finished:
    pygame.draw.rect(screen, WHITE, (0, 0, brdrx + 2*R, brdry + 3*R))
    pygame.draw.rect(screen, BLACK, (R, R, brdrx, brdry), 1)
    pygame.draw.circle(screen, RED, (0.5*R + brdrx, 0.5*R), 0.25*R)
    f2 = pygame.font.Font(None, 80)
    text2 = f2.render('Score: ' + str(Score), True,(0, 0, 0))
    screen.blit(text2, (R + 0.25*brdrx, R + 0.45*brdry))
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
