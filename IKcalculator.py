import numpy as np
import sympy
from sympy import sin, cos
from sympy.matrices import Matrix
from mpmath import radians, degrees

def positioninversekinematics(R06, px, py, pz, a1, a2, a3, a4, a5):
    wx = px - a5 * R06[0][2]
    wy = py - a5 * R06[1][2]
    wz = pz - a5 * R06[2][2]

    r = np.sqrt(wx ** 2 + wy ** 2)
    s = wz - a1

    theta1 = np.arctan2(wy, wx)
    theta3 = np.arccos((r ** 2 + s ** 2 - a2 ** 2 - a3 ** 2)/(2 * a2 * a3))
    theta2 = np.arcsin(((a2 + a3 * np.cos(theta3)) * s - a3 * np.sin(theta3) * r)/(r ** 2 + s ** 2))

    R03 = [[np.cos(theta1) * np.cos(theta2 + theta3), -np.cos(theta1) * np.sin(theta2 + theta3), np.sin(theta1)],
           [np.sin(theta1) * np.cos(theta2 + theta3), -np.sin(theta1) * np.sin(theta2 + theta3), -np.cos(theta1)],
           [np.sin(theta2 + theta3), np.cos(theta2 + theta3), 0]]

    invR03 = np.linalg.inv(R03)
    R36 = np.dot(invR03, R06)

    theta4 = np.arctan2(R36[1][2], R36[0][2])
    theta5 = np.arccos(R36[2][2])
    theta6 = np.arctan2(R36[2][1], -R36[2][0])

    return theta1, theta2, theta3, theta4, theta5, theta6

