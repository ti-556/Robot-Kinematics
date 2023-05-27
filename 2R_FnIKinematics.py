import math

def forwardkinematic(r1, r2, a1, a2):
    angle1 = math.radians(a1)
    angle2 = math.radians(a2)
    x = r1*math.cos(angle1) + r2*math.cos(angle1 + angle2)
    y = r1*math.sin(angle1) + r2*math.sin(angle1 + angle2)
    print(f"The x-coordinate is: {x}")
    print(f"The y-coordinate is: {y}")

def forwardinput(): 
    len1 = float(input("Input length of first arm: "))
    len2 = float(input("Input length of second arm: "))
    ang1 = float(input("Input first angle: "))
    ang2 = float(input("Input second angle: "))
    forwardkinematic(len1, len2, ang1, ang2)
    
def inversekinematic(elbow, r1, r2, x, y):
    if(elbow == "up"):
        angle2 = -(math.degrees(math.acos(((x ** 2) + (y ** 2) - (r1 ** 2) - (r2 ** 2))/(2 * r1 * r2))))
        angle1 = math.degrees(math.atan(y / x)) + math.degrees(math.atan((r2 * math.sin(math.radians(angle2)))/(r1 + r2 * math.cos(math.radians(angle2)))))
    elif(elbow == "down"):
        angle2 = math.degrees(math.acos(((x ** 2) + (y ** 2) - (r1 ** 2) - (r2 ** 2))/(2 * r1 * r2)))
        angle1 = math.degrees(math.atan(y / x)) - math.degrees(math.atan((r2 * math.sin(math.radians(angle2)))/(r1 + r2 * math.cos(math.radians(angle2)))))
    print(f"The first angle is: {angle1}")
    print(f"The second angle is: {angle2}")

def inverseinput():
    elbow = input("Choose elbow 'up' or 'down': ")
    len1 = float(input("Input length of first arm: "))
    len2 = float(input("Input length of second arm: "))
    x = float(input("Input x-coordinate: "))
    y = float(input("Input y-coordinate: "))
    inversekinematic(elbow, len1, len2, x, y)

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
