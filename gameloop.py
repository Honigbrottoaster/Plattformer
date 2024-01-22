import pygame
import sys
from settings import *

class Player:
    def __init__(self, floor):
        self.width = 30
        self.height = 50
        self.x_pos = 100
        self.y_pos = SCREEN_HEIGHT - floor.height - self.height
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.on_ground = True
        self.gravity = 0.4
        self.jump_force = 10
        self.y_input = 0
    
    def get_onGround(self, floor):
        if self.rect.colliderect(floor.rect):
            self.on_ground = True
        else:
            self.on_ground = False
    
    def move(self):
        self.rect.y += self.y_input

        self.get_onGround(game.floor)

        if not self.on_ground:
            self.y_input += self.gravity
        else:
            self.y_input = 0

    def jump(self):
        if self.on_ground:
            self.y_input = -self.jump_force

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
        if self.rect.x <= -self.width:
            self.rect.x = SCREEN_WIDTH + 2

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

        #player
        self.player = Player(self.floor)

    def run(self):
        self.handleEvents()
        self.update()
        self.draw() 

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def draw(self):
        self.screen.fill((70, 100, 10))

        self.platform.draw(self)

        pygame.draw.ellipse(self.screen, "black", self.player.rect)

        pygame.draw.rect(self.screen, "red", self.floor.rect)

    def update(self):
        #platform 
        self.platform.move()

        #player
        self.player.get_onGround(self.floor)
        self.player.move()

        pygame.display.update()
        self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    while True:
        game.run()