import pygame
from entities import *
from settings import *
from camera import *
from location import *

pygame.init()
camera = Camera()

clock = pygame.time.Clock()


silver_cavern = SilverCavern()
blocks = silver_cavern.load()

player = Player(0, -500)
blocks_with_collision = []
blocks_with_collision.extend(blocks)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(blocks)

main_game_loop = True
while main_game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                player.jump = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.moving_left = True
        player.is_moving = True
        player.right = False
    if keys[pygame.K_d]:
        player.moving_right = True
        player.is_moving = True
        player.right = True
    if not keys[pygame.K_a]:
        player.moving_left = False
    if not keys[pygame.K_d]:
        player.moving_right = False
    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        player.is_moving = False

    screen.fill(('GRAY'))

    all_sprites.update(blocks_with_collision=blocks_with_collision)
    all_sprites.draw(screen)
    # change camera view
    camera.update(player)

    # update all sprites positions
    for sprite in all_sprites:
        camera.apply(sprite)




    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()