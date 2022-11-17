import math

def ik(target_x, target_y, target_z):
    # Mechanical Measurements
    B2bv = 100
    a2br = 15
    b2c = 120
    c2e = 120
    e2Tv = 10.0
    e2Tr = 110.0

    # target_x = 100.0
    # target_y = 150.0
    # target_z = 100.0
    GA = 0  # relative_gripper_angle

    wrist_x = target_x - ((e2Tr * math.cos(math.radians(GA)) + e2Tv * math.sin(math.radians(GA))) * math.cos(math.atan2(target_y, target_x)))
    wrist_y = target_y - ((e2Tr*math.cos(math.radians(GA)) + e2Tv * math.sin(math.radians(GA))) * math.sin(math.atan2(target_y, target_x)))
    wrist_z = target_z + ( e2Tr * math.sin(math.radians(GA)) ) +(e2Tv*math.cos(math.radians(GA) ) )

    joint_b_x = a2br*math.cos(math.atan2(target_y,target_x))
    joint_b_y = a2br*math.sin(math.atan2(target_y,target_x))
    joint_b_z = B2bv

    b2e = math.sqrt( (wrist_x - joint_b_x)**2 + (wrist_y - joint_b_y)**2 + (wrist_z - joint_b_z)**2 )
    b2eAngle = math.degrees(math.atan2((wrist_z - joint_b_z), math.sqrt( (wrist_x-joint_b_x)**2 + (wrist_y-joint_b_y)**2 )  ))
    bAngle1 = math.degrees(math.acos((b2e**2 + b2c**2 - c2e**2) / (2*b2e*b2c)))
    b2cAngle = math.degrees(math.acos((b2c**2+c2e**2-b2e**2)/(2*b2c*c2e)))
    a = 90 - math.degrees(math.atan2(target_y, target_x ))
    b = b2eAngle + bAngle1
    c = 180 - b2cAngle
    e = c - b + 90
    return {'a': a, 'b': b, 'c': c, 'e': e}
    # print(f'A:{a} B:{b} C:{c} E:{e}')
