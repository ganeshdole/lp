def fcfs():
    nop = int(input("Enter No. Of processes: "))
    pname = []
    arr_time = []
    burst_time = []
    completion_time = []
    turn_around_time = []
    waiting_time = []

    for i in range(nop):
        print(f"Enter Process {i + 1} | Enter Arrival Time | Enter Burst Time")
        pname.append(input())
        arr_time.append(int(input()))
        burst_time.append(int(input()))

    for i in range(nop):
        if i == 0:
            completion_time.append(arr_time[i] + burst_time[i])
        else:
            if arr_time[i] > completion_time[i - 1]:
                completion_time.append(arr_time[i] + burst_time[i])
            else:
                completion_time.append(completion_time[i - 1] + burst_time[i])

        turn_around_time.append(completion_time[i] - arr_time[i])
        waiting_time.append(turn_around_time[i] - burst_time[i])

    print("Process\tArrival Time\tBurst Time\tTurnaround Time\tWaiting Time")
    for i in range(nop):
        print(f"{pname[i]}\t{arr_time[i]}\t{burst_time[i]}\t{turn_around_time[i]}\t{waiting_time[i]}")

    total_turnaround_time = sum(turn_around_time)
    total_waiting_time = sum(waiting_time)
    avg_turnaround_time = total_turnaround_time / nop
    avg_waiting_time = total_waiting_time / nop

    print("Average Turnaround Time:", avg_turnaround_time)
    print("Average Waiting Time:", avg_waiting_time)


def preemptive_sjf():
    nop = int(input("Enter no of processes: "))
    pname = []
    arr_time = []
    burst_time = []
    completion_time = [0] * nop
    turn_around_time = [0] * nop
    waiting_time = [0] * nop
    run = [0] * nop
    rp = nop
    time = 0

    for i in range(nop):
        print(f"Enter process {i + 1} arrival time:")
        arr_time.append(int(input()))
        print(f"Enter process {i + 1} burst time:")
        burst_time.append(int(input()))
        pname.append(i + 1)
        run[i] = burst_time[i]

    while rp != 0:
        min_burst = float('inf')
        c = nop
        for i in range(nop):
            if arr_time[i] <= time and run[i] < min_burst and run[i] > 0:
                min_burst = run[i]
                c = i

        if c == nop:
            time += 1
        else:
            run[c] -= 1
            time += 1
            if run[c] == 0:
                completion_time[c] = time
                rp -= 1

    for i in range(nop):
        turn_around_time[i] = completion_time[i] - arr_time[i]
        waiting_time[i] = turn_around_time[i] - burst_time[i]

    print("Process\tArrival Time\tBurst Time\tTurnaround Time\tWaiting Time")
    for i in range(nop):
        print(f"{pname[i]}\t{arr_time[i]}\t{burst_time[i]}\t{turn_around_time[i]}\t{waiting_time[i]}")
    
    total_turnaround_time = sum(turn_around_time)
    total_waiting_time = sum(waiting_time)
    avg_turnaround_time = total_turnaround_time / nop
    avg_waiting_time = total_waiting_time / nop

    print("Average Turnaround Time:", avg_turnaround_time)
    print("Average Waiting Time:", avg_waiting_time)




def priority():
    nop = int(input("Enter the number of processes: "))
    pname = []
    arr_time = []
    burst_time = []
    priority = []
    completion_time = [0] * nop
    turn_around_time = [0] * nop
    waiting_time = [0] * nop

    for i in range(nop):
        pname.append(f"p{i + 1}")
        arr_time.append(0)
        burst_time.append(0)
        priority.append(0)

    for i in range(nop):
        print(f"Enter arrival time for process {i + 1}:")
        arr_time[i] = int(input())
        print(f"Enter burst time for process {i + 1}:")
        burst_time[i] = int(input())
        print(f"Enter priority for process {i + 1}:")
        priority[i] = int(input())

    for i in range(nop - 1):
        for j in range(i + 1, nop):
            if arr_time[i] > arr_time[j]:
                arr_time[i], arr_time[j] = arr_time[j], arr_time[i]
                burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
                priority[i], priority[j] = priority[j], priority[i]
                pname[i], pname[j] = pname[j], pname[i]

    for i in range(nop):
        if i == 0:
            completion_time[i] = arr_time[i] + burst_time[i]
        else:
            completion_time[i] = completion_time[i - 1] + burst_time[i]

        turn_around_time[i] = completion_time[i] - arr_time[i]
        waiting_time[i] = turn_around_time[i] - burst_time[i]

    print("Process\tArrival Time\tBurst Time\tTurnaround Time\tWaiting Time")
    for i in range(nop):
        print(f"{pname[i]}\t{arr_time[i]}\t{burst_time[i]}\t{turn_around_time[i]}\t{waiting_time[i]}")
    
    total_turnaround_time = sum(turn_around_time)
    total_waiting_time = sum(waiting_time)
    avg_turnaround_time = total_turnaround_time / nop
    avg_waiting_time = total_waiting_time / nop

    print("Average Turnaround Time:", avg_turnaround_time)
    print("Average Waiting Time:", avg_waiting_time)




def round_robin():
    nop = int(input("Enter the number of processes: "))
    pname = []
    burst_time = []
    run = []
    completion_time = [0] * nop
    turn_around_time = [0] * nop
    waiting_time = [0] * nop
    rp = nop
    time = 0
    quantom = int(input("Enter Quantom: "))

    for i in range(nop):
        pname.append(f"p{i + 1}")
        burst_time.append(int(input()))
        run.append(burst_time[i])

    i = 0
    while rp != 0:
        if run[i] > quantom:
            run[i] -= quantom
            time += quantom
        elif run[i] <= quantom and run[i] > 0:
            time += run[i]
            run[i] = 0
            completion_time[i] = time
            rp -= 1
        i = (i + 1) % nop

    for i in range(nop):
        turn_around_time[i] = completion_time[i]
        waiting_time[i] = turn_around_time[i] - burst_time[i]

    print("Process\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i in range(nop):
        print(f"{pname[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turn_around_time[i]}\t{waiting_time[i]}")
    
    total_turnaround_time = sum(turn_around_time)
    total_waiting_time = sum(waiting_time)
    avg_turnaround_time = total_turnaround_time / nop
    avg_waiting_time = total_waiting_time / nop

    print("Average Turnaround Time:", avg_turnaround_time)
    print("Average Waiting Time:", avg_waiting_time)


if __name__ == "__main__":
    print("Choose Scheduling Algorithm:")
    print("1. FCFS\n2. Preemptive SJF\n3. Priority\n4. Round Robin")
    choice = int(input())
    if choice == 1:
        fcfs()
    elif choice == 2:
        preemptive_sjf()
    elif choice == 3:
        priority()
    elif choice == 4:
        round_robin()
    else:
        print("Invalid choice. Please select a valid option.")
