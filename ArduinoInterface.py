import serial
import threading


class ArduinoInterface:

    def get_sensor_distance(self):
        self.check.acquire()
        returner = self.sensor_distances
        self.check.release()

        return returner

    def get_speed(self):
        self.check.acquire()
        returner = self.speed
        self.check.release()

        return returner

    def update(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
            print(line)
            data = line.split(',')

            self.check.acquire()
            self.speed = float(data[0])

            self.sensor_distances.clear()
            for i in range(0, len(data) - 1):
                self.sensor_distances.append(float(data[i + 1]))

            self.check.release()

    def __init__(self, loc, baud=115200):
        self.ser = serial.Serial(loc, baud, timeout=0.25)
        self.ser.reset_input_buffer()
        self.thread = threading.Thread(target=self.update)
        self.check = threading.Condition()
        self.speed = 0
        self.sensor_distances = []

        self.thread.start()
