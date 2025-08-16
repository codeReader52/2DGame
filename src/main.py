import pygame
import pymunk
from Raider import Raider
from GameConfig import Config
from Ground import Ground
from PhysicsBody import RaiderPhysicsBody
from HealthBar import HealthBar
from Goomba import Enemy

pygame.init()
clock = pygame.time.Clock()
FRAMES_PER_MIN = 60
BACKGROUND_COLOR = (225, 225, 225)
STOP_ATTACK_EVENT = pygame.USEREVENT + 1

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("2D Game")

space = pymunk.Space()
space.gravity = Config.gravity

ground = Ground(screen, space)
raider = Raider(screen, space)
health_bar = HealthBar(450, 10, screen)
enemy = Enemy([300, 0], 20, screen)

space.on_collision(Ground.COLLISION_TYPE, RaiderPhysicsBody.COLLISION_TYPE, begin=lambda *args: raider.finish_jump())
dt = 0

while True:
  health_bar.health = 15

  index = 0
  events = pygame.event.get()
  while index < len(events):
    event = events[index]
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    elif event.type == STOP_ATTACK_EVENT:
      raider.finish_attack()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        exit()
      elif event.key == pygame.K_RIGHT:
        raider.run_right()
      elif event.key == pygame.K_LEFT:
        raider.run_left()
      elif event.key == pygame.K_c:
        raider.jump()
      elif event.key == pygame.K_x:
        raider.attack()
        pygame.time.set_timer(STOP_ATTACK_EVENT, Config.attack_duration_ms, loops=1)
    elif event.type == pygame.KEYUP:
      if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
        raider.stop_run()
    index += 1

  space.step(1 / FRAMES_PER_MIN)
  raider.update(dt)

  screen.fill(BACKGROUND_COLOR)
  raider.draw()
  ground.draw()
  enemy.draw()
  health_bar.draw()
  pygame.display.update()
  dt = clock.tick(FRAMES_PER_MIN)
