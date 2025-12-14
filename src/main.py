import pygame
import pymunk
from Raider import Raider
from GameConfig import Config
from Ground import Ground
from pymunk import Vec2d
from HealthBar import HealthBar
from Goomba import Enemy

pygame.init()
clock = pygame.time.Clock()
FRAMES_PER_MIN = 60
BACKGROUND_COLOR = (225, 225, 225)
STOP_ATTACK_EVENT = pygame.USEREVENT + 1

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("2D Game")

background = pygame.image.load("./assets/Background/level1.png")
background = pygame.transform.scale(background, (1000, 800))

space = pymunk.Space()
space.gravity = Config.gravity

ground = Ground(screen, space)
raider = Raider(screen, space)
health_bar = HealthBar(50, screen)


def decrease_health(*args):
  health_bar.health = max(0, health_bar.health - 5)


enemies = []

space.on_collision(Ground.COLLISION_TYPE, Raider.COLLISION_TYPE, begin=lambda *_a: raider.finish_jump())
space.on_collision(Raider.COLLISION_TYPE, Enemy.COLLISION_TYPE, begin=decrease_health)
dt = 0
last_enemy_added = 0

while True:
  # last_enemy_added = last_enemy_added + dt
  # if last_enemy_added > 3000:
  # enemy = Enemy(space, Config.enemy_mass, [350, 20], Config.enemy_radius, Config.enemy_elasticity, screen)
  # enemies.append(enemy)
  # last_enemy_added = 0

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

  if health_bar.health <= 0:
    raider.die()

  space.step(1 / FRAMES_PER_MIN)
  raider.update(dt)

  screen.blit(background, (0, 0))
  raider.draw()
  # ground.draw()
  eidx = 0
  while eidx < len(enemies):
    enemy = enemies[eidx]
    enemy.draw()
    eidx += 1
  health_bar.draw()
  pygame.display.update()

  dt = clock.tick(FRAMES_PER_MIN)
