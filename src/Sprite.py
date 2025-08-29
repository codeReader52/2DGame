import pygame
import typing


class SpriteActor:

  def __init__(self, screen: pygame.Surface, name, frame_live_time, do_not_loop=False):
    self.screen = screen
    self.name = name
    self.frame_live_time = frame_live_time
    self.frames = []
    self.active_frame_index = 0
    self.time_from_last_frame_transition = 0
    self.do_not_loop = do_not_loop

  def add_frame(self, sprite_file: str):
    self.frames.append(pygame.image.load(sprite_file).convert_alpha())

  def update(self, dt: float):
    self.time_from_last_frame_transition += dt
    if self.time_from_last_frame_transition < self.frame_live_time:
      return
    if self.do_not_loop and self.active_frame_index == len(self.frames) - 1:
      return

    self.time_from_last_frame_transition = 0
    self.active_frame_index = (self.active_frame_index + 1) % len(self.frames)

  def reset(self):
    self.active_frame_index = 0
    self.time_from_last_frame_transition = 0

  def draw(self, lower_left: typing.Tuple[int, int], flip_vertically: bool):
    width, height = self.get_size()
    if flip_vertically:
      self.screen.blit(pygame.transform.flip(self.frames[self.active_frame_index], True, False),
                       pygame.Rect(lower_left[0], lower_left[1] - height, width, height))
    else:
      self.screen.blit(self.frames[self.active_frame_index], pygame.Rect(lower_left[0], lower_left[1] - height, width, height))

  def get_size(self):
    active_frame = self.frames[self.active_frame_index]
    return (active_frame.get_width(), active_frame.get_height())
