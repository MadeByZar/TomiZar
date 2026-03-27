import serial
import time
import requests
import sys

arduino = serial.Serial(port='/dev/cu.usbmodem1301', baudrate=9600, timeout=1)

def send_data(data):
    print(f"Sending: {data}")
    arduino.write(f"{data}\n".encode('utf-8'))
    time.sleep(0.1)
    
    response = arduino.readline().decode('utf-8').strip()
    if response:
        print(f"Arduino responded: {response}")

def get_data():

    response = requests.get('http://10.0.0.103:4242/player/status')
    x = response.json()
    y = x['title']
    return y

def channel_up():
    requests.get('http://10.0.0.103:4242/player/channels/up')

def channel_down():
    requests.get('http://10.0.0.103:4242/player/channels/up')

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg == "pgup":
        channel_up()
    if arg == "pgdown":
        channel_down()
    if arg == "status":
        print(get_data())
