time = 0
rotation_velocity = 0
direction = 0
def start():
    global time
    global rotation_velocity
    global direction
    rotation_velocity = 125
    time = 0
    tools.timer_ctrl(rm_define.timer_start)

    while notttime >= 3:
        chassis_ctrl.set_rotate_speed(rotation_velocity)
        direction = time * rotation_velocity) * -1
        direction = ((direction + 190) % 360) - 180
        chassis_ctrl.move_and_rotate(direction, rm_define.clockwise)
        time = tools.timer_current()
