import pygame


class HealthBar:

  def __init__(self, health, screen):
    self.health = health
    self.screen = screen

  def draw(self):
    pygame.draw.rect(self.screen, [255, 0, 0], pygame.Rect(400, 20, 500, 15))
    pygame.draw.rect(self.screen, [0, 255, 0], pygame.Rect(400, 20, self.health * 5, 15))
