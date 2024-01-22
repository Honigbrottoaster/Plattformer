import pygame
import sys
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Farming Simulator 2D")
        self.clock = pygame.time.Clock()

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
        self.screen.fill((70, 255, 10))

    def update(self):
        pygame.display.update()
        self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    while True:
        game.run()