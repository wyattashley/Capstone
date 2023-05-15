import PySimpleGUI as sg
from Shunt import Shunt
from ArduinoInterface import ArduinoInterface
import Gauge
import time
import PinoutMap
from pygame import mixer
import AutoShift

def build_primary_window(theme=None):
    sg.theme(theme)

    gauge_size = (450, 250)
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

    layout_sensor = [[sg.Button('100', size=(4, 2), k="lf", pad=(0, 0), disabled=True, font=('Any', 20, 'bold')), sg.Button('100', size=(4, 2), k="rf", pad=(0, 0), disabled=True, font=('Any', 20, 'bold'))],
                     [sg.Button('100', size=(4, 2), k="lm", pad=(0, 0), disabled=True, font=('Any', 20, 'bold')), sg.Button('100', size=(4, 2), k="rm", pad=(0, 0), disabled=True, font=('Any', 20, 'bold'))],
                     [sg.Button('100', size=(4, 2), k="lb", pad=(0, 0), disabled=True, font=('Any', 20, 'bold')), sg.Button('100', size=(4, 2), k="rb", pad=(0, 0), disabled=True, font=('Any', 20, 'bold'))]]

    layout = [[sg.Col(layout_info), sg.Col(layout_sensor), sg.Col(layout_progress), sg.Col(layout_direction), sg.Col(layout_processor)], #sg.Col(layout_horn)],
              [layout_speed]]

    return sg.Window('Panel 1',
                     layout,
                     finalize=True,
                     right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                     keep_on_top=True,
                     size=(1024, 600),
                     element_justification='c')
    ##no_titlebar=True, )
    # grab_anywhere=True)


