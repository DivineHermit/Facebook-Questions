import pygame
import sys


class Player(pygame.sprite.Sprite):
    """Class description here."""
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((75, 25))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))

    @staticmethod
    def create_bullet():
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    def update(self):
        """
        Method description & DocTests here.
        """
        self.rect.center = pygame.mouse.get_pos()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += 5
        if self.rect.x >= screen_width + 50:
            self.kill()


pygame.init()
clock = pygame.time.Clock()
resolution = screen_width, screen_height = 800, 600
screen = pygame.display.set_mode(resolution)
pygame.mouse.set_visible(False)

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
bullet_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())

    screen.fill((30, 30, 30))
    bullet_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    bullet_group.update()
    pygame.display.flip()
    clock.tick(60)
