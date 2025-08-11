import pygame
import pymunk
from Raider import Raider

pygame.init()
clock = pygame.time.Clock()
FRAME_PER_MIN = 60
BACKGROUND_COLOR = (225, 225, 225)

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("2D Game")

STOP_JUMP_SIGNAL = pygame.USEREVENT + 1
space = pymunk.Space()

raider = Raider(screen, space)
dt = 0

while True:
  dt = clock.tick(FRAME_PER_MIN)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        exit()
      elif event.key == pygame.K_RIGHT:
        raider.run_right()
      elif event.key == pygame.K_LEFT:
        raider.run_left()
      elif event.key == pygame.K_SPACE:
        raider.jump()
        pygame.time.set_timer(STOP_JUMP_SIGNAL, raider.get_jump_duration(), loops=1)
    elif event.type == pygame.KEYUP:
      if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
        raider.stop_run()
    elif event.type == STOP_JUMP_SIGNAL:
      raider.finish_jump()

  raider.update(dt)

  screen.fill(BACKGROUND_COLOR)
  raider.draw([400, 200])
  pygame.display.update()
