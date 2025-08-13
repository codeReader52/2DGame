from pygame import Surface
from pymunk import Space
import math
from statemachine import State

from GameConfig import Config
from PhysicsBody import RaiderPhysicsBody
from CharacterStateMachine import RaiderCharacterSM, DirectionsM
from SpriteManager import SpriteActor


class Raider:

  def __init__(self, screen: Surface, space: Space):
    self.sprite_actor = SpriteActor(screen, "./assets/Raider_sprite_list.txt", "./assets/Raider_1/")
    self.physics = RaiderPhysicsBody(space, {
        "idle": self.sprite_actor.get_size("idle"),
        "run": self.sprite_actor.get_size("run"),
        "jump": self.sprite_actor.get_size("jump"),
    }, "idle")
    self.screen_height = screen.get_height()
    self.init_chracter_sm()
    self.direction_sm = DirectionsM()

  def init_chracter_sm(self):

    class RaiderEventHandler:

      @staticmethod
      def on_enter_idle():
        self.physics.set_velocity((0, 0))

      @staticmethod
      def on_enter_jump(source: State):
        if source == RaiderCharacterSM.run:
          self.physics.apply_force(Config.raider_diagonal_right_jump if self.direction_sm.is_facing_right() else Config.raider_diagonal_left_jump)
        elif source == RaiderCharacterSM.idle:
          self.physics.apply_force(Config.raider_vertical_jump)

      @staticmethod
      def on_enter_run():
        if self.direction_sm.is_facing_right():
          self.physics.set_velocity(Config.raider_run_right_velocity)
        else:
          self.physics.set_velocity(Config.raider_run_left_velocity)

    self.sm = RaiderCharacterSM(listeners=[RaiderEventHandler()], allow_event_without_transition=True)

  def update(self, dt: float):
    self.sprite_actor.update(self.sm.current_state.name.lower(), dt)

  def draw(self):
    # TODO: make this to be the "active" shape
    bb = self.physics.get_bounding_box()
    self.sprite_actor.draw(self.sm.current_state.name.lower(), (bb.left, self.screen_height - bb.bottom), not self.direction_sm.is_facing_right())

  def run_right(self):
    if not self.direction_sm.is_facing_right():
      self.direction_sm.turn_around()
    self.sm.trigger_run()

  def run_left(self):
    if self.direction_sm.is_facing_right():
      self.direction_sm.turn_around()
    self.sm.trigger_run()

  def stop_run(self):
    self.sm.stop_run()

  def jump(self):
    self.sm.trigger_jump()

  def finish_jump(self):
    self.sm.finish_jump()
