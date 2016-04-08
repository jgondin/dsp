# Matrix Algebra
#import sympy as sp
from sympy import *
from sympy.matrices import *
init_printing()

#Create the matrices

A = Matrix(2, 3, [1, 2, 3, 2, 7, 4])
B = Matrix(2, 2, [1, -1, 0, 1])
C = Matrix(3, 2, [5, -1, 9, 1, 6, 0])
D = Matrix(2, 3, [3, -2, -1, 1, 2, 3])
u = Matrix([[6, 2, -3, 5]])
v = Matrix([[3, 5, -1, 4]])
w = Matrix([1, 8, 0, 5])

mat_dict = {'A': A,'B': B, 'C': C, 'D': D, 'u': u, 'v': v, 'w': w}
for k, val in mat_dict.items():
    print(k,'=')
    pprint(val)
    print()

#1. Matrix Dimensions.
for k, val in mat_dict.items():
    values = (k,) + val.shape  
    print('Dimension of %s = %dx%d' % values) 

#2. Vector Operations.
print('u + v=')
pprint(u + v)
print()

print('u - v=')
pprint(u - v)
print()

print('av' )
pprint(6*u)
print()

print('u*v' )
pprint(u*v.T)
print()

print('|u|=')
pprint(u.norm())
print()

#3. Matrix Operations.
print('A + C = Not Defined')
print()

print('A - C^T = ')
pprint(A + C.T)
print()

print('C^T + 3D=')
pprint(C.T + 3 *D)
print()

print('BA=')
pprint(B*A)
print()

print('BA^T= Not Defined')
print()

print('BC = Not Defined')
print()

print('CB = ')
print(C*B)
print()

print('B^4=')
pprint(B**4)
print()

print('AA^T=')
pprint(A*A.T)
print()

print('D^TD=')
pprint(D.T * D) 
print()

