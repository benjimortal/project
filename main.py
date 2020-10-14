import pygame
import random


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
WHEAT = (245, 222, 179)
LAVENDER = (230, 230, 250)
ALICEBLUE = (240, 248, 255)
SNOW = (255, 250, 250)

screen_width = 800
screen_height = 600

background = pygame.image.load("background.png")
icon = pygame.image.load("monster.png")
pygame.display.set_icon(icon)



class Ball:
    def __init__(self,x, y, x_step, y_step, color, radius, screen):
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        self.color = color
        self.radius = radius
        self.screen = screen


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y),self.radius)


        if self.x < 0 + self.radius:
            self.x_step = 1
        if self.x > 800 - self.radius:
            self.x_step = -1

class Enemy:
    def __init__(self, x, y, x_step, y_step, color, radius, screen):
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        self.color = color
        self.radius = radius
        self.screen = screen


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y),self.radius)

    def move(self):
        #self.x += self.x_step
        self.y += self.y_step

        if self.y >= screen_height - self.radius or self.y < self.radius:
            self.y_step *= -1

        if self.y <= 0 - self.radius:
            self.y_step *= -1
        #if self.y < 0 + self.radius:
           # self.y_step *= -1
def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    running = True
    colors = [RED, GREEN, BLUE, SNOW, ALICEBLUE, LAVENDER, WHEAT, PINK]
    pygame.display.set_caption("Beyond The Nowhere...")
    ball = Ball(400, 550, -1, 1, random.choice(colors), 20, screen)


    enemys = []
    for _ in range(10):
        x = random.randrange(10, screen_width - 20)
        y = random.randrange(10, screen_height - 20)
        x_step = random.choice([-3, -2, -1, 1, 2, 3])
        y_step = random.choice([-3, -2, -1, 1, 2, 3])
        color = random.choice(colors)
        radius = 20  # or just add radius = 20
        enemy = Enemy(x, y, x_step, y_step, color, radius, screen)
        enemys.append(enemy)



    while running:
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    ball.x = mouse_x
                    ball.y = mouse_y


        screen.blit(background, (0, 0))
        for enemy in enemys:
            enemy.draw()
            enemy.move()
        ball.draw()
        #pygame.draw.circle(screen, RED, (370, 520), 20)
        pygame.display.update()
        clock.tick(90)


if __name__ == '__main__':
    main()
