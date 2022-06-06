def SJF(process, n):
    # Sorting process according to their Burst Time
    process = sorted(process, key=lambda x: x[1])
    wait = 0
    # Initializng Sum of Wait-Time -> 0
    waitSum, turnSum = 0, 0
    # Initializng Sum of Tuenaround-Time -> 0

    print("Process\t    Burst-Time\tWaiting-Time\tTurnaround-Time")
    # Iterating through all processes
    for i in range(n):
        # Turnaround-Time  = Wait-Time + Burst-Time
        turn = wait + process[i][1]

        print("P" + str(process[i][0]) + "\t\t" + str(process[i]
              [1]) + "\t\t" + str(wait) + "\t\t" + str(turn))
        # Adding wait-time with burst time of current process
        wait += process[i][1]
        waitSum += wait                                     # Incrementing Sum of Wait-Time
        # Incrementing Sum of Turnaround-Time
        turnSum += turn

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
    process = []

    # Taking user-input for Burst-Time of process
    for i in range(1, n+1):
        process.append(
            [i, int(input("Enter Burst-Time for Process-"+str(i)+": "))])

    print("\n\nShortest Job First Scheduling: ")
    resultTuple = SJF(process, n)
    print("\nAverage Waiting-Time is", resultTuple[0])
    print("Average Turnaround-Time is", resultTuple[1])
