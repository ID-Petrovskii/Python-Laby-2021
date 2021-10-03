import pygame
import math
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((556, 787))

def ch(V, ch, k):
    return int(k*(V+ch))

def iglu(dx, dy, k):
    circle(screen, (225, 225, 225), (ch(174, dx, k), ch(454, dy, k)), ch(132, 0, k))
    circle(screen, (0, 0, 0), (ch(174, dx, k), ch(454, dy, k)), ch(132, 0, k), 2)
    if ch(454, dy, k)+ch(132, 0, k) <= 352:
        rect(screen, (225, 225, 225), (ch(42, dx, k), ch(454, dy, k), ch(264, 0, k), ch(132, 0, k)))
    elif ch(454, dy, k) >= 352:
        rect(screen, (255, 255, 255), (ch(42, dx, k), ch(454, dy, k), ch(264, 0, k), ch(132, 0, k)))
    else:
        rect(screen, (225, 225, 225), (ch(42, dx, k), ch(454, dy, k), ch(264, 0, k), 352 - (ch(454, dy, k))))
        rect(screen, (255, 255, 255), (ch(42, dx, k), 352, ch(264, 0, k), ch(132, 0, k) - 352 + (ch(454, dy, k))))
    line(screen, (0, 0, 0), (ch(42, dx, k), ch(454, dy, k)), (ch(306, dx, k), ch(454, dy, k)))
    line(screen, (0, 0, 0), (ch(54, dx, k), ch(398, dy, k)), (ch(292, dx, k), ch(398, dy, k)))
    line(screen, (0, 0, 0), (ch(79, dx, k), ch(362, dy, k)), (ch(267, dx, k), ch(362, dy, k)))
    line(screen, (0, 0, 0), (ch(118, dx, k), ch(335, dy, k)), (ch(230, dx, k), ch(335, dy, k)))
    line(screen, (0, 0, 0), (ch(183, dx, k), ch(323, dy, k)), (ch(183, dx, k), ch(335, dy, k)))
    line(screen, (0, 0, 0), (ch(135, dx, k), ch(335, dy, k)), (ch(135, dx, k), ch(362, dy, k)))
    line(screen, (0, 0, 0), (ch(177, dx, k), ch(335, dy, k)), (ch(177, dx, k), ch(362, dy, k)))
    line(screen, (0, 0, 0), (ch(218, dx, k), ch(335, dy, k)), (ch(218, dx, k), ch(362, dy, k)))
    line(screen, (0, 0, 0), (ch(103, dx, k), ch(362, dy, k)), (ch(103, dx, k), ch(398, dy, k)))
    line(screen, (0, 0, 0), (ch(160, dx, k), ch(362, dy, k)), (ch(160, dx, k), ch(398, dy, k)))
    line(screen, (0, 0, 0), (ch(211, dx, k), ch(362, dy, k)), (ch(211, dx, k), ch(398, dy, k)))
    line(screen, (0, 0, 0), (ch(256, dx, k), ch(362, dy, k)), (ch(256, dx, k), ch(398, dy, k)))
    line(screen, (0, 0, 0), (ch(67, dx, k), ch(398, dy, k)), (ch(67, dx, k), ch(454, dy, k)))
    line(screen, (0, 0, 0), (ch(130, dx, k), ch(398, dy, k)), (ch(130, dx, k), ch(454, dy, k)))
    line(screen, (0, 0, 0), (ch(193, dx, k), ch(398, dy, k)), (ch(193, dx, k), ch(454, dy, k)))
    line(screen, (0, 0, 0), (ch(242, dx, k), ch(398, dy, k)), (ch(242, dx, k), ch(454, dy, k)))
    line(screen, (0, 0, 0), (ch(288, dx, k), ch(398, dy, k)), (ch(288, dx, k), ch(454, dy, k)))

