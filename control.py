from State import State
from Transition import Transition
from Machine import Machine

alphabet = ['a', 'b']
state0 = State('0', True, False)
state1 = State('1', False, False)
state2 = State('2', True, False)
state3 = State('3', False, True)

states = [state0, state1, state2, state3]

tran0 = Transition(state0, state1, ['a'])
tran1 = Transition(state0, state3, ['b'])
tran2 = Transition(state1, state2, ['b'])
tran3 = Transition(state1, state3, ['a'])
tran4 = Transition(state2, state0, ['a'])
tran5 = Transition(state2, state3, ['b'])
tran6 = Transition(state3, state3, ['a', 'b'])

transitions = [tran0, tran1, tran2, tran3, tran4, tran5, tran6]

machine = Machine(alphabet, states, transitions, "DFA")

print(machine)
