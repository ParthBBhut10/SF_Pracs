# FCFS Disk Scheduling
def FCFS(head, sequence):
    seek_operations = 0
    for i in sequence:
        if i != head:
            print("Moving header from ", head, " to", end=" ")
            if head >= i:
                difference = head - i
                seek_operations += difference
                head = i
            if head <= i:
                difference = i - head
                seek_operations += difference
                head = i
            print(i)

    return seek_operations


if __name__ == "__main__":
    Number_disk = int(input("Enter the number of disks:	"))
    if Number_disk > 0:
        head = int(input("Enter initial header position : 	"))
        while not head in range(Number_disk + 1):
            head = int(input("Please enter valid initial head position :"))
        sequence = []
        sequence = list(map(int, input("Enter the sequence : 	").split()))
        for i in sequence:
            if i < 0 or i > Number_disk:
                print("Sequence out of range")
                exit(0)

        seek_operations = FCFS(head, sequence)
        print("Total number of seek operations : ", seek_operations)
