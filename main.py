distance = 0
def Mundur():
    pins.analog_write_pin(AnalogPin.P5, 0)
    pins.analog_write_pin(AnalogPin.P9, 1023)
    pins.analog_write_pin(AnalogPin.P11, 1023)
    pins.analog_write_pin(AnalogPin.P15, 0)
def Kanan():
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P12, 1)
    pins.analog_write_pin(AnalogPin.P5, 400)
    pins.analog_write_pin(AnalogPin.P9, 0)
    pins.analog_write_pin(AnalogPin.P11, 400)
    pins.analog_write_pin(AnalogPin.P15, 0)
def readDistance():
    global distance
    pins.digital_write_pin(DigitalPin.P1, 0)
    control.wait_micros(2)
    pins.digital_write_pin(DigitalPin.P1, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P1, 0)
    distance = Math.idiv(pins.pulse_in(DigitalPin.P2, PulseValue.HIGH), 58)
    basic.pause(100)
def Maju():
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.analog_write_pin(AnalogPin.P5, 1023)
    pins.analog_write_pin(AnalogPin.P9, 0)
    pins.analog_write_pin(AnalogPin.P11, 0)
    pins.analog_write_pin(AnalogPin.P15, 1023)
def Kiri():
    pins.analog_write_pin(AnalogPin.P5, 0)
    pins.analog_write_pin(AnalogPin.P9, 400)
    pins.analog_write_pin(AnalogPin.P11, 0)
    pins.analog_write_pin(AnalogPin.P15, 400)
def Stop():
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P11, 0)
    pins.digital_write_pin(DigitalPin.P15, 0)

def on_forever():
    readDistance()
    if distance > 40:
        Maju()
    if distance >= 25 and distance <= 40:
        Kanan()
        basic.pause(100)
    if distance >= 3 and distance <= 24:
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P12, 0)
        Stop()
        basic.pause(100)
        Mundur()
        basic.pause(100)
        Kiri()
        basic.pause(100)
basic.forever(on_forever)
