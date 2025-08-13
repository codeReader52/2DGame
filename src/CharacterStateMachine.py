from statemachine import State, StateMachine


class RaiderCharacterSM(StateMachine):
  idle = State(initial=True)
  run = State()
  jump = State()
  # attack = State()

  trigger_run = idle.to(run)
  stop_run = run.to(idle)
  trigger_jump = idle.to(jump) | run.to(jump)
  finish_jump = jump.to(idle)


class DirectionsM(StateMachine):
  right = State(initial=True)
  left = State()

  turn_around = right.to(left) | left.to(right)

  def is_facing_right(self):
    return self.current_state == self.right
