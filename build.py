import itertools


def solution(t):
    result = []
    values = [v[1] for v in sorted(t.items())]
    result = list("".join(perm) for perm in itertools.product(*values))
    return result

d = {'one': ['a', 'b'], 'two': ['c', 'd']}
print solution(d)
