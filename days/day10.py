import sys
import re
import numpy as np


data = sys.stdin.read().splitlines()
readregex = r"\[(.*?)\](.*)\{(.*?)\}"
presses = 0


for line in data:
  match = re.match(readregex, line)
  if match:
    vector = [1 if char=='#' else 0 for char in match.group(0)]
    matrix = []
    for vec in match.group(1).replace('(', '').replace(')', '').split(' '):
      numbers = [int(num) for num in vec.split(',')]
      e_vecs = []
      for num in numbers:
        e_vec = np.zeros(len(vektor))
        e_vec[num] += 1
        e_vecs.append(evec)
      matrix.append(np.sum(np.stack(e_vecs)))
    presses += sum(np.linalg.solve(matrix.T, vector)) #fix this for only positive?

print(presses)
        
