---
layout: post
title: Solving Systems of Linear Equations
permalink: /guides/solving-systems-of-linear-equations
---
# Solving $A\vec{x} = \vec{b}$

## Introduction

Earlier guides introduced [vectors](vectors) and [matrices](matrices) and showed how we can perform operations with them. These operations will prove useful because it was shown in the [linear systems](linear-systems) guide that we can represent a system of linear equations as matrices and vectors. This wouldn't be all that useful if we couldn't do anything with it. The benefit of representing systems of linear equations this way is that it allows us to perform matrix and vector operations easily to arrive at the solution.

Armed with this knowledge, we are now equipped to solve Harry's system using matrices. Introduced in the [linear systems](linear-systems) guide, Harry has a problem that he needs our help in solving:

> Harry recently set up shop at a baseball game. Things went well, but at the end of the day, Harry realized that he didn't keep track of how many individual hotdogs and hamburgers he sold, but he does have totals. He knows that he sold of a combined total of 50 hotdogs and hamburgers, and he made \\$85.00 total. Harry sells the hotdogs for \\$1.50 and the hamburgers for \\$2.00. In order to restock, Harry would like to know how many hotdogs and hamburgers he individually sold.

Using the details from above, we are able to formalize Harry's problem into a system of linear equations:

$$
\begin{align}
d + h &= 50 \\[3pt]
1.5d + 2h &= 85
\end{align}
$$

We showed that you can represent a system of linear equations using matrices by putting the coefficients into a matrix, $A$, the unknown variables into a vector, $\vec{x}$, and the constants to the right of the equals sign into a vector, $\vec{b}$:

$$
A = \begin{bmatrix}1 & 1 \\ 1.5 & 2\end{bmatrix}, \enspace
\vec{x} = \begin{bmatrix}d \\ h\end{bmatrix}, \enspace
\vec{b} = \begin{bmatrix}50 \\ 85\end{bmatrix}
$$

And, then we can represent this system in the matrix form $A\vec{x} = \vec{b}$:

$$
A\vec{x} = \vec{b} \\[5pt]
\begin{bmatrix}1 & 1 \\ 1.5 & 2\end{bmatrix}
\begin{bmatrix}d \\ h\end{bmatrix}
=
\begin{bmatrix}50 \\ 85\end{bmatrix}
$$

In order to solve this system, we're interested in finding the vector $\vec{x}$ which contains the components $d$ and $h$. After finding the solution $\vec{x}$, we should be able to plug the values back in to the system and verify that the equations equal what we expect them to. To find the solution, we revisit elimination and show how we can apply it systematically to the system in order to find $d$ and $h$. If you need a quick refresher on the basics of elimination, check out the [linear systems](linear-systems) guide.

## Elimination

The goal of elimination is to systematically eliminate variables of a system of linear equations by performing operations until we're left with an equation that only has one variable in it (hence we eliminated all the other variables in that equation). We can then solve for that variable and then _back-substitute_ into the other equations to find the values of other variables. For matrices, elimination is done by performing operations on the rows of the matrix. The types of operations that we're allowed to perform are:

1. Swapping two rows
2. Multiplying a row by a nonzero scalar number
3. Adding (or subtracting) a multiple of one row to another row

We perform these row operations modifying the matrix until the lower left-hand corner of the matrix is filled with zeros. Given the matrix $A$ from above:

$$\begin{bmatrix}1 & 1 \\ 1.5 & 2\end{bmatrix}$$

The goal is to perform operations until we arrive at a matrix that resembles the following (note, the `*` is a placeholder for a number):

$$\begin{bmatrix}* & * \\ 0 & *\end{bmatrix}$$

In doing so, the last row represents an equation with only one variable that we can easily solve for. The steps for elimination are pretty straightforward: we start with the first row, and repeat the following 2 steps for all rows or until the matrix has all zeros in the bottom left corner:

  1. Find the first non-zero element in the row. This element is called the **pivot**
  2. Use one of the above row operations to get all zeros below the pivot

