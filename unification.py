
def unify(x, y, substitution=None):
    if substitution is None:
        substitution = {}

    if x == y:
        return substitution

    if isinstance(x, str) and x.islower():
        if x in substitution:
            return unify(substitution[x], y, substitution)
        if occurs_check(x, y, substitution):
            return None
        substitution[x] = y
        return substitution

    if isinstance(y, str) and y.islower():
        return unify(y, x, substitution)

    if isinstance(x, tuple) and isinstance(y, tuple):
        if x[0] != y[0] or len(x) != len(y):
            return None

        for a, b in zip(x[1:], y[1:]):
            substitution = unify(a, b, substitution)
            if substitution is None:
                return None
        return substitution

    return None


def occurs_check(var, term, substitution):
    if var == term:
        return True
    if term in substitution:
        return occurs_check(var, substitution[term], substitution)
    if isinstance(term, tuple):
        return any(occurs_check(var, t, substitution)
                   for t in term[1:])
    return False


# Example
expr1 = ("Eats", "Riya", "Apple")
expr2 = ("Eats", "Riya", "Apple")

result = unify(expr1, expr2)

if result:
    print("Unification Successful")
    print("Substitution:", result)
else:
    print("Unification Failed")
