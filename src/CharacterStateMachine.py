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

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.allow_event_without_transition = True
