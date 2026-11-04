
from itertools import product

print("P Q R | Q->P P->~Q Q∨R | KB")

models = []

for P, Q, R in product([False, True], repeat=3):

    rule1 = (not Q) or P
    rule2 = (not P) or (not Q)
    rule3 = Q or R

    KB = rule1 and rule2 and rule3

    print(int(P), int(Q), int(R), "| ",
          int(rule1), "   ", int(rule2), "   ",
          int(rule3), " | ", int(KB))

    if KB:
        models.append((P, Q, R))

print("\nModels of KB:", models)

# Check queries
queries = {
    "R": lambda P, Q, R: R,
    "R -> P": lambda P, Q, R: (not R) or P,
    "Q -> R": lambda P, Q, R: (not Q) or R
}

for query, func in queries.items():
    entails = all(func(P, Q, R) for P, Q, R in models)
    print("KB entails", query, ":", entails)
