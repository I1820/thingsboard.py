# In The Name Of God
# ========================================
# [] File Name : example-aolab.py
#
# [] Creation Date : 23-05-2018
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
import io
import serial
import sys


from tb.app import ThingsBoardApp


token = 'DHT11_DEMO_TOKEN'

app = ThingsBoardApp(token, '127.0.0.1')

ser = serial.serial_for_url('/dev/ttyUSB0', baudrate=115200, timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

thing_sensors = {
    't': 'temperature',
    'l': 'light',
    'h': 'humidity',
    'm': 'motion',
    'g': 'gas'
}


def serial_read():
    message = sio.readline()

    if len(message) == 0 or message[0] != '@':
            return
    parts = message.split(',')
    node = parts[0][1:]
    if parts[-1][0].isalpha():
        battery = 0
        parts[-1] = parts[-1][:-2]
    else:
        battery = parts[-1][:-2]
        parts.pop()
    try:
        battery = (int(battery) - 2900) // 13
    except (KeyError, ValueError):
        battery = 0

    states = []
    for thing in parts[1:]:
        states.append({
            thing_sensors[thing[0]]: thing[2:],
        })
    print(states)
    app.log(states)


if __name__ == '__main__':
    app.run()
    while True:
        try:
            serial_read()
        except serial.SerialException:
            sys.exit(1)
        except Exception as e:
            print(e)