def velocityinversekinematics(vx, vy, vz, ox, oy, oz, theta1, theta2, theta3, theta4, theta5, theta6, alpha1, alpha2, alpha3, alpha4, alpha5, alpha6, rlength1, rlength2, rlength3, rlength4, rlength5, rlength6, dlength1, dlength2, dlength3, dlength4, dlength5, dlength6):
    
    t1 = sympy.symbols("t1")
    t2 = sympy.symbols("t2")
    t3 = sympy.symbols("t3")
    t4 = sympy.symbols("t4")
    t5 = sympy.symbols("t5")
    t6 = sympy.symbols("t6")
    
    al1 = sympy.symbols("al1")
    al2 = sympy.symbols("al2")
    al3 = sympy.symbols("al3")
    al4 = sympy.symbols("al4")
    al5 = sympy.symbols("al5")
    al6 = sympy.symbols("al6")
    
    r1 = sympy.symbols("r1")
    r2 = sympy.symbols("r2")
    r3 = sympy.symbols("r3")
    r4 = sympy.symbols("r4")
    r5 = sympy.symbols("r5")
    r6 = sympy.symbols("r6")
    
    d1 = sympy.symbols("d1")
    d2 = sympy.symbols("d2")
    d3 = sympy.symbols("d3")
    d4 = sympy.symbols("d4")
    d5 = sympy.symbols("d5")
    d6 = sympy.symbols("d6")
    
    
    H01 = [[cos(t1), -sin(t1) * cos(al1), sin(t1) * sin(al1), r1 * cos(t1)],
           [sin(t1), cos(t1) * cos(al1), -cos(t1) * sin(al1), r1 * sin(t1)],
           [0, sin(al1), cos(al1), d1],
           [0, 0, 0, 1]]
    
    H12 = [[cos(t2), -sin(t2) * cos(al2), sin(t2) * sin(al2), r2 * cos(t2)],
           [sin(t2), cos(t2) * cos(al2), -cos(t2) * sin(al2), r2 * sin(t2)],
           [0, sin(al2), cos(al2), d2],
           [0, 0, 0, 1]]
    
    H23 = [[cos(t3), -sin(t3) * cos(al3), sin(t3) * sin(al3), r3 * cos(t3)],
           [sin(t3), cos(t3) * cos(al3), -cos(t3) * sin(al3), r3 * sin(t3)],
           [0, sin(al3), cos(al3), d3],
           [0, 0, 0, 1]]
    
    H34 = [[cos(t4), -sin(t4) * cos(al4), sin(t4) * sin(al4), r4 * cos(t4)],
           [sin(t4), cos(t4) * cos(al4), -cos(t4) * sin(al4), r4 * sin(t4)],
           [0, sin(al4), cos(al4), d4],
           [0, 0, 0, 1]]
    
    H45 = [[cos(t5), -sin(t5) * cos(al5), sin(t5) * sin(al5), r5 * cos(t5)],
           [sin(t5), cos(t5) * cos(al5), -cos(t5) * sin(al5), r5 * sin(t5)],
           [0, sin(al5), cos(al5), d5],
           [0, 0, 0, 1]]
    
    H56 = [[cos(t6), -sin(t6) * cos(al6), sin(t6) * sin(al6), r6 * cos(t6)],
           [sin(t6), cos(t6) * cos(al6), -cos(t6) * sin(al6), r6 * sin(t6)],
           [0, sin(al6), cos(al6), d6],
           [0, 0, 0, 1]]
    
    
    
    H02 = Matrix(H01) * Matrix(H12)
    H03 = Matrix(H02) * Matrix(H23)
    H04 = Matrix(H03) * Matrix(H34)
    H05 = Matrix(H04) * Matrix(H45)
    H06 = Matrix(H05) * Matrix(H56)
    
    
    H01calc = sympy.N(Matrix(H01).subs({t1: radians(theta1), t2: radians(theta2), t3: radians(theta3), t4: radians(theta4), t5: radians(theta5), t6: radians(theta6), al1: radians(alpha1), al2: radians(alpha3), al3: radians(alpha3), al4: radians(alpha4), al5: radians(alpha5), al6: radians(alpha6), r1: rlength1, r2: rlength2, r3: rlength3, r4: rlength4, r5: rlength5, r6: rlength6, d1: dlength1, d2: dlength2, d3: dlength3, d4: dlength4, d5: dlength5, d6: dlength6}), 4, chop=True)
    H02calc = sympy.N(Matrix(H02).subs({t1: radians(theta1), t2: radians(theta2), t3: radians(theta3), t4: radians(theta4), t5: radians(theta5), t6: radians(theta6), al1: radians(alpha1), al2: radians(alpha3), al3: radians(alpha3), al4: radians(alpha4), al5: radians(alpha5), al6: radians(alpha6), r1: rlength1, r2: rlength2, r3: rlength3, r4: rlength4, r5: rlength5, r6: rlength6, d1: dlength1, d2: dlength2, d3: dlength3, d4: dlength4, d5: dlength5, d6: dlength6}), 4, chop=True)
    H03calc = sympy.N(Matrix(H03).subs({t1: radians(theta1), t2: radians(theta2), t3: radians(theta3), t4: radians(theta4), t5: radians(theta5), t6: radians(theta6), al1: radians(alpha1), al2: radians(alpha3), al3: radians(alpha3), al4: radians(alpha4), al5: radians(alpha5), al6: radians(alpha6), r1: rlength1, r2: rlength2, r3: rlength3, r4: rlength4, r5: rlength5, r6: rlength6, d1: dlength1, d2: dlength2, d3: dlength3, d4: dlength4, d5: dlength5, d6: dlength6}), 4, chop=True)
    H04calc = sympy.N(Matrix(H04).subs({t1: radians(theta1), t2: radians(theta2), t3: radians(theta3), t4: radians(theta4), t5: radians(theta5), t6: radians(theta6), al1: radians(alpha1), al2: radians(alpha3), al3: radians(alpha3), al4: radians(alpha4), al5: radians(alpha5), al6: radians(alpha6), r1: rlength1, r2: rlength2, r3: rlength3, r4: rlength4, r5: rlength5, r6: rlength6, d1: dlength1, d2: dlength2, d3: dlength3, d4: dlength4, d5: dlength5, d6: dlength6}), 4, chop=True)
    H05calc = sympy.N(Matrix(H05).subs({t1: radians(theta1), t2: radians(theta2), t3: radians(theta3), t4: radians(theta4), t5: radians(theta5), t6: radians(theta6), al1: radians(alpha1), al2: radians(alpha3), al3: radians(alpha3), al4: radians(alpha4), al5: radians(alpha5), al6: radians(alpha6), r1: rlength1, r2: rlength2, r3: rlength3, r4: rlength4, r5: rlength5, r6: rlength6, d1: dlength1, d2: dlength2, d3: dlength3, d4: dlength4, d5: dlength5, d6: dlength6}), 4, chop=True)
    H06calc = sympy.N(Matrix(H06).subs({t1: radians(theta1), t2: radians(theta2), t3: radians(theta3), t4: radians(theta4), t5: radians(theta5), t6: radians(theta6), al1: radians(alpha1), al2: radians(alpha3), al3: radians(alpha3), al4: radians(alpha4), al5: radians(alpha5), al6: radians(alpha6), r1: rlength1, r2: rlength2, r3: rlength3, r4: rlength4, r5: rlength5, r6: rlength6, d1: dlength1, d2: dlength2, d3: dlength3, d4: dlength4, d5: dlength5, d6: dlength6}), 4, chop=True)
    
    """
    print(f"H01: {H01calc}")
    print(f"H02: {H02calc}")
    print(f"H03: {H03calc}")
    print(f"H04: {H04calc}")
    print(f"H05: {H05calc}")
    print(f"H06: {H06calc}")
    """
    
    
    Z0 = [0, 0, 1]
    Z1 = [Matrix(H01calc)[0,2], Matrix(H01calc)[1,2], Matrix(H01calc)[0,2]]
    Z2 = [Matrix(H02calc)[0,2], Matrix(H02calc)[1,2], Matrix(H02calc)[0,2]]
    Z3 = [Matrix(H03calc)[0,2], Matrix(H03calc)[1,2], Matrix(H03calc)[0,2]]
    Z4 = [Matrix(H04calc)[0,2], Matrix(H04calc)[1,2], Matrix(H04calc)[0,2]]
    Z5 = [Matrix(H05calc)[0,2], Matrix(H05calc)[1,2], Matrix(H05calc)[0,2]]
    Z6 = [Matrix(H06calc)[0,2], Matrix(H06calc)[1,2], Matrix(H06calc)[0,2]]
    
    
    D0 = [0, 0, 0]
    D1 = [Matrix(H01calc)[0,3], Matrix(H01calc)[1,3], Matrix(H01calc)[2,3]]
    D2 = [Matrix(H02calc)[0,3], Matrix(H02calc)[1,3], Matrix(H02calc)[2,3]]
    D3 = [Matrix(H03calc)[0,3], Matrix(H03calc)[1,3], Matrix(H03calc)[2,3]]
    D4 = [Matrix(H04calc)[0,3], Matrix(H04calc)[1,3], Matrix(H04calc)[2,3]]
    D5 = [Matrix(H05calc)[0,3], Matrix(H05calc)[1,3], Matrix(H05calc)[2,3]]
    D6 = [Matrix(H06calc)[0,3], Matrix(H06calc)[1,3], Matrix(H06calc)[2,3]]
    
    Jv1 = Matrix(Z0).cross(Matrix(D6) - Matrix(D0))
    Jv2 = Matrix(Z1).cross(Matrix(D6) - Matrix(D1))
    Jv3 = Matrix(Z2).cross(Matrix(D6) - Matrix(D2))
    Jv4 = Matrix(Z3).cross(Matrix(D6) - Matrix(D3))
    Jv5 = Matrix(Z4).cross(Matrix(D6) - Matrix(D4))
    Jv6 = Matrix(Z5).cross(Matrix(D6) - Matrix(D5))
    
    jacobian = [[Jv1[0], Jv2[0], Jv3[0], Jv4[0], Jv5[0], Jv6[0]],
                [Jv1[1], Jv2[1], Jv3[1], Jv4[1], Jv5[1], Jv6[1]],
                [Jv1[2], Jv2[2], Jv3[2], Jv4[2], Jv5[2], Jv6[2]],
                [Z0[0], Z1[0], Z2[0], Z3[0], Z4[0], Z5[0]],
                [Z0[1], Z1[1], Z2[1], Z3[1], Z4[1], Z5[1]],
                [Z0[2], Z1[2], Z2[2], Z3[2], Z4[2], Z5[2]]]
    
    jacobiancalc = sympy.N(Matrix(jacobian).subs({t1: radians(theta1), t2: radians(theta2), t3: radians(theta3), t4: radians(theta4), t5: radians(theta5), t6: radians(theta6), al1: radians(alpha1), al2: radians(alpha3), al3: radians(alpha3), al4: radians(alpha4), al5: radians(alpha5), al6: radians(alpha6), r1: rlength1, r2: rlength2, r3: rlength3, r4: rlength4, r5: rlength5, r6: rlength6, d1: dlength1, d2: dlength2, d3: dlength3, d4: dlength4, d5: dlength5, d6: dlength6}))
    
    #print(f"Jacobian Matrix: {jacobiancalc.evalf(3)}")
    
    if jacobiancalc.det() == 0:
        print("singularity. can't find inverse of jacobian matrix.")
    else:
        jacobianinv = jacobiancalc.inv()
    
        #print(f"Jacobian Inverse: {jacobianinv.evalf(3)}")
    
        endmatrix = Matrix([vx, vy, vz, ox, oy, oz])

        qdotmatrix = jacobianinv * endmatrix

        qdot1 = qdotmatrix[0]
        qdot2 = qdotmatrix[1]
        qdot2 = qdotmatrix[1]
        qdot3 = qdotmatrix[2]
        qdot4 = qdotmatrix[3]
        qdot5 = qdotmatrix[4]
        qdot6 = qdotmatrix[5]
    
        return qdot1, qdot2, qdot3, qdot4, qdot5, qdot6

