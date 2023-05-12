import math

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

#Forward: Input values are length of each segment, base length, angles between each segments, and the final angle of the arm from the xy plane
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

#Inverse: Output values are angles between each arm and the base angle
def inversekinematic(elbow, r1, r2, r3, d, x, y, z, a):
    if(elbow == "up"):
        angle1 = math.degrees(math.atan(y/x))
        
        x2 = x - math.cos(math.radians(angle1))*r3*math.cos(math.radians(a))
        y2 = y - math.sin(math.radians(angle1))*r3*math.cos(math.radians(a))
        z2 = z - r3*math.sin(math.radians(a))
        
        angle3 = -(math.degrees(math.acos(((x2 ** 2) + (y2 ** 2) + ((z2 - d) ** 2)- (r1 ** 2) - (r2 ** 2))/(2 * r1 * r2))))
        angle2 = math.degrees(math.atan((z2 - d) / (math.sqrt((x2 ** 2) + (y2 ** 2))))) + math.degrees(math.atan((r2 * math.sin(math.radians(angle3)))/(r1 + r2 * math.cos(math.radians(angle3)))))
        angle4 = a - angle2 - angle3
        
        print(f"The base angle is {angle1}")
        print(f"The second angle is: {angle2}")
        print(f"The third angle is: {angle3}")
        print(f"The fourth angle is {angle4}")

    elif(elbow == "down"):
        angle1 = math.degrees(math.atan(y/x))
        
        x2 = x - math.cos(math.radians(angle1))*r3*math.cos(math.radians(a))
        y2 = y - math.sin(math.radians(angle1))*r3*math.cos(math.radians(a))
        z2 = z - r3*math.sin(math.radians(a))
        
        angle3 = math.degrees(math.acos(((x2 ** 2) + (y2 ** 2) + ((z2 - d) ** 2)- (r1 ** 2) - (r2 ** 2))/(2 * r1 * r2)))
        angle2 = math.degrees(math.atan((z2 - d) / (math.sqrt((x2 ** 2) + (y2 ** 2))))) - math.degrees(math.atan((r2 * math.sin(math.radians(angle3)))/(r1 + r2 * math.cos(math.radians(angle3)))))
        angle4 = a - angle2 - angle3
        
        print(f"The base angle is {angle1}")
        print(f"The second angle is: {angle2}")
        print(f"The third angle is: {angle3}")
        print(f"The fourth angle is {angle4}")

    else:
        print(f"Was unable to comprehend {elbow}")

#Inverse: Input values are elbow side, length of each segment, base length, x, y, z coordinates of arm, and final angle of arm from xy axis 
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
    
    inversekinematic(elbow, len1, len2, len3, base, x, y, z, armangle)

#User chooses inverse or forward kinematic calculation
def userchoice():
    choice = input("Choose from 'forward' or 'inverse' kinematic analysis: ")
    if(choice == "forward"):
        forwardinput()
    elif(choice == "inverse"):
        inverseinput()
    else:
        print(f"Was unable to comprehend {choice}.\nPlease try again.")
        userchoice()
    
userchoice()
