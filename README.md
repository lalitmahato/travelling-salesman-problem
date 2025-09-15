# Travelling Salesman Problem

---

*Run the following command*
```
python3 Travelling_Salesman_Problem.py
```

---

## Approaches taken to solve the task

- Defines the distance matrix (Based on the given values).
- Generates all possible permutations of cities, leaving the starting city (ie, A)   >>>   [B, C, D, E, F].
- Calculating the total distance for each route starting and ending at A.
  - Starting from the first city (ie. A) to the first permutation city (any [B, C, D, E, F])
  - Last Permutation city (any [B, C, D, E, F]) to starting city (ie. A).
- Identifies the route with the minimum distance.

---