def main():
    R06 = [[-1, 0, 0],
           [0, -1, 0],
           [0, 0, 1]]

    a1 = 10
    a2 = 10
    a3 = 10
    a4 = 10
    a5 = 10

    px = float(input("input x coordinate of end factor: "))
    py = float(input("input y coordinate of end factor: ")) 
    pz = float(input("input z coordinate of end factor: "))
    
    posikresults = positioninversekinematics(R06, px, py, pz, a1, a2, a3, a4, a5)
    print(f"angle1: {np.degrees(posikresults[0])} \nangle2: {np.degrees(posikresults[1])} \nangle3: {np.degrees(posikresults[2])} \nangle4: {np.degrees(posikresults[3])} \nangle5: {np.degrees(posikresults[4])} \nangle6: {np.degrees(posikresults[5])}")
    
    vx = float(input("input x component of linear velocity: "))
    vy = float(input("input y component of linear velocity: "))
    vz = float(input("input z component of linear velocity: "))
    
    ox = float(input("input x component of angular velocity: "))
    oy = float(input("input y component of angular velocity: "))
    oz = float(input("input z component of angular velocity: "))
    
    velikresults = velocityinversekinematics(vx, vy, vz, ox, oy, oz, posikresults[0], posikresults[1], posikresults[2], posikresults[3], posikresults[4], posikresults[5], 90, 0, 0, -90, 90, 0, 0, a2, a3, 0, 0, 0, a1, 0, 0, 0, 0, a5)
    print(f"angular velocity1: {velikresults[0]} \nangular velocity2: {velikresults[1]} \nangular velocity3: {velikresults[2]} \nangular velocity4: {velikresults[3]} \nangular velocity5: {velikresults[4]} \nangular velocity6: {velikresults[5]} \n")

main()

    
    
    