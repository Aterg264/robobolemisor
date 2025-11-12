joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.down, function () {
    RadioGrup += 5
    if (RadioGrup >= 11) {
        RadioGrup = 1
    }
    radio.setGroup(RadioGrup)
    basic.showString("" + RadioGrup)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.down, function () {
    RadioGrup += -5
    if (RadioGrup <= 0) {
        RadioGrup = 1
    }
    radio.setGroup(RadioGrup)
    basic.showString("" + RadioGrup)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.down, function () {
    radio.sendString("D")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.down, function () {
    RadioGrup += 1
    if (RadioGrup == 11) {
        RadioGrup = 1
    }
    radio.setGroup(RadioGrup)
    basic.showString("" + RadioGrup)
})
let Yvalue = 0
let Xvalue = 0
let RadioGrup = 0
joystickbit.initJoystickBit()
RadioGrup = 1
radio.setGroup(RadioGrup)
basic.showString("" + RadioGrup)
music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.UntilDone)
basic.forever(function () {
    Xvalue = Math.map(joystickbit.getRockerValue(joystickbit.rockerType.X), 1023, 0, -100, 100)
    Yvalue = Math.map(joystickbit.getRockerValue(joystickbit.rockerType.Y), 1023, 0, -100, 100)
    radio.sendValue("x", Xvalue)
    radio.sendValue("y", Yvalue)
})
