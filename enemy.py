from setting import *

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
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.y += self.y_step

        if self.y >= screen_height:
            self.x = random.randrange(self.radius, screen_width - self.radius)
            self.y = -self.radius


