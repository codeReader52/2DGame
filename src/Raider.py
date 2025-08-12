from pygame import Surface
from pymunk import Space
import typing
from statemachine import State

from GameConfig import Config
from PhysicsBody import RaiderPhysicsBody
from CharacterStateMachine import RaiderCharacterSM
from SpriteManager import SpriteActor


class Raider:

  def __init__(self, screen: Surface, space: Space):
    self.sprite_actor = SpriteActor(screen, "./assets/Raider_sprite_list.txt", "./assets/Raider_1/")
    self.physics = RaiderPhysicsBody(
        space, {
            "idle": self.sprite_actor.get_size("idle"),
            "run": self.sprite_actor.get_size("run"),
            "jump": self.sprite_actor.get_size("jump"),
        }, "idle")
    self.face_left = False
    self.screen_height = screen.get_height()
    self.sm = RaiderCharacterSM({"idle": self.on_enter_idle, "jump": self.on_enter_jump, "run": self.on_enter_run})

  def on_enter_idle(self, _event: str, source: State):
    self.physics.set_velocity((0, 0))

  def on_enter_jump(self, _event: str, source: State):
    if source == RaiderCharacterSM.run:
      self.physics.apply_force(Config.raider_diagonal_jump)
    elif source == RaiderCharacterSM.idle:
      self.physics.apply_force(Config.raider_vertical_jump)

  def on_enter_run(self):
    self.physics.set_velocity(Config.raider_run_velocity)

  def update(self, dt: float):
    self.sprite_actor.update(self.sm.current_state.name.lower(), dt)

  def draw(self):
    # TODO: make this to be the "active" shape
    bb = self.physics.get_bounding_box()
    self.sprite_actor.draw(self.sm.current_state.name.lower(), (bb.left, self.screen_height - bb.bottom),
                           self.face_left)

  def run_right(self):
    self.face_left = False
    self.sm.trigger_run()

  def run_left(self):
    self.face_left = True
    self.sm.trigger_run()

  def stop_run(self):
    self.sm.stop_run()

  def jump(self):
    self.sm.trigger_jump()

  def finish_jump(self):
    self.sm.finish_jump()
