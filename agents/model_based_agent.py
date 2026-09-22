'''
A two-room vacuum world (Room A, Room B). Each room is independently Dirty or Clean,
and dirt never reappears on its own once cleaned.
The agent starts with no knowledge of either room's status.
Each cycle,it perceives only its current location and whether that location is dirty —
it cannot see the other room.
It can act: Left, Right, Suck, NoOp.
Design an agent that,
over repeated cycles, cleans both rooms without ever re-checking a room it already knows is clean,
by remembering what it has learned.
'''
class modelAgent:
    def __init__(self):
        self.model = {'A': "Unknown", 'B': "Unknown"}

    def program(self, percept):
        location, status = percept
        self.model[location] = status

        other = 'B' if location == 'A' else 'A'

        if self.model[location].lower() == 'dirty':
            return 'Suck'
        elif self.model[other].lower() in ('unknown', 'dirty'):
            return ('Moved to ' + other)
        else:
            return 'NoOp'
        

m = modelAgent()

# Test case 
print(m.program('A', 'Dirty')) 