def build_secondary_window():
    gauge_size = (450, 250)
    layout_speed = [
        [sg.Graph(gauge_size, (-gauge_size[0] // 2, 0), (gauge_size[0] // 2, gauge_size[1]), key='-SpeedGauge-')],
        [sg.T(size=(12, 1), font='Any 20', justification='c', k="-SpeedGauge-Text-", auto_size_text=True)]]

    layout_shift = [
        [sg.Button(button_text="High", font='Any 30', button_color=('white', 'red'), key="-High-")],
        [sg.Button(button_text="Auto", font='Any 30', button_color=('white', 'blue'), key="-Auto-")],
        [sg.Button(button_text="Low", font='Any 30', button_color=('white', 'green'), key="-Low-")]
    ]

    layout_pinout = [[sg.Button(button_text="Pinout\nMap", size=(6, 2), font='Any 30', button_color=('white', 'grey'), key="-Pinout-")]]

    layout_challenge = [[sg.Button(button_text="Challenge\nConfig", size=(9, 2), font='Any 20', button_color=('white', 'grey'), key="-Challenge-")]]

    layout = [[sg.Col(layout_challenge), sg.Col(layout_shift, justification='c'), sg.Col(layout_pinout)], #sg.Col(layout_horn)],
              [layout_speed]]

    return sg.Window('Panel 2',
                     layout,
                     finalize=True,
                     right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                     keep_on_top=True,
                     size=(1024, 600),
                     element_justification='c')
    ##no_titlebar=True, )
    # grab_anywhere=True)

window_primary = build_primary_window('Dark')
window_secondary = build_secondary_window()
# window.Maximize()


speed_gauge = Gauge.Gauge(pointer_color='red', clock_color=sg.theme_text_color(),
                          major_tick_color=sg.theme_text_color(),
                          minor_tick_color=sg.theme_input_background_color(),
                          pointer_outer_color=sg.theme_text_color(),
                          major_tick_start_radius=160,
                          minor_tick_start_radius=160, minor_tick_stop_radius=200, major_tick_stop_radius=200,
                          major_tick_step=(180 // 5),
                          clock_radius=200, pointer_line_width=3, pointer_inner_radius=10, pointer_outer_radius=200,
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


forwardVoltageReadPin = None
reverseVoltageReadPin = None
forwardControlRelayPin = None
reverseControlRelayPin = None
shiftSolenoidHighPin = None
shiftSolenoidLowPin = None
hornControlRelayPin = None

battery_shunt = None
motor_shunt = None

auto_shift = AutoShift.AutoShift()

#arduino_interface = ArduinoInterface('/dev/ttyACM0')
#arduino_interface = ArduinoInterface('COM3')
arduino_interface = None

debug = True

if not debug:
    import RPi.GPIO as GPIO

    forwardVoltageReadPin = 23
    reverseVoltageReadPin = 24
    forwardControlRelayPin = 9
    reverseControlRelayPin = 10

    shiftSolenoidHighPin = 11
    shiftSolenoidLowPin = 25

    hornControlRelayPin = 19

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
    #battery_shunt = Shunt(address=0x41)
    motor_shunt = Shunt()


# Shifting Function
# True - High
# False - Low
# None - Not set
def shift(value):
    if (shiftSolenoidLowPin is None) or (shiftSolenoidHighPin is None):
        return

    if value is None:
        GPIO.output(shiftSolenoidLowPin, GPIO.LOW)
        GPIO.output(shiftSolenoidHighPin, GPIO.LOW)
    elif value:
        GPIO.output(shiftSolenoidLowPin, GPIO.LOW)
        GPIO.output(shiftSolenoidHighPin, GPIO.HIGH)
    elif not value:
        GPIO.output(shiftSolenoidLowPin, GPIO.HIGH)
        GPIO.output(shiftSolenoidHighPin, GPIO.LOW)


# Finds direction of manual forward reverse
# True  - Forward
# False - Reverse
# None  - Unknown
def manual_direction():
    if (forwardVoltageReadPin is None) or (reverseVoltageReadPin is None):
        return None

    if GPIO.input(forwardVoltageReadPin):
        return True
    elif GPIO.input(reverseVoltageReadPin):
        return False
    else:
        return None


def set_software_direction(direction):
    if (forwardControlRelayPin is None) or (reverseControlRelayPin is None):
        return

    if direction is None:
        GPIO.output(forwardControlRelayPin, GPIO.LOW)
        GPIO.output(reverseControlRelayPin, GPIO.LOW)
    elif direction:
        GPIO.output(forwardControlRelayPin, GPIO.HIGH)
        GPIO.output(reverseControlRelayPin, GPIO.LOW)
    else:
        GPIO.output(forwardControlRelayPin, GPIO.LOW)
        GPIO.output(reverseControlRelayPin, GPIO.HIGH)

def get_distance_color(distance):
    if distance == 0:
        return 'green'
    elif distance < 15:
        return 'red'
    elif distance < 50:
        return 'yellow'
    else:
        return 'green'


last_loop_time = time.time_ns()
last_time = time.time()

update_period = 0.1
current_speed = 0

force_shift = False
shift(False)
window_secondary["-Low-"].update(disabled=False)
window_secondary["-Auto-"].update(disabled=True)
window_secondary["-High-"].update(disabled=False)

window_primary["-Reverse-"].update(disabled=False)
window_primary["-Forward-"].update(disabled=True)
set_software_direction(True)

current_direction_reading = False

mixer.init()
alert=mixer.Sound('beep.wav')

# True - Horn On
# False - Horn Off
kartHornState = False

while True:
    event, values = window_primary.read(timeout=0)
    event2, values2 = window_secondary.read(timeout=0)

    if time.time() - last_time > update_period:

        # Update all the sensor values
        if motor_shunt is not None:
            window_primary["-Motor-AMP-Progress-"].update(motor_shunt.current())
            window_primary["-Motor-AMP-"].update(motor_shunt.current())
            window_primary["-Motor-V-"].update(motor_shunt.voltage())

        if battery_shunt is not None:
            window_primary["-Battery-Percent-Progress-"].update(battery_shunt.voltage())
            window_primary["-Battery-AMP-"].update(battery_shunt.current())
            window_primary["-Battery-V-"].update(battery_shunt.voltage())

        if kartHornState and hornControlRelayPin is not None:
            GPIO.output(hornControlRelayPin, GPIO.LOW)
            kartHornState = False

        if event == "-Horn-" and hornControlRelayPin is not None:
            GPIO.output(hornControlRelayPin, GPIO.HIGH)
            kartHornState = True

        if arduino_interface is not None:
            window_primary["-SpeedGauge-Text-"].update(str(int(arduino_interface.get_speed())) + "MPH")
            speed_gauge.change(degree=((arduino_interface.get_speed() / 40.0) * 180))

            distances = arduino_interface.get_sensor_distances()
            if len(distances) > 5:
                window_primary["lf"].update(distances[0], disabled_button_color=('black', get_distance_color(distances[0])), button_color=get_distance_color(distances[0]))
                window_primary["lm"].update(distances[1], disabled_button_color=('black', get_distance_color(distances[1])), button_color=get_distance_color(distances[1]))
                window_primary["lb"].update(distances[2], disabled_button_color=('black', get_distance_color(distances[2])), button_color=get_distance_color(distances[2]))

                window_primary["rf"].update(distances[3], disabled_button_color=('black', get_distance_color(distances[3])), button_color=get_distance_color(distances[3]))
                window_primary["rm"].update(distances[4], disabled_button_color=('black', get_distance_color(distances[4])), button_color=get_distance_color(distances[4]))
                window_primary["rb"].update(distances[5], disabled_button_color=('black', get_distance_color(distances[5])), button_color=get_distance_color(distances[5]))

                for distance in distances:
                    if 15 > distance > 0 and not mixer.get_busy():
                        alert.play()

        window_primary["-Loop-Time-"].update((time.time_ns() - last_loop_time) / 1_000_000)

        last_time = time.time()

        # Check for the manual direction change
        current_direction_reading = manual_direction()

    # Need to add a diode to the forward reverse
    if current_direction_reading is None:
        if event == "-Forward-":
            # Update buttons to reflect a forward state
            window_primary["-Reverse-"].update(disabled=False)
            window_primary["-Forward-"].update(disabled=True)

            # Set forward relay to be active
            set_software_direction(True)
        elif event == "-Reverse-":
            # Update buttons to reflect a reverse state
            window_primary["-Reverse-"].update(disabled=True)
            window_primary["-Forward-"].update(disabled=False)

            # Set reverse relay to be active
            set_software_direction(False)
    elif current_direction_reading is True:
        # Disable both direction relays
        set_software_direction(None)

        # Set manual value to display
        window_primary["-Reverse-"].update(disabled=False)
        window_primary["-Forward-"].update(disabled=True)
    elif current_direction_reading is False:
        # Disable both direction relays
        set_software_direction(None)

        # Set manual value to display
        window_primary["-Reverse-"].update(disabled=True)
        window_primary["-Forward-"].update(disabled=False)

    if event2 == "-Low-":
        # Update buttons to reflect a low state
        window_secondary["-Low-"].update(disabled=True)
        window_secondary["-Auto-"].update(disabled=False)
        window_secondary["-High-"].update(disabled=False)
        force_shift = True
    elif event2 == "-High-":
        # Update buttons to reflect a low state
        window_secondary["-Low-"].update(disabled=False)
        window_secondary["-Auto-"].update(disabled=False)
        window_secondary["-High-"].update(disabled=True)
        force_shift = True
    elif event2 == "-Auto-":
        # Update buttons to reflect a low state
        window_secondary["-Low-"].update(disabled=False)
        window_secondary["-Auto-"].update(disabled=True)
        window_secondary["-High-"].update(disabled=False)
        force_shift = False

    # sg.Print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if battery_shunt is not None:
        battery_shunt.update()

    if motor_shunt is not None:
        motor_shunt.update()
        shift_suggestion = auto_shift.update(motor_shunt.current(), motor_shunt.voltage())

        if shift_suggestion is not None and not force_shift:
            shift(shift_suggestion)

    last_loop_time = time.time_ns()

    if arduino_interface is not None:
        arduino_interface.update()

window_primary.close()
