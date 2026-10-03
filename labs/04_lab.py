def dfs(start):

    if start.left is None:
        return start

    dfs(start.left)

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class System:
    def __init__(self):
        self.record = {}

    def add(self, name, regno, gender, age, marks, grade):
        self.record[regno] = {"name": name, "gender": gender, "age": age, "marks": marks, "grade": grade}

    def updateName(self, regno, name):
        if regno in self.record:
            self.record[regno]["name"] = name
        else:
            print('Record not found')

    def updateAge(self, regno, age):
        if regno in self.record:
            self.record[regno]["age"] = age
        else:
            print('Record not found')

    def updateMarks(self, regno, marks):
        if regno in self.record:
            self.record[regno]["marks"] = marks
        else:
            print('Record not found')

    def updateGrade(self, regno, grade):
        if regno in self.record:
            self.record[regno]["grade"] = grade
        else:
            print('Record not found')

    def remove(self, regno):
        if regno in self.record:
            del self.record[regno]
        else:
            print('Record not found')

# 4. Sort students by their scores(used a lymbda function)

    def sort(self):
        return sorted(self.record.items(), key=lambda x: x[1]["marks"], reverse=True)

    def topStudent(self):
        sort = sorted(self.record.items(), key=lambda x: x[1]["marks"], reverse=True)
        return sort[0]

s = System()

# 1. Add new students
s.add('Ahmad', 'SP25-BSE-019', 'Male', 20, 90, 'B')
s.add('Ribal', 'SP25-BSE-041', 'Male', 20, 92, 'A')
s.add('Ibrahim', 'FA24-BSE-074', 'Male', 20, 67, 'D')

print(s.record)

# 2. Update student details
s.updateName('SP25-BSE-019', 'Ahmad Hamim')
print(s.record)

s.updateAge('SP25-BSE-019', 50)
print(s.record)

s.updateGrade('SP25-BSE-019', 'A')
print(s.record)

s.updateMarks('SP25-BSE-019', 85)
print(s.record)

# 3. Remove students from the system
s.remove('FA24-BSE-074')
print(s.record)

print(s.topStudent())

# D.1 Plain BFS
def bfs(graph, visited, start):
    q = []

    q.append(start)
    visited.add(start)

    while q:
        node = q.pop(0)

        print(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)

graph = {
    '5': ['3', '7'],
    "3": ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

bfs(graph, set(), '5')