def turn_left():
    pass


def wall_on_right():
    pass


def move():
    pass


def front_is_clear():
    pass


def right_is_clear():
    pass


def wall_in_front():
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def avoid_wall():
    if right_is_clear():
        turn_right()
    else:
        turn_left()


def kanan():
    if right_is_clear():
        turn_right()
        while wall_on_right():
            if wall_in_front():
                avoid_wall()
    elif front_is_clear():
        move()
        while front_is_clear():
            move()


while not at_goal():
    if wall_in_front():
        if right_is_clear():
            turn_right()
            while wall_in_front():
                turn_left()
        else:
            turn_left()
    elif front_is_clear():
        while wall_on_right():
            if wall_in_front():
                avoid_wall()
            elif front_is_clear():
                move()
            elif right_is_clear():
                turn_right()
            else:
                move()
    else:
        move()


def avoid_wall():
    if right_is_clear():
        turn_right()
    else:
        turn_left()