def cat(dx, dy):
    #koshka (cat) telo
    ellipse(screen, (200, 200, 200), (83+dx, 589+dy, 100, 25))
    ellipse(screen, (200, 200, 200), (49+dx, 604+dy, 60, 10))
    polygon(screen, (200, 200, 200), [(102+dx, 612+dy), (91+dx, 616+dy), (82+dx, 618+dy), (75+dx, 620+dy), (61+dx, 626+dy), (61+dx, 628+dy), (81+dx, 628+dy), (101+dx, 623+dy), (113+dx, 620+dy), (120+dx, 616+dy), (121+dx, 611+dy)])
    polygon(screen, (200, 200, 200), [(152+dx, 613+dy), (166+dx, 625+dy), (179+dx, 633+dy), (198+dx, 642+dy), (201+dx, 642+dy), (201+dx, 639+dy), (191+dx, 630+dy), (177+dx, 620+dy), (166+dx, 613+dy), (163+dx, 610+dy)])
    polygon(screen, (200, 200, 200), [(170+dx, 609+dy), (188+dx, 619+dy), (211+dx, 628+dy), (219+dx, 628+dy), (219+dx, 626+dy), (209+dx, 619+dy), (194+dx, 611+dy), (183+dx, 607+dy), (179+dx, 605+dy)])
    polygon(screen, (200, 200, 200), [(182+dx, 604+dy), (197+dx, 602+dy), (212+dx, 596+dy), (235+dx, 586+dy), (251+dx, 574+dy), (251+dx, 571+dy), (243+dx, 571+dy), (225+dx, 576+dy), (208+dx, 583+dy), (195+dx, 589+dy), (181+dx, 597+dy), (179+dx, 600+dy)])
    #rybka (fish)
    polygon(screen, (147, 172, 167), [(68+dx, 580+dy), (88+dx, 586+dy), (100+dx, 600+dy), (115+dx, 600+dy), (111+dx, 609+dy), (100+dx, 600+dy), (79+dx, 594+dy)])
    polygon(screen, (0, 0, 0), [(68+dx, 580+dy), (88+dx, 586+dy), (100+dx, 600+dy), (115+dx, 600+dy), (111+dx, 609+dy), (100+dx, 600+dy), (79+dx, 594+dy)], 1)
    polygon(screen, (213, 95, 95), [(74+dx, 590+dy), (73+dx, 593+dy), (86+dx, 604+dy), (81+dx, 595+dy)])
    polygon(screen, (0, 0, 0), [(74+dx, 590+dy), (73+dx, 593+dy), (86+dx, 604+dy), (81+dx, 595+dy)], 1)
    polygon(screen, (213, 95, 95), [(82+dx, 583+dy), (77+dx, 577+dy), (91+dx, 578+dy), (86+dx, 584+dy)])
    polygon(screen, (0, 0, 0), [(82+dx, 583+dy), (77+dx, 577+dy), (91+dx, 578+dy), (86+dx, 584+dy)], 1)
    circle(screen, (0, 0, 255), (78+dx, 587+dy), 3)
    circle(screen, (0, 0, 0), (78+dx, 587+dy), 1)
    #koshka (cat) golova
    ellipse(screen, (200, 200, 200), (83+dx, 574+dy, 32, 20))
    polygon(screen, (200, 200, 200), [(93+dx, 574+dy), (94+dx, 569+dy), (100+dx, 574+dy), (106+dx, 574+dy), (110+dx, 570+dy), (113+dx, 580+dy)])
    ellipse(screen, (255, 255, 255), (85+dx, 577+dy, 8, 5))
    ellipse(screen, (255, 255, 255), (96+dx, 579+dy, 8, 5))
    ellipse(screen, (0, 0, 0), (89+dx, 579+dy, 4, 3))
    ellipse(screen, (0, 0, 0), (100+dx, 580+dy, 4, 3))
    ellipse(screen, (0, 0, 0), (88+dx, 586+dy, 3, 2))
    line(screen, (255, 255, 255), (85+dx, 589+dy), (85+dx, 592+dy), 2)
    line(screen, (255, 255, 255), (92+dx, 591+dy), (92+dx, 594+dy), 2)

