import sys

def best_fit(block_size, m, process_size, n):
    allocation = [-1]*n

    for i in range(n):
        best_idx = -1
        for j in range(m):
            if block_size[j] >= process_size[i]:
                if best_idx == -1:
                    best_idx = j
                elif block_size[best_idx] > block_size[j]:
                    best_idx = j

        if best_idx != -1:
            allocation[i] = best_idx
            block_size[best_idx] -= process_size[i]

    print("\nProcess No.\tProcess Size\tBlock no.")
    for i in range(n):
        if allocation[i] != -1:
            print("   "+str(i+1)+"\t\t"+str(process_size[i])+"\t\t"+str(allocation[i]+1))
        else:
            print("   "+str(i+1)+"\t\t"+str(process_size[i])+"\t\tNot Allocated")

def first_fit(block_size, m, process_size, n):
    allocation = [-1]*n

    for i in range(n):
        for j in range(m):
            if block_size[j] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break

    print("\nProcess No.\tProcess Size\tBlock no.")
    for i in range(n):
        if allocation[i] != -1:
            print(" "+str(i+1)+"\t\t"+str(process_size[i])+"\t\t"+str(allocation[i]+1))
        else:
            print(" "+str(i+1)+"\t\t"+str(process_size[i])+"\t\tNot Allocated")

def next_fit(block_size, m, process_size, n):
    allocation = [-1]*n
    j = 0

    for i in range(n):
        while j < m:
            if block_size[j] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break
            j = (j + 1) % m

    print("\nProcess No.\tProcess Size\tBlock no.")
    for i in range(n):
        if allocation[i] != -1:
            print(str(i+1)+"\t\t"+str(process_size[i])+"\t\t"+str(allocation[i]+1))
        else:
            print(str(i+1)+"\t\t"+str(process_size[i])+"\t\tNot Allocated")

def worst_fit(block_size, m, process_size, n):
    allocation = [-1]*n

    for i in range(n):
        wst_idx = -1
        for j in range(m):
            if block_size[j] >= process_size[i]:
                if wst_idx == -1:
                    wst_idx = j
                elif block_size[wst_idx] < block_size[j]:
                    wst_idx = j

        if wst_idx != -1:
            allocation[i] = wst_idx
            block_size[wst_idx] -= process_size[i]

    print("\nProcess No.\tProcess Size\tBlock no.")
    for i in range(n):
        if allocation[i] != -1:
            print("      "+str(i+1)+"\t\t"+str(process_size[i])+"\t\t"+str(allocation[i]+1))
        else:
            print("      "+str(i+1)+"\t\t"+str(process_size[i])+"\t\tNot Allocated")

def main():
    while True:
        print("\nEnter the number of Blocks: ")
        m = int(input())
        print("Enter the number of Processes: ")
        n = int(input())

        block_size = []
        process_size = []

        print("Enter the Size of all the blocks: ")
        for i in range(m):
            block_size.append(int(input()))

        print("Enter the size of all processes: ")
        for i in range(n):
            process_size.append(int(input()))

        while True:
            print("\nMenu")
            print("1. First Fit ")
            print("2. Next Fit")
            print("3. Worst Fit")
            print("4. Best Fit")
            print("5. Change data")
            print("6. Exit")
            print("Select the algorithm you want to implement or change data: ")
            choice = int(input())

            if choice == 1:
                first_fit(block_size[:], m, process_size, n)
            elif choice == 2:
                next_fit(block_size[:], m, process_size, n)
            elif choice == 3:
                worst_fit(block_size[:], m, process_size, n)
            elif choice == 4:
                best_fit(block_size[:], m, process_size, n)
            elif choice == 5:
                break
            elif choice == 6:
                print("Exiting the code...")
                sys.exit()
            else:
                print("Invalid option")

if __name__ =="__main__":
    main()