When performing row operations, we need to be careful that the operations are performed to both sides of the equation. In other words, when performing an operation to a row of $A$, we need to ensure the same operation is performed to the corresponding component of $\vec{b}$. Let's see how we can do elimination on the matrix $A$ above:

$$\begin{bmatrix}1 & 1 \\ 1.5 & 2\end{bmatrix}$$

Starting with the first row, the first step is to find the pivot, which is $1$ in position $A_{1,1}$ (highlighted in red below). The next step is to use a row operation to turn all components below the pivot into $0$. Since $A$ has only 2 rows, we just need to turn $1.5$ in position $A_{2,1}$ into $0$. We can do this in a couple of steps. First, using operation 2, let's multiply the first row by $1.5$:

$$
\begin{bmatrix}\color{red}{1} & 1 \\ 1.5 & 2\end{bmatrix} \xrightarrow{\text{R1 = 1.5*R1}} \begin{bmatrix}(1.5) * 1& (1.5) * 1 \\ 1.5 & 2\end{bmatrix} = \begin{bmatrix}1.5 & 1.5 \\ 1.5 & 2\end{bmatrix}
$$

A quick aside for notation: it's common to log the operations that are being performed to the matrix by putting them above the arrow. In the example above, $R1 = 1.5 * R1$ can be interpreted as: replace row 1 with $1.5$ times itself. This is equivalent to multiplying the row by a scalar number. Remember, anything we do to a row of $A$, we need to also do to the corresponding component of $\vec{b}$. So, let's also multiply the first component of $\vec{b}$ by $1.5$:

$$
\begin{bmatrix}50 \\ 85\end{bmatrix} \xrightarrow{\text{R1 = 1.5*R1}} \begin{bmatrix}(1.5) * 50 \\ 85\end{bmatrix} = \begin{bmatrix}75 \\ 85\end{bmatrix}
$$


The third row operation allows us to add/subtract a multiple of one row to/from another row. Since we're looking to turn $1.5$ into $0$ and the value above $1.5$ is $1$, we can subtract the first row from the second row:

$$
\begin{bmatrix}1.5 & 1.5 \\ 1.5 & 2\end{bmatrix} \xrightarrow{\text{R2 = R2 - R1}} \begin{bmatrix}1.5  & 1.5 \\ 1.5 - (1.5) & 2 - (1.5)\end{bmatrix} = \begin{bmatrix}1.5 & 1.5 \\ 0 & 0.5\end{bmatrix}
$$

Similarly for $\vec{b}$, we need to subtract the first row from the second row:

$$
\begin{bmatrix}75 \\ 85\end{bmatrix} \xrightarrow{\text{R2 = R2 - R1}} \begin{bmatrix}75 \\ 85 - (75)\end{bmatrix} = \begin{bmatrix}75 \\ 10\end{bmatrix}
$$

Going back to $A$, there are no more components below the pivot in $A_{1,1}$, so we're done with this row. If $A$ had a third row, the next step would be get a $0$ in the $A_{3,1}$ position, and so on and so forth for all the other components below the pivot. But, since we only have 2 rows, we're done with the first row.

We now move on to the second row and repeat the same process. The first step is to identify the pivot in the second row. The first non-zero component in the second row is $0.5$ in $A_{2,1}$:

$$\begin{bmatrix}1.5 & 1.5 \\ 0 & \color{red}{0.5}\end{bmatrix}$$

The next step is get all zeros in the components below the pivot, however there are no components below the pivot, so we're done with this row. Since we've processed all rows, we're also done with elimination, and we're left with the following "eliminated" version of the above system:

$$
A\vec{x} = \vec{b} \\[5pt]
\begin{bmatrix}1.5 & 1.5 \\ 0 & 0.5\end{bmatrix} \begin{bmatrix}d \\ h\end{bmatrix} = \begin{bmatrix}75 \\ 10\end{bmatrix}
$$

This corresponds to a modified version of the original system. We can translate this matrix form back to equation form:

$$
\begin{align}
1.5d + 1.5h &= 75 \\[3pt]
0.5h &= 10
\end{align}
$$

Looking at the equations, it should be obvious as to what we achieved through elimination, namely the elimination of $d$ in the second equation. This allows us to solve for $h$:

