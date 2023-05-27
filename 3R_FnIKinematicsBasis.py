import math

#Forward: Output values are x and y coordinates of the arm
def forwardkinematic(r1, r2, r3, a1, a2, arm):
    angle1 = math.radians(a1)
    angle2 = math.radians(a2)
    armrad = math.radians(arm)
    x = r1*math.cos(angle1) + r2*math.cos(angle1 + angle2) + r3*math.cos(armrad)
    y = r1*math.sin(angle1) + r2*math.sin(angle1 + angle2) + r3*math.sin(armrad)
    print(f"The x-coordinate is: {x}")
    print(f"The y-coordinate is: {y}")

#Forward: Input values are length of each segment, angles between each segments, and the final angle of the arm from the +x axis
def forwardinput(): 
    len1 = float(input("Input length of first arm: "))
    len2 = float(input("Input length of second arm: "))
    len3 = float(input("Input length of third arm: "))
    ang1 = float(input("Input first angle: "))
    ang2 = float(input("Input second angle: "))
    armangle = float(input("Input arm angle from x-axis: "))
    forwardkinematic(len1, len2, len3, ang1, ang2, armangle)

#Inverse: Output values are angles between each arm
def inversekinematic(elbow, r1, r2, r3, x, y, a):
    if(elbow == "up"):
        x2 = x - r3*math.cos(math.radians(a))
        y2 = y - r3*math.sin(math.radians(a))
        angle2 = -(math.degrees(math.acos(((x2 ** 2) + (y2 ** 2) - (r1 ** 2) - (r2 ** 2))/(2 * r1 * r2))))
        angle1 = math.degrees(math.atan(y2 / x2)) + math.degrees(math.atan((r2 * math.sin(math.radians(angle2)))/(r1 + r2 * math.cos(math.radians(angle2)))))
        angle3 = a - angle1 - angle2
        print(f"The first angle is: {angle1}")
        print(f"The second angle is: {angle2}")
        print(f"The third angle is {angle3}")
    elif(elbow == "down"):
        x2 = x - r3*math.cos(math.radians(a))
        y2 = y - r3*math.sin(math.radians(a))
        angle2 = math.degrees(math.acos(((x2 ** 2) + (y2 ** 2) - (r1 ** 2) - (r2 ** 2))/(2 * r1 * r2)))
        angle1 = math.degrees(math.atan(y2 / x2)) - math.degrees(math.atan((r2 * math.sin(math.radians(angle2)))/(r1 + r2 * math.cos(math.radians(angle2)))))
        angle3 = a - angle1 - angle2
        print(f"The first angle is: {angle1}")
        print(f"The second angle is: {angle2}")
        print(f"The third angle is {angle3}")
    else:
        print(f"Was unable to comprehend {elbow}")

#Inverse: Input values are elbow side, length of each segment, x and y coordinates of arm, and final angle of arm from +x axis 
def inverseinput():
    elbow = input("Choose elbow 'up' or 'down' for the joint between first and second arm: ")
    len1 = float(input("Input length of first arm: "))
    len2 = float(input("Input length of second arm: "))
    len3 = float(input("Input length of third arm: "))
    x = float(input("Input x-coordinate: "))
    y = float(input("Input y-coordinate: "))
    armangle = float(input("Input arm angle from x-axis: "))
    inversekinematic(elbow, len1, len2, len3, x, y, armangle)

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
