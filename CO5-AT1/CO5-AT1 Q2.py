# Exam Timetabling using Graph Coloring and Backtracking

# Number of exams
n = 4

# Exam names
exams = ["E1", "E2", "E3", "E4"]

# Conflict Graph
# Edge = common students between exams
graph = [
    [0, 1, 1, 0],  # E1
    [1, 0, 0, 1],  # E2
    [1, 0, 0, 1],  # E3
    [0, 1, 1, 0]   # E4
]

# Number of students taking each exam
students = [30, 25, 20, 35]

# Available time slots
m = 3

# Room capacity per slot
room_capacity = 60

# Color array (Time Slot Assignment)
color = [0] * n


# Check if assigning color c to exam v is safe
def is_safe(v, c):
    for i in range(n):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


# Check room capacity constraint
def check_capacity():
    for slot in range(1, m + 1):
        total_students = 0

        for exam in range(n):
            if color[exam] == slot:
                total_students += students[exam]

        if total_students > room_capacity:
            return False

    return True


# Backtracking Graph Coloring
def graph_coloring(v):

    if v == n:
        return check_capacity()

    for c in range(1, m + 1):

        if is_safe(v, c):

            color[v] = c

            if graph_coloring(v + 1):
                return True

            color[v] = 0

    return False


# Main Program
if graph_coloring(0):

    print(" EXAM TIMETABLE \n")

    for i in range(n):
        print(exams[i], "-> Time Slot", color[i])

    print("\n SLOT UTILIZATION ")

    for slot in range(1, m + 1):

        total_students = 0

        print("\nTime Slot", slot)

        for exam in range(n):
            if color[exam] == slot:
                print(" ", exams[exam], "- Students:", students[exam])
                total_students += students[exam]

        print("Total Students =", total_students)
        print("Room Capacity  =", room_capacity)

else:
    print("No feasible timetable exists.")