$$
\begin{align}
0.5h &= 10 \\[3pt]
h &= 20
\end{align}
$$

We can now take $h = 20$ and plug it back into the first equation to find the value of $d$:

$$
\begin{align}
1.5d + 1.5h &= 75 \\[3pt]
1.5d + 1.5(20) &= 75 \\[3pt]
1.5d + 30 &= 75 \\[3pt]
1.5d &= 45 \\[3pt]
d &= 30 \\[3pt]
\end{align}
$$

And, just like that, we've found the values for $d$ and $h$. We can happily communicate to Harry that he sold 30 hotdogs and 20 hamburgers.

## Elimination follow up

While we successfully solved the system by finding the values for $d$ and $h$, we can make our lives easier in the future by employing a couple of additional techniques.

### Augmented matrix

Above, we needed to keep track of the operations performed on the rows of $A$ and perform the same operations on the rows of $\vec{b}$. We can actually combine these two steps into one by performing elimination on an "augmented" version of $A$. To create the augmented matrix, you take $A$ and "append" $\vec{b}$ to the right of it:

$$
\left[\begin{array}{@{}cc|c@{}}
1 & 1 & 50 \\
1.5 & 2 & 85
\end{array}\right]
$$

You can see that in addition to the components of $A$, we've added a vertical line and the components of $\vec{b}$ to the matrix as well. For brevity, the augmented matrix is sometimes abbreviated as:

$$\left[\begin{array}{@{}c|c@{}}A & \vec{b}\end{array}\right]$$

The benefit of using an augmented matrix is that you don't need to perform the same row operation twice—it happens in one step. For example, the first row operation performed during elimination above was multiplying the first row by $1.5$. The same can be done for the augmented matrix, which takes care of both sides of the equation:

$$
\left[\begin{array}{@{}cc|c@{}}
1 & 1 & 50 \\
1.5 & 2 & 85
\end{array}\right]
\xrightarrow{\text{R1 = 1.5*R1}}
\left[\begin{array}{@{}cc|c@{}}
1 * (1.5) & 1 * (1.5) & 50 * (1.5) \\
1.5 & 2 & 85
\end{array}\right] =
\left[\begin{array}{@{}cc|c@{}}
1.5 & 1.5 & 75 \\
1.5 & 2 & 85
\end{array}\right]
$$

Using augmented matrices makes keeping track of things easier, so it will be the preferred method moving forward.

### Adding/subtracting a multiple

The second step of elimination above, we worked to get zeros below the pivot in $A_{1,1}$. We did this in 2 steps by first multiplying the first row by $1.5$, and then subtracting the first row from the second row. It's possible to save a step by using the third row operation of: _adding (or subtracting) a multiple of one row to another row_. Ultimately, we're looking to eliminate $1.5$ and we can do this by subtracting a multiple of the first row from the second row. In order to do this, we simply need to find what that multiple is. If we subtract $1.5$ of the first row from the second row, we can eliminate the value in $A_{2,1}$ in one step:

$$
\left[\begin{array}{@{}cc|c@{}}
1 & 1 & 50 \\
1.5 & 2 & 85
\end{array}\right]
\xrightarrow{\text{R2 = R2 - 1.5*R1}}
\left[\begin{array}{@{}cc|c@{}}
1 & 1 & 50 \\
1.5 - (1 * 1.5) & 2 - (1 * 1.5) & 85 - (50 * 1.5)
\end{array}\right] =
\left[\begin{array}{@{}cc|c@{}}
1 & 1 & 50 \\
0 & 0.5 & 10
\end{array}\right]
$$

Solving for $d$ and $h$, you will find that you arrive at the same values as above.

### Bigger example

The elimination steps above were pretty undramatic because there weren't many steps, but the process applies to matrices of any size. Let's take a slightly larger system that has 3 equations and 3 variables:

$$
\begin{align}
x + 2y + z &= 2 \\
3x + 8y + z &= 12 \\
2x + 4y + z &= 2
\end{align}
$$

Putting the coefficients and values to the right of the equals sign into an augmented matrix results in:

