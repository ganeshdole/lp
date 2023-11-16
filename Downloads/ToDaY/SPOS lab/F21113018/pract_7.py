from collections import deque, OrderedDict

def fifoPageFaults(pages, n, capacity):
    s = set()
    indexes = deque()
    page_faults = 0
    for i in range(n):
        print(f"Processing page {pages[i]}")
        if pages[i] not in s:
            if len(s) < capacity:
                s.add(pages[i])
                indexes.append(pages[i])
            else:
                val = indexes.popleft()
                s.remove(val)
                s.add(pages[i])
                indexes.append(pages[i])
            page_faults += 1
            print(f"Page {pages[i]} is a page fault. Frames: {list(indexes)}")
        else:
            print(f"Page {pages[i]} is a page hit. Frames: {list(indexes)}")
    return page_faults

def lruPageFaults(pages, n, capacity):
    s = set()
    indexes = OrderedDict()
    page_faults = 0
    for i in range(n):
        print(f"Processing page {pages[i]}")
        if pages[i] not in s:
            if len(s) < capacity:
                s.add(pages[i])
            else:
                lru = next(iter(indexes))
                del indexes[lru]
                s.remove(lru)
                s.add(pages[i])
            indexes[pages[i]] = None
            page_faults += 1
            print(f"Page {pages[i]} is a page fault. Frames: {list(indexes)}")
        else:
            del indexes[pages[i]]
            indexes[pages[i]] = None
            print(f"Page {pages[i]} is a page hit. Frames: {list(indexes)}")
    return page_faults

def optimalPageFaults(pages, n, capacity):
    fr = []
    hit = 0
    for i in range(n):
        print(f"Processing page {pages[i]}")
        if pages[i] in fr:
            hit += 1
            print(f"Page {pages[i]} is a page hit. Frames: {list(fr)}")
            continue
        if len(fr) < capacity:
            fr.append(pages[i])
            print(f"Page {pages[i]} is a page fault. Frames: {list(fr)}")
        else:
            j = predict(pages, fr, n, i + 1)
            replaced_page = fr[j]
            fr[j] = pages[i]
            print(f"Page {replaced_page} is replaced by page {pages[i]}. Frames: {list(fr)}")
    return n - hit

def predict(pg, fr, pn, index):
    res = -1
    farthest = index
    for i in range(len(fr)):
        j = 0
        for j in range(index, pn):
            if fr[i] == pg[j]:
                if j > farthest:
                    farthest = j
                    res = i
                break
        if j == pn:
            return i
    return 0 if res == -1 else res

while True:
    print("\nMenu:")
    print("1. FIFO Algorithm")
    print("2. LRU Algorithm")
    print("3. Optimal Algorithm")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1 or choice == 2 or choice == 3:
        pages = list(map(int, input("Enter the page reference sequence (space-separated): ").split()))
        capacity = int(input("Enter the number of frames: "))
        n = len(pages)

        if choice == 1:
            print("FIFO Algorithm:")
            print("Number of page faults =", fifoPageFaults(pages, n, capacity))
        elif choice == 2:
            print("LRU Algorithm:")
            print("Number of page faults =", lruPageFaults(pages, n, capacity))
        elif choice == 3:
            print("Optimal Algorithm:")
            print("Number of page faults =", optimalPageFaults(pages, n, capacity))
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
