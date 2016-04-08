---
title: "matrix_algebra_worksheet_ANSWER"
author: "J Gondin"
date: "March 29, 2016"
output: pdf_document
---

### Linear Algebra - Worksheet ANSWER

$$
A = 
\left[\begin{array}{ccc} 
1 & 2 & 3 \\
2 & 7 & 4
\end{array}\right]
, \
B = 
\left[\begin{array}{cc} 
1 & -1 \\
0 & 1
\end{array}\right]
, \
C = 
\left[\begin{array}{cc} 
5 & -1\\
9 & 1 \\
6 & 0
\end{array}\right]
, \
D = 
\left[\begin{array}{ccc} 
3 & -2 & -1\\
1 &  2 & 3
\end{array}\right]
$$ 

$$
u = 
\left[\begin{array}{cccc} 
6 & 2 & -3 & 5
\end{array}\right]
, \
v = 
\left[\begin{array}{cccc} 
3 &  5 & -1 & 4
\end{array}\right]
, \
w = 
\left[\begin{array}{c} 
1 \\
8 \\
0 \\
5
\end{array}\right]
$$

####1. Matrix Dimensions
Write the dimansions of each matrix.

1.1) A: $2x3$    
1.2) B: $2x2$    
1.3) C: $3x2$   
1.4) D: $2x3$      
1.5) u: $1x4$   
1.6) w: $4x1$   

####2. Vector Operations
Perform the following operations. Assume $\alpha =6$.

2.1)   
$\begin{array}{ll}
\vec{u} + \vec{v} = &{
                      \left[\begin{array}{cccc} 
                        6 & 2 & -3 & 5
                      \end{array}\right]
                      +
                      \left[\begin{array}{cccc} 
                        3 & 5 & -1 & 4
                      \end{array}\right]
                      =
                      \left[\begin{array}{cccc} 
                        (6+3) & (2+5) & (-3-1) & (5+4)
                      \end{array}\right]
                      }
                      \\
=>\vec{u} + \vec{v} =   &
                      \left[\begin{array}{cccc} 
                        9 & 7 & -4 & 9
                      \end{array}\right]
\end{array}$


2.2)   
$\begin{array}{ll}
\vec{u} - \vec{v} = &{
                      \left[\begin{array}{cccc} 
                        6 & 2 & -3 & 5
                      \end{array}\right]
                      -
                      \left[\begin{array}{cccc} 
                        3 & 5 & -1 & 4
                      \end{array}\right]
                      =
                      \left[\begin{array}{cccc} 
                        (6-3) & (2-5) & (-3+1) & (5-4)
                      \end{array}\right]
                      }
                      \\
=>\vec{u} - \vec{v} =   &
                      \left[\begin{array}{cccc} 
                        3 & -3 & -2 & 1
                      \end{array}\right]
\end{array}$

2.3)   
$\begin{array}{ll}
\alpha \vec{u} = &{6 \cdot \vec{u} =
                      6 \cdot
                      \left[\begin{array}{cccc} 
                        6 & 2 & -3 & 5
                      \end{array}\right]
                      =
                      \left[\begin{array}{cccc} 
                      (6\cdot 6) & (6\cdot 2) & (6\cdot -3) &(6\cdot 5 )
                      \end{array}\right]
                      }
                      \\
=>\alpha \vec{v} =   &
                      \left[\begin{array}{cccc} 
                        36 & 12 & -18 & 30
                      \end{array}\right]
\end{array}$


  
2.4)   
$\begin{array}{ll}
\vec{u} \cdot \vec{v} = & {
                      \left[\begin{array}{cccc} 
                        6 & 2 & -3 & 5
                      \end{array}\right]
                      \cdot
                      \left[\begin{array}{cccc} 
                        3 & 5 & -1 & 4
                      \end{array}\right]
                      = (6\cdot 3) + (2\cdot 5) + (-3\cdot(-1)) + (5\cdot 4) } \\
                      &
                      = 18 + 10 + 3 + 20 = 51 
                    \\
=>\vec{u} \cdot \vec{v} =   & 51
\end{array}$



2.5)   
$\begin{array}{ll}
\| \vec{u} \| = &{\sqrt{ \vec{u} \cdot \vec{u}} =
                  \sqrt{
                  \left[\begin{array}{cccc} 
                  6 & 2 & -3 & 5
                  \end{array}\right]
                  \cdot
                  \left[\begin{array}{cccc} 
                  6 & 2 & -3 & 5
                  \end{array}\right]
                  } =
                  \sqrt{
                  (6\cdot 6) + (2\cdot 2) + (-3\cdot (-3)) + (5\cdot 5)}
                  } =
                  \\
                  &=\sqrt{ 36 + 4 + 9 + 25}
                  \\
                  &
                  = \sqrt{74}
                  \\
=> \| \vec{u} \| = & {\sqrt{2} \sqrt{37} \approx 9}
\end{array}$

####3. Matrix Operations
Evaluate each of the foolowing expressionas, if it is defined; else fill in with ``not defined''. Do your work by hand on scratch paper.

3.1)   
``$A +C=$ Not defined'': the dimensions of $A$ and $C$ do not match.

3.2)  
$\begin{array}{ll}
A + C^{T} = & {
          \left[\begin{array}{ccc} 
          1 & 2 & 3 \\
          2 & 7 & 4
          \end{array}\right]
          \left[\begin{array}{cc} 
          5 & -1\\
          9 & 1 \\
          6 & 0
          \end{array}\right]^T
          = 
          \left[\begin{array}{ccc} 
          1 & 2 & 3 \\
          2 & 7 & 4
          \end{array}\right]
          \left[\begin{array}{ccc} 
          5  & 9 & 6  \\
          -1 & 1 & 0  
          \end{array}\right]
          =
          \left[\begin{array}{ccc} 
          1 + 5 & 2 + 9 & 3 + 6  \\
          2 - 1 & 7 + 1 & 4 + 0  
          \end{array}\right]}
          \\
=>A + C^{T} =&
          {
          \left[\begin{array}{ccc} 
          6 & 11 & 9  \\
          1 & 8  & 4  
          \end{array}\right]
          }
\end{array}$


3.3)  
$\begin{array}{ll}
C^{T} + 3D = & {
          \left[\begin{array}{ccc} 
          5  & 9 & 6  \\
          -1 & 1 & 0  
          \end{array}\right]
          + 
          3\cdot
          \left[\begin{array}{ccc} 
          3 & -2 & -1\\
          1 &  2 & 3
          \end{array}\right]
          }
          \\
=>C^{T} + 3D =&
          {
          \left[\begin{array}{ccc} 
          14 & 3 & 3  \\
           2 & 7 & 9   
          \end{array}\right]
          }
\end{array}$

3.4)   
$\begin{array}{ll}
BA = & {
        \left[\begin{array}{cc} 
        1 & -1 \\ 
        0 & 1
        \end{array}\right]
        \left[\begin{array}{ccc} 
        1 & 2 & 3 \\
        2 & 7 & 4
        \end{array}\right]
        =
        \left[\begin{array}{ccc} 
        (1-2) & (2-7) & (3-4) \\ 
        (0+2) & (0+7) & (0+4)
        \end{array}\right]
        }
        \\
=>BA= & {
        \left[\begin{array}{ccc} 
        -1 & -5 & -1 \\ 
         2 & 7 & 4
        \end{array}\right]
        }
\end{array}$



3.5)  
``$BA=$ Not defined''