$$
A = \left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
3 & 8 & 1 & 12 \\
2 & 4 & 1 & 2
\end{array}\right]
$$

Now, let's see if we can use elimination to find the values of $x$, $y$, and $z$. Step 1 is to find the pivot in the first row, which is $2$ in $A_{1,1}$. Step 2 is to get zeros in the column below the pivot, so we need to get zeros in $A_{2,1}$ and $A_{3,1}$. To get a $0$ in $A_{2,1}$, we can add $\frac{3}{2}$ of the first row to the second row:

$$
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
3 & 8 & 1 & 12 \\
2 & 4 & 1 & 2
\end{array}\right]
\xrightarrow{\text{R2 = R2 + -3*R1}}
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
2 & 4 & 1 & 2
\end{array}\right]
$$

Translating what's going on here, we are going to replace the second row with itself added to a multiple of the first row. Specifically a multiple of $-3$:

$$
\begin{array}{r}
& & & 3x & + & 8y & + & 1z & = & 12  \\
+& -3 & * & (1x & + & 2y & + & 1z & = & 2) \\
\hline
& & & 0 & + & 2y & - & 2z & = & 6
\end{array}
$$

Since $1 * -3 = -3$, and $3 + (-3) = 0$, we've eliminated $x$ from the second equation. Next, we work to get a 0 in the position $A_{3,1}$. We can easily do this by adding $-2$ of the first row to the third row:

$$
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
2 & 4 & 1 & 2
\end{array}\right]
\xrightarrow{\text{R3 = R3 + -2*R1}}
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
0 & 0 & -1 & -2
\end{array}\right]
$$

Okay, we've got all zeros below our pivot in $A_{1,1}$, so the first column is in good shape. Next, we move on to the second row and find the pivot. The first non-zero element in row 2 is $2$ in $A_{2,2}$. Like above, we want go get all zeros in the column below the pivot. Since there's only one element below the pivot, we need to get a zero in $A_{3,2}$, but it's already $0$, so there's nothing to do.

Next, we move onto the third row and find the pivot, which is now $-1$ in $A_{3,3}$. Since there are no elements below $A_{3,3}$, we're done. Converting this eliminated matrix back into equation form, we have:

$$
\begin{align}
x + 2y + z &= 2 \\[3pt]
2y - 2z &= 6 \\[3pt]
-z &= -2
\end{align}
$$

We can easily solve for $z$ to get $z = 2$. We now begin the process of back-substituting upwards by plugging $z$ into the second equation and solving for $y$:

$$
\begin{align}
2y - 2z &= 6 \\
2y - 2(2) &= 6 \\
2y - 4 &= 6 \\
2y &= 10 \\
y &= 5
\end{align}
$$

We've found $y$ and $z$ and now need to find $x$. We plug $y$ and $z$ back into the first equation to find $x$:

$$
\begin{align}
x + 2y + z &= 2 \\
x + 2(5) + (2) &= 2 \\
x + 10 + 2 &= 2 \\
x + 12 &= 2 \\
x &= -10 \\
\end{align}
$$

Awesome! We've used elimination and back-substitution to solve for $x$, $y$, and $z$. We can verify that we arrived at the correct $x$, $y$, and $z$ by plugging the values back into an original equation:

$$
\begin{align}
x + 2y + z &= 2 \\[3pt]
(-10) + 2(5) + (2) &= 2 \\[3pt]
-10 + 10 + 2 &= 2 \\[3pt]
2 &= 2 \enspace \checkmark
\end{align}
$$

And, indeed it checks out.

## Echelon form

Above we mentioned that the goal of elimination is to perform row operations on the augmented matrix until the lower left-hand corner of the matrix is filled with zeros. This matrix has a special name: **upper triangular matrix**. If you were to draw a line through the diagonal of the matrix, the triangle above the line will contain numbers (represented as $*$ below) and the triangle below the line will contain all zeros:

$$
\begin{bmatrix}
\textbf{*} & * & * \\
0 & \textbf{*} & * \\
0 & 0 & \textbf{*}
\end{bmatrix}
$$

Likewise, there exists a **lower triangular matrix**:

