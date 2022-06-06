processes = [1, 2, 3, 4, 5, 6]
burst_time = [7, 5, 3, 1, 2, 1]
num = len(processes)
quantum = 4


def waiting_time(processes, num, burst_time, wait_time, quantum):
    remaining_burst_time = [0] * num
    for i in range(num):
        remaining_burst_time[i] = burst_time[i]
    current_time = 0
    while(1):
        completed = True
        for i in range(num):
            if(remaining_burst_time[i] > 0):
                completed = False
                if(remaining_burst_time[i] > quantum):
                    current_time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    current_time = current_time + remaining_burst_time[i]
                    wait_time[i] = current_time - burst_time[i]
                    remaining_burst_time[i] = 0
        if(completed == True):
            break


def turn_around_time(processes, num, burst_time, wait_time, turn_ar_time):
    for i in range(num):
        turn_ar_time[i] = burst_time[i] + wait_time[i]


def average_time(processes, num, burst_time, quantum):
    wait_time = [0] * num
    turn_ar_time = [0] * num
    total_wait_time = 0
    total_turn_ar_time = 0

    waiting_time(processes, num, burst_time, wait_time, quantum)
    turn_around_time(processes, num, burst_time, wait_time, turn_ar_time)

    print("Processes " " Burst Time " + " Wait Time " + " Turnaround Time")
    for i in range(num):
        total_wait_time = total_wait_time + wait_time[i]
        total_turn_ar_time = total_turn_ar_time + turn_ar_time[i]
        print("   P" + str(i + 1) + "\t\t" +
              str(burst_time[i]) + "\t  " + str(wait_time[i]) + "\t\t " + str(turn_ar_time[i]))

    print("Average Waiting Time = " + str(round(total_wait_time / num, 2)))
    print("Average Turnaround Time = " +
          str(round(total_turn_ar_time / num, 2)))


average_time(processes, num, burst_time, quantum)
