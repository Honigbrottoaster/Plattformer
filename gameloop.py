import pygame
import sys
from settings import *

class Player:
    def __init__(self):
        pass

class Floor:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = 50
        self.x_pos = 0
        self.y_pos = SCREEN_HEIGHT - self.height
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

class Platform:
    def __init__(self):
        self.speed = 4
        self.width = 20
        self.height = 50
        self.x_pos = SCREEN_WIDTH - self.width - 50
        self.y_pos = SCREEN_HEIGHT - 100
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def draw(self, game):
        pygame.draw.rect(game.screen, (0, 80, 150), self.rect)

    def move(self):
        self.rect.x -= self.speed

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("2d Platformer")
        self.clock = pygame.time.Clock()

        #plattform
        self.platform = Platform()

        #ground
        self.floor = Floor()

    def run(self):
        self.handleEvents()
        self.draw()
        self.update()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.fill((70, 100, 10))

        self.platform.draw(self)

        pygame.draw.rect(self.screen, "red", self.floor.rect)

    def update(self):
        #platform 
        self.platform.move()

        pygame.display.update()
        self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    while True:
        game.run()