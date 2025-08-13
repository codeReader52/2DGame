from statemachine import State, StateMachine


class RaiderCharacterSM(StateMachine):
  idle = State(initial=True)
  run = State()
  jump_run = State()
  jump_idle = State()
  attack_run = State()
  attack_idle = State()

  trigger_run = idle.to(run) | jump_idle.to(jump_run) | attack_idle.to(attack_run)
  trigger_attack = idle.to(attack_idle) | run.to(attack_run)
  finish_attack = attack_idle.to(idle) | attack_run.to(run)
  stop_run = run.to(idle) | jump_run.to(jump_idle) | attack_run.to(attack_idle)
  trigger_jump = idle.to(jump_idle) | run.to(jump_run)
  finish_jump = jump_idle.to(idle) | jump_run.to(run)

  def is_jumping(self):
    return self.current_state in [self.jump_idle, self.jump_run]

  def is_attacking(self):
    return self.current_state in [self.attack_idle, self.attack_run]

  def get_state_name(self):
    if self.current_state == self.idle: return "idle"
    elif self.current_state == self.run: return "run"
    elif self.is_attacking(): return "attack"
    else: return "jump"


class DirectionsM(StateMachine):
  right = State(initial=True)
  left = State()

  turn_around = right.to(left) | left.to(right)

  def is_facing_right(self):
    return self.current_state == self.right
