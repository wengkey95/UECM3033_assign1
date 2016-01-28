import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.sqrt(x)*sy.exp(-x**2), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[1,2,3,4,5,6,7,8,9,0],
                   [2,3,4,5,6,7,8,9,0,1],
                   [3,4,5,6,7,8,9,0,1,2],
                   [4,5,6,7,8,9,0,1,2,3],
                   [5,6,7,8,9,0,1,2,3,4],
                   [6,7,8,9,0,1,2,3,4,5],
                   [7,8,9,0,1,2,3,4,5,6],
                   [8,9,0,1,2,3,4,5,6,7],
                   [9,0,1,2,3,4,5,6,7,8],
                   [9,0,6,7,8,5,4,3,1,2],
                   ] )
    b = np.array([9,8,7,6,5,5,4,3,2,1])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1304638
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())