$$
\begin{bmatrix}
* & 0 & 0 \\
* & * & 0 \\
* & * & *
\end{bmatrix}
$$

Often upper triangular matrices are said to be in row echelon form. Echelon matrices follow a "stair step" pattern. Matrices in row echelon form can be of any size as long as they follow this stair step pattern. Here are a few examples of matrices in echelon form:

$$
\begin{bmatrix}
* & * & * & * & * \\
0 & 0 & * & * & * \\
0 & 0 & 0 & 0 & *
\end{bmatrix}, \enspace\enspace
\begin{bmatrix}
* & * & * \\
0 & * & * \\
0 & 0 & *
\end{bmatrix}, \enspace\enspace
\begin{bmatrix}
* & * & * \\
0 & 0 & * \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}
$$

Notice after elimination is completed, the eliminated matrix is in row echelon form.

## Implementing elimination

Performing matrix elimination by hand is instructive, but tedious and error prone. Imagine trying to perform elimination by hand of a system with 50 equations and 50 variables. In practice, elimination is handled by software, so let's implement the steps of elimination. First, let's bring in the `size` method that we implemented in a previous guide:



```python
def size(matrix):
    """Gets the size of the matrix. Returns a tuple of the form (M, N) where M is the number of
    rows and N is the number of columns.
    """
    M = len(matrix)
    N = len(matrix[0]) if M > 0 else 0
    return (M, N)
```


The first step of elimination is to find the pivot in the first row, so let's implement a method for finding the pivot in a row:



```python
def find_pivot_in_row(row):
    """Given a row of a matrix, returns the index and value of the first non-zero element in the row. The
    row is a list of the form [e1, e2, ..., eN].
    """
    for i in range(len(row)):
        if row[i] != 0:
            return (i, row[i])

    # Uh, oh. Row is all zeros
    return (-1, -1)
```


After identifying the pivot, the next step is to eliminate all components below the pivot. We will implement a method that takes a matrix, the index of the pivot row, and the index of the actual pivot, and eliminates the components below the pivot:



```python
def eliminate(A, b, pivot_row_idx, pivot):
    M, N = size(A)
    
    for r in range(pivot_row_idx + 1, M):
        # Find the multiple of the pivot that eliminates the component in this row
        multiplier = A[r][pivot_row_idx] / float(pivot)

        # For each element in the row, subtract the multiple of the pivot row from the row
        for c in range(N):
            A[r][c] = A[r][c] - A[pivot_row_idx][c] * multiplier

        # Make sure we do to the right side what we did to the left side
        b[r] = b[r] - b[pivot_row_idx] * multiplier

    return A, b
```


For a given row, the above computation will eliminate all components below the pivot in that row, so now we need to ensure that perform this operation for all rows in the matrix. Below, we will implement a method that iterates over all the rows and performs this elimination:



```python
def elimination(A, b):
    """Given a matrix A and a vector of constants b, perform elimination on A until A is in row-echelon
    form. This elimination method returns a modified A and b such that row operations have been applied to
    both.
    """
    M, N = size(A)
    
    for row_idx in range(M):
        pivot_idx, pivot = find_pivot_in_row(A[row_idx])

        # Eliminate all the components below the pivot
        eliminate(A, b, row_idx, pivot)

    return A, b
```


After these steps, we should have an eliminated matrix. The final step is to perform back substitution to find the values of the variables. The steps in the algorithm for back-substitution are:

  1. Start from the last row, $i$, and solve for the variable in the last column, $j$
  2. Add that variable value to the solutions
  3. Once solved, propagate that variable to the rows above by multiplying the components in that column
  4. "Consolidate" each row above by updating the values of $\vec{b}$. This is equivalent to subtracting components from the left side of the equation from the right side
  5. Move to the row above, $i - 1$ and solve for variable $j - 1$ using steps 2-5



