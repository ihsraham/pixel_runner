# importing pygame
import pygame
from sys import exit

# initializing pygame
pygame.init()

# creating a display surface
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
snail_rect = snail_surf.get_rect(midbottom=(snail_x_pos, 300))


player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

    screen.blit(score_surf, score_rect)
    snail_rect.x -= 4
    if snail_rect.x < -100:
        snail_rect.x = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)
    
    # if player_rect.colliderect(snail_rect):
    #   print('collision')
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)
