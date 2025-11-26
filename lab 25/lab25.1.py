import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)

time.sleep(2)  

def send_message(message):
    arduino.write((message + "\n").encode())  
    time.sleep(0.1)
    data = arduino.readline().decode().strip() 
    return data


msg = "Hello Arduino"
response = send_message(msg)

print("Message sent:", msg)
print("Arduino replied:", response)

arduino.close()