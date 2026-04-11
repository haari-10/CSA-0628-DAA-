import itertools

def total_value(items, values):
    return sum(values[i] for i in items)

def is_feasible(items, weights, capacity):
    return sum(weights[i] for i in items) <= capacity

def knapsack(weights, values, capacity):
    n = len(weights)
    best_val = 0
    best_set = []
    
    for i in range(n+1):
        for comb in itertools.combinations(range(n), i):
            if is_feasible(comb, weights, capacity):
                val = total_value(comb, values)
                if val > best_val:
                    best_val = val
                    best_set = comb
    return list(best_set), best_val

w1 = [2,3,1]
v1 = [4,5,3]
c1 = 4

w2 = [1,2,3,4]
v2 = [2,4,6,3]
c2 = 6

print("Test Case 1:", knapsack(w1, v1, c1))
print("Test Case 2:", knapsack(w2, v2, c2))