import PySimpleGUI as sg
from Shunt import Shunt
from ArduinoInterface import ArduinoInterface
import Gauge
import time


def build_primary_window(theme=None):
    sg.theme(theme)

    gauge_size = (200, 100)
    layout_speed = [
        [sg.Graph(gauge_size, (-gauge_size[0] // 2, 0), (gauge_size[0] // 2, gauge_size[1]), key='-SpeedGauge-')],
        [sg.T(size=(12, 1), font='Any 20', justification='c', k="-SpeedGauge-Text-", auto_size_text=True)]]

    layout_info = [[sg.Frame("Motor", [
        [sg.Text("Current: 200amp", size=(17, 1), font='Any 10', justification='c', k="-Motor-AMP-",
                 auto_size_text=True)],
        [sg.Text("Voltage: 12v", size=(17, 1), font='Any 10', justification='c', k="-Motor-V-", auto_size_text=True)],
    ])], [sg.Frame("Battery", [
        [sg.Text("Capacity: 180amp", size=(17, 1), font='Any 10', justification='c', k="-Battery-Capacity-",
                 auto_size_text=True)],
        [sg.Text("Current: 200amp", size=(17, 1), font='Any 10', justification='c', k="-Battery-AMP-",
                 auto_size_text=True)],
        [sg.Text("Voltage: 12v", size=(17, 1), font='Any 10', justification='c', k="-Battery-V-",
                 auto_size_text=True)],
        [sg.Text("Resistance: 12ohm", size=(17, 1), font='Any 10', justification='c', k="-Battery-Resistance-",
                 auto_size_text=True)],
    ])]]

    layout_progress = [[sg.Frame("Motor AMP", [
        [sg.ProgressBar(100, orientation='v', size=(13, 60), style='winnative', key='-Motor-AMP-Progress-')],
    ]), sg.Frame("Battery %", [
        [sg.ProgressBar(100, orientation='v', size=(13, 60), style='winnative', key='-Battery-Percent-Progress-')],
    ])]]

    layout_direction = [
        [sg.Button(button_text="Reverse", font='Any 30', button_color=('white', 'red'), key="-Reverse-")],
        [sg.Button(button_text="Forward", font='Any 30', button_color=('white', 'green'), key="-Forward-")]
    ]

    layout_horn = [
        [sg.RealtimeButton("Horn", font='Any 30', size=(5, 2), button_color="grey", key='-Horn-')]
    ]

    layout_processor = [[sg.Frame("Loop Time MS", [
        [sg.ProgressBar(5, orientation='v', size=(13, 60), style='winnative', key='-Loop-Time-')],
    ])]]

    layout = [[sg.Col(layout_speed, p=0), sg.Col(layout_info, p=0), sg.Col(layout_progress, p=0),
               sg.Col(layout_direction, p=0), sg.Col(layout_horn, p=0), sg.Col(layout_processor, p=0)]]

    return sg.Window('The PySimpleGUI Element List',
                     layout,
                     finalize=True,
                     right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                     keep_on_top=True,)
                     ##no_titlebar=True, )
    # grab_anywhere=True)

def build_secondary_window(theme=None):
    sg.theme(theme)

    gauge_size = (200, 100)
    layout_speed = [
        [sg.Graph(gauge_size, (-gauge_size[0] // 2, 0), (gauge_size[0] // 2, gauge_size[1]), key='-SpeedGauge-')],
        [sg.T(size=(12, 1), font='Any 20', justification='c', k="-SpeedGauge-Text-", auto_size_text=True)]]

    layout_info = [[sg.Frame("Motor", [
        [sg.Text("Current: 200amp", size=(17, 1), font='Any 10', justification='c', k="-Motor-AMP-",
                 auto_size_text=True)],
        [sg.Text("Voltage: 12v", size=(17, 1), font='Any 10', justification='c', k="-Motor-V-", auto_size_text=True)],
    ])], [sg.Frame("Battery", [
        [sg.Text("Capacity: 180amp", size=(17, 1), font='Any 10', justification='c', k="-Battery-Capacity-",
                 auto_size_text=True)],
        [sg.Text("Current: 200amp", size=(17, 1), font='Any 10', justification='c', k="-Battery-AMP-",
                 auto_size_text=True)],
        [sg.Text("Voltage: 12v", size=(17, 1), font='Any 10', justification='c', k="-Battery-V-",
                 auto_size_text=True)],
        [sg.Text("Resistance: 12ohm", size=(17, 1), font='Any 10', justification='c', k="-Battery-Resistance-",
                 auto_size_text=True)],
    ])]]

    layout_progress = [[sg.Frame("Motor AMP", [
        [sg.ProgressBar(100, orientation='v', size=(13, 60), style='winnative', key='-Motor-AMP-Progress-')],
    ]), sg.Frame("Battery %", [
        [sg.ProgressBar(100, orientation='v', size=(13, 60), style='winnative', key='-Battery-Percent-Progress-')],
    ])]]

    layout_direction = [
        [sg.Button(button_text="Reverse", font='Any 30', button_color=('white', 'red'), key="-Reverse-")],
        [sg.Button(button_text="Forward", font='Any 30', button_color=('white', 'green'), key="-Forward-")]
    ]

    layout_horn = [
        [sg.RealtimeButton("Horn", font='Any 30', size=(5, 2), button_color="grey", key='-Horn-')]
    ]

    layout = [[sg.Col(layout_speed, p=0), sg.Col(layout_info, p=0), sg.Col(layout_progress, p=0),
               sg.Col(layout_direction, p=0), sg.Col(layout_horn, p=0)]]

    return sg.Window('The PySimpleGUI Element List',
                     layout,
                     finalize=True,
                     right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                     keep_on_top=True,)
                     ##no_titlebar=True, )
    # grab_anywhere=True)

window_primary = build_primary_window('Dark')
# window.Maximize()

speed_gauge = Gauge.Gauge(pointer_color='red', clock_color=sg.theme_text_color(),
                          major_tick_color=sg.theme_text_color(),
                          minor_tick_color=sg.theme_input_background_color(),
                          pointer_outer_color=sg.theme_text_color(),
                          major_tick_start_radius=80,
                          minor_tick_start_radius=80, minor_tick_stop_radius=100, major_tick_stop_radius=100,
                          major_tick_step=30,
                          clock_radius=100, pointer_line_width=3, pointer_inner_radius=10, pointer_outer_radius=100,
                          graph_elem=window_primary['-SpeedGauge-'])

speed_gauge.change(degree=0)

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
    
    - Battery Shunt I2C Address 0x40
    - Motor Shunt I2C Address 0x41
    
    - Forward Voltage Reading GPIO 23
    - Reverse Voltage Reading GPIO 24
    - Forward Control Relay GPIO 9
    - Reverse Control Relay GPIO 10
    
    - Shift Solenoid High GPIO 11
    - Shift Solenoid Low GPIO 25
    
Possibly Moving to Arduino
    - Trigger Left Distance Sensor GPIO 8
    - Trigger Right Distance Sensor GPIO 7
    - Echo Left Front Distance Sensor GPIO 1
    - Echo Right Front Distance Sensor GPIO 0
    - Echo Left Distance Sensor GPIO 5
    - Echo Right Distance Sensor GPIO 6
    - Echo Left Back Distance Sensor GPIO 12
    - Echo Right Back Distance Sensor GPIO 13
    
    - Horn Pin 19
"""
forwardVoltageReadPin = 23
reverseVoltageReadPin = 24
forwardControlRelayPin = 9
reverseControlRelayPin = 10

shiftSolenoidHighPin = 11
shiftSolenoidLowPin = 25

hornControlRelayPin = 19

#arduino_interface = ArduinoInterface('/dev/ttyACM0')

debug = True

if not debug:
    import RPi.GPIO as GPIO

    # Setup GPIO Pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Define Voltage Pins for direction
    GPIO.setup(forwardVoltageReadPin, GPIO.IN)
    GPIO.setup(reverseVoltageReadPin, GPIO.IN)
    GPIO.setup(forwardControlRelayPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(reverseControlRelayPin, GPIO.OUT, initial=GPIO.LOW)

    # Define the Horn Control Pin
    GPIO.setup(hornControlRelayPin, GPIO.OUT, initial=GPIO.LOW)

    # Define the Shifter Control Pins
    GPIO.setup(shiftSolenoidLowPin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(shiftSolenoidHighPin, GPIO.OUT, initial=GPIO.LOW)

    # Setup Battery Shunt
    battery_shunt = Shunt()
    motor_shunt = Shunt(address=0x41)

# Shifting Function
# True - High
# False - Low
# None - Not set
def shift(value):
    if value is None:
        GPIO.output(shiftSolenoidLowPin, GPIO.LOW)
        GPIO.output(shiftSolenoidHighPin, GPIO.LOW)
    elif value:
        GPIO.output(shiftSolenoidLowPin, GPIO.LOW)
        GPIO.output(shiftSolenoidHighPin, GPIO.HIGH)
    elif not value:
        GPIO.output(shiftSolenoidLowPin, GPIO.HIGH)
        GPIO.output(shiftSolenoidHighPin, GPIO.LOW)


last_loop_time = time.time_ns()
last_time = time.time()

update_period = 0.1

current_degree = 0

# 0 - Unknown/Unset
# 1 - Force Forward
# 2 - Force Reverse
# 3 - Electric Forward
# 4 - Electric Reverse
kartDirectionState = 0

# True - Horn On
# False - Horn Off
kartHornState = False

# True - Hall Effect High
# False - Hall Effect Low
kartSpeedHallEffectState = False

while True:
    event, values = window_primary.read(timeout=0)

    if time.time() - last_time > update_period:
        if not debug:

            window_primary["-Motor-AMP-Progress-"].update(motor_shunt.current())
            window_primary["-Motor-AMP-"].update(motor_shunt.current())
            window_primary["-Motor-V-"].update(motor_shunt.voltage())

            window_primary["-Battery-Percent-Progress-"].update(battery_shunt.voltage())
            window_primary["-Battery-AMP-"].update(battery_shunt.current())
            window_primary["-Battery-V-"].update(battery_shunt.voltage())

            if kartHornState:
                GPIO.output(hornControlRelayPin, GPIO.LOW)
                kartHornState = False

            if event == "-Horn-":
                GPIO.output(hornControlRelayPin, GPIO.HIGH)
                kartHornState = True

            window_primary["-SpeedGauge-Text-"].update(str(int(arduino_interface.get_speed())) + "MPH")
            speed_gauge.change(degree=((arduino_interface.get_speed() / 35.0) * 180))

        window_primary["-Loop-Time-"].update((time.time_ns() - last_loop_time) / 1_000_000)

        last_time = time.time()

    # sg.Print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if not debug:
        battery_shunt.update()
        motor_shunt.update()

        forceForwardKartDirection = GPIO.input(forwardVoltageReadPin)
        forceReverseKartDirection = GPIO.input(reverseVoltageReadPin)

        if (kartDirectionState == 1 or kartDirectionState == 2) and not forceForwardKartDirection and not forceReverseKartDirection:
            kartDirectionState = 0
            window_primary["-Reverse-"].update(disabled=False)
            window_primary["-Forward-"].update(disabled=False)

        if forceForwardKartDirection and kartDirectionState != 1:
            kartDirectionState = 1
            GPIO.output(forwardControlRelayPin, GPIO.LOW)
            GPIO.output(reverseControlRelayPin, GPIO.LOW)

            window_primary["-Reverse-"].update(disabled=False)
            window_primary["-Forward-"].update(disabled=True)
        elif forceReverseKartDirection and kartDirectionState != 2:
            kartDirectionState = 2
            GPIO.output(forwardControlRelayPin, GPIO.LOW)
            GPIO.output(reverseControlRelayPin, GPIO.LOW)

            window_primary["-Reverse-"].update(disabled=True)
            window_primary["-Forward-"].update(disabled=False)
        elif event == "-Reverse-" and (kartDirectionState != 2 or kartDirectionState != 1 or kartDirectionState != 4):
            kartDirectionState = 4
            GPIO.output(reverseControlRelayPin, GPIO.HIGH)
            GPIO.output(forwardControlRelayPin, GPIO.LOW)

            window_primary["-Reverse-"].update(disabled=True)
            window_primary["-Forward-"].update(disabled=False)
        elif event == "-Forward-" and (kartDirectionState != 2 or kartDirectionState != 1 or kartDirectionState != 3):
            kartDirectionState = 3
            GPIO.output(reverseControlRelayPin, GPIO.LOW)
            GPIO.output(forwardControlRelayPin, GPIO.HIGH)

            window_primary["-Reverse-"].update(disabled=False)
            window_primary["-Forward-"].update(disabled=True)

    last_loop_time = time.time_ns()


window_primary.close()
