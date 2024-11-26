def sjf_preemptive():
    # Get the number of processes from user
    n = int(input("Enter the number of processes: "))

    # Initialize lists to hold process data
    arrival_time = []
    burst_time = []
    remaining_time = []
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    response_time = [-1] * n  # Track response time for each process

    # Get arrival and burst times for each process
    for i in range(n):
        arrival_time.append(int(input(f"Enter arrival time for process {i + 1}: ")))
        burst_time.append(int(input(f"Enter burst time for process {i + 1}: ")))
        remaining_time.append(burst_time[i])

    current_time = 0
    completed = 0
    gantt_chart = []  # To keep track of the process names in Gantt chart
    gantt_times = []  # To keep track of time slots for Gantt chart

    while completed < n:
        idx = -1
        min_time = float('inf')

        # Find the process with the minimum remaining time among the processes that have arrived
        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] > 0:
                if remaining_time[i] < min_time:
                    min_time = remaining_time[i]
                    idx = i

        if idx == -1:  # No process is currently ready
            current_time += 1
            continue

        # Record the current process in the Gantt chart
        if not gantt_chart or gantt_chart[-1] != f"P{idx + 1}":
            gantt_chart.append(f"P{idx + 1}")
            gantt_times.append(current_time)

        # Set response time if it's the first time the process is scheduled
        if response_time[idx] == -1:
            response_time[idx] = current_time - arrival_time[idx]

        # Decrease the remaining time of the executing process
        remaining_time[idx] -= 1

        # Check if the process is completed
        if remaining_time[idx] == 0:
            completed += 1
            completion_time[idx] = current_time + 1
            turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
            waiting_time[idx] = turnaround_time[idx] - burst_time[idx]

        current_time += 1

    # Output the results
    print("\nSJF Preemptive Scheduling:")
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

# Call the SJF Preemptive function
sjf_preemptive()