```python
def back_substitute(A, b):
    """Given a matrix A in row-echelon form and a vector of constants b, perform back-subsitution on the matrix
    to find the solutions to the system's variables. Returns a list representing the solutions to the unknown
    variables.
    """
    M, N = size(A)
    solutions = []
    row_num, col_num = M - 1, N - 1

    # Start with the last row and work upwards
    while row_num >= 0:
        # Get the variable value in the current column
        var = A[row_num][col_num]
        b_comp = b[row_num]

        # Solve for the variable in current column (i.e., divide by sides by the 
        # coefficient of the variable)
        b_comp /= var
        solutions.append(b_comp)
        
        # Propagate variable upwards and consolidate the values in b
        for j in range(0, row_num):
            A[j][col_num] *= b_comp
            b[j] -= A[j][col_num]
        
        row_num, col_num = row_num - 1, col_num - 1

    return list(reversed(solutions))
```


Finally, we need a method to wire it all together. We'll implement a `solve` method that calls the elimination and back-substitution steps:



```python
def solve(A, b):
    """Given a matrix A and a vector of constants b, perform elimination and back-substitution to find the
    solutions to the system of linear equations. Returns a list representing the solutions to the unknown
    variables.
    """
    eliminated_A, eliminated_b = elimination(A, b)
    solutions = back_substitute(eliminated_A, eliminated_b)
    return solutions
```


Let's test out the implementation with the systems we solved by hand above:



```python
"""
The matrix A and vector b represent Harry's system above:
  x + y = 50
  1.5x + 2y = 85
"""
A = [[1, 1], [1.5, 2]]
b = [50, 85]

# For Harry's system, find the values for d and h
d, h = solve(A, b)
print(f'Harry sold {d} hotdogs and {h} hamburgers.')

# For the 3x3 case, solve for x, y, z
A = [[1, 2, 1], [3, 8, 1], [2, 4, 1]]
b = [2, 12, 2]
x, y, z = solve(A, b)
print(f'x: {x}, y: {y}, z: {z}')
```


    Harry sold 30.0 hotdogs and 20.0 hamburgers.
    x: -10.0, y: 5.0, z: 2.0


## Elimination on rectangular matrices

The elimination examples we've seen above have all been _square_ matrices, but elimination works on rectangular matrices as well (i.e., matrices that aren't square). For example, we have an arbitrary matrix and let's pretend after one round of row operations, we got zeros in $A_{2,1}$ and  $A_{3,1}$.

$$
\left[\begin{array}{@{}cccc|c@{}}
1 & 3 & 5 & 7 & 9 \\
0 & 0 & 2 & 4 & 6 \\
0 & 0 & 8 & 10 & 12
\end{array}\right]
$$

Inadvertently, we also have zeros in $A_{2,2}$ and $A_{3,2}$, so when we move to row 2, there is no pivot in $A_{2,2}$ but instead $A_{2,3}$, so we use that as the pivot and try to get zeros in the elements below $A_{2,3}$. We're done with elimination when we've gotten our matrix in row echelon form.

## Row exchanges

Occasionally, during elimination when we try to find the pivot in the next row, it may be zero. For example, let's say that we've done a round of elimination and got all $0$'s in the first column below the pivot in $A_{1,1}$:

$$
\left[\begin{array}{@{}cccc|c@{}}
1 & 3 & 5 & 7 & 9 \\
0 & 0 & 2 & 4 & 6 \\
0 & 1 & 8 & 10 & 12
\end{array}\right]
$$

As intended, we have a $0$ in $A_{2,1}$ and $A_{3,1}$. The next step is to move to the next row. We expect a pivot to be in $A_{2,2}$, but instead we have a $0$. If this happens, we should immediately look below to see if there is a non-zero entry anywhere below in the second column. There is a $1$ in $A_{3,2}$, so we should exchange rows. Row exchange is a valid row operation. After performing the row exchange, our augmented matrix looks like:

$$
\xrightarrow{\text{R2 = R2} \leftrightarrow \text{R3}}
\left[\begin{array}{@{}cccc|c@{}}
1 & 3 & 5 & 7 & 9 \\
0 & 1 & 8 & 10 & 12 \\
0 & 0 & 2 & 4 & 6
\end{array}\right]
$$

So, now we have a non-zero pivot in our expected position of $A_{2,2}$ and elimination can proceed normally. If nothing but zeros were below $A_{2,2}$, we would move on to the next column and repeat this process.

## Elimination matrices

