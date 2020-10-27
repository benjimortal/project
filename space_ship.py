from setting import *
class Spaceship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health

    def draw(self, screen):
        screen.blit(self.ship_img, (self.x, self.y))

class Player(Spaceship):
    def __init__(self, x, y, health = 100):
        super(). __init__(x, y , health)
        self.ship_img = player_img
        self.laser_img = bullet
        self.mask = pygame.mask.from_surface(self.ship_img)  #mask is pixel perfet collision
        self.max_health = health
