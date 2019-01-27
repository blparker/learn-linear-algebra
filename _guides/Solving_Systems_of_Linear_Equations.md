---
layout: post
title: Solving Systems of Linear Equations
permalink: /guides/solving-systems-of-linear-equations
---

# Solving $A\vec{x} = \vec{b}$

## Introduction

In earlier guides, we were introduced to [vectors](vectors) and [matrices](matrices) and have learned how to work with them. These are proving useful because we showed in the [linear systems](linear-systems) guide that we can represent a system of linear equations as matrices and vectors. This wouldn't be all that useful if we couldn't do anything with it. The benefit of representing systems of linear equations this way is that it allows us to perform matrix and vector operations easily to arrive at the solution.

Armed with this knowledge, we are now equipped to help solve Harry's system using matrices. We introduced Harry's problem in the [linear systems](linear-systems) guide. Harry has a problem that he needs our help in solving:

> Harry recently set up shop at a baseball game. Things went well, but at the end of the day, Harry realizes that he didn't keep track of how many individual hotdogs and hamburgers he sold, but he does have totals. He realizes that he sold of a combined total of 50 hotdogs and hamburgers and he made \\$85.00 total. Harry sells the hotdogs for \\$1.50 and the hamburgers for \\$2.00. In order to restock, Harry would like to know how many hotdogs and hamburgers he individually sold.

Using the details from above, we are able to formalize Harry's problem into a system of linear equations:

$$
d + h = 50 \\[3pt]
1.5d + 2h = 85
$$

In the [matrices](matrices) guide we showed that you can represent Harry's system of linear equations using matrices—we put the coefficients into a matrix called $A$, the unknown variables into a vector called $\vec{x}$, and the constants to the right of the equals sign into a vector called $\vec{b}$:

$$
A = \begin{bmatrix}1 & 1 \\ 1.5 & 2\end{bmatrix}, \enspace
\vec{x} = \begin{bmatrix}d \\ h\end{bmatrix}, \enspace
\vec{b} = \begin{bmatrix}50 \\ 85\end{bmatrix}
$$

And, then we can represent this system in the matrix form $A\vec{x} = \vec{b}$:

$$
\begin{bmatrix}1 & 1 \\ 1.5 & 2\end{bmatrix}
\begin{bmatrix}d \\ h\end{bmatrix}
=
\begin{bmatrix}50 \\ 85\end{bmatrix}
$$

We're interested in finding the solution vector $\vec{x}$ which contains the components $d$ and $h$. After finding the solution $\vec{x}$, we should be able to plug the values back in to the system and verify that the equations equal what they expect to. To find the solutions, we revisit elimination and show how we can apply it systematically to a matrix to find $d$ and $h$. If you need a quick refresher on the basics of elimination, check out the [linear systems](linear-systems) guide.

## Elimination

Recall the goal of elimination is to repeatedly do a bunch of operations on the equations until we're left with an equation that has only one variable in it (hence we eliminated all the other variables in that equation). We can then solve for that variable and then _back-substitute_ into the other equations. For matrices, the elimination is done by performing operations on the rows of the matrix. The types of operations that we're allowed to perform on the rows are:

1. Swapping two rows
2. Multiplying a row by a nonzero number
3. Adding (or subtracting) a multiple of one row to another row

We perform these row operations to modify the matrix until the lower left-hand corner of the matrix is filled with zeros. Let's see how we can do elimination on the coefficients matrix $A$ above. Our starting matrix is essentially $A$, but with a little twist:

$$
\left[\begin{array}{@{}cc|c@{}}
1 & 1 & 50 \\
1.5 & 2 & 85
\end{array}\right]
$$

You can see that in addition to the coefficients, we've added a vertical line and the components of $\vec{b}$ to the matrix as well. A matrix in this form is called an **augmented matrix** because we've augmented the coefficients matrix by adding the constants from $\vec{b}$ to it. The reason we do this is because when we do something to one side of an equation, we have to do it the other side as well. When performing the row operations on the matrix, we need to make sure that we do it to both sides. Creating the augmented matrix isn't absolutely necessary, but if you don't, you need to ensure that whatever operations you perform on $A$, you perform on $\vec{b}$ as well. With an augmented matrix, it happens in one step.

Okay, let's systematically work through trying to eliminate the values in the matrix. We perform elimination on a row-by-row basis by starting with the first row and working our way down. Per row, our goals are:

1. Find the **pivot** in the row. The pivot is the first non-zero element in the row.
2. Use row operations to get all zeros below the pivot.

This will become clearer as we walk through an example. Revisiting our augmented matrix from above, we start with  the first row and find the pivot:

