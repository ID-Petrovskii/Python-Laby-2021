import math
from random import choice
from random import randint

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

n_balls = 0
g = 1
score = 0
text_time = 0


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.vy != 0 or self.y < HEIGHT - self.r - 1 :
            self.vy += g
        elif self.vx != 0:
            self.vx *= 0.97
            if self.vx**2 < 1:
                self.vx = 0
        else:
            self.live -= 1
            if self.live < 1:
                balls.remove(self)
        self.x += self.vx
        self.y += self.vy
        if self.x < 1 or self.x > WIDTH - 1:
            self.vx *= -1
            self.x += self.vx
            self.y += self.vy
        elif self.y > HEIGHT - self.r - 1:
            if self.vy**2 < 1:
                self.vy = 0
            self.vy *= -0.5
           

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r,
            1
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        r = math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)
        if self.r + obj.r > r:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = BLACK

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        if event.pos[0] != new_ball.x:
            self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        elif (event.pos[1]-new_ball.y) > 0:
            self.an = math.pi/2
        else:
            self.an = math.pi/2
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] != 20:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
            elif (event.pos[1]-450) > 0: 
                self.an = math.pi/2
            else:
                self.an = -math.pi/2
        if self.f2_on:
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self):
        Surface_for_Gun = pygame.Surface((100, 5))
        Surface_for_Gun.set_colorkey(WHITE)
        pygame.draw.rect(Surface_for_Gun, WHITE, (0, 0, 100, 5))
        pygame.draw.rect(Surface_for_Gun, self.color, (0, 0, self.f2_power, 5))
        Surface_for_Gun = pygame.transform.rotate(Surface_for_Gun, -self.an*180/math.pi)
        if self.an > 0:
            screen.blit(Surface_for_Gun, (40, 450))
        else:
            screen.blit(Surface_for_Gun, (40, 450 - Surface_for_Gun.get_height()))
        

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = YELLOW
        else:
            self.color = BLACK


class Target:

    def __init__(self):
        """ Инициализация новой цели. """
        self.screen = screen
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.vx = randint(0, 5)
        self.vy = randint(0, 5)
        self.r = randint(2, 50)
        self.color = RED
        self.live = 1
        self.points = 0

    def move(self):
        if self.x + self.vx > 780 or self.x + self.vx < 600:
            self.vx *= -1
        if self.y + self.vy > 550 or self.y + self.vy < 300:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy
        

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def new_target(self):
        self.__init__()

    def score(self):
        return self.points
    
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r,
            1
        )


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
targets = [Target()]
targets.append(Target())
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for t in targets:
        t.draw()
    for b in balls:
        b.draw()
    f1 = pygame.font.Font(None, 30)
    text1 = f1.render(str(score), True, (0, 0, 0))
    screen.blit(text1, (10, 10))
    if text_time > 0:
        text_time -= 1
        f2 = pygame.font.Font(None, 30)
        text2 = f2.render("Вы уничтожили цель за " + str(text) + " выстрелов", True, (0, 0, 0))
        screen.blit(text2, (WIDTH//4, HEIGHT//2 - 30))
    
    pygame.display.update()

    

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
            n_balls += 1
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for t in targets:
        t.move()

    for b in balls:
        b.move()
        for t in targets:
            if b.hittest(t) and t.live:
                t.live = 0
                t.hit()
                t.new_target()
                score += 1
                text = n_balls
                n_balls = 0
                text_time = 30
    gun.power_up()

pygame.quit()
