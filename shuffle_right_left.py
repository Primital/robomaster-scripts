def flip_rotation(rotation):
    if rotation == rm_define.clockwise:
        return rm_define.anticlockwise
    return rm_define.clockwise

def shuffle(right=True):

    variable_r_v = 45
    variable_time = 0
    variable_direction = 90
    rot_cw = right
    rot_var = rm_define.clockwise
    dir_mod = 1

    # Time to revolve one quarter circle
    qc_time = 90 / variable_r_v

    if not rot_cw:
        rot_var = rm_define.anticlockwise
        dir_mod = -1

    chassis_ctrl.move_with_time(dir_mod * variable_direction, 0.1)

    chassis_ctrl.set_rotate_speed(variable_r_v)

    tools.timer_ctrl(rm_define.timer_start)
    while not variable_time >= qc_time / 2:
        variable_direction = 90 - ((variable_time * variable_r_v) % 45)
        chassis_ctrl.move_and_rotate(dir_mod * variable_direction, rot_var)
        variable_time = tools.timer_current()

    tools.timer_ctrl(rm_define.timer_reset)
    tools.timer_ctrl(rm_define.timer_start)
    variable_time = 0
    rot_var = flip_rotation(rot_var)

    while not variable_time >= qc_time:
        variable_direction = 45 + ((variable_time * variable_r_v) /  qc_time)

        chassis_ctrl.move_and_rotate(dir_mod * variable_direction, rot_var)
        variable_time = tools.timer_current()

    tools.timer_ctrl(rm_define.timer_reset)
    tools.timer_ctrl(rm_define.timer_start)
    variable_time = 0
    rot_var = flip_rotation(rot_var)

    while not variable_time >= qc_time:
        variable_direction = 135 - ((variable_time * variable_r_v))

        chassis_ctrl.move_and_rotate(dir_mod * variable_direction, rot_var)
        variable_time = tools.timer_current()


    tools.timer_ctrl(rm_define.timer_reset)
    tools.timer_ctrl(rm_define.timer_start)
    variable_time = 0
    rot_var = flip_rotation(rot_var)

    while not variable_time >= qc_time / 2:
        variable_direction = 45 + ((variable_time * variable_r_v))
        chassis_ctrl.move_and_rotate(dir_mod * variable_direction, rot_var)
        variable_time = tools.timer_current()


def start():
    shuffle(right=True)
    time.sleep(1)
    shuffle(right=False)
