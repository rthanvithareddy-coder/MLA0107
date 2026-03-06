from collections import deque

def water_jug(capacity, start, goal, refill):

    n = len(capacity)
    visited = set()
    queue = deque([(start, [start])])

    while queue:

        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        if goal(state):
            print("(Jug states)")
            for p in path:
                print(*p)
            print("Goal Reached\n")
            return

        # Pour water
        for i in range(n):
            for j in range(n):

                if i != j and state[i] > 0 and state[j] < capacity[j]:

                    transfer = min(state[i], capacity[j] - state[j])

                    new = list(state)
                    new[i] -= transfer
                    new[j] += transfer

                    queue.append((tuple(new), path + [tuple(new)]))

        # Empty jug
        for i in range(n):
            if state[i] > 0:
                new = list(state)
                new[i] = 0
                queue.append((tuple(new), path + [tuple(new)]))

        # Refill jug (only when allowed)
        if refill:
            for i in range(n):
                if state[i] < capacity[i]:
                    new = list(state)
                    new[i] = capacity[i]
                    queue.append((tuple(new), path + [tuple(new)]))


# ---------------- Problem 1 ----------------
print("Problem 1 (5L, 3L → Target 4L)")
water_jug(
    [5,3],
    (0,0),
    lambda s: 4 in s,
    True
)


# ---------------- Problem 2 ----------------
print("Problem 2 (12L, 8L, 5L → Target 6L)")
water_jug(
    [12,8,5],
    (12,0,0),
    lambda s: 6 in s,
    False
)


# ---------------- Problem 3 ----------------
print("Problem 3 (3L, 5L, 8L → Target 4L in 5L and 8L)")
water_jug(
    [3,5,8],
    (0,0,8),
    lambda s: s[1]==4 and s[2]==4,
    False
)
