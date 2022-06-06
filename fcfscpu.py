# FCFS CPU Scheduling
def FCFS(process, n):
    # Initailzing some variables that will be used in function
    wait, time = 0, 0
    waitSum, turnSum = 0, 0          # Initializing Sum of Waiting-Time
    # Initializing Sum of Turnaround Time

    print("Process\t    Burst-Time\tWaiting-Time\tTurnaround-Time")
    for i in range(n):                                  # Iterating through all process
        # Turnaround-Time  = Waiting-Time + Burst-Time of Process
        turn = wait + process[i][1]

        print("P" + str(process[i][0]) + "\t\t" + str(process[i]
              [1]) + "\t\t" + str(wait) + "\t\t" + str(turn))
        # Incrementing waiting-time with Burst-Time of current process
        wait += process[i][1]
        waitSum += wait                                 # Incrementing Sum of Wait-Time
        turnSum += turn                                 # Incrementing Sum of Wait-Time

    waitSum -= wait
    # Rounding Average Waiting Time upto 3 decimal places
    avgWaitTime = round(waitSum/n, 3)
    # Rounding Average Turnaround-Time upto 3 decimal places
    avgTurnTime = round(turnSum/n, 3)

    return (avgWaitTime, avgTurnTime)


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of process: ")
            )           # Number of processes
    # Process is list for all the processes to be executed
    process = []

    for i in range(1, n+1):
        process.append(
            [i, int(input("Enter Burst-Time for Process-"+str(i)+": "))])

    print("\n\nFirst Come First Served Scheduling: ")
    resultTuple = FCFS(process, n)
    print("\nAverage Waiting-Time is", resultTuple[0])
    print("Average Turnaround-Time is", resultTuple[1])
