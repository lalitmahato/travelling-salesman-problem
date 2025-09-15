# Travelling Salesman Problem

*To run the file, enter the following command in the command prompt*
```
python3 Travelling_Salesman_Problem.py
```

---

## Approaches taken to solve the task

- Defines the distance matrix (Based on the given values).
- Generates all possible permutations of cities, leaving the starting city (ie, A)   >>>   [B, C, D, E, F].
- Calculating the total distance for each route starting and ending at A.
  - Starting from the first city (ie, A) to the first permutation city (any [B, C, D, E, F])
  - Calculate the distance between the permutation cities [B, C, D, E, F].
  - Last Permutation city (any [B, C, D, E, F]) to starting city (ie, A).
- If the distance is less than the previously calculated distance, then update the route with the minimum distance.

---
