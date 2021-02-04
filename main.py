def on_button_pressed_a():
    music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
    kitronik_smart_greenhouse.control_high_power_pin(kitronik_smart_greenhouse.HighPowerPins.PIN13,
        kitronik_smart_greenhouse.on_off(True))
    basic.pause(100)
    kitronik_smart_greenhouse.control_high_power_pin(kitronik_smart_greenhouse.HighPowerPins.PIN13,
        kitronik_smart_greenhouse.on_off(False))
input.on_button_pressed(Button.A, on_button_pressed_a)

zipLEDs = kitronik_smart_greenhouse.create_greenhouse_zip_display(3)
kitronik_smart_greenhouse.set_buzzer_pin()
kitronik_smart_greenhouse.set_time(0, 0, 0)

def on_forever():
    zipLEDs.set_zip_led_color(0, kitronik_smart_greenhouse.colors(ZipLedColors.RED))
    zipLEDs.set_zip_led_color(1, kitronik_smart_greenhouse.colors(ZipLedColors.GREEN))
    zipLEDs.set_zip_led_color(2, kitronik_smart_greenhouse.colors(ZipLedColors.BLUE))
    zipLEDs.show()
    basic.show_string(kitronik_smart_greenhouse.read_time())
    if kitronik_smart_greenhouse.read_io_pin(kitronik_smart_greenhouse.PinType.ANALOG,
    kitronik_smart_greenhouse.IOPins.P0) > 500:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
    basic.pause(1000)
    basic.clear_screen()
    basic.show_string("P:")
    basic.show_number(0)
    basic.pause(500)
    basic.clear_screen()
    basic.show_string("T:")
    basic.show_number(0)
    basic.pause(500)
    basic.clear_screen()
    basic.show_string("H:")
    basic.show_number(0)
    basic.pause(500)
    basic.clear_screen()
    basic.show_number(kitronik_smart_greenhouse.pressure(PressureUnitList.M_BAR))
    basic.show_number(kitronik_smart_greenhouse.temperature(TemperatureUnitList.C))
    basic.show_number(kitronik_smart_greenhouse.humidity())
basic.forever(on_forever)
