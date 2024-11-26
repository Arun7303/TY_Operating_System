def calculate_sjf_non_preemptive(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    time = 0
    completed = 0
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    response_time = [0] * n
    gantt_chart = []  # To store Gantt chart information
    gantt_chart_time = []  # To store Gantt chart time points

    while completed < n:
        # Select processes that have arrived and sort by burst time
        available_processes = [i for i in range(n) if processes[i][1] <= time and completion_time[i] == 0]
        if available_processes:
            idx = min(available_processes, key=lambda x: processes[x][2])  # Select SJF
            gantt_chart.append(processes[idx][0] + 1)  # Add process number to Gantt chart
            gantt_chart_time.append(time)  # Record the current time before execution
            time += processes[idx][2]
            completion_time[idx] = time
            completed += 1
            gantt_chart_time.append(time)  # Record the time after execution
        else:
            time += 1  # Wait for the next process to arrive

    # Calculate turnaround time, waiting time, and response time
    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]
        response_time[i] = waiting_time[i]  # For non-preemptive, response time = waiting time

    # Print results
    print("SJF Non-Preemptive Scheduling:")
    print("Process No. Arrival Time   Burst Time  Completion Time   Turnaround Time   Waiting Time   Response Time")
    for i in range(n):
        print(f"{processes[i][0] + 1:<12} {processes[i][1]:<13} {processes[i][2]:<11} {completion_time[i]:<17} "
              f"{turnaround_time[i]:<16} {waiting_time[i]:<12} {response_time[i]:<13}")
    
    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    # Gantt Chart
    print("\nGantt Chart:")
    for i in range(len(gantt_chart)):
        print(f"| P{gantt_chart[i]} ", end="")
    print("|")
    for t in gantt_chart_time:
        print(t, end=" ")
    print()

# Input from user
if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append((i, arrival_time, burst_time))  # (Process No, Arrival Time, Burst Time)

    calculate_sjf_non_preemptive(processes)
