# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

import pygame


import random as rdm


def uptdate_screen() -> None:
    pygame.display.flip()


class Balle:

    def __init__(self, screen: pygame.Surface) -> None:
        self.x = rdm.randint(0, screen.get_width())
        self.y = rdm.randint(0, screen.get_height())
        self.screen = screen
        self.color = None
        self.change_color()
        self.radius = 30
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

    def afficher(self) -> str:
        return_val = "screen : {}\nCouleur : {}\n radius : {}\nx : {}" \
            "\ny : {}\ngo_up : {}\ngo_left : {}".format(
                self.get_screen(),
                self.get_radius(),
                self.get_x(),
                self.get_y(),
                self.get_go_up(),
                self.get_go_left()
                )
        return return_val

    def give_random_color(self) -> tuple:
        return (rdm.randint(0, 255), rdm.randint(0, 255), rdm.randint(0, 255))

    def change_color(self) -> None:
        self.color = self.give_random_color()

    def display(self) -> None:
        pygame.draw.circle(
            self.get_screen(),
            self.get_color(),
            (self.get_x(), self.y),
            self.get_radius()
            )

    def move(self) -> None:
        self.x = self.get_x() + (1, -4)[self.get_go_left()]
        self.y = self.get_y() + (1, -4)[self.get_go_up()]
        self.rebound()

    def rebound(self) -> None:
        if self.get_y() >= self.screen.get_height():
            self.go_up = True
            self.change_color()

        elif self.get_y() < 0:
            self.go_up = False
            self.change_color()

        if self.get_x() >= self.screen.get_width():
            self.go_left = True
            self.change_color()

        elif self.get_x() < 0:
            self.go_left = False
            self.change_color()

    def set_coord(self, new_coord: tuple) -> None:
        x, y = new_coord
        self.x = x
        self.y = y


class Jeu:

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.balles = []
        self.run = True
        self.add_balle()

    def get_screen(self) -> pygame.Surface:
        return self.screen

    def get_balles(self, k: int = None) -> list or Balle:
        if k is not None:
            return_val = self.balles[k]
        else:
            return_val = self.balles
        return return_val

    def get_run(self) -> bool:
        return self.run

    def add_balle(self) -> None:
        self.get_balles().append(Balle(self.get_screen()))
        print("+1\ttotal = ", len(self.get_balles()))

    def remove_balle(self, k: int = 0) -> None:
        self.get_balles().pop(k)


    def move_and_display(self) -> None:
        for balle in self.get_balles():
            balle: Balle
            balle.move()
            balle.display()

    def move(self) -> None:
        for balle in self.get_balles():
            balle: Balle
            balle.move()

    def display(self) -> None:
        for balle in self.get_balles():
            balle: Balle
            balle.display()

    def keep_only_one(self):
        print("______reset______")
        self.balles = []
        self.add_balle()

    def stop_while(self) -> None:
        self.run = False


# début de l'application:
pygame.init()

# paramètres de la fenêtre:
pygame.display.set_caption("for Earth")
format_screen = (1200, 650)
screen = pygame.display.set_mode(format_screen)

game = Jeu(screen)
balle1 = Balle(screen)

while game.get_run():
    # display background
    screen.fill((100, 100, 100))
    # déplace et affiche les balles les balles
    game.move_and_display()
    # mise à jour de l'écran
    uptdate_screen()
    # on balaye les evénement de la page
    for event in pygame.event.get():
        # si la croix rouge
        if event.type == pygame.QUIT:
            # on arrète la boucle
            game.stop_while()
        # sinon si une est préssée et que c'est échap on arrète aussi la boucle
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.stop_while()
            elif event.key == pygame.K_RETURN:
                game.add_balle()
            elif event.key == pygame.K_a:
                game.keep_only_one()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                game.get_balles(
                    rdm.randint(0, len(game.get_balles()) - 1)
                    ).set_coord(event.pos)
            elif event.button == 2 or 3:
                game.add_balle()


# on quitte la fenêtre
pygame.quit()
