def my_function():
    global RadioGrup
    RadioGrup += 5
    if RadioGrup >= 11:
        RadioGrup = 1
    radio.set_group(RadioGrup)
    basic.show_string("" + str(RadioGrup))
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function)

def my_function2():
    global RadioGrup
    RadioGrup += -5
    if RadioGrup <= 0:
        RadioGrup = 1
    radio.set_group(RadioGrup)
    basic.show_string("" + str(RadioGrup))
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function2)

def my_function3():
    radio.send_string("D")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function3)

def my_function4():
    global RadioGrup
    RadioGrup += 1
    if RadioGrup == 11:
        RadioGrup = 1
    radio.set_group(RadioGrup)
    basic.show_string("" + str(RadioGrup))
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.DOWN,
    my_function4)

Yvalue = 0
Xvalue = 0
RadioGrup = 0
joystickbit.init_joystick_bit()
RadioGrup = 1
radio.set_group(RadioGrup)
basic.show_string("" + str(RadioGrup))
music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    global Xvalue, Yvalue
    Xvalue = Math.map(joystickbit.get_rocker_value(joystickbit.rockerType.X),
        1023,
        0,
        -100,
        100)
    Yvalue = Math.map(joystickbit.get_rocker_value(joystickbit.rockerType.Y),
        1023,
        0,
        -100,
        100)
    radio.send_value("X", Xvalue)
    radio.send_value("Y", Yvalue)
basic.forever(on_forever)
