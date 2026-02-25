# R Programming - A622 | Complete Practice Questions & Answers

> **Total Unique Questions: 55** (compiled from 6 exam papers, duplicates removed)
> Each question includes the **correct answer** and a detailed **explanation**.
> Questions where multiple answers may be valid are clearly flagged.

---

## Table of Contents

1. [R Basics & Environment](#1-r-basics--environment)
2. [Data Types & Data Structures](#2-data-types--data-structures)
3. [Operators & Expressions](#3-operators--expressions)
4. [Control Flow (if/else, loops)](#4-control-flow-ifelse-loops)
5. [Functions & Commands](#5-functions--commands)
6. [Data Manipulation](#6-data-manipulation)
7. [Matrices & Arrays](#7-matrices--arrays)
8. [Statistics & Hypothesis Testing](#8-statistics--hypothesis-testing)
9. [Regression Analysis](#9-regression-analysis)
10. [Machine Learning & Classification](#10-machine-learning--classification)
11. [Clustering & Association Rules](#11-clustering--association-rules)
12. [Data Visualization & Analytics](#12-data-visualization--analytics)

---

## 1. R Basics & Environment

---

### Q1. What does A stand for in CRAN?

A. Acknowledge
B. Archive
C. Applied
D. Academic

**Correct Answer: B. Archive**

**Explanation:** CRAN stands for **Comprehensive R Archive Network**. It is a network of servers around the world that store identical, up-to-date versions of R code, packages, and documentation. The word "Archive" reflects its role as a repository/storage for R packages.

---

### Q2. ____________ is an open source language used as statistical and visualization software.

A. R
B. Python
C. C++
D. Java

**Correct Answer: A. R**

**Explanation:** R was specifically designed for statistical computing and data visualization. While Python can also be used for statistics, R is purpose-built for it. C++ and Java are general-purpose languages not primarily designed for statistics. R is free and open source under the GNU General Public License.

---

### Q3. Which software does not recognize R?

A. SAS
B. Python
C. C
D. C++

**Correct Answer: C. C**

**Explanation:** This is a somewhat ambiguous question. SAS has R integration capabilities, Python can interface with R via the `rpy2` package, and C++ integrates with R through the popular `Rcpp` package. While R itself is built using C and Fortran, the C language does not natively "recognize" or interface with R in the way the other options do. C is a low-level language that does not have a dedicated R integration framework comparable to `rpy2` (Python) or `Rcpp` (C++).

> **Note:** This question is debatable. R has a C API (`.C()` function), so technically C can interface with R too. The intended answer likely focuses on which language lacks a well-known, commonly-used R integration package.

---

### Q4. To comment in R software, which character is placed at the beginning?

A. \*
B. \#\#
C. \#
D. \*\*

**Correct Answer: C. #**

**Explanation:** In R, the `#` symbol is used to write comments. Everything after `#` on that line is ignored by the R interpreter. R does not have multi-line comment syntax (like `/* */` in C). While `##` also works (it starts with `#`), the standard single `#` is the correct commenting character. `*` and `**` are not used for comments in R.

---

### Q5. Which one of the following options is not a feature of CRAN?

A. Allows updating packages with open source license
B. Allows to upload self-built packages
C. Allows downloading any package
D. Allows updation without open source license

**Correct Answer: D. Allows updation without open source license**

**Explanation:** CRAN requires all packages to have an open source license. This is a core policy of CRAN - every package uploaded must comply with open source licensing requirements. Options A, B, and C are all valid features of CRAN. Option D violates this policy, making it the feature that CRAN does **not** support.

---

### Q6. Which one of the following is the left assignment?

A. `age <- 18`
B. `age -> 18`
C. `18 -> age`
D. `18 <- age`

**Correct Answer: A. `age <- 18`**

**Explanation:** In R, the **left assignment operator** is `<-`. It assigns the value on the right to the variable on the left. So `age <- 18` assigns the value 18 to the variable `age`. Option C (`18 -> age`) uses the **right assignment** operator, which also works but is NOT left assignment. Option B is invalid syntax. Option D would try to assign `age` to the literal `18`, which doesn't work.

---

## 2. Data Types & Data Structures

---

### Q7. Which one of the following options is not a Data Structure in R?

A. Atomic Vector
B. Arrays
C. Tuples
D. Factor

**Correct Answer: C. Tuples**

**Explanation:** R does not have a native Tuple data structure. Tuples are a feature of Python, not R. The main data structures in R are:
- **Atomic Vectors** (homogeneous, 1D)
- **Lists** (heterogeneous, 1D)
- **Matrices** (homogeneous, 2D)
- **Arrays** (homogeneous, n-dimensional)
- **Data Frames** (heterogeneous, 2D)
- **Factors** (categorical data)

All options except Tuples are valid R data structures.

---

### Q8. Which one of the following options is not a homogeneous data structure?

A. Factor
B. Data Frame
C. Array
D. Atomic Vectors

**Correct Answer: B. Data Frame**

**Explanation:** A **Data Frame** is a heterogeneous data structure in R - it can hold columns of different data types (numeric, character, logical, etc.). In contrast:
- **Atomic Vectors** hold elements of only one type (homogeneous)
- **Arrays** are multi-dimensional and hold only one type (homogeneous)
- **Factors** store categorical data of one type (homogeneous)

A Data Frame is essentially a list of equal-length vectors, where each column can be a different type.

---

### Q9. In `int a = 5` statement, what is `int`?

A. Data Structure
B. Data Type
C. Data Base
D. Data Variable

**Correct Answer: B. Data Type**

**Explanation:** `int` is a **data type** declaration that specifies the kind of data a variable can hold. In languages like C/C++/Java, `int` tells the compiler that variable `a` will store integer values. A data type defines the type of value (integer, float, character, etc.), while a data structure (like arrays, lists) defines how data is organized. Note: R itself doesn't use `int` declarations like this, but the concept of data types still applies.

---

### Q10. X = Factor, Y = Numeric. Which one of these is a data structure and a data type?

A. X is a data structure, Y is a data type
B. Both X and Y are data type
C. Both X and Y are data structure
D. X is a data type and Y is a data structure

**Correct Answer: A. X is a data structure, Y is a data type**

**Explanation:** In R:
- **Factor** is a **data structure** - it is a special vector that stores categorical data with predefined levels. It has structure (levels, labels, internal integer codes).
- **Numeric** is a **data type** - it defines the kind of value (numbers with decimals). It tells R what kind of data is stored, not how it is organized.

The distinction is: data types define *what kind* of values are stored, while data structures define *how* data is organized and accessed.

---

## 3. Operators & Expressions

---

### Q11. What is the output of `5 %% 2`?

A. 2
B. 3
C. 1
D. 0

**Correct Answer: C. 1**

**Explanation:** The `%%` operator in R is the **modulus (remainder)** operator. It returns the remainder after division.
- `5 %% 2` = 5 divided by 2 = **2 remainder 1**
- So the output is **1**

Think of it as: 5 = 2 × 2 + **1** → the remainder is 1.

---

### Q12. What is the output of `9 %/% 2`?

A. 8
B. 4
C. 3
D. 1

**Correct Answer: B. 4**

**Explanation:** The `%/%` operator in R is the **integer division** operator. It divides and returns only the whole number part (floor of the division), discarding any remainder.
- `9 %/% 2` = floor(9 ÷ 2) = floor(4.5) = **4**

Regular division `9 / 2` would give `4.5`, but integer division truncates to `4`.

---

### Q13. What is the output of `4 ^ 3`?

A. 72
B. 41
C. 64
D. 20

**Correct Answer: C. 64**

**Explanation:** The `^` operator in R is the **exponentiation** operator.
- `4 ^ 3` = 4 × 4 × 4 = **64**

This raises 4 to the power of 3 (4 cubed). You can also use `**` for exponentiation in R, e.g., `4 ** 3` also gives 64.

---

### Q14. What is the output of `2 != 3`?

A. FALSE
B. TRUE
C. Cannot Say
D. None of these

**Correct Answer: B. TRUE**

**Explanation:** The `!=` operator in R means **"not equal to"**. It checks whether two values are different.
- Is 2 not equal to 3? **Yes**, 2 and 3 are different numbers.
- Therefore, the output is **TRUE**.

If the values were equal (e.g., `2 != 2`), the result would be FALSE.

---

### Q15. If `x = 1, y = 2`, what is the output of `x == 1 || y == 3`?

A. TRUE
B. FALSE
C. Cannot Say
D. None of these

**Correct Answer: A. TRUE**

**Explanation:** The `||` operator is the **logical OR** operator in R. It returns TRUE if **at least one** condition is TRUE.
- `x == 1` → `1 == 1` → **TRUE**
- `y == 3` → `2 == 3` → **FALSE**
- `TRUE || FALSE` → **TRUE**

With OR (`||`), only one condition needs to be TRUE for the whole expression to be TRUE. Since `x == 1` is TRUE, the result is TRUE regardless of the second condition.

---

### Q16. What is the output of `x < 1 && y > 4`, if `x = 1, y = 2`?

A. TRUE
B. FALSE
C. Cannot Say
D. None of these

**Correct Answer: B. FALSE**

**Explanation:** The `&&` operator is the **logical AND** operator in R. It returns TRUE only if **both** conditions are TRUE.
- `x < 1` → `1 < 1` → **FALSE** (1 is not less than 1, it's equal)
- `y > 4` → `2 > 4` → **FALSE**
- `FALSE && FALSE` → **FALSE**

With AND (`&&`), both conditions must be TRUE. Since both are FALSE, the result is FALSE. Even if one were TRUE, the result would still be FALSE because AND requires both.

---

## 4. Control Flow (if/else, loops)

---

### Q17. What is the output of the following code?

```r
Age <- 20
if (Age > 18) {
    print("Major")
} else {
    print("Minor")
}
```

A. Major
B. Minor
C. Code Wrong
D. None of these

**Correct Answer: A. Major**

**Explanation:** The variable `Age` is assigned the value 20. The `if` condition checks whether `Age > 18`:
- Is `20 > 18`? → **YES (TRUE)**
- So the code inside the `if` block executes: `print("Major")`
- The `else` block is skipped

Output: `"Major"`

---

### Q18. What is the output of the following code?

```r
Data <- c(2,4,6,8,10)
for (i in data) {
    print(i*2)
}
```

A. 2 4 6 8 10
B. 4 8 12 16 20
C. 4 8 14 16 20
D. 2 8 14 16 22

**Correct Answer: B. 4 8 12 16 20** (with important caveat below)

**Explanation:**
**If the code worked as intended**, the `for` loop would iterate through each element of the vector `c(2,4,6,8,10)` and multiply each by 2:
- 2 × 2 = 4
- 4 × 2 = 8
- 6 × 2 = 12
- 8 × 2 = 16
- 10 × 2 = 20

Result: **4 8 12 16 20**

> **IMPORTANT CAVEAT - Case Sensitivity Issue:** R is **case-sensitive**. The vector is stored in `Data` (capital D), but the for loop references `data` (lowercase d). In R, `data` is a built-in function, NOT the vector `Data`. Running this code would actually produce an **error** (`invalid for() loop sequence`). However, the exam expects answer **B**, treating the code as if `data` and `Data` refer to the same variable. This is likely an intentional trick question testing case-sensitivity awareness, or simply a typo in the exam paper.

---

## 5. Functions & Commands

---

### Q19. __________ command can be invoked to run an R script from the command line.

A. R file()
B. R Console()
C. R script()
D. R Data()

**Correct Answer: C. R script()**

**Explanation:** The `Rscript` command is used to run R scripts from the command line/terminal. For example: `Rscript myscript.R` will execute the R code in `myscript.R`. The other options are not valid commands for running R scripts from the command line. `R Console()` is not a command, `R file()` doesn't exist, and `R Data()` is not used for script execution.

---

### Q20. A __________ is a code to execute a specific task.

A. Function
B. Command
C. Block
D. Data

**Correct Answer: A. Function**

**Explanation:** A **function** is a reusable block of code designed to perform a specific task. In R, functions are defined using the `function()` keyword and can accept parameters and return values. Examples: `mean()`, `sum()`, `print()`. While "command" and "block" are related concepts, the most accurate term for "code to execute a specific task" is **function**. Data is not code at all.

---

### Q21. Which function converts a string from lower case to upper case?

A. tolower()
B. toupper()
C. toLower()
D. toUpper()

**Correct Answer: B. toupper()**

**Explanation:** In R:
- `toupper()` converts a string to **UPPER CASE** (e.g., `toupper("hello")` → `"HELLO"`)
- `tolower()` converts a string to **lower case** (e.g., `tolower("HELLO")` → `"hello"`)
- `toLower()` and `toUpper()` are **NOT valid R functions** (these are JavaScript-style naming conventions)

Note: R uses all-lowercase function names by convention, not camelCase.

---

### Q22. Which one of the following options will install dplyr?

A. installall.packages("dplyr")
B. install.packages("dplyr")
C. installed.packages("dplyr")
D. installany.packages("dplyr")

**Correct Answer: B. install.packages("dplyr")**

**Explanation:** The correct function to install packages in R is `install.packages()`. It downloads and installs the specified package from CRAN.
- `installed.packages()` (option C) is a real R function, but it **lists** already installed packages rather than installing new ones.
- `installall.packages()` and `installany.packages()` do not exist in R.

Usage: `install.packages("dplyr")` installs the dplyr package. After installation, use `library(dplyr)` to load it.

---

### Q23. Identify the function that allows you to choose specific columns from large datasets.

A. Filter()
B. Search()
C. Choose()
D. Select()

**Correct Answer: D. Select()**

**Explanation:** In the `dplyr` package (part of the tidyverse):
- `select()` is used to **choose specific columns** from a data frame
- `filter()` is used to choose specific **rows** based on conditions
- `Search()` and `Choose()` are not standard dplyr functions for column selection

Example: `select(data, column1, column2)` returns only the specified columns.

---

## 6. Data Manipulation

---

### Q24. What is the output of the following code?

```r
data <- c(4,5,6,7,8)
length(data)
```

A. 2
B. 3
C. 4
D. 5

**Correct Answer: D. 5**

**Explanation:** The `c()` function creates a vector combining the values 4, 5, 6, 7, 8. The `length()` function returns the **number of elements** in the vector.
- The vector `data` contains 5 elements: `4, 5, 6, 7, 8`
- `length(data)` = **5**

Note: `length()` counts the number of elements, not the range or sum of values.

---

### Q25. What is the output of the following?

```r
data <- matrix(c(2,1,3,2), 2, 2)
apply(data, 1, sum)
```

A. 3, 5
B. 4, 4
C. 5, 3
D. None of these

**Correct Answer: C. 5, 3**

**Explanation:** Step by step:

**Step 1:** `matrix(c(2,1,3,2), 2, 2)` creates a 2×2 matrix filled **column-wise** (R default):
```
     [,1] [,2]
[1,]   2    3
[2,]   1    2
```
The vector `c(2,1,3,2)` fills: column 1 gets (2,1), column 2 gets (3,2).

**Step 2:** `apply(data, 1, sum)` applies `sum` along **MARGIN = 1 (rows)**:
- Row 1: 2 + 3 = **5**
- Row 2: 1 + 2 = **3**

Output: **5, 3**

---

### Q26. Identify the output of the following code.

```r
x <- list(a = 1:5, b = rnorm(10))
lapply(x, mean)
```

A. `$a [1] 3` and `$b [1] 0.1322028`
B. `$a [1] 4` and `$b [1] 0.1322028`
C. `$a [1] 5` and `$b [1] 0.1322028`
D. `$a [1] 6` and `$b [1] 0.1322028`

**Correct Answer: A. `$a [1] 3`**

**Explanation:** `lapply()` applies a function to each element of a list and returns a list.
- `mean(1:5)` = mean of (1, 2, 3, 4, 5) = 15 / 5 = **3**
- `mean(rnorm(10))` = mean of 10 random normal values (this varies each run)

Since `mean(1:5)` is definitively **3**, the correct answer is **A**. The `$b` value depends on the random number generator and will differ each time, but the `$a` value is always 3. This is how we determine the answer.

---

## 7. Matrices & Arrays

---

### Q27. In R, by default, a matrix is filled __________.

A. row-wise
B. column-wise
C. Rand only
D. First row, then column

**Correct Answer: B. column-wise**

**Explanation:** By default, R fills matrices **column by column** (column-major order). For example:
```r
matrix(1:6, nrow=2, ncol=3)
```
Produces:
```
     [,1] [,2] [,3]
[1,]   1    3    5
[2,]   2    4    6
```
The values fill down column 1 first, then column 2, then column 3. To fill row-wise, you must explicitly set `byrow = TRUE`:
```r
matrix(1:6, nrow=2, ncol=3, byrow=TRUE)
```

---

### Q28. Elements in R are accessed using __________.

A. []
B. {}
C. ()
D. [{}]

**Correct Answer: A. []**

**Explanation:** In R, square brackets `[]` are used to **access/index elements** of vectors, matrices, data frames, and lists.
- `x[1]` accesses the first element of vector x
- `m[1,2]` accesses row 1, column 2 of matrix m
- `df[,"col"]` accesses a column in a data frame

The other brackets have different purposes:
- `()` is used for function calls: `mean(x)`
- `{}` is used for code blocks: `if(TRUE) { ... }`
- `[{}]` is not a valid indexing syntax in R

---

### Q29. In a 3-dimensional array, the order of an array is `c(3,4,2)`. What does each number represent?

A. 3 is the number of rows, 4 is the number of columns, 2 is the number of matrices
B. 4 is the number of rows, 2 is the number of columns, 3 is the number of matrices
C. 2 is the number of rows, 4 is the number of columns, 3 is the number of matrices
D. 4 is the number of rows, 3 is the number of columns, 2 is the number of matrices

**Correct Answer: A. 3 is the number of rows, 4 is the number of columns, 2 is the number of matrices**

**Explanation:** In R's `array()` function, the `dim` parameter follows the order: **(rows, columns, layers/matrices)**.
- `c(3, 4, 2)` means:
  - **3** = number of rows
  - **4** = number of columns
  - **2** = number of matrices (layers/slices)

This creates 2 matrices, each with 3 rows and 4 columns. This follows R's convention of specifying dimensions as (row, column, depth).

---

### Q30. If you want to access the third row of the second matrix of a 3-dimensional array `A`, what will be the code? (considering `A` of order `c(4,4,2)`)

A. A[3,3,2]
B. A[3,,3]
C. A[3,,1]
D. A[3,,2]

**Correct Answer: D. A[3,,2]**

**Explanation:** In R's array indexing: `A[row, column, matrix]`
- **Third row** → first index = 3
- **All columns** → second index is left **empty** (meaning "select all")
- **Second matrix** → third index = 2

So `A[3,,2]` means: "Give me the 3rd row, all columns, from the 2nd matrix."
- `A[3,3,2]` would give only one element (row 3, column 3, matrix 2) - not the entire row
- `A[3,,3]` would try to access a 3rd matrix, but only 2 exist (error)
- `A[3,,1]` would give the 3rd row of the **1st** matrix, not the 2nd

---

## 8. Statistics & Hypothesis Testing

---

### Q31. A null hypothesis is denoted by ______.

A. H1
B. H0
C. H2
D. H4

**Correct Answer: B. H0**

**Explanation:** The **null hypothesis** is denoted by **H₀** (H-zero or H-naught). It represents the default assumption that there is no effect or no difference. The **alternative hypothesis** is denoted by **H₁** (or Hₐ). H2 and H4 are not standard statistical notation.

---

### Q32. Which one of the following options is the opposite of Null Hypothesis?

A. True Hypothesis
B. Alternative Hypothesis
C. Value Hypothesis
D. None of these

**Correct Answer: B. Alternative Hypothesis**

**Explanation:** The **Alternative Hypothesis (H₁ or Hₐ)** is the opposite of the Null Hypothesis (H₀). It represents the claim that there IS an effect, difference, or relationship. In hypothesis testing:
- **H₀ (Null)**: No effect / no difference (status quo)
- **H₁ (Alternative)**: There IS an effect / difference (what you're trying to prove)

"True Hypothesis" and "Value Hypothesis" are not standard statistical terms.

---

### Q33. In _______ hypothesis, there exists a relationship between two variables, one dependent and another independent.

A. Statistical
B. Complex
C. TRUE
D. Simple

**Correct Answer: D. Simple**

**Explanation:** A **Simple Hypothesis** states a relationship between exactly **two variables** - one dependent and one independent. For example: "Increased study time (independent) leads to higher test scores (dependent)."

A **Complex Hypothesis** involves relationships between **multiple** independent and/or dependent variables. A "Statistical Hypothesis" is a broader term, and "TRUE" is not a type of hypothesis.

---

### Q34. Which one of the following options does the researcher initially assume in the testing hypothesis?

A. The Alternative Hypothesis is true
B. The Null Hypothesis is true
C. Errors cannot be made
D. The population parameter of interest is known

**Correct Answer: B. The Null Hypothesis is true**

**Explanation:** In hypothesis testing, the researcher **always starts by assuming the Null Hypothesis (H₀) is true**. The goal of the test is to determine whether there is enough statistical evidence to **reject** this assumption in favor of the Alternative Hypothesis. This is similar to "innocent until proven guilty" - we assume no effect (H₀) until data proves otherwise.

---

### Q35. What is valid for confidence interval?

A. A confidence interval between 20% and 40% means that the population proportion lies between 20% and 40%
B. A 99% confidence interval procedure has a higher probability of producing intervals that will include the population parameter than a 95% confidence interval procedure
C. An approximate formula for a 95% confidence interval is sample estimate ± margin of error
D. A confidence interval is an interval of values computed from sample data that is likely to include the true population value

**Correct Answer: B. A 99% confidence interval procedure has a higher probability of producing intervals that will include the population parameter than a 95% confidence interval procedure**

**Explanation:**

- **Option A is INCORRECT:** A specific confidence interval (e.g., 20% to 40%) does NOT guarantee the population parameter is within it. The confidence level refers to the long-run success rate of the *procedure*, not a probability statement about one specific interval.

- **Option B is CORRECT:** A 99% CI procedure captures the population parameter 99% of the time vs. 95% for a 95% CI. Higher confidence level = wider interval = higher probability of capturing the parameter.

- **Option C is CORRECT:** The formula `sample estimate ± margin of error` is indeed the standard CI formula.

- **Option D is CORRECT:** This is the general definition of a confidence interval.

> **Multiple Valid Answers:** Options **B, C, and D** are all correct statements. However, **Option A** is a common misconception. If forced to choose one, **B** is the most precise and testable statement that demonstrates understanding of confidence levels. Options C and D, while correct, are more definitional.

---

### Q36. What is the formula for calculating the confidence interval in confidence interval estimation?

A. point estimate − margin of error
B. point estimate + margin of error
C. point estimate ± margin of error
D. point estimate × margin of error

**Correct Answer: C. point estimate ± margin of error**

**Explanation:** The confidence interval formula is:

**CI = point estimate ± margin of error**

This gives us two bounds:
- **Lower bound** = point estimate − margin of error
- **Upper bound** = point estimate + margin of error

Option A (subtraction only) gives only the lower bound. Option B (addition only) gives only the upper bound. Option D (multiplication) is not how confidence intervals are calculated. Only option C with **±** captures both bounds of the interval.

---

## 9. Regression Analysis

---

### Q37. Sum of Squared Residuals (SSR) is a _________.

A. Measure of an unexplained variance
B. Measure of the total variation in Y
C. Measure of an explained variance
D. Measure of minimum variation in Y

**Correct Answer: A. Measure of an unexplained variance**

**Explanation:** In regression analysis:
- **SSR (Sum of Squared Residuals)** = Σ(yᵢ - ŷᵢ)² = the variation in Y that the model **cannot explain** = **unexplained variance**
- **SSE/SSM (Sum of Squares due to regression/Model)** = the variation **explained** by the model
- **SST (Total Sum of Squares)** = total variation in Y = SSR + SSE

Residuals are the differences between actual and predicted values. Large residuals mean the model doesn't fit well, hence SSR measures the unexplained portion.

---

### Q38. The values of R-square lie between __________________.

A. [-1, 1]
B. [0, 1]
C. [0, 8)
D. (-8, 0]

**Correct Answer: B. [0, 1]**

**Explanation:** **R-squared (R²)** is the proportion of variance in the dependent variable that is explained by the independent variable(s).
- **R² = 0** → the model explains **none** of the variance
- **R² = 1** → the model explains **all** of the variance
- R² **cannot be negative** (in standard linear regression) because it's a proportion
- R² **cannot exceed 1** because you can't explain more than 100% of the variance

Note: The **correlation coefficient (r)** ranges from [-1, 1], but **R-squared (R² = r²)** ranges from [0, 1]. Don't confuse the two.

---

### Q39. Which one of the following options can be used to evaluate regression models?

(i) R-squared
(ii) Adjusted R-square
(iii) F Statistics
(iv) RMSE/MSE/MAE

A. (ii) and (iv)
B. (i) and (ii)
C. (ii), (iii), and (iv)
D. (i), (ii), (iii), and (iv)

**Correct Answer: D. (i), (ii), (iii), and (iv)**

**Explanation:** **ALL** of these metrics are used to evaluate regression models:

| Metric | Purpose |
|--------|---------|
| **R-squared** | Measures proportion of variance explained by the model |
| **Adjusted R-squared** | Adjusts R² for the number of predictors (penalizes overfitting) |
| **F Statistics** | Tests overall significance of the model (whether at least one predictor is significant) |
| **RMSE/MSE/MAE** | Measures prediction error (how far predictions are from actual values) |

Each metric provides different insights into model performance. Using them together gives a comprehensive evaluation.

---

### Q40. In the equation `Y = β1 + β2 * X + e`, what do (β1, β2) refer to?

A. (X-intercept, Slope)
B. (Slope, X-intercept)
C. (Y-intercept, Slope)
D. (Slope, Y-intercept)

**Correct Answer: C. (Y-intercept, Slope)**

**Explanation:** The general form of a linear regression equation is: **Y = β₀ + β₁X + ε**

In `Y = β1 + β2 * X + e`:
- **β1** is the **Y-intercept (β₀)** → the value of Y when X = 0
- **β2** is the **Slope (β₁)** → for every 1-unit increase in X, Y increases by β2
- **e** is the error term (residual)

The Y-intercept is NOT the X-intercept. The Y-intercept is where the line crosses the Y-axis (X=0). The slope tells us the rate of change.

---

### Q41. If a linear regression model perfectly fits the training data (training error = 0), then _________.

A. Test error is also always zero
B. Test error is non-zero
C. Cannot comment on test error
D. Test error equals to train error

**Correct Answer: C. Cannot comment on test error**

**Explanation:** A training error of 0 means the model perfectly memorizes the training data, but this tells us **nothing definitive** about test/unseen data performance.
- This is often a sign of **overfitting** - the model learned noise in the training data rather than the underlying pattern
- Test error could be high (overfitting), low (genuinely good model), or anything in between
- We cannot make any guaranteed statement about test error based solely on training error

This is a fundamental concept in machine learning: **low training error does NOT guarantee low test error**.

---

### Q42. Identify the term that describes when the independent variables in a multiple regression model are correlated.

A. Regression
B. Correlation
C. Multi-collinearity
D. Non-collinearity

**Correct Answer: C. Multi-collinearity**

**Explanation:** **Multicollinearity** specifically refers to the situation where two or more **independent (predictor) variables** in a multiple regression model are **highly correlated** with each other.

Problems caused by multicollinearity:
- Unstable and unreliable coefficient estimates
- Inflated standard errors
- Difficulty determining which predictor is truly affecting the outcome
- Can be detected using **VIF (Variance Inflation Factor)**

"Correlation" is a general term, while "multicollinearity" specifically refers to correlation among independent variables in regression.

---

## 10. Machine Learning & Classification

---

### Q43. What is logistic regression used for?

A. Binary Classification
B. Multi-Classification
C. Not used for Classification
D. None of these

**Correct Answer: A. Binary Classification**

**Explanation:** **Logistic regression** is primarily used for **binary classification** - predicting outcomes with exactly two classes (e.g., Yes/No, Spam/Not Spam, 0/1). It models the probability of the outcome being in a particular class using the logistic (sigmoid) function.

> **Note:** While logistic regression CAN be extended to multi-class problems (multinomial logistic regression), in its basic/standard form, it is a **binary** classifier. The exam answer is **A**.

---

### Q44. What should you do to find the best model for Support Vector Machines (SVM)?

A. Maximize the margin
B. Minimize the margin
C. Increase support vectors
D. Decrease data points

**Correct Answer: A. Maximize the margin**

**Explanation:** The core principle of SVM is to find the **optimal hyperplane** that separates classes with the **maximum margin**. The margin is the distance between the hyperplane and the nearest data points (support vectors) from each class.

- **Maximizing the margin** gives better generalization to unseen data
- **Minimizing the margin** would lead to poor generalization
- The number of support vectors is determined by the data, not manually controlled
- Decreasing data points removes information and doesn't improve the model

The optimal SVM model is the one with the **widest possible margin** between classes.

---

### Q45. What is the formula for Bayes' theorem?

A. P(Y|X) = (P(X|Y) × P(Y)) / P(X)
B. P(Y|X) = (P(X|Y) × P(X)) / P(Y)
C. P(Y|X) = P(X|Y) × P(X)
D. P(Y|X) = P(X|Y) × P(Y)

**Correct Answer: A. P(Y|X) = (P(X|Y) × P(Y)) / P(X)**

**Explanation:** Bayes' theorem formula:

**P(Y|X) = [P(X|Y) × P(Y)] / P(X)**

Where:
- **P(Y|X)** = Posterior probability (probability of Y given X)
- **P(X|Y)** = Likelihood (probability of X given Y)
- **P(Y)** = Prior probability of Y
- **P(X)** = Evidence / marginal probability of X

This is the foundation of **Naive Bayes classification**. Option B swaps P(X) and P(Y) incorrectly. Options C and D are missing the denominator P(X).

---

### Q46. How is a nearest neighbor approach best used?

A. With large-sized datasets
B. When irrelevant attributes have been removed from the data
C. When a generalised model of the data is desirable
D. When an explanation of what has been found is of primary importance

**Correct Answer: B. When irrelevant attributes have been removed from the data**

**Explanation:** K-Nearest Neighbor (KNN) is a **distance-based** algorithm. Its performance is heavily affected by irrelevant or noisy features because:
- Irrelevant attributes add meaningless dimensions, distorting distance calculations (curse of dimensionality)
- KNN works best when **only relevant features** are present in the data
- KNN is computationally expensive on large datasets (not A)
- KNN is a "lazy learner" - it doesn't build a generalised model (not C)
- KNN is a "black box" - it doesn't easily explain its decisions (not D)

---

### Q47. Which one of the approaches is best used for the given problem? "Do meaningful attribute relationships exist in a database containing information about credit card customers?"

A. Supervised Learning
B. Unsupervised Learning
C. Data Query
D. Data Inspection

**Correct Answer: B. Unsupervised Learning**

**Explanation:** The question asks about **discovering meaningful relationships** in data without a specific target variable to predict. This is exactly what **unsupervised learning** does:
- It finds hidden patterns, groupings, and relationships in data
- No predefined labels or target variables are needed
- Techniques like clustering and association rules can reveal customer segments and spending patterns

**Supervised learning** requires labeled data with a known target variable. **Data Query** and **Data Inspection** are basic data operations, not analytical methods for finding relationships.

---

### Q48. Supervised learning and unsupervised clustering both require at least one __________.

A. Hidden attribute
B. Output attribute
C. Input attribute
D. Categorical attribute

**Correct Answer: C. Input attribute**

**Explanation:** Both supervised and unsupervised learning require **input attributes** (features/predictors) - this is the data they work with.

The key difference:
- **Supervised learning** requires BOTH input attributes AND output attributes (labels)
- **Unsupervised learning** requires ONLY input attributes (no labels needed)

The **common requirement** for both is at least one **input attribute**. Hidden attributes are not required, output attributes are only needed for supervised learning, and categorical attributes are not mandatory.

---

## 11. Clustering & Association Rules

---

### Q49. You want to use the optimal clustering model. What should you do?

A. Maximize the distance between clusters and minimize the distance within clusters
B. Maximize the distance within clusters, minimize the distance between clusters
C. Maximize the distance within clusters as well as between clusters
D. Minimize the distance within clusters as well as between clusters

**Correct Answer: A. Maximize the distance between clusters and minimize the distance within clusters**

**Explanation:** The goal of optimal clustering is:
- **Minimize intra-cluster distance** (within clusters) → points in the same cluster should be as **close** to each other as possible (high cohesion)
- **Maximize inter-cluster distance** (between clusters) → different clusters should be as **far apart** as possible (high separation)

This creates **tight, well-separated clusters**. Think of it as: "birds of a feather flock together" (close within) while being "far from other flocks" (far between).

---

### Q50. What is the effect of reducing minimum confidence criteria?

A. Number of association rules remains same
B. Some association rules will add to the current set of association rules
C. Some association rules become invalid while others might become a rule
D. Cannot say

**Correct Answer: B. Some association rules will add to the current set of association rules**

**Explanation:** In association rule mining:
- **Confidence** measures how often items in the consequent appear in transactions that contain the antecedent
- **Reducing** the minimum confidence threshold makes the criteria **less strict**
- Rules that previously didn't meet the threshold will now qualify
- **No existing rules are lost** (they still meet the lower threshold)
- Therefore, **new rules are added** to the existing set

Think of it like lowering a height requirement: everyone who qualified before still qualifies, plus shorter people now qualify too.

---

## 12. Data Visualization & Analytics

---

### Q51. Kernel Density plots are used over histogram because it determines the shape of distribution.

A. TRUE
B. FALSE
C. Cannot Say
D. Depends on the data

**Correct Answer: A. TRUE**

**Explanation:** Kernel Density Estimation (KDE) plots are preferred over histograms in many cases because:
- They produce a **smooth, continuous curve** that better represents the underlying distribution shape
- Histograms are sensitive to **bin width** and **bin boundaries** - different binning can show different shapes
- KDE plots are not affected by arbitrary bin choices
- They make it easier to compare multiple distributions on the same plot
- The smooth curve better reveals the true shape (skewness, modality) of the distribution

---

### Q52. Descriptive analytics include ___________.

A. Optimal Decision Making
B. Data queries
C. Data dashboards
D. Both Data query and data dashboards

**Correct Answer: D. Both Data query and data dashboards**

**Explanation:** **Descriptive analytics** answers the question "What happened?" by summarizing historical data. It includes:
- **Data queries** (SQL queries, data retrieval to examine past events)
- **Data dashboards** (visual summaries of key metrics and KPIs)
- Reports, visualizations, and basic statistical summaries

**Optimal Decision Making** falls under **Prescriptive analytics** (the most advanced type), which answers "What should we do?" Descriptive analytics is the most basic form of analytics.

---

### Q53. Which type of analytics gains insight from historical data with reporting, dashboards, and so on?

A. Decisive
B. Description
C. Predictive
D. Prescriptive

**Correct Answer: B. Description (Descriptive Analytics)**

**Explanation:** The four types of analytics:

| Type | Question Answered | Example |
|------|-------------------|---------|
| **Descriptive** | What happened? | Reports, dashboards, historical summaries |
| **Diagnostic** | Why did it happen? | Root cause analysis |
| **Predictive** | What will happen? | Forecasting, predictions |
| **Prescriptive** | What should we do? | Optimization, recommendations |

Reporting and dashboards that summarize historical data fall under **Descriptive analytics**.

---

### Q54. ____________ is a modern equivalent of visual communication that involves visual representation of data.

A. Data Visualization
B. Data Graphics
C. Data Charting
D. Data Presentation

**Correct Answer: A. Data Visualization**

**Explanation:** **Data Visualization** is the standard and widely accepted term for the modern practice of representing data visually using charts, graphs, maps, and other visual elements. It is the formal discipline that combines statistics, design, and computer science to communicate data effectively. While "Data Graphics," "Data Charting," and "Data Presentation" are related concepts, **Data Visualization** is the established, industry-standard term.

---

### Q55. __________ are used when we want to draw the graph between a numeric and a categorical variable.

A. Bar Charts
B. Histogram
C. Boxplots
D. Pie Chart

**Correct Answer: C. Boxplots**

**Explanation:** **Boxplots** are specifically designed to display the **distribution of a numeric variable** across different **categories**:
- X-axis: categorical variable (groups)
- Y-axis: numeric variable (values)
- Shows median, quartiles, range, and outliers for each category

Why not the others?
- **Bar Charts** typically show counts/frequencies of categories (categorical vs count)
- **Histograms** show the distribution of a single numeric variable (no categorical axis)
- **Pie Charts** show proportions of a categorical variable (no numeric distribution)

Boxplots are the ideal choice for comparing a numeric variable across categories (e.g., salary by department).

---

## Summary Table: Quick Answer Key

| # | Topic | Answer |
|---|-------|--------|
| Q1 | A in CRAN | **B. Archive** |
| Q2 | Open source stats language | **A. R** |
| Q3 | Software not recognizing R | **C. C** |
| Q4 | Comment character in R | **C. #** |
| Q5 | Not a CRAN feature | **D. Without open source license** |
| Q6 | Left assignment | **A. age <- 18** |
| Q7 | Not a data structure | **C. Tuples** |
| Q8 | Not homogeneous | **B. Data Frame** |
| Q9 | `int` is a... | **B. Data Type** |
| Q10 | Factor vs Numeric | **A. X=structure, Y=type** |
| Q11 | 5 %% 2 | **C. 1** |
| Q12 | 9 %/% 2 | **B. 4** |
| Q13 | 4 ^ 3 | **C. 64** |
| Q14 | 2 != 3 | **B. TRUE** |
| Q15 | x==1 \|\| y==3 | **A. TRUE** |
| Q16 | x<1 && y>4 | **B. FALSE** |
| Q17 | if (Age > 18) | **A. Major** |
| Q18 | for loop (Data/data) | **B. 4 8 12 16 20** |
| Q19 | Run R script command | **C. R script()** |
| Q20 | Code to execute task | **A. Function** |
| Q21 | Lower to upper case | **B. toupper()** |
| Q22 | Install dplyr | **B. install.packages()** |
| Q23 | Choose columns | **D. Select()** |
| Q24 | length(c(4,5,6,7,8)) | **D. 5** |
| Q25 | apply(data, 1, sum) | **C. 5, 3** |
| Q26 | lapply(x, mean) | **A. $a=3** |
| Q27 | Matrix default fill | **B. column-wise** |
| Q28 | Access elements | **A. []** |
| Q29 | c(3,4,2) meaning | **A. 3 rows, 4 cols, 2 matrices** |
| Q30 | 3rd row, 2nd matrix | **D. A[3,,2]** |
| Q31 | Null hypothesis symbol | **B. H0** |
| Q32 | Opposite of null | **B. Alternative Hypothesis** |
| Q33 | Simple hypothesis | **D. Simple** |
| Q34 | Researcher assumes | **B. Null is true** |
| Q35 | Valid for CI | **B. 99% > 95% probability** |
| Q36 | CI formula | **C. estimate ± margin** |
| Q37 | SSR is | **A. Unexplained variance** |
| Q38 | R-square range | **B. [0, 1]** |
| Q39 | Evaluate regression | **D. All (i)(ii)(iii)(iv)** |
| Q40 | Y = β1 + β2*X + e | **C. (Y-intercept, Slope)** |
| Q41 | Perfect training fit | **C. Cannot comment** |
| Q42 | Correlated predictors | **C. Multi-collinearity** |
| Q43 | Logistic regression | **A. Binary Classification** |
| Q44 | Best SVM model | **A. Maximize margin** |
| Q45 | Bayes' theorem | **A. P(X\|Y)P(Y)/P(X)** |
| Q46 | KNN best used | **B. Irrelevant attrs removed** |
| Q47 | Credit card relationships | **B. Unsupervised Learning** |
| Q48 | Both require | **C. Input attribute** |
| Q49 | Optimal clustering | **A. Max between, min within** |
| Q50 | Reduce min confidence | **B. Rules will add** |
| Q51 | Kernel Density vs Histogram | **A. TRUE** |
| Q52 | Descriptive analytics | **D. Both query & dashboards** |
| Q53 | Historical data analytics | **B. Description** |
| Q54 | Visual representation | **A. Data Visualization** |
| Q55 | Numeric vs Categorical | **C. Boxplots** |

---

*Compiled from 6 R Programming A622 exam papers (90 total questions, 55 unique after deduplication). All answers verified with explanations.*
