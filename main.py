import PySimpleGUI as sg
import Gauge
import time
from Shunt import Shunt


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

    layout = [[sg.Col(layout_speed, p=0), sg.Col(layout_info, p=0), sg.Col(layout_progress, p=0),
               sg.Col(layout_direction, p=0), sg.Col(layout_horn, p=0)]]

    return sg.Window('The PySimpleGUI Element List',
                     layout,
                     finalize=True,
                     right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                     keep_on_top=True,
                     no_titlebar=True, )
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
    
    -
"""

last_time = time.time()
update_period = 0.1

current_degree = 0

battery_shunt = None
motor_shunt = None

# battery_shunt = Shunt()
# motor_shunt = Shunt(address=0x41)

while True:
    event, values = window_primary.read(timeout=0)

    if battery_shunt:
        battery_shunt.update()
    if motor_shunt:
        motor_shunt.update()

    if time.time() - last_time > update_period:
        if motor_shunt:
            window_primary["-Motor-AMP-Progress-"].update(motor_shunt.current())
            window_primary["-Motor-AMP-"].update(motor_shunt.current())
            window_primary["-Motor-V-"].update(motor_shunt.voltage())
        if battery_shunt:
            window_primary["-Battery-Percent-Progress-"].update(battery_shunt.voltage())
            window_primary["-Battery-AMP-"].update(battery_shunt.current())
            window_primary["-Battery-V-"].update(battery_shunt.voltage())

        current_degree += 2
        current_degree = current_degree % 180
        speed_gauge.change(degree=current_degree)
        window_primary["-SpeedGauge-Text-"].update(str(current_degree) + " MPH")
        # print("Changed")
        last_time = time.time()

    # sg.Print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == "-Reverse-":
        window_primary["-Reverse-"].update(disabled=True)
        window_primary["-Forward-"].update(disabled=False)
    elif event == "-Forward-":
        window_primary["-Reverse-"].update(disabled=False)
        window_primary["-Forward-"].update(disabled=True)

window_primary.close()
