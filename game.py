from enemy import Enemy
from space_ship import Spaceship, Player
from setting import *

class Game:
    def __init__(self):
        pygame.init()
        keep_alive = True
        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        player = Player(400, 500)

        enemies = []
        for _ in range(20):
            x = random.randrange(10, screen_width - 20)
            y = random.randrange(10, screen_height - 20)
            x_step = random.choice([-3, -2, -1, 1, 2, 3])
            y_step = random.choice([1, 2, 3])
            color = random.choice(colors)
            radius = 15
            enemy = Enemy(x, y, x_step, y_step, color, radius, screen)
            enemies.append(enemy)

        keep_alive = True
        while keep_alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_alive = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player.x - player_speed >= -5:
                player.x -= player_speed
            if keys[pygame.K_d] and player.x + player_speed + 55 < screen_width:
                player.x += player_speed
            if keys[pygame.K_w] and player.y - player_speed > 0:
                player.y -= player_speed
            if keys[pygame.K_s] and player.y + player_speed + 65 < screen_height:
                player.y += player_speed

            screen.blit(BG, (0, 0))
            for enemy in enemies:
                enemy.draw()
                enemy.move()
            player.draw(screen)

            screen.blit(lives_label, (10, 10))
            screen.blit(levels_label, (screen_width - levels_label.get_width() - 10, 10))
            clock.tick(FPS)
            pygame.display.update()