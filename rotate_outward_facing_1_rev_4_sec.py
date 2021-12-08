variable_time = 0
variable_v = 0
variable_r_v = 0
variable_direction = 0
variable_right = True
def start():
    global variable_time
    global variable_v
    global variable_r_v
    global variable_direction
    global variable_right

    variable_r_v = 90
    variable_time = 0
    variable_direction = 90
    rot_cw = True
    rot_var = rm_define.clockwise
    tools.timer_ctrl(rm_define.timer_start)

    if not rot_cw:
        variable_direction *= -1
        rot_var = rm_define.anticlockwise
    #chassis_ctrl.move_with_distance(0, 0.5)
    while not variable_time >= 4:
        chassis_ctrl.set_rotate_speed(variable_r_v)
        #chassis_ctrl.rotate(rm_define.anticlockwise)
        #chassis_ctrl.rotate(rm_define.clockwise)

        chassis_ctrl.move_and_rotate(variable_direction, rot_var)
        variable_time = tools.timer_current()
