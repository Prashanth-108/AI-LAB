
# Initial Knowledge Base (Facts)
KB = [
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
]

# Forward Chaining
def forward_chaining(KB):

    # Apply rules repeatedly
    while True:
        old_size = len(KB)

        for fact in KB[:]:

            # Rule 1: Missile(x) -> Weapon(x)
            if fact[0] == "Missile":
                new_fact = ("Weapon", fact[1])
                if new_fact not in KB:
                    KB.append(new_fact)

            # Rule 2: Enemy(x, America) -> Hostile(x)
            if fact[0] == "Enemy":
                new_fact = ("Hostile", fact[1])
                if new_fact not in KB:
                    KB.append(new_fact)

        # Rule 3: Missile(x) and Owns(A,x)
        #         -> Sells(Robert,x,A)
        for m in KB:
            for o in KB:
                if (m[0] == "Missile" and o[0] == "Owns"
                    and m[1] == o[2] and o[1] == "A"):
                    new_fact = ("Sells", "Robert", m[1], "A")
                    if new_fact not in KB:
                        KB.append(new_fact)

        # Rule 4: Crime rule
        for a in KB:
            for w in KB:
                for s in KB:
                    for h in KB:
                        if (a[0] == "American" and
                            w[0] == "Weapon" and
                            s[0] == "Sells" and
                            h[0] == "Hostile" and
                            a[1] == s[1] and
                            w[1] == s[2] and
                            s[3] == h[1]):

                            new_fact = ("Criminal", a[1])
                            if new_fact not in KB:
                                KB.append(new_fact)

        if len(KB) == old_size:
            break

    return KB


# Execute
result = forward_chaining(KB)

print("Knowledge Base:")
for fact in result:
    print(fact)

# Check Goal
if ("Criminal", "Robert") in result:
    print("\nGoal Proved: Robert is Criminal")
else:
    print("\nGoal Not Proved")
