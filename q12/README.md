# Q12: The Idempotency Prober

## ELI15 Step-by-Step (Complete Beginner)

1. You are given:
   - a CSV with 100 rows
   - a preprocessing function
2. The function does two things:
   - clips numeric columns between their 10th and 90th percentiles
   - fills missing values using forward-fill and backward-fill
3. You must test 3 properties.

## 1. Idempotency

4. Idempotency means:
   - running the function once and running it twice should give the same result
   - in math words: `f(f(x)) = f(x)`
5. So:
   - run `result1 = preprocess(df, "value_a")`
   - run `result2 = preprocess(result1, "value_a")`
6. Then compare each row of `result1` and `result2`.
7. If **any** column in a row changed, that row violates idempotency.
8. For float columns, use tolerance `1e-9`.
9. On this dataset, the count is:
   - `28`

## 2. Monotonicity

10. The monotonicity column here is `value_a`.
11. Look at all row pairs `(A, B)` where:
   - original `value_a` of A is strictly greater than original `value_a` of B
   - and neither original value is null
12. After preprocessing, the order should not reverse.
13. Because clipping is a monotone non-decreasing transform, ties at the clipping boundary are acceptable.
14. So we count a violation only if:
   - original `A > B`
   - but processed `A < B`
15. On this dataset, the count is:
   - `0`

## 3. Null Stability

16. If an input row had no nulls, the output row should also have no nulls.
17. Check each row:
   - if input row null count is `0`
   - but output row null count is greater than `0`
   - then it is a violation
18. Because the preprocessing fills missing values and does not create new nulls here, the count is:
   - `0`

## Files in This Folder

- `records.csv`: copied from your Downloads folder
- `solution.py`: property checker
- `answer.txt`: final submission string

## Run

```powershell
cd C:\Users\sriva\OneDrive\Documents\TDS\ga6\q12
python solution.py
```

## Final Answer To Submit

```text
28,0,0
```
