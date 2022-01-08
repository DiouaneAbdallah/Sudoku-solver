# Sudoku-solver
This is a sudoku solver using the backtracking algorithm.

## Approach
💡 Like all other Backtracking problems, Sudoku can be solved by one by one assigning numbers to empty cells. 

📌 Before assigning a number, check whether it is safe to assign.

📌 Check that the same number is not present in the current row, current column and current 3X3 subgrid.

📌 After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not.

&emsp;   📍 If the assignment doesn’t lead to a solution, then try the next number for the current empty cell.

&emsp;   📍 If none of the number (1 to 9) leads to a solution, return false and print no solution exists. 
  

## Example

```python
Input:
board = [
        [0, 5, 0, 0, 2, 0, 9, 0, 3],
        [9, 0, 0, 0, 0, 6, 0, 0, 4],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 2, 0, 4, 6, 0, 0, 0, 8],
        [0, 7, 4, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 7, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 5],
        [5, 0, 1, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
Output:
          _ _ _   _ _ _   _ _ _
        | 6 5 8 | 7 2 4 | 9 1 3 |
        | 9 1 7 | 3 8 6 | 2 5 4 |
        | 4 3 2 | 5 1 9 | 6 8 7 |
          - - -   - - -   - - -
        | 1 2 9 | 4 6 7 | 5 3 8 |
        | 3 7 4 | 8 9 5 | 1 6 2 |
        | 8 6 5 | 2 3 1 | 4 7 9 |
          - - -   - - -   - - -
        | 2 9 6 | 1 7 8 | 3 4 5 |
        | 5 8 1 | 9 4 3 | 7 2 6 |
        | 7 4 3 | 6 5 2 | 8 9 1 |
          - - -   - - -   - - -
```