As mentioned, one of the benefits of using elimination on matrices is that it allows the use of matrix operations, however, the row operations above didn't really seem like matrix operations. While maybe not obvious, the row operations above can actually be captured in something called elimination matrices. In doing so, the process of elimination simply becomes matrix multiplication. Let's take the augmented matrix from the 3-equation system above:

$$
A = \left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
3 & 8 & 1 & 12 \\
2 & 4 & 1 & 2
\end{array}\right]
$$

The first step was to eliminate the components ($A_{2,1}$ and $A_{3,1}$) below the pivot. We did this by subtracting $3$ times the first row from the second row. This left us with the following result:

$$
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
3 & 8 & 1 & 12 \\
2 & 4 & 1 & 2
\end{array}\right]
\xrightarrow{\text{R2 = R2 + -3*R1}}
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
2 & 4 & 1 & 2
\end{array}\right]
$$

We can represent this row operation as the following $3x3$ elimination matrix, $E$:

$$
E = \begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

And, the first step of elimination can be computed as a matrix multiplication of $EA$:

$$
EA \\[5pt]
\begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
3 & 8 & 1 & 12 \\
2 & 4 & 1 & 2
\end{array}\right] =
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
2 & 4 & 1 & 2
\end{array}\right]
$$

Notice that we're multiplying $E$ on the left side of $A$. Recall from the [matrices](matrices) guide that by multiplying $E$ on the left of $A$, this can be viewed as combining the _rows_ of $A$ using the rows of $E$. Since we're looking to perform row operations on $A$, combining the rows of $A$ is appropriate. If we multiplied $E$ from the right side of $A$, we'd be combining the columns of $A$ using $E$. Since we're looking to modify the second row of $A$, the row operations reside in the second row of $E$, which can be interpreted as: multiply the first row of $A$ by $-3$ and add $1$ times the second row and $0$ times the third row. Since this is the second row of $E$, the result becomes the second row of the eliminated matrix. This step is equivalent to the following linear combination:

$$
-3 * \begin{bmatrix}1 & 2 & 1 & 2\end{bmatrix} + 1 * \begin{bmatrix}3 & 8 & 1 & 12\end{bmatrix} + 0 * \begin{bmatrix}2 & 4 & 1 & 2\end{bmatrix} = \begin{bmatrix}0 & 2 & -2 & 6\end{bmatrix}
$$

The second step was to eliminate the component in $A_{3,1}$. This involved subtracting $2$ of the first row from the third row:

$$
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
2 & 4 & 1 & 2
\end{array}\right]
\xrightarrow{\text{R3 = R3 + -2*R1}}
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
0 & 0 & -1 & -2
\end{array}\right]
$$

This step can be represented with the following elimination matrix:

$$
E = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-2 & 0 & 1
\end{bmatrix}
$$

And again, the elimination happens with a matrix multiplication:

$$
EA \\[5pt]
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-2 & 0 & 1
\end{bmatrix}
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
2 & 4 & 1 & 2
\end{array}\right] =
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
0 & 0 & -1 & -2
\end{array}\right]
$$

Interestingly enough, we could chain together the first and second elimination into one multiplication. We'll label the first elimination matrix above as $E_1$ and the second as $E_2$:

$$
E_2E_1A \\[5pt]
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-2 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
3 & 8 & 1 & 12 \\
2 & 4 & 1 & 2
\end{array}\right] =
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
0 & 0 & -1 & -2
\end{array}\right]
$$

What we're effectively doing is the following:

$$
(E_2(E_1(A))
$$

We're multiplying $E_1$ and $A$, and then multiplying the result by $E_2$. The annoying thing is that that we're left building intermediate representations of $A$ after each multiplication. Instead, due to the associative nature of matrix multiplication, we can take both of the elimination matrices and combine them into one elimination matrix, $E$ that performs all the matrix operations in one multiplication. This is equivalent to:

$$
(E_2E_1)A
$$

And with this, we can eliminate $A$ in one step:

$$
E = E_2E_1 =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-2 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
-2 & 0 & 1
\end{bmatrix}
$$

Notice $E$ has the components from both $E_1$ and $E_2$. Now, elimination can be done in a single multiplication:

$$
EA \\[5pt]
\begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
-2 & 0 & 1
\end{bmatrix}
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
3 & 8 & 1 & 12 \\
2 & 4 & 1 & 2
\end{array}\right] =
\left[\begin{array}{@{}ccc|c@{}}
1 & 2 & 1 & 2 \\
0 & 2 & -2 & 6 \\
0 & 0 & -1 & -2
\end{array}\right]
$$

