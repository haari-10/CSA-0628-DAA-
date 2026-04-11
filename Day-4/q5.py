import itertools

def total_cost(assign, cost):
    return sum(cost[i][assign[i]] for i in range(len(assign)))

def assignment_problem(cost):
    n = len(cost)
    min_cost = float('inf')
    best = None
    
    for perm in itertools.permutations(range(n)):
        c = total_cost(perm, cost)
        if c < min_cost:
            min_cost = c
            best = perm
    return best, min_cost

cost1 = [[3,10,7],[8,5,12],[4,6,9]]
cost2 = [[15,9,4],[8,7,18],[6,12,11]]

print("Test Case 1:", assignment_problem(cost1))
print("Test Case 2:", assignment_problem(cost2))