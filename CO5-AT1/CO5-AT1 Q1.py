from dataclasses import dataclass

@dataclass
class Job:
    id: str
    deadline: int
    duration: int
    skill: str

@dataclass
class Employee:
    id: str
    skills: set

def is_feasible(job, employee, start_time, schedule):
    if job.skill not in employee.skills:
        return False

    finish_time = start_time + job.duration
    if finish_time > job.deadline:
        return False

    for j_id, (e_id, s, f) in schedule.items():
        if e_id == employee.id:
            if not (finish_time <= s or start_time >= f):
                return False

    return True

def feasible_start_times(job):
    return range(0, job.deadline - job.duration + 1)

def backtrack(jobs, employees, schedule, index):
    if index == len(jobs):
        return True

    job = jobs[index]

    for employee in employees:
        for start_time in feasible_start_times(job):
            if is_feasible(job, employee, start_time, schedule):
                schedule[job.id] = (employee.id, start_time, start_time + job.duration)

                if backtrack(jobs, employees, schedule, index + 1):
                    return True

                del schedule[job.id]

    return False

def job_scheduling_solution():
    jobs = [
        Job("J1", deadline=4, duration=2, skill="A"),
        Job("J2", deadline=6, duration=3, skill="B"),
        Job("J3", deadline=5, duration=2, skill="A"),
    ]

    employees = [
        Employee("E1", skills={"A", "B"}),
        Employee("E2", skills={"A"}),
    ]

    # Heuristic: earliest deadline first
    jobs.sort(key=lambda x: x.deadline)

    schedule = {}
    if backtrack(jobs, employees, schedule, 0):
        print("Feasible Schedule Found:")
        for job_id, (emp_id, start, end) in schedule.items():
            print(f"{job_id} -> {emp_id}, Time: {start} to {end}")
    else:
        print("No feasible schedule exists.")

job_scheduling_solution()
