"""
    3.3v    |  5v
I2C GPIO 2  |  5v
I2C GPIO 3  |  GND
    GPIO 4  |  GPIO 14 (TX)
    GND     |  GPIO 15 (RX)
    GPIO 17 |  GPIO 18
    GPIO 27 |  GND
    GPIO 22 |  GPIO 23
    3.3v    |  GPIO 24
    GPIO 10 |  GND
    GPIO 9  |  GPIO 25
    GPIO 11 |  GPIO 8
    GND     |  GPIO 7
    GPIO 0  |  GPIO 1
    GPIO 5  |  GND
    GPIO 6  |  GPIO 12
    GPIO 13 |  GND
    GPIO 19 |  GPIO 16
    GPIO 26 |  GPIO 20
    GND     |  GPIO 21
    -------------------
"""
class PinoutMap:

    def __init__(self, sg, update_values=True):
        if update_values:
            import RPi.GPIO as GPIO

        self.sg = sg

        CIRCLE = '⚫'
        CIRCLE_OUTLINE = '⚪'

        layout = [
            [sg.Text("3.3V", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE, text_color="red", justification='c'),
             sg.Text(CIRCLE, text_color="red", justification='c'),
             sg.Text("5V", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 2", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO2Stat"),
             sg.Text(CIRCLE, text_color="red", justification='c'),
             sg.Text("5V", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 3", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO3Stat"),
             sg.Text(CIRCLE, text_color="black", justification='c'),
             sg.Text("GND", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 4", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO4Stat"),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO14Stat"),
             sg.Text("GPIO 14", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GND", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE, text_color="black", justification='c'),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO15Stat"),
             sg.Text("GPIO 15", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 17", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO17Stat"),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO18Stat"),
             sg.Text("GPIO 18", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 27", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO27Stat"),
             sg.Text(CIRCLE, text_color="black", justification='c'),
             sg.Text("GND", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 22", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO22Stat"),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO23Stat"),
             sg.Text("GPIO 23", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("3.3V", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE, text_color="red", justification='c'),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO24Stat"),
             sg.Text("GPIO 24", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 10", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO10Stat"),
             sg.Text(CIRCLE, text_color="black", justification='c'),
             sg.Text("GND", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 9", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO9Stat"),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO25Stat"),
             sg.Text("GPIO 25", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 11", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO11Stat"),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO8Stat"),
             sg.Text("GPIO 8", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GND", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE, text_color="black", justification='c'),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO7Stat"),
             sg.Text("GPIO 7", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 0", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO0Stat"),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO1Stat"),
             sg.Text("GPIO 1", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 5", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO5Stat"),
             sg.Text(CIRCLE, text_color="black", justification='c'),
             sg.Text("GND", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 6", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO2Stat"),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO12Stat"),
             sg.Text("GPIO 12", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 13", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO13Stat"),
             sg.Text(CIRCLE, text_color="black", justification='c'),
             sg.Text("GND", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 19", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO19Stat"),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO16Stat"),
             sg.Text("GPIO 16", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GPIO 26", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO26Stat"),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO20Stat"),
             sg.Text("GPIO 20", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.Text("GND", size=(17, 1), font='Any 10', justification='r', auto_size_text=True),
             sg.Text(CIRCLE, text_color="black", justification='c'),
             sg.Text(CIRCLE_OUTLINE, text_color="blue", justification='c', key="GPIO21Stat"),
             sg.Text("GPIO 21", size=(17, 1), font='Any 10', justification='l', auto_size_text=True)],

            [sg.OK()]
        ]

        self.window = sg.Window("Pinout View",
                           layout)

        while True:
            event, values = self.window.read(timeout=100)

            if update_values:
                self.update()

            if event == sg.WIN_CLOSED or event == 'Exit':
                break

        self.window.close()

    def update(self):
        for i in range(0, 27):
            function = GPIO.gpio_function(i)

            CIRCLE = '⚫'
            CIRCLE_OUTLINE = '⚪'

            if function == GPIO.IN:
                if(GPIO.input(i)):
                    self.window["GPIO" + str(i) + "Stat"].update(CIRCLE, text_color_for_value='blue')
                else:
                    self.window["GPIO" + str(i) + "Stat"].update(CIRCLE_OUTLINE, text_color_for_value='blue')
            elif function == GPIO.OUT:
                if(GPIO.input(i)):
                    self.window["GPIO" + str(i) + "Stat"].update(CIRCLE, text_color_for_value='red')
                else:
                    self.window["GPIO" + str(i) + "Stat"].update(CIRCLE_OUTLINE, text_color_for_value='red')
            elif function == GPIO.SPI:
                self.window["GPIO" + str(i) + "Stat"].update(CIRCLE_OUTLINE, text_color_for_value='violet')
            elif function == GPIO.I2C:
                self.window["GPIO" + str(i) + "Stat"].update(CIRCLE_OUTLINE, text_color_for_value='green')
            elif function == GPIO.HARD_PWM:
                self.window["GPIO" + str(i) + "Stat"].update(CIRCLE_OUTLINE, text_color_for_value='purple')
            elif function == GPIO.SERIAL:
                self.window["GPIO" + str(i) + "Stat"].update(CIRCLE_OUTLINE, text_color_for_value='white')
