# Robot-Kinematics
Python code for forward and inverse kinematic calculations of a robotic arm.

## Analytical Method
Simple trignometry based kinematic calculations.

### 2R Robotic Arm


### 4R Robotic Arm
For forward kinematics, the 3D coordinates can be determined by:

$x=(r_1\cos(\theta_2)+r_2\cos(\theta_2+\theta_3)+r_3\cos(\phi))\cos(\theta_1)$
$y=(r_1\cos(\theta_2)+r_2\cos(\theta_2+\theta_3)+r_3\cos(\phi))\sin(\theta_1)$
$z=d+r_1\sin(\theta_2)+r_2sin(\theta_2+\theta_3)+r_3\sin(\phi)$
