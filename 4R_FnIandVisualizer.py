import math
import matplotlib.pyplot as plt
import numpy

#Forward: Output values are x, y, z coordinates of the arm
def forwardkinematic(r1, r2, r3, d, a1, a2, a3, arm):
    angle1 = math.radians(a1)
    angle2 = math.radians(a2)
    angle3 = math.radians(a3)
    armrad = math.radians(arm)
    
    x = math.cos(angle1)*(r1*math.cos(angle2) + r2*math.cos(angle2 + angle3) + r3*math.cos(armrad))
    y = math.sin(angle1)*(r1*math.cos(angle2) + r2*math.cos(angle2 + angle3) + r3*math.cos(armrad))
    z = d + r1*math.sin(angle2) + r2*math.sin(angle2 + angle3) + r3*math.sin(armrad)
    
    print(f"The x-coordinate is: {x}")
    print(f"The y-coordinate is: {y}")
    print(f"The z-coordinate is: {z}")

#Forward: Input values are length of each segment, angles between each segments, and the final angle of the arm from the +x axis
def forwardinput(): 
    len1 = float(input("Input length of first arm: "))
    len2 = float(input("Input length of second arm: "))
    len3 = float(input("Input length of third arm: "))
    
    base = float(input("Input length of base arm: "))
    
    ang1 = float(input("Input base angle: "))
    ang2 = float(input("Input second angle: "))
    ang3 = float(input("Input third angle: "))
    
    armangle = float(input("Input arm angle from xy-plane: "))
    
    forwardkinematic(len1, len2, len3, base, ang1, ang2, ang3, armangle)

#Inverse: Output values are angles between each arm and the coordinates of each joint
def inversekinematic(elbow, r1, r2, r3, d, x, y, z, a):
    if(elbow == "up"):
        if(x == 0 and y > 0):
            angle1 = 90
        elif(x == 0 and y < 0):
            angle1 = -90
        elif(y == 0 and x < 0):
            angle1 = -180
        else:
            angle1 = math.degrees(math.atan(y/x))
        
        x2 = x - math.cos(math.radians(angle1))*r3*math.cos(math.radians(a))
        y2 = y - math.sin(math.radians(angle1))*r3*math.cos(math.radians(a))
        z2 = z - r3*math.sin(math.radians(a))
        
        angle3 = -(math.degrees(math.acos(((x2 ** 2) + (y2 ** 2) + ((z2 - d) ** 2)- (r1 ** 2) - (r2 ** 2))/(2 * r1 * r2))))
        angle2 = math.degrees(math.atan((z2 - d) / (math.sqrt((x2 ** 2) + (y2 ** 2))))) + math.degrees(math.atan((r2 * math.sin(math.radians(angle3)))/(r1 + r2 * math.cos(math.radians(angle3)))))
        angle4 = a - angle2 - angle3

    elif(elbow == "down"):
        if(elbow == "up"):
            if(x == 0 and y > 0):
                angle1 = 90
            elif(x == 0 and y < 0):
                angle1 = -90
            elif(y == 0 and x < 0):
                angle1 = -180
            else:
                angle1 = math.degrees(math.atan(y/x))
        
        x2 = x - math.cos(math.radians(angle1))*r3*math.cos(math.radians(a))
        y2 = y - math.sin(math.radians(angle1))*r3*math.cos(math.radians(a))
        z2 = z - r3*math.sin(math.radians(a))
        
        angle3 = math.degrees(math.acos(((x2 ** 2) + (y2 ** 2) + ((z2 - d) ** 2)- (r1 ** 2) - (r2 ** 2))/(2 * r1 * r2)))
        angle2 = math.degrees(math.atan((z2 - d) / (math.sqrt((x2 ** 2) + (y2 ** 2))))) - math.degrees(math.atan((r2 * math.sin(math.radians(angle3)))/(r1 + r2 * math.cos(math.radians(angle3)))))
        angle4 = a - angle2 - angle3

    else:
        print(f"Was unable to comprehend {elbow}")
        
    x3 = math.cos(math.radians(angle1))*r1*math.cos(math.radians(angle2))
    y3 = math.sin(math.radians(angle1))*r1*math.cos(math.radians(angle2))
    z3 = d + r1*math.sin(math.radians(angle2))
    
    x4 = 0
    y4 = 0
    z4 = d
    
    return angle1, angle2, angle3, angle4, x4, x3, x2, x, y4, y3, y2, y, z4, z3, z2, z

#Inverse: Input values are elbow side, length of each segment, x and y coordinates of arm, and final angle of arm from +x axis 
def inverseinput():
    elbow = input("Choose elbow 'up' or 'down' for the joint between first and second arm: ")
    
    len1 = float(input("Input length of first arm: "))
    len2 = float(input("Input length of second arm: "))
    len3 = float(input("Input length of third arm: "))
    
    base = float(input("Input length of base arm: "))
    
    x = float(input("Input x-coordinate: "))
    y = float(input("Input y-coordinate: "))
    z = float(input("Input z-coordinate: "))
    
    armangle = float(input("Input arm angle from xy-plane: "))
    
    result = inversekinematic(elbow, len1, len2, len3, base, x, y, z, armangle)
    
    print(f"The base angle is {result[0]}")
    print(f"The second angle is: {result[1]}")
    print(f"The third angle is: {result[2]}")
    print(f"The fourth angle is {result[3]}")
    
    return result

#User chooses inverse or forward kinematic calculation
def userchoice():
    choice = input("Choose from 'forward' or 'inverse' kinematic analysis: ")
    if(choice == "forward"):
        forwardinput()
    elif(choice == "inverse"):
        visualizeinv()
    else:
        print(f"Was unable to comprehend {choice}.\nPlease try again.")
        userchoice()

#Setting coordinates for 3D visualizer
def visualizeinv():
    armdata = inverseinput()
    xcoords = [
        0,
        armdata[4],
        armdata[5],
        armdata[6],
        armdata[7]
    ]
    ycoords = [
        0,
        armdata[8],
        armdata[9],
        armdata[10],
        armdata[11]
    ]
    zcoords = [
        0,
        armdata[12],
        armdata[13],
        armdata[14],
        armdata[15]
    ]
    origin = [0, 0, 0]
    point1 = [
        armdata[4],
        armdata[8],
        armdata[12]
    ]
    point2 = [
        armdata[5],
        armdata[9],
        armdata[13]
    ]
    point3 = [
        armdata[6],
        armdata[10],
        armdata[14]
    ]
    endpoint =  [
        armdata[7],
        armdata[11],
        armdata[15]
    ]
    
    #Visualizing Arm
    fig = plt.figure()
    
    ax = fig.add_subplot(projection = '3d')
    
    ax.scatter(origin[0], origin[1], origin[2], color = 'blue')
    ax.scatter(point1[0], point1[1], point1[2], color = 'red')
    ax.scatter(point2[0], point2[1], point2[2], color = 'orange')
    ax.scatter(point3[0], point3[1], point3[2], color = 'purple')
    ax.scatter(endpoint[0], endpoint[1], endpoint[2], color = 'green')
    
    ax.plot(xcoords, ycoords, zcoords, color = 'black')
    
    for xcoords, ycoords, zcoords, in zip(xcoords, ycoords, zcoords):
        label = "(%d, %d, %d)" % (xcoords, ycoords, zcoords)
        ax.text(xcoords, ycoords, zcoords, label)
    
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    
    plt.show()

userchoice()
