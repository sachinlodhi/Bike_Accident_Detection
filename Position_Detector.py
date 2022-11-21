# This is the main file and others are dependencies . This works with the Sensor Node Free App
# Download Sensor app here : https://play.google.com/store/apps/details?id=com.mscino.sensornode&hl=en_IN&gl=US
from socket import *
import threading
import message_sending
import os
import Extractor

#things for sound
duration = 1  # seconds
freq = 440  # Hz

# things for socket
PORT = 5555
IP = "0.0.0.0"
sock = socket(AF_INET, SOCK_DGRAM) # SOCK_DGRAM means UDP socket
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind((IP, PORT))

# things for beeping
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1  # Set Duration To 1 = 1 seconds
def beep(stop):
    while True:
        # winsound.Beep(frequency, 2000) # uncomment if pc is windows
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        print('always in this')
        if exit_flag:
            break

time_down = 0 # check how long vehicle is not in correct position
exit_flag = False # variable to check vehicle position and stopping beep and starting it
old_axis = 2
sms_flag = True # to send sms only once
while True:
    data, addr = sock.recvfrom(1024) # blocking of data
    values = Extractor.get_data(data)
    print(values[2])
    if old_axis < 2 and float(values[2]) < 2:
        # print("STILL DOWN")
        time_down += 1  # if car keeps down increase the timer to check
        if time_down > 5 and sms_flag:
            # message_sending.sendAlert([LIST_OF_RECIPIENTS], latitute,longitude)
            message_sending.sendAlert(['+919340164878'], values[0],values[1])
            time_down = 0
            print(f'Access the location at : https://www.google.com/search?q={values[0]}+%2C+{values[1]}')
            sms_flag = False
        continue
    if old_axis > 2 and float(values[2]) > 2:

        time_down = 0  # if car gets back up it resets to 0
        print("BACKS UP")
        continue

    # Updating previous status if the position changes
    old_axis = float(values[2]) # -> previous state of the vehicle position
    if old_axis < 2:
        print("DOWN")




        exit_flag = False
        t = threading.Thread(target=beep, args=(lambda: exit_flag,))
        t.start() # start beeping
        continue
    # stop beeping if old_axis>2
    exit_flag = True
    try:
        t.join() # stopping beep if old_axis changes
    except:
        None
    print("UP")