$$
\left[\begin{array}{@{}cc|c@{}}
\textbf{1} & \textbf{1} & \textbf{50} \\
1.5 & 2 & 85
\end{array}\right]
$$

The first non-zero element in the first row is $1$ in position $A_{1,1}$. Our goal now is to get all zeros in the column below the pivot. Since our matrix has only 2 rows, we just need to get a zero in $A_{2,1}$. What operation can we perform on the second row to turn that $1.5$ into $0$? If we cycle through our rules above, there are no other rows to swap with to get a $0$ there, and also no nonzero number we can multiply the second row with to get a 0 there. However, since we're trying to get a $0$ in $A_{2,1}$, we can subtract some multiple of the first row from the second row. What is that multiplier? Since $A_{2,1}$ is $1.5$ and $A_{1,1}$ is $1$, we can simply multiply the first row by $1.5$ and subtract that from the second row, replacing the second row. Note, we aren't actually changing the coefficients of the first row, we're just subtracting some multiple of it from the second row. Below, we're performing that row operation and we're left with a modified version of $A$, which has all zeros below the pivot:

$$
\left[\begin{array}{@{}cc|c@{}}
1 & 1 & 50 \\
1.5 & 2 & 85
\end{array}\right]
\xrightarrow{\text{R2 = R2 - 1.5*R1}}
\left[\begin{array}{@{}cc|c@{}}
1 & 1 & 50 \\
1.5 - (1.5*1) & 2 - (1.5*1) & 85 - (1.5*50)
\end{array}\right]
=
\left[\begin{array}{@{}cc|c@{}}
1 & 1 & 50 \\
0 & 0.5 & 10
\end{array}\right]
$$

It's common to log the operations that are being performed to the matrix by putting it above the arrow. In the example above, $R2 = R2 - 1.5*R1$ can be interpreted as: subtract from row 2, $1.5$ times row 1 and replace row 2. Moving on, if we had a third row, the next step would be get a $0$ in the $A_{3,1}$ position, but since we only have 2 rows, we're done with the first row. Our next step is to move to the second row of this modified matrix and identify the pivot. The first non-zero element in the modified matrix is $0.5$. Next, we need to get zeros in all the elements below the pivot, but since there are no more rows below, we're done with elimination.

The matrix after these row operations:

$$
\left[\begin{array}{@{}cc|c@{}}
1 & 1 & 50 \\
0 & 0.5 & 10
\end{array}\right]
$$

This corresponds to a modified version of the original system. We can rewrite the modified matrix as a system to see:

$$
d + h = 50 \\[3pt]
0.5h = 10
$$

We've eliminated $d$ from the second equation and so we're able to easily solve for $h$:

$$h = 20$$

Now that we know $h$, we can begin working our way back up the equations and plug in our solutions for the known variables and solving for the other variables. This step is called _back-substitution_. Knowing $h$, we back-substitute $h$ into the first equation and solve for $d$:

$$d + (20) = 50$$

Solving for $d$:

$$d = 30$$

And, we're left with $d = 30$ and $h = 20$. We can now inform Harry that he sold 30 hotdogs and 20 hamburgers.

### Bigger example

The elimination steps above were pretty undramatic because there was only one step, but the process applies to matrices of any size. Let's take a slightly larger system that has 3 equations and 3 variables:

$$
2x + y - z = 8 \\
-3x - y + 2z = -11 \\
-2x + y + 2z = -3
$$

This results in the augmented matrix:

$$
A = \left[\begin{array}{@{}ccc|c@{}}
2 & 1 & -1 & 8 \\
-3 & -1 & 2 & -11 \\
-2 & 1 & 2 & -3
\end{array}\right]
$$

Step 1 is to find the pivot in the first row, which is $2$ in $A_{1,1}$. Step 2 is to get zeros in the column below the pivot, so we need to get zeros in $A_{2,1}$ and $A_{3,1}$. To get a 0 in $A_{2,1}$, we can add $\frac{3}{2}$ of the first row to the second, replacing the second row:

$$
\left[\begin{array}{@{}ccc|c@{}}
2 & 1 & -1 & 8 \\
-3 & -1 & 2 & -11 \\
-2 & 1 & 2 & -3
\end{array}\right]
\xrightarrow{\text{R2 = R2 + 3/2*R1}}
\left[\begin{array}{@{}ccc|c@{}}
2 & 1 & -1 & 8 \\
0 & \frac{1}{2} & \frac{1}{2} & 1 \\
-2 & 1 & 2 & -3
\end{array}\right]
$$

Reiterating what's going on here, we are going to replace the second row with itself added to a multiple of the first row. Specifically a multiple of $\frac{3}{2}$:

