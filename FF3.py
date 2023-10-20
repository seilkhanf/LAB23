def solve(num_heads, num_legs):
    for birds in range(num_heads + 1):
        animals = num_heads - birds
        if 2 * birds + 4 * animals == num_legs:
            return birds, animals
    return None 


num_heads = 35
num_legs = 94
solution = solve(num_heads, num_legs)

if solution:
    birds, animals = solution
    print(f"Birds: {birds}")
    print(f"Rabbits: {animals}")
else:
    print("NOT SOLUTION")