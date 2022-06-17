import pygame
import math
from settings import *

SCALE = 3.5

player_idle_6_ah = pygame.image.load('data/images/player/ahead/idle/6/0.gif')
player_idle_6_ah = pygame.transform.scale(player_idle_6_ah, (int(player_idle_6_ah.get_width() * SCALE),
                                                         int(player_idle_6_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_13_ah = pygame.image.load('data/images/player/ahead/idle/13/0.gif')
player_idle_13_ah = pygame.transform.scale(player_idle_13_ah, (int(player_idle_13_ah.get_width() * SCALE),
                                                         int(player_idle_13_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_20_ah = pygame.image.load('data/images/player/ahead/idle/20/0.gif')
player_idle_20_ah = pygame.transform.scale(player_idle_20_ah, (int(player_idle_20_ah.get_width() * SCALE),
                                                         int(player_idle_20_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_27_ah = pygame.image.load('data/images/player/ahead/idle/27/0.gif')
player_idle_27_ah = pygame.transform.scale(player_idle_27_ah, (int(player_idle_27_ah.get_width() * SCALE),
                                                         int(player_idle_27_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_34_ah = pygame.image.load('data/images/player/ahead/idle/34/0.gif')
player_idle_34_ah = pygame.transform.scale(player_idle_34_ah, (int(player_idle_34_ah.get_width() * SCALE),
                                                         int(player_idle_34_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_41_ah = pygame.image.load('data/images/player/ahead/idle/41/0.gif')
player_idle_41_ah = pygame.transform.scale(player_idle_41_ah, (int(player_idle_41_ah.get_width() * SCALE),
                                                         int(player_idle_41_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_48_ah = pygame.image.load('data/images/player/ahead/idle/48/0.gif')
player_idle_48_ah = pygame.transform.scale(player_idle_48_ah, (int(player_idle_48_ah.get_width() * SCALE),
                                                         int(player_idle_48_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_55_ah = pygame.image.load('data/images/player/ahead/idle/55/0.gif')
player_idle_55_ah = pygame.transform.scale(player_idle_55_ah, (int(player_idle_55_ah.get_width() * SCALE),
                                                         int(player_idle_55_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_62_ah = pygame.image.load('data/images/player/ahead/idle/62/0.gif')
player_idle_62_ah = pygame.transform.scale(player_idle_62_ah, (int(player_idle_62_ah.get_width() * SCALE),
                                                         int(player_idle_62_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_69_ah = pygame.image.load('data/images/player/ahead/idle/69/0.gif')
player_idle_69_ah = pygame.transform.scale(player_idle_69_ah, (int(player_idle_69_ah.get_width() * SCALE),
                                                         int(player_idle_69_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_76_ah = pygame.image.load('data/images/player/ahead/idle/76/0.gif')
player_idle_76_ah = pygame.transform.scale(player_idle_76_ah, (int(player_idle_76_ah.get_width() * SCALE),
                                                         int(player_idle_76_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_83_ah = pygame.image.load('data/images/player/ahead/idle/83/0.gif')
player_idle_83_ah = pygame.transform.scale(player_idle_83_ah, (int(player_idle_83_ah.get_width() * SCALE),
                                                         int(player_idle_83_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_90_ah = pygame.image.load('data/images/player/ahead/idle/90/0.gif')
player_idle_90_ah = pygame.transform.scale(player_idle_90_ah, (int(player_idle_90_ah.get_width() * SCALE),
                                                         int(player_idle_90_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_97_ah = pygame.image.load('data/images/player/ahead/idle/97/0.gif')
player_idle_97_ah = pygame.transform.scale(player_idle_97_ah, (int(player_idle_97_ah.get_width() * SCALE),
                                                         int(player_idle_97_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_105_ah = pygame.image.load('data/images/player/ahead/idle/105/0.gif')
player_idle_105_ah = pygame.transform.scale(player_idle_105_ah, (int(player_idle_105_ah.get_width() * SCALE),
                                                         int(player_idle_105_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_112_ah = pygame.image.load('data/images/player/ahead/idle/112/0.gif')
player_idle_112_ah = pygame.transform.scale(player_idle_112_ah, (int(player_idle_112_ah.get_width() * SCALE),
                                                         int(player_idle_112_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_119_ah = pygame.image.load('data/images/player/ahead/idle/119/0.gif')
player_idle_119_ah = pygame.transform.scale(player_idle_119_ah, (int(player_idle_119_ah.get_width() * SCALE),
                                                         int(player_idle_119_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_126_ah = pygame.image.load('data/images/player/ahead/idle/126/0.gif')
player_idle_126_ah = pygame.transform.scale(player_idle_126_ah, (int(player_idle_126_ah.get_width() * SCALE),
                                                         int(player_idle_126_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_133_ah = pygame.image.load('data/images/player/ahead/idle/133/0.gif')
player_idle_133_ah = pygame.transform.scale(player_idle_133_ah, (int(player_idle_133_ah.get_width() * SCALE),
                                                         int(player_idle_133_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_140_ah = pygame.image.load('data/images/player/ahead/idle/140/0.gif')
player_idle_140_ah = pygame.transform.scale(player_idle_140_ah, (int(player_idle_140_ah.get_width() * SCALE),
                                                         int(player_idle_140_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_147_ah = pygame.image.load('data/images/player/ahead/idle/147/0.gif')
player_idle_147_ah = pygame.transform.scale(player_idle_147_ah, (int(player_idle_147_ah.get_width() * SCALE),
                                                         int(player_idle_147_ah.get_height() * SCALE))).convert_alpha(screen)


player_idle_154_ah = pygame.image.load('data/images/player/ahead/idle/154/0.gif')
player_idle_154_ah = pygame.transform.scale(player_idle_154_ah, (int(player_idle_154_ah.get_width() * SCALE),
                                                         int(player_idle_154_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_161_ah = pygame.image.load('data/images/player/ahead/idle/161/0.gif')
player_idle_161_ah = pygame.transform.scale(player_idle_161_ah, (int(player_idle_161_ah.get_width() * SCALE),
                                                         int(player_idle_161_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_168_ah = pygame.image.load('data/images/player/ahead/idle/168/0.gif')
player_idle_168_ah = pygame.transform.scale(player_idle_168_ah, (int(player_idle_168_ah.get_width() * SCALE),
                                                         int(player_idle_168_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_175_ah = pygame.image.load('data/images/player/ahead/idle/175/0.gif')
player_idle_175_ah = pygame.transform.scale(player_idle_175_ah, (int(player_idle_175_ah.get_width() * SCALE),
                                                         int(player_idle_175_ah.get_height() * SCALE))).convert_alpha(screen)

player_idle_13_bk = pygame.image.load('data/images/player/back/idle/13/0.gif')
player_idle_13_bk = pygame.transform.scale(player_idle_13_bk, (int(player_idle_13_bk.get_width() * SCALE),
                                                         int(player_idle_13_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_20_bk = pygame.image.load('data/images/player/back/idle/20/0.gif')
player_idle_20_bk = pygame.transform.scale(player_idle_20_bk, (int(player_idle_20_bk.get_width() * SCALE),
                                                         int(player_idle_20_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_27_bk = pygame.image.load('data/images/player/back/idle/27/0.gif')
player_idle_27_bk = pygame.transform.scale(player_idle_27_bk, (int(player_idle_27_bk.get_width() * SCALE),
                                                         int(player_idle_27_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_34_bk = pygame.image.load('data/images/player/back/idle/34/0.gif')
player_idle_34_bk = pygame.transform.scale(player_idle_34_bk, (int(player_idle_34_bk.get_width() * SCALE),
                                                         int(player_idle_34_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_41_bk = pygame.image.load('data/images/player/back/idle/41/0.gif')
player_idle_41_bk = pygame.transform.scale(player_idle_41_bk, (int(player_idle_41_bk.get_width() * SCALE),
                                                         int(player_idle_41_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_48_bk = pygame.image.load('data/images/player/back/idle/48/0.gif')
player_idle_48_bk = pygame.transform.scale(player_idle_48_bk, (int(player_idle_48_bk.get_width() * SCALE),
                                                      int(player_idle_48_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_55_bk = pygame.image.load('data/images/player/back/idle/55/0.gif')
player_idle_55_bk = pygame.transform.scale(player_idle_55_bk, (int(player_idle_55_bk.get_width() * SCALE),
                                                      int(player_idle_55_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_62_bk = pygame.image.load('data/images/player/back/idle/62/0.gif')
player_idle_62_bk = pygame.transform.scale(player_idle_62_bk, (int(player_idle_62_bk.get_width() * SCALE),
                                                      int(player_idle_62_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_69_bk = pygame.image.load('data/images/player/back/idle/69/0.gif')
player_idle_69_bk = pygame.transform.scale(player_idle_69_bk, (int(player_idle_69_bk.get_width() * SCALE),
                                                      int(player_idle_69_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_76_bk = pygame.image.load('data/images/player/back/idle/76/0.gif')
player_idle_76_bk = pygame.transform.scale(player_idle_76_bk, (int(player_idle_76_bk.get_width() * SCALE),
                                                      int(player_idle_76_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_83_bk = pygame.image.load('data/images/player/back/idle/83/0.gif')
player_idle_83_bk = pygame.transform.scale(player_idle_83_bk, (int(player_idle_83_bk.get_width() * SCALE),
                                                      int(player_idle_83_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_90_bk = pygame.image.load('data/images/player/back/idle/90/0.gif')
player_idle_90_bk = pygame.transform.scale(player_idle_90_bk, (int(player_idle_90_bk.get_width() * SCALE),
                                                      int(player_idle_90_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_97_bk = pygame.image.load('data/images/player/back/idle/97/0.gif')
player_idle_97_bk = pygame.transform.scale(player_idle_97_bk, (int(player_idle_97_bk.get_width() * SCALE),
                                                      int(player_idle_97_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_105_bk = pygame.image.load('data/images/player/back/idle/105/0.gif')
player_idle_105_bk = pygame.transform.scale(player_idle_105_bk, (int(player_idle_105_bk.get_width() * SCALE),
                                                      int(player_idle_105_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_112_bk = pygame.image.load('data/images/player/back/idle/112/0.gif')
player_idle_112_bk = pygame.transform.scale(player_idle_112_bk, (int(player_idle_112_bk.get_width() * SCALE),
                                                      int(player_idle_112_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_119_bk = pygame.image.load('data/images/player/back/idle/119/0.gif')
player_idle_119_bk = pygame.transform.scale(player_idle_119_bk, (int(player_idle_119_bk.get_width() * SCALE),
                                                      int(player_idle_119_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_126_bk = pygame.image.load('data/images/player/back/idle/126/0.gif')
player_idle_126_bk = pygame.transform.scale(player_idle_126_bk, (int(player_idle_126_bk.get_width() * SCALE),
                                                      int(player_idle_126_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_133_bk = pygame.image.load('data/images/player/back/idle/133/0.gif')
player_idle_133_bk = pygame.transform.scale(player_idle_133_bk, (int(player_idle_133_bk.get_width() * SCALE),
                                                      int(player_idle_133_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_140_bk = pygame.image.load('data/images/player/back/idle/140/0.gif')
player_idle_140_bk = pygame.transform.scale(player_idle_140_bk, (int(player_idle_140_bk.get_width() * SCALE),
                                                      int(player_idle_140_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_147_bk = pygame.image.load('data/images/player/back/idle/147/0.gif')
player_idle_147_bk = pygame.transform.scale(player_idle_147_bk, (int(player_idle_147_bk.get_width() * SCALE),
                                                      int(player_idle_147_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_154_bk = pygame.image.load('data/images/player/back/idle/154/0.gif')
player_idle_154_bk = pygame.transform.scale(player_idle_154_bk, (int(player_idle_154_bk.get_width() * SCALE),
                                                      int(player_idle_154_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_161_bk = pygame.image.load('data/images/player/back/idle/161/0.gif')
player_idle_161_bk = pygame.transform.scale(player_idle_161_bk, (int(player_idle_161_bk.get_width() * SCALE),
                                                      int(player_idle_161_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_168_bk = pygame.image.load('data/images/player/back/idle/168/0.gif')
player_idle_168_bk = pygame.transform.scale(player_idle_168_bk, (int(player_idle_168_bk.get_width() * SCALE),
                                                      int(player_idle_168_bk.get_height() * SCALE))).convert_alpha(screen)

player_idle_175_bk = pygame.image.load('data/images/player/back/idle/175/0.gif')
player_idle_175_bk = pygame.transform.scale(player_idle_175_bk, (int(player_idle_175_bk.get_width() * SCALE),
                                                      int(player_idle_175_bk.get_height() * SCALE))).convert_alpha(screen)

player_run_6_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/6/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_6_ah.append(image)

player_run_13_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/13/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_13_ah.append(image)

player_run_20_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/20/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_20_ah.append(image)

player_run_27_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/27/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_27_ah.append(image)

player_run_34_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/34/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_34_ah.append(image)

player_run_41_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/41/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_41_ah.append(image)

player_run_48_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/48/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_48_ah.append(image)

player_run_55_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/55/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_55_ah.append(image)

player_run_62_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/62/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_62_ah.append(image)


player_run_69_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/69/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_69_ah.append(image)

player_run_76_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/76/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_76_ah.append(image)

player_run_83_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/83/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_83_ah.append(image)

player_run_90_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/90/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_90_ah.append(image)

player_run_97_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/97/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_97_ah.append(image)

player_run_105_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/105/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_105_ah.append(image)

player_run_112_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/112/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_112_ah.append(image)

player_run_119_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/119/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_119_ah.append(image)

player_run_126_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/126/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_126_ah.append(image)

player_run_133_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/133/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_133_ah.append(image)

player_run_140_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/140/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_140_ah.append(image)

player_run_147_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/147/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_147_ah.append(image)

player_run_154_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/154/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_154_ah.append(image)

player_run_161_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/161/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_161_ah.append(image)

player_run_168_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/168/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_168_ah.append(image)

player_run_175_ah = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/ahead/run/175/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_175_ah.append(image)

player_run_13_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/13/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_13_bk.append(image)

player_run_20_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/20/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_20_bk.append(image)


player_run_27_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/27/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_27_bk.append(image)


player_run_34_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/34/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_34_bk.append(image)


player_run_41_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/41/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_41_bk.append(image)


player_run_48_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/48/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_48_bk.append(image)


player_run_55_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/55/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_55_bk.append(image)


player_run_62_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/62/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_62_bk.append(image)


player_run_69_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/69/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_69_bk.append(image)


player_run_76_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/76/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_76_bk.append(image)


player_run_83_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/83/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_83_bk.append(image)


player_run_90_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/90/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_90_bk.append(image)


player_run_97_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/97/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_97_bk.append(image)

player_run_105_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/105/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_105_bk.append(image)


player_run_112_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/112/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_112_bk.append(image)


player_run_119_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/119/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_119_bk.append(image)


player_run_126_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/126/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_126_bk.append(image)


player_run_133_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/133/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_133_bk.append(image)


player_run_140_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/140/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_140_bk.append(image)


player_run_147_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/147/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_147_bk.append(image)


player_run_154_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/154/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_154_bk.append(image)


player_run_161_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/161/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_161_bk.append(image)


player_run_168_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/168/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_168_bk.append(image)


player_run_175_bk = []
for i in range(4):
    image = pygame.image.load(f'data/images/player/back/run/175/{i}.gif')
    image = pygame.transform.scale(image, (int(image.get_width() * SCALE), int(image.get_height() * SCALE))).convert_alpha(screen)
    player_run_175_bk.append(image)


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super(Entity, self).__init__()
        self.left = False
        self.moving_left = False
        self.moving_right = False
        self.right = True
        self.is_moving = False
        self.animation_tick = 0
        self.ang = 90


class Player(Entity):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.image = player_idle_90_ah
        self.rect = self.image.get_rect()
        self.rect.width -= 50
        self.rect.center = (x, y)
        self.speed = 6.5
        self.jump = False
        self.vel_y = 0
        self.in_air = False

    def update(self, *args, **kwargs):
        super(Player, self).update(*args, **kwargs)
        dx = 0
        dy = 0

        blocks_with_collision = kwargs['blocks_with_collision']

        if self.moving_left:
            dx = -self.speed

        if self.moving_right:
            dx = self.speed

        if self.jump and not self.in_air:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        self.vel_y += GRAVITY
        dy += self.vel_y

        for block in blocks_with_collision:
            # check collision in the x direction
            if block.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
            # check for collision in the y direction
            if block.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = block.rect.bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = block.rect.top - self.rect.bottom

        self.rect.x += dx
        self.rect.y += dy

        mouse_x, mouse_y = pygame.mouse.get_pos()
        start_pos = (self.rect.x + (self.rect.right - self.rect.left) // 2,
                     self.rect.y + (self.rect.bottom - self.rect.top) // 2)
        ang = math.atan2(mouse_x - start_pos[0], mouse_y - start_pos[1])
        self.ang = abs(math.degrees(ang))

        self.image = player_idle_90_ah

        if (self.right and mouse_x > self.rect.x) or (not self.right and mouse_x < self.rect.x):

            if self.is_moving:
                self.image = player_run_90_ah[self.animation_tick // 20]
                if 0 <= self.ang < 13:
                    self.image = player_run_6_ah[self.animation_tick // 20]
                elif 13 <= self.ang < 20:
                    self.image = player_run_13_ah[self.animation_tick // 20]
                elif 20 <= self.ang < 27:
                    self.image = player_run_20_ah[self.animation_tick // 20]
                elif 27 <= self.ang < 34:
                    self.image = player_run_27_ah[self.animation_tick // 20]
                elif 34 <= self.ang < 41:
                    self.image = player_run_34_ah[self.animation_tick // 20]
                elif 41 <= self.ang < 48:
                    self.image = player_run_41_ah[self.animation_tick // 20]
                elif 48 <= self.ang < 55:
                    self.image = player_run_48_ah[self.animation_tick // 20]
                elif 55 <= self.ang < 62:
                    self.image = player_run_55_ah[self.animation_tick // 20]
                elif 62 <= self.ang < 69:
                    self.image = player_run_62_ah[self.animation_tick // 20]
                elif 69 <= self.ang < 76:
                    self.image = player_run_69_ah[self.animation_tick // 20]
                elif 76 <= self.ang < 83:
                    self.image = player_run_76_ah[self.animation_tick // 20]
                elif 83 <= self.ang < 90:
                    self.image = player_run_83_ah[self.animation_tick // 20]
                elif 90 <= self.ang < 97:
                    self.image = player_run_90_ah[self.animation_tick // 20]
                elif 97 <= self.ang < 105:
                    self.image = player_run_97_ah[self.animation_tick // 20]
                elif 105 <= self.ang < 112:
                    self.image = player_run_105_ah[self.animation_tick // 20]
                elif 112 <= self.ang < 119:
                    self.image = player_run_112_ah[self.animation_tick // 20]
                elif 119 <= self.ang < 126:
                    self.image = player_run_119_ah[self.animation_tick // 20]
                elif 126 <= self.ang < 133:
                    self.image = player_run_126_ah[self.animation_tick // 20]
                elif 133 <= self.ang < 140:
                    self.image = player_run_133_ah[self.animation_tick // 20]
                elif 140 <= self.ang < 147:
                    self.image = player_run_140_ah[self.animation_tick // 20]
                elif 147 <= self.ang < 154:
                    self.image = player_run_147_ah[self.animation_tick // 20]
                elif 154 <= self.ang < 161:
                    self.image = player_run_154_ah[self.animation_tick // 20]
                elif 161 <= self.ang < 168:
                    self.image = player_run_161_ah[self.animation_tick // 20]
                elif 168 <= self.ang < 175:
                    self.image = player_run_168_ah[self.animation_tick // 20]
                elif 175 <= self.ang <= 180:
                    self.image = player_run_175_ah[self.animation_tick // 20]

            if not self.is_moving:
                if 0 <= self.ang < 13:
                    self.image = player_idle_6_ah
                elif 13 <= self.ang < 20:
                    self.image = player_idle_13_ah
                elif 20 <= self.ang < 27:
                    self.image = player_idle_20_ah
                elif 27 <= self.ang < 34:
                    self.image = player_idle_27_ah
                elif 34 <= self.ang < 41:
                    self.image = player_idle_34_ah
                elif 41 <= self.ang < 48:
                    self.image = player_idle_41_ah
                elif 48 <= self.ang < 55:
                    self.image = player_idle_48_ah
                elif 55 <= self.ang < 62:
                    self.image = player_idle_55_ah
                elif 62 <= self.ang < 69:
                    self.image = player_idle_62_ah
                elif 69 <= self.ang < 76:
                    self.image = player_idle_69_ah
                elif 76 <= self.ang < 83:
                    self.image = player_idle_76_ah
                elif 83 <= self.ang < 90:
                    self.image = player_idle_83_ah
                elif 90 <= self.ang < 97:
                    self.image = player_idle_90_ah
                elif 97 <= self.ang < 105:
                    self.image = player_idle_97_ah
                elif 105 <= self.ang < 112:
                    self.image = player_idle_105_ah
                elif 112 <= self.ang < 119:
                    self.image = player_idle_112_ah
                elif 119 <= self.ang < 126:
                    self.image = player_idle_119_ah
                elif 126 <= self.ang < 133:
                    self.image = player_idle_126_ah
                elif 133 <= self.ang < 140:
                    self.image = player_idle_133_ah
                elif 140 <= self.ang < 147:
                    self.image = player_idle_140_ah
                elif 147 <= self.ang < 154:
                    self.image = player_idle_147_ah
                elif 154 <= self.ang < 161:
                    self.image = player_idle_154_ah
                elif 161 <= self.ang < 168:
                    self.image = player_idle_161_ah
                elif 168 <= self.ang < 175:
                    self.image = player_idle_168_ah
                elif 175 <= self.ang <= 180:
                    self.image = player_idle_175_ah

        if (self.right and mouse_x < self.rect.centerx) or (not self.right and mouse_x > self.rect.centery):
            if self.is_moving:
                if 0 <= self.ang < 20:
                    self.image = player_run_13_bk[self.animation_tick // 20]

                elif 20 <= self.ang < 27:
                    self.image = player_run_20_bk[self.animation_tick // 20]

                elif 27 <= self.ang < 34:
                    self.image = player_run_27_bk[self.animation_tick // 20]

                elif 34 <= self.ang < 41:
                    self.image = player_run_34_bk[self.animation_tick // 20]

                elif 41 <= self.ang < 48:
                    self.image = player_run_41_bk[self.animation_tick // 20]

                elif 48 <= self.ang < 55:
                    self.image = player_run_48_bk[self.animation_tick // 20]

                elif 55 <= self.ang < 62:
                    self.image = player_run_55_bk[self.animation_tick // 20]

                elif 62 <= self.ang < 69:
                    self.image = player_run_62_bk[self.animation_tick // 20]

                elif 69 <= self.ang < 76:
                    self.image = player_run_69_bk[self.animation_tick // 20]

                elif 76 <= self.ang < 83:
                    self.image = player_run_76_bk[self.animation_tick // 20]

                elif 83 <= self.ang < 90:
                    self.image = player_run_83_bk[self.animation_tick // 20]

                elif 90 <= self.ang < 97:
                    self.image = player_run_90_bk[self.animation_tick // 20]

                elif 97 <= self.ang < 104:
                    self.image = player_run_97_bk[self.animation_tick // 20]

                elif 105 <= self.ang < 112:
                    self.image = player_run_105_bk[self.animation_tick // 20]

                elif 112 <= self.ang < 119:
                    self.image = player_run_112_bk[self.animation_tick // 20]

                elif 119 <= self.ang < 126:
                    self.image = player_run_119_bk[self.animation_tick // 20]

                elif 126 <= self.ang < 133:
                    self.image = player_run_126_bk[self.animation_tick // 20]

                elif 133 <= self.ang < 140:
                    self.image = player_run_133_bk[self.animation_tick // 20]

                elif 140 <= self.ang < 147:
                    self.image = player_run_140_bk[self.animation_tick // 20]

                elif 147 <= self.ang < 154:
                    self.image = player_run_147_bk[self.animation_tick // 20]

                elif 154 <= self.ang < 161:
                    self.image = player_run_154_bk[self.animation_tick // 20]

                elif 161 <= self.ang < 168:
                    self.image = player_run_161_bk[self.animation_tick // 20]

                elif 168 <= self.ang < 175:
                    self.image = player_run_168_bk[self.animation_tick // 20]

                elif 175 <= self.ang < 182:
                    self.image = player_run_175_bk[self.animation_tick // 20]

            if not self.is_moving:
                if 0 <= self.ang < 6:
                    self.image = player_idle_13_bk

                elif 6 <= self.ang < 20:
                    self.image = player_idle_13_bk

                elif 20 <= self.ang < 27:
                    self.image = player_idle_20_bk

                elif 27 <= self.ang < 34:
                    self.image = player_idle_27_bk

                elif 34 <= self.ang < 41:
                    self.image = player_idle_34_bk

                elif 41 <= self.ang < 48:
                    self.image = player_idle_41_bk

                elif 48 <= self.ang < 55:
                    self.image = player_idle_48_bk

                elif 55 <= self.ang < 62:
                    self.image = player_idle_55_bk

                elif 62 <= self.ang < 69:
                    self.image = player_idle_62_bk

                elif 69 <= self.ang < 76:
                    self.image = player_idle_69_bk

                elif 76 <= self.ang < 83:
                    self.image = player_idle_76_bk

                elif 83 <= self.ang < 90:
                    self.image = player_idle_83_bk

                elif 90 <= self.ang < 97:
                    self.image = player_idle_90_bk

                elif 97 <= self.ang < 105:
                    self.image = player_idle_97_bk

                elif 105 <= self.ang < 112:
                    self.image = player_idle_105_bk

                elif 112 <= self.ang < 119:
                    self.image = player_idle_112_bk

                elif 119 <= self.ang < 126:
                    self.image = player_idle_119_bk

                elif 126 <= self.ang < 133:
                    self.image = player_idle_126_bk

                elif 133 <= self.ang < 140:
                    self.image = player_idle_133_bk

                elif 140 <= self.ang < 147:
                    self.image = player_idle_140_bk

                elif 147 <= self.ang < 154:
                    self.image = player_idle_147_bk

                elif 154 <= self.ang < 161:
                    self.image = player_idle_154_bk

                elif 161 <= self.ang < 168:
                    self.image = player_idle_161_bk

                elif 168 <= self.ang < 175:
                    self.image = player_idle_168_bk

                elif 175 <= self.ang <= 180:
                    self.image = player_idle_175_bk


        if not self.right:
            self.image = pygame.transform.flip(self.image, True, False)


        self.animation_tick += 1
        if self.animation_tick == 61:
            self.animation_tick = 0