$$
\begin{array}{r}
& & & -3x & - & y & + & 2z & = & -11  \\
+& \frac{3}{2} & * & (2x & + & y & - & z & = & 8) \\
\hline
& & & 0 & + & \frac{1}{2}y & + & \frac{1}{2}z & = & 1
\end{array}
$$

Next, we work to get a 0 in the position $A_{3,1}$. We do easily do this by replacing the third row with itself added to the first row.

$$
\left[\begin{array}{@{}ccc|c@{}}
2 & 1 & -1 & 8 \\
0 & \frac{1}{2} & \frac{1}{2} & 1 \\
-2 & 1 & 2 & -3
\end{array}\right]
\xrightarrow{\text{R3 = R3 + R1}}
\left[\begin{array}{@{}ccc|c@{}}
2 & 1 & -1 & 8 \\
0 & \frac{1}{2} & \frac{1}{2} & 1 \\
0 & 2 & 1 & 5
\end{array}\right]
$$

Okay, we've got all zeros below our pivot in $A_{1,1}$, so the first column is in good shape. Next, we move on to the second row and find the pivot. The first non-zero element in row 2 is $\frac{1}{2}$ in $A_{2,2}$. Like above, we want go get all zeros in the column below the pivot. Since there's only one element below the pivot, we need to get a zero in $A_{3,2}$. To get a zero in $A_{3,2}$, we can multiply the second row by $-4$ and add it to third row:

$$
\left[\begin{array}{@{}ccc|c@{}}
2 & 1 & -1 & 8 \\
0 & \frac{1}{2} & \frac{1}{2} & 1 \\
0 & 2 & 1 & 5
\end{array}\right]
\xrightarrow{\text{R3 = -4*R2 + R3}}
\left[\begin{array}{@{}ccc|c@{}}
2 & 1 & -1 & 8 \\
0 & \frac{1}{2} & \frac{1}{2} & 1 \\
0 & 0 & -1 & 1
\end{array}\right]
$$

Next, we move onto the third row and find the pivot, which is now $-1$ in $A_{3,3}$. Since there are no elements below $A_{3,3}$, we're done. If we convert this matrix back into equation form, we have:
$$
\begin{align*}
  2x + y - z &= \,8 \\ 
  \frac{1}{2}y + \frac{1}{2}z &= 1 \\
  -z &= \,1
\end{align*}
$$

We can easily solve for $z$ to get $z = -1$. We now begin the process of back-substituting upwards by plugging $z$ into one the second equation and solving for $y$:

$$
\frac{1}{2}y + \frac{1}{2}z = 1 \\
\frac{1}{2}y + \frac{1}{2}(-1) = 1 \\
\frac{1}{2}y + -\frac{1}{2} = 1 \\
\frac{1}{2}y = \frac{3}{2} \\
y = 3
$$

We've found $y$ and $z$ and now need to find $x$. We plug $y$ and $z$ back into the first equation to find $x$:

$$
2x + y - z = 8 \\
2x + (3) - (-1) = 8 \\
2x + 4 = 8 \\
2x = 4 \\
x = 2
$$

Awesome! We've used elimination and back-substitution to solve $x$, $y$, and $z$. We can verify that we arrived at the correct $x$, $y$, and $z$ by plugging the values back into an original equation:

$$
2x + y - z = 8 \\[3pt]
2(2) + (3) - (-1) = 8 \\[3pt]
4 + 3 + 1 = 8 \\[3pt]
8 = 8 \enspace \checkmark
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

## Implementing elimination



