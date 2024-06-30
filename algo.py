from scipy.optimize import linprog

# Coefficients for the objective function (to minimize)
c = [1, 1, 1, 1] 

# Coefficients for inequality constraints
A = [[1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 1]]
b = [100, 100, 100]

# Bounds for each variable
x0_bounds = (20, 100)
x1_bounds = (20, 100)
x2_bounds = (20, 100)
x3_bounds = (20, 100)

# Solve the linear programming problem
res = linprog(c, A_eq=[[1, 1, 1, 1]], b_eq=[120], bounds=[x0_bounds, x1_bounds, x2_bounds, x3_bounds])

d1, d2, d3, d4 = res.x

# Calculate total red light time Z
Z = 3 * (d1 + d2 + d3 + d4)

print(f"Green light times: d1 = {d1}, d2 = {d2}, d3 = {d3}, d4 = {d4}")
print(f"Total red light time Z = {Z}")
