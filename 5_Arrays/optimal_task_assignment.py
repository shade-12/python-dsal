"""
Problem desription:
Assign tasks to workers so that the time it takes to complete all the tasks
is minimized given a count of workers and an array where each element indicates
the duration of a task.
"""

def assign_tasks(tasks_duration):
    # Time complexity: O(nlogn)
    tasks_duration = sorted(tasks_duration)
    res = list()
    for i in range(len(tasks_duration) // 2):
        # "~i": bitwise complement operator (puts a negative sign in front of i)
        res.append([tasks_duration[i], tasks_duration[~i]])

    return res