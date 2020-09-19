# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

import pygame


import random as rdm


class Balle:

    def __init__(self,
                 screen,
                 x: int,
                 y: int,
                 color: tuple) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen
        self.radius = 34
        self.go_up = False
        self.go_left = False

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_color(self) -> str:
        return self.color

    def get_radius(self) -> int:
        return self.radius

    def get_go_up(self) -> bool:
        return self.go_up
    
    def get_go_left(self) -> bool:
        return self.go_left

    def get_screen(self) -> pygame.Surface:
        return self.screen

    def get_image(self) -> pygame.Surface:
        return self.image

    def print_ball(self) -> None:
        pygame.draw.circle(
                self.get_screen(),
                self.get_color(),
                (
                        self.get_x(),
                        self.get_y()
                    ),
                3
            )

    def move(self) -> None:
        
        def f(self, x: int) -> int:
            assert 0 < x < 1200, "x not valuable"
            y = 4
            print("x =", x, "f(x) =", y)
            assert 0 < y < 650, "y not valueable"
            return y
        
        value_x = self.get_x() + (3, -3)[self.get_go_left()]
        value_y = f(self, value_x)
        self.rebound(value_x, value_y)
        self.x = value_x
        self.y = value_y

    def rebound(self, new_x: int, new_y: int) -> None:
        if new_y + self.get_radius() >= self.screen.get_height() \
                or new_y <= 0:
            self.go_up = not(self.get_go_up())
        elif new_x + self.get_radius() >= self.screen.get_width() \
                or new_x <= 0:
            self.go_left = not(self.get_go_left())
            print(self.get_go_left())


# début de l'application:
pygame.init()

# paramètres de la fenêtre:
pygame.display.set_caption("for Earth")
format_screen = (1200, 650)
screen = pygame.display.set_mode(format_screen)

balle_1: Balle = Balle(screen, 203, 323, (0, 255, 255))

run = True

while run:
    screen.fill((0, 0, 120))
    balle_1.print_ball()
    balle_1.move()
    print(balle_1.get_color(), balle_1.get_color(), balle_1.get_x(), balle_1.get_y())
    pygame.draw.circle(
                screen,
                balle_1.get_color(),
                (
                        balle_1.get_x(),
                        balle_1.get_y()
                    ),
                3
            )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
pygame.quit()
