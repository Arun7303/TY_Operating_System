def fcfs():
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for process {i+1}: "))
        burst_time = int(input(f"Enter burst time for process {i+1}: "))
        processes.append((i+1, arrival_time, burst_time))  # (Process No., Arrival Time, Burst Time)
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time
    gantt_chart = []
    completion_time = [0] * n
    turn_around_time = [0] * n
    waiting_time = [0] * n
    response_time = [0] * n
    current_time = 0
    for i in range(n):
        process_no, arrival_time, burst_time = processes[i]
        if current_time < arrival_time:
            current_time = arrival_time
        completion_time[i] = current_time + burst_time
        current_time += burst_time
        gantt_chart.append((process_no, current_time))
        turn_around_time[i] = completion_time[i] - arrival_time
        waiting_time[i] = turn_around_time[i] - burst_time
        response_time[i] = waiting_time[i]
    avg_tat = sum(turn_around_time) / n
    avg_wt = sum(waiting_time) / n
    # Display results
    print("\nFCFS Scheduling:")
    print(f"{'Process No.':<12}{'Arrival Time':<15}{'Burst Time':<12}{'Completion Time':<18}{'Turnaround Time':<18}{'Waiting Time':<15}{'Response Time':<15}")
    for i in range(n):    print(f"{processes[i][0]:<12}{processes[i][1]:<15}{processes[i][2]:<12}{completion_time[i]:<18}{turn_around_time[i]:<18}{waiting_time[i]:<15}{response_time[i]:<15}")
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}\n")
    # Display Gantt Chart
    print("Gantt Chart:")
    for p, time in gantt_chart:
        print(f"| P{p} ", end="")
    print("|")
    for _, time in gantt_chart:
        print(f"{time} ", end="")
    print("\n")

# Execute FCFS
fcfs()
