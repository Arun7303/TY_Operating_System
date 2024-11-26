def is_safe_state(processes, avail, max_resources, allot):
    n = len(processes)      # Number of processes
    m = len(avail)          # Number of resources
    # Calculate the Need matrix
    need = [[max_resources[i][j] - allot[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n    # Track finished processes
    safe_seq = []           # To store the safe sequence
    work = avail[:]         # Initialize the work vector with available resources

    while len(safe_seq) < n:  # While not all processes are finished
        allocated = False
        for i in range(n):
            # Check if process i can finish
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                # Process i can be allocated
                work = [work[j] + allot[i][j] for j in range(m)]  # Release resources
                finish[i] = True  # Mark process i as finished
                safe_seq.append(processes[i])  # Add to safe sequence
                allocated = True
        if not allocated:
            # No process could be allocated, so the system is not in a safe state
            return False, []
    return True, safe_seq

if __name__ == "__main__":
    # Input number of processes and resources
    n = int(input("Enter the number of processes: "))
    m = int(input("Enter the number of resources: "))
    processes = list(range(n))  # Process IDs from 0 to n-1

    # Input available resources
    avail = list(map(int, input(f"Enter available instances of resources (space-separated): ").split()))
    
    # Input maximum resources for each process
    print("Enter maximum resources required by each process (space-separated for each process):")
    max_resources = []
    for i in range(n):
        max_row = list(map(int, input(f"Process {i} maximum resources: ").split()))
        max_resources.append(max_row)

    # Input allocated resources for each process
    print("Enter allocated resources for each process (space-separated for each process):")
    allot = []
    for i in range(n):
        allot_row = list(map(int, input(f"Process {i} allocated resources: ").split()))
        allot.append(allot_row)

    # Check for safe state
    safe, safe_sequence = is_safe_state(processes, avail, max_resources, allot)
    if safe:
        print("System is in a safe state.")
        print("Safe sequence is:", safe_sequence)
    else:
        print("System is not in a safe state.")
