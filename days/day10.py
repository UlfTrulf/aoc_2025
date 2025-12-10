import sys
import re
import numpy as np
from scipy.optimize import milp, LinearConstraint

def check_equal(a,b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

data = sys.stdin.read().splitlines()
readregex = r"\[(.*?)\](.*)\{(.*?)\}"
presses_button = 0
presses_jolatage = 0

for line in data:
    match = re.match(readregex, line)
    if match:
        vector = [1 if char=='#' else 0 for char in match.group(1)]
        read_matrix = []
        for vec in match.group(2).strip().replace('(', '').replace(')', '').split(' '):
            numbers = [int(num) for num in vec.split(',')]
            e_vecs = np.zeros(len(vector))
            for num in numbers:
                e_vec = np.zeros(len(vector))
                e_vec[num] += 1
                e_vecs = np.add(e_vecs, e_vec)
            read_matrix.append(e_vecs)
        matrix = np.array(read_matrix, dtype=np.int64).T
        joltage = [int(num) for num in match.group(3).split(',')]
        joltage = np.array(joltage, dtype=np.int64)

        num_variables = matrix.shape[1]
        num_constraints = matrix.shape[0]
        c = np.ones(num_variables, dtype=np.int64)
        constraints = LinearConstraint(matrix, joltage, joltage)
        integrality = np.ones(num_variables, dtype=np.int64)
        res = milp(c=c, constraints=constraints, integrality=integrality)
        resu = np.array(res.x, dtype=np.int64)
        presses_jolatage += int(np.sum(round(res.fun)))


        vector = np.array(vector, dtype=np.int64)
        s = [np.zeros(matrix.shape[1], dtype=np.int64)]
        visited = {tuple(s[0])}
        buttons = False
        while len(s) > 0:
            cur_sol = s.pop(0)
            vec_sol = np.array(np.matmul(matrix, cur_sol) % 2, dtype=np.int64)
            if check_equal(vec_sol, vector):
                presses_button += np.sum(cur_sol)
                break

            for iter in range(len(cur_sol)):
                next_sol = cur_sol.copy()
                next_sol[iter] += 1
                next_sol_t = tuple(next_sol)
                if next_sol_t not in visited:
                    s.append(next_sol)
                    visited.add(next_sol_t)




print(presses_button)
print(presses_jolatage)
        