def eskimos(dx, dy, k):
    ellipse(screen, (227, 222, 219), (ch(393, dx, k), ch(423, dy, k), 95*k, 59*k))
    ellipse(screen, (145, 124, 111), (ch(365, dx, k), ch(488, dy, k), 60*k, 17*k))
    polygon(screen, (145, 124, 111), [(ch(472, dx, k), ch(488, dy, k)), (ch(477, dx, k), ch(489, dy, k)), (ch(490, dx, k), ch(496, dy, k)),
                                      (ch(501, dx, k), ch(505, dy, k)), (ch(509, dx, k), ch(515, dy, k)), (ch(509, dx, k), ch(520, dy, k)), (ch(505, dx, k),
                                        ch(522, dy, k)), (ch(498, dx, k), ch(520, dy, k)), (ch(489, dx, k), ch(517, dy, k)), (ch(482, dx, k), ch(512, dy, k))])
    ellipse(screen, (145, 124, 111), (ch(394, dx, k), ch(577, dy, k), 36*k, 14*k))
    ellipse(screen, (145, 124, 111), (ch(457, dx, k), ch(580, dy, k), 36*k, 12*k))
    ellipse(screen, (145, 124, 111), (ch(408, dx, k), ch(543, dy, k), 25*k, 45*k))
    ellipse(screen, (145, 124, 111), (ch(452, dx, k), ch(543, dy, k), 29*k, 45*k))
    polygon(screen, (145, 124, 111), [(ch(388, dx, k), ch(565, dy, k)), (ch(388, dx, k), ch(553, dy, k)), (ch(390, dx, k), ch(541, dy, k)), (ch(393, dx, k), ch(526, dy, k)),
                                      (ch(396, dx, k), ch(511, dy, k)), (ch(399, dx, k), ch(500, dy, k)), (ch(405, dx, k), ch(486, dy, k)), (ch(410, dx, k), ch(477, dy, k)),
                                      (ch(414, dx, k), ch(470, dy, k)), (ch(463, dx, k), ch(472, dy, k)), (ch(471, dx, k), ch(479, dy, k)), (ch(477, dx, k), ch(489, dy, k)),
                                      (ch(489, dx, k), ch(516, dy, k)), (ch(492, dx, k), ch(529, dy, k)), (ch(495, dx, k), ch(544, dy, k)), (ch(496, dx, k), ch(565, dy, k))])
    rect(screen, (108, 93, 83), (ch(388, dx, k), ch(553, dy, k), 110*k, 12*k))
    rect(screen, (108, 93, 83), (ch(427, dx, k), ch(478, dy, k), 26*k, 73*k))
    ellipse(screen, (172, 157, 147), (ch(405, dx, k), ch(432, dy, k), 71*k, 44*k))
    ellipse(screen, (227, 219, 219), (ch(416, dx, k), ch(442, dy, k), 49*k, 31*k))
    line(screen, (0, 0, 0), (ch(421, dx, k), ch(451, dy, k)), (ch(433, dx, k), ch(455, dy, k)))
    line(screen, (0, 0, 0), (ch(445, dx, k), ch(455, dy, k)), (ch(458, dx, k), ch(453, dy, k)))
    lines(screen, (0, 0, 0), 0, [(ch(432, dx, k), ch(466, dy, k)), (ch(436, dx, k), ch(464, dy, k)), (ch(447, dx, k), ch(464, dy, k)), (ch(454, dx, k), ch(467, dy, k))])
    line(screen, (0, 0, 0), (ch(373, dx, k), ch(579, dy, k)), (ch(373, dx, k), ch(427, dy, k)))


rect(screen, (255, 255, 255), (0, 0, 556, 787))
rect(screen, (225, 225, 225), (0, 0, 556, 352))

iglu(-15, 500, 0.4)
iglu(600, 550, 0.4)
iglu(0, 0, 1)
iglu(-10, 410, 0.6)
iglu(200, 450, 0.6)

cat(100, 0)
cat(-150, 20)
cat(-20, 100)
cat(200, 170)
cat(395, 145)

eskimos(10, 50, 1)
eskimos(1000, 725, 0.3)
eskimos(1250, 760, 0.3)
eskimos(1080, 800, 0.3)
eskimos(1000, 925, 0.3)
eskimos(1200, 930, 0.3)
eskimos(800, 890, 0.3)
eskimos(735, 1100, 0.3)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