Fortunately, this process scales to any number of elimination.

## Summary, tl;dr

Things are really starting to get interesting. We are starting to put together all the things we've seen so far. We took what we know about vectors and matrices and combined it with linear systems in order to represent systems of linear equations as matrices. This allows us to use matrix operations to perform elimination to arrive at the solution to the system.

We started by reiterating how a system of linear equations can be represented as a product of matrices and vectors:

$$
a_{1,1}x_1 + a_{1,2}x_2 + \dots + a_{1,n}x_n = b_1 \\
a_{2,1}x_1 + a_{2,2}x_2 + \dots + a_{2,n}x_n = b_2 \\
\vdots \\
a_{m,1}x_1 + a_{m,2}x_2 + \dots + a_{m,n}x_n = b_m \\
$$

Can be represented as $A\vec{x} = \vec{b}$:

$$
\begin{bmatrix}
a_{1,1} & a_{1,2} & \dots & a_{1,n} \\
a_{2,1} & a_{2,2} & \dots & a_{1,n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m,1} & a_{m,2} & \dots & a_{m,n}
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ \vdots \\ x_n
\end{bmatrix} =
\begin{bmatrix}
b_1 \\ b_2 \\ \vdots \\ b_m
\end{bmatrix}
$$

Our ultimate goal is to find the values of $x_i$ in $\vec{x}$ that satisfy the system. We are able to find the values of $\vec{x}$ by performing a series of row operations on an _augmented matrix_. An augmented matrix is simply the coefficient matrix with the components of $\vec{b}$ tacked on to the right:

$$
\left[\begin{array}{@{}cccc|c@{}}
a_{1,1} & a_{1,2} & \dots & a_{1,n} & b_1 \\
a_{2,1} & a_{2,2} & \dots & a_{1,n} & b_2 \\
\vdots & \vdots & \ddots & \vdots  & \vdots \\
a_{m,1} & a_{m,2} & \dots & a_{m,n} & b_m
\end{array}\right]
$$

The reason we do this is so that when we perform row operations on the matrix, we perform them to both sides of the equation. Ultimately, we're interested in performing row operations, until we've arrived at a matrix that is in echelon form. Matrices in echelon form share a characteristic in that they have zeros in the bottom hand corner and follow a "stair-step" pattern:

$$
\begin{bmatrix}
* & * & * & \dots & * \\
0 & * & * & \dots & * \\
0 & 0 & * & \dots & * \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \dots & 0
\end{bmatrix}
$$

We perform elimination by following a few simple steps. We start with the first row, and repeat the following 2 steps for all rows or until the matrix has all zeros in the bottom left corner:

  1. Find the first non-zero element in the row. This element is called the **pivot**
  2. Use one of the below row operations to get all zeros below the pivot

The type of row operations that we can perform on the augmented matrix are constrained to the following operations:

1. Swapping two rows
2. Multiplying a row by a nonzero scalar number
3. Adding (or subtracting) a multiple of one row to another row

After elimination has been done on the matrix, the last equation (usually) contains one non-zero variable. This allows us to solve for that one variable, and then begin working our way upwards substituting in the variables we've solved for. This process, known as _back-substitution_ will yield all the components of $\vec{x}$.

## What's next?

In the next guide, we'll see an intuitive way for how we can easily solve a certain class of systems using matrices. We'll be introduced to the concept of _inverses_ which can loosely be seen as something akin to matrix division. Inverses are a critical part of linear algebra, so buckle up and let's get to it!

<nav class="links">
    <a href="linear-systems" class="prev">Linear Systems</a>
    <a href="inverses" class="next">Inverses</a>
</nav>
