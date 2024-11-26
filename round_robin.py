def round_robin():
    # Get the number of processes and time quantum from user
    n = int(input("Enter the number of processes: "))
    time_quantum = int(input("Enter the time quantum: "))

    # Initialize lists to hold process data
    arrival_time = []
    burst_time = []
    remaining_time = []
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    response_time = [-1] * n  # To track response time for each process

    # Get arrival and burst times for each process
    for i in range(n):
        arrival_time.append(int(input(f"Enter arrival time for process {i + 1}: ")))
        burst_time.append(int(input(f"Enter burst time for process {i + 1}: ")))
        remaining_time.append(burst_time[i])

    current_time = 0
    completed = 0
    gantt_chart = []  # To keep track of the process names in Gantt chart
    gantt_times = []  # To keep track of time slots for Gantt chart
    ready_queue = []  # Ready queue to keep track of processes that are ready to execute
    last_executed = -1  # To ensure fairness

    # Continue until all processes are completed
    while completed < n:
        # Check for arriving processes
        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] > 0 and i not in ready_queue:
                ready_queue.append(i)

        # If no processes are found in the ready queue, increment the time
        if not ready_queue:
            current_time += 1
            continue

        # Select the next process in a round-robin fashion
        last_executed = (last_executed + 1) % len(ready_queue)
        idx = ready_queue[last_executed]

        # If the process has not started yet, record the response time
        if response_time[idx] == -1:
            response_time[idx] = current_time - arrival_time[idx]

        # Calculate the time to run this process
        if remaining_time[idx] > time_quantum:
            gantt_chart.append(f"P{idx + 1}")
            gantt_times.append(current_time)
            current_time += time_quantum
            remaining_time[idx] -= time_quantum
        else:
            gantt_chart.append(f"P{idx + 1}")
            gantt_times.append(current_time)
            current_time += remaining_time[idx]
            completion_time[idx] = current_time
            turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
            waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
            remaining_time[idx] = 0
            completed += 1
            ready_queue.pop(last_executed)  # Remove from queue when complete
            last_executed -= 1  # Adjust index for the removed process

    # Output the results
    print("\nRound Robin Scheduling:")
    print("Process No. Arrival Time   Burst Time  Completion Time   Turnaround Time   Waiting Time   Response Time")
    for i in range(n):
        print(f"{i + 1:<12} {arrival_time[i]:<14} {burst_time[i]:<11} {completion_time[i]:<17} {turnaround_time[i]:<17} {waiting_time[i]:<13} {response_time[i]:<14}")

    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    # Gantt chart output
    gantt_times.append(current_time)  # Add the last time slot
    print("\nGantt Chart:")
    print("|", " | ".join(gantt_chart), "|")
    print(" ".join(map(str, gantt_times)))

# Call the Round Robin function
round_robin()
