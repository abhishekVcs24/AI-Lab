def unify(x, y, substitution=None):
    if substitution is None:
        substitution = {}

    x = substitute(x, substitution)
    y = substitute(y, substitution)

    if x == y:
        return substitution

    if is_variable(x):
        substitution[x] = y
        return substitution

    if is_variable(y):
        substitution[y] = x
        return substitution

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y) or x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            substitution = unify(a, b, substitution)

            if substitution is None:
                return None

        return substitution

    return None


def is_variable(x):
    return isinstance(x, str) and x.isupper()


def substitute(expr, substitution):
    while isinstance(expr, str) and expr in substitution:
        expr = substitution[expr]

    if isinstance(expr, tuple):
        return (expr[0],) + tuple(
            substitute(arg, substitution)
            for arg in expr[1:]
        )

    return expr


# Example expressions:
# AND(P, Q) and AND(A, B)

expr1 = ("AND", "P", "Q")
expr2 = ("AND", "A", "B")

result = unify(expr1, expr2)

if result is not None:
    print("Unification successful")
    print("Substitution:", result)
else:
    print("Unification failed")
