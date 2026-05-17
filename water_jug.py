from collections import deque

jug1 = int(input("Enter capacity of jug1: "))
jug2 = int(input("Enter capacity of jug2: "))
target = int(input("Enter target amount: "))

visited = set()
queue = deque()
queue.append((0,0))

while queue:
    x, y = queue.popleft()

    if (x,y) in visited:
        continue

    visited.add((x,y))
    print((x,y))

    if x == target or y == target:
        print("Target achieved")
        break

    # Fill jugs
    queue.append((jug1,y))
    queue.append((x,jug2))

    # Empty jugs
    queue.append((0,y))
    queue.append((x,0))

    # Pour jug1 → jug2
    transfer = min(x, jug2-y)
    queue.append((x-transfer, y+transfer))

    # Pour jug2 → jug1
    transfer = min(y, jug1-x)
    queue.append((x+transfer, y-transfer))
