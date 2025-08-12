import pygame
import pymunk
from Raider import Raider
from GameConfig import Config
from Ground import Ground
from PhysicsBody import RaiderPhysicsBody

pygame.init()
clock = pygame.time.Clock()
FRAMES_PER_MIN = 60
BACKGROUND_COLOR = (225, 225, 225)

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("2D Game")

space = pymunk.Space()
space.gravity = Config.gravity

ground = Ground(screen, space)
raider = Raider(screen, space)

space.on_collision(Ground.COLLISION_TYPE, RaiderPhysicsBody.COLLISION_TYPE, begin=lambda *args: raider.finish_jump())
dt = 0

while True:
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
    elif event.type == pygame.KEYUP:
      if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
        raider.stop_run()

  space.step(1 / FRAMES_PER_MIN)
  raider.update(dt)

  screen.fill(BACKGROUND_COLOR)
  raider.draw()
  ground.draw()
  pygame.display.update()
  dt = clock.tick(FRAMES_PER_MIN)
