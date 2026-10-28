def heuristic(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def hill_climbing(state):
    n = len(state)

    while True:
        h = heuristic(state)
        print("State:", state, "Heuristic:", h)

        if h == 0:
            print("Solution found!")
            return state

        best_state = state[:]
        best_h = h

        for col in range(n):
            for row in range(n):
                if state[col] != row:
                    neighbor = state[:]
                    neighbor[col] = row
                    neighbor_h = heuristic(neighbor)

                    if neighbor_h < best_h:
                        best_h = neighbor_h
                        best_state = neighbor

        if best_h >= h:
            print("Hill climbing terminated at local minimum.")
            return state

        state = best_state


# Given initial state
initial_state = [3, 1, 2, 0]

solution = hill_climbing(initial_state)

print("Final state:", solution)
print("Final heuristic:", heuristic(solution))