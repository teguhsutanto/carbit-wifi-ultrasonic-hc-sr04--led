let distance = 0
function Mundur () {
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.analogWritePin(AnalogPin.P8, 0)
    pins.analogWritePin(AnalogPin.P9, 200)
    pins.analogWritePin(AnalogPin.P12, 200)
    pins.analogWritePin(AnalogPin.P15, 0)
}
function Kanan () {
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.analogWritePin(AnalogPin.P8, 150)
    pins.analogWritePin(AnalogPin.P9, 0)
    pins.analogWritePin(AnalogPin.P12, 150)
    pins.analogWritePin(AnalogPin.P15, 0)
}
function readDistance () {
    pins.digitalWritePin(DigitalPin.P1, 0)
    control.waitMicros(2)
    pins.digitalWritePin(DigitalPin.P1, 1)
    control.waitMicros(10)
    pins.digitalWritePin(DigitalPin.P1, 0)
    distance = Math.idiv(pins.pulseIn(DigitalPin.P2, PulseValue.High), 58)
    basic.pause(100)
}
function Maju () {
    pins.digitalWritePin(DigitalPin.P11, 1)
    pins.analogWritePin(AnalogPin.P8, 220)
    pins.analogWritePin(AnalogPin.P9, 0)
    pins.analogWritePin(AnalogPin.P12, 0)
    pins.analogWritePin(AnalogPin.P15, 220)
}
function Kiri () {
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.analogWritePin(AnalogPin.P8, 0)
    pins.analogWritePin(AnalogPin.P9, 150)
    pins.analogWritePin(AnalogPin.P12, 0)
    pins.analogWritePin(AnalogPin.P15, 150)
}
function Stop () {
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P9, 0)
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.digitalWritePin(DigitalPin.P15, 0)
}
basic.forever(function () {
    readDistance()
    if (distance > 40) {
        Maju()
    }
    if (distance >= 25 && distance <= 40) {
        Kanan()
    }
    if (distance >= 3 && distance <= 25) {
        Stop()
        basic.pause(200)
        Mundur()
        basic.pause(200)
        Kiri()
    }
})