```python
A = [[1, 1], [1.5, 2]]
b = [50, 85]
#A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
#b = [8, -11, -3]

def size(matrix):
    """Gets the size of the matrix. Returns a tuple of the form (M, N) where M is the number of
    rows and N is the number of columns.
    """
    M = len(matrix)
    N = len(matrix[0]) if M > 0 else 0
    return (M, N)


def find_pivot_in_row(row):
    """Given a row of a matrix, returns the index of the first non-zero element in the row. The
    row is a list of the form [e1, e2, ..., eN].
    """
    for i in range(len(row)):
        if row[i] != 0:
            return i

    return -1


def swap_rows(A, r1, r2):
    """Swaps two rows in the matrix by putting r1 in the position of r2 and vice versa."""
    A[r1], A[r2] = A[r2], A[r1]

    
def create_augmented_matrix(A, b):
    aug = []
    for row, b_component in zip(A, b):
        # Create a row in the augmented matrix which is the original row concatenated with the component of b
        aug_row = [] + row + [b_component]
        aug.append(aug_row)

    return aug


def elimination(A, b):
    """Given a matrix A and a vector of constants b, perform elimination on A until A is in row-echelon
    form. This elimination method returns a modified A and b such that row operations have been applied to
    both.
    """
    M, N = size(A)

    for row_idx in range(M):
        # Find the pivot in the row
        pivot_idx = find_pivot_in_row(A[row_idx])
        pivot = A[row_idx][pivot_idx]

        # For each row below the current row, find the multiplier to knock out that row
        for r in range(row_idx + 1, M):
            multiplier = A[r][pivot_idx] / float(pivot)
            # For each element in the row, subtract the element from above multiplied by the multiplier
            for c in range(N):
                A[r][c] = A[r][c] - A[row_idx][c] * multiplier

            # Make sure we do to the right side what we did to the left side
            b[r] = b[r] - b[row_idx] * multiplier

    return A, b


def back_substitute(A, b):
    """Given a matrix A in row-echelon form and a vector of constants b, perform back-subsitution on the matrix
    to find the solutions to the system's variables. Returns a list representing the solutions to the unknown
    variables.
    """
    M, N = size(A)
    # Initial solutions are all 0
    solutions = [0] * N
    
    # A is in echelon form, so start from the bottom row and work upwards plugging in the known solutions and
    # solving for that row
    for r in range(M - 1, -1, -1):
        idx = find_pivot_in_row(A[r])
        # Any elements to the right of the current variable already have a solution for their variable,
        # so just substitute the solution for that variable and move to the other side
        for e in range(idx + 1, N):
            b[r] -= A[r][e] * solutions[e]

        solutions[r] = b[r] / A[r][idx] 

    return solutions


def solve(A, b):
    """Given a matrix A and a vector of constants b, perform elimination and back-substitution to find the
    solutions to the system of linear equations. Returns a list representing the solutions to the unknown
    variables.
    """
    eliminated_A, eliminated_b = elimination(A, b)
    solutions = back_substitute(eliminated_A, eliminated_b)
    return solutions

# For Harry's system, find the values for d and h
d, h = solve(A, b)
print('Harry sold %d hotdogs and %d hamburgers.' % (d, h))
```


    Harry sold 30 hotdogs and 20 hamburgers.


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

As instructed, we have a $0$ in $A_{2,1}$ and $A_{3,1}$. The next step is to move to the next row. We expect a pivot to be in $A_{2,2}$, but instead we have a $0$. If this happens, we should immediately look below to see if there is a non-zero entry anywhere below in the second column. There is a $1$ in $A_{3,2}$, so we should exchange rows. Row exchange is a valid row operation. After performing the row exchange, our augmented matrix looks like:

$$
\xrightarrow{\text{R2 = R2} \leftrightarrow \text{R3}}
\left[\begin{array}{@{}cccc|c@{}}
1 & 3 & 5 & 7 & 9 \\
0 & 1 & 8 & 10 & 12 \\
0 & 0 & 2 & 4 & 6
\end{array}\right]
$$

So, now we have a non-zero pivot in our expected position of $A_{2,2}$ and elimination can proceed normally. If nothing but zeros were below $A_{2,2}$, we would move on to the next column and repeat this process.

## Summary

Things are really starting to get interesting. We are really starting to put together all the things we've seen so far. We took what we know about vectors and matrices and combined it with linear systems in order to represent systems of linear equations as matrices and matrix multiplication. This allows us to use matrix operations to perform elimination to arrive at the solution to the system.

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

Our ultimate goal is to find the values of $x_i$ in $\vec{x}$ that satisfy the system. We are able to find the values of $\vec{x}$ by performing a series of row operations on an _augmented matrix_. An augmented matrix is simply the coefficient matrix with the components of $\vec{b}$ tacked on to the end. The reason we do this is so that when we perform row operations on the matrix, we perform them to both sides of the equation.

Elimination is performed by starting with the first row and working your way down. Per row, the first step is to find the pivot and perform a series of row operations such that all the components below the pivot are zero. After elimination has been done on the matrix, the last equation (usually) contains one non-zero variable. This allows us to solve for that one variable, and then begin working our way upwards substituting in the variables we've solved for. This process, known as _back-substitution_ will yield all the components of $\vec{x}$.

## What's next?

In the next guide, we'll see an intuitive way for how we can easily solve a certain class of systems using matrices. We'll be introduced to the concept of _inverses_ which can loosely be seen as something akin to matrix division. Inverses are a critical part of linear algebra, so buckle up and let's get to it!

<nav class="links">
    <a href="linear-systems" class="prev">Linear Systems</a>
    <a href="inverses" class="next">Inverses</a>
</nav>
