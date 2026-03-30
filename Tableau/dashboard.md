# Dashboard KPI Formulas

## 1. Employee Count
- **Value:** 1,470
- **Formula:** Raw data field (direct count from source data)
- **Explanation:** Total number of employees in the dataset, both active and attrited.

## 2. Attrition Count
- **Value:** 237
- **Formula:** `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END`
- **Explanation:** Converts the text field "Attrition" into a numeric flag — 1 if the employee left, 0 if they stayed. Summing this gives the total attrition count.

## 3. Attrition Rate
- **Value:** 16.12%
- **Formula:** `SUM([At count]) / SUM([Employee Count])`
- **Explanation:** The percentage of employees who left. Calculated as 237 / 1,470 = 0.1612 → 16.12%.

## 4. Active Employees
- **Value:** 1,233
- **Formula:** `SUM([Employee Count]) - SUM([At count])`
- **Explanation:** Employees still with the company. Calculated as 1,470 - 237 = 1,233.

## 5. Avg. Age
- **Value:** 37
- **Formula:** `AVG([Age])`
- **Explanation:** The mean age across all employees in the dataset. Standard average aggregation on the Age field.
