import heapq

from tasks import Task
from tasks import create_priority_queues



"""
a heapq priority queue is used to manage tasks based on their priority. The priority queue ensures that tasks with higher priority are processed first. After executing a task for the time quantum, if the task isn't finished, it is reinserted into the priority queue for further processing
"""
def priority_based(queues, queue_quanta, task_quantum, reinsert=True):
    print("Execution Order:")
    queue_count = len(queues)
    current_queue = queue_count - 1  # Start with the last queue (more priority)

    while any(queues):  # Continue until all queues are empty
        if queues[current_queue]:
            remaining_time = queue_quanta[current_queue]  # Quantum for the current queue

            task_to_reinsert = []
            while remaining_time > 0 and queues[current_queue]:
                task = heapq.heappop(queues[current_queue])

                execution_time = min(task.burst_time, task_quantum, remaining_time)
                print(f"Task {task.name} (Queue {current_queue}) executed for {execution_time} units")
                task.burst_time -= execution_time
                remaining_time -= execution_time

                if task.burst_time > 0:
                    if reinsert:
                        heapq.heappush(queues[current_queue], task)
                    else:
                        task_to_reinsert.append(task)
                else:
                    print(f"Task {task.name} completed")

        if len(task_to_reinsert) > 0:
            for task in task_to_reinsert:
                heapq.heappush(queues[current_queue], task)

        # Move to the next queue
        current_queue = (current_queue - 1)
        if current_queue < 0:
            current_queue = queue_count - 1


if __name__ == "__main__":

    # Example
    tasks = [
        Task("Task1", priority=2, burst_time=10),
        Task("Task2", priority=8, burst_time=20),
        Task("Task3", priority=4, burst_time=5),
        Task("Task4", priority=6, burst_time=15),
        Task("Task5", priority=5, burst_time=8)
    ]

    queues = create_priority_queues(tasks, None)

    queue_quanta = [6, 8, 10]  # Queue 0 has the shortest quantum, Queue 2 has the longest quantum

    task_quantum = 4
    priority_based(queues, queue_quanta, task_quantum, reinsert=True)
