# Bike Accident Detection System[Concept+Demo]

A program to detect if the bike has met an accident.

_[It is a demo and may require additional changes]_

## Features
- Can detect if the bike has met an accident based on the orientation of the bike(It is a demo
- Use a free app named [Sensor Node Free](https://play.google.com/store/apps/details?id=com.mscino.sensornode&hl=en_IN&gl=US)
- Can send an SOS message to the selected contact with the exact location of the bike
- Can locate the vehicle by the SOS sound produced by the device mounted

## Installation and initial setup

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt by using following command


```bash
pip install -r requirements.txt
```
- [Unblock port](https://learn.microsoft.com/en-us/answers/questions/291348/can39t-open-ports-in-windows-10.html) 5555 on your PC.
- Install  [Sensor Node Free](https://play.google.com/store/apps/details?id=com.mscino.sensornode&hl=en_IN&gl=US) on android device.
- Connect PC and android phone on the same local network.
- Open [Sensor Node Free](https://play.google.com/store/apps/details?id=com.mscino.sensornode&hl=en_IN&gl=US) app on android phone and navigate to _STREAM_ -> _STREAM LIVE DATA(XML)_.
- Select _Accelerometer_ and _GPS Coordinates_ from the list of available sensors. Scroll to find all sensors.
- Enter the Local IPv4 address of your PC in the _Target IP Address_ prompt and enter _PORT_ as _5555_.
- Click on button shown on same screen.
- Make a free account on [Twillio](https://www.twilio.com/) and get a free phone number from there and register the phone number(s) you want to receive messages on.
- Download repository files as ZIP.
- Extract ZIP files in the local directory.


## Usage

- Open the _Position_Detector.py_ file and assign the free number you got from Twillio and add your the number(s) you want to receive SOS message(s) on.


```python

free_num_from_twillio = '+19876543210' # replace this with your generated free twillio number (add country code)

contact_numbers = ['1111111111', '222222222222'] # assign the number here you want to send message on

```

-  Inside _beep_ function, uncomment the second statement if you are using Windows or uncomment the fourth statement if you are using Linux.
```python
# For windows
# winsound.Beep(2500, 2000) # uncomment if pc is windows
# For Linux
#os.system('play -nq -t alsa synth {} sine {}'.format(duration, frequency))
```


- Run _Position_Detector.py_ file and try changing the position of the android device.

## Assumptions

- Mobile is kept flat on its back: This is the idea position, which means the bike is running or standing properly.
- Any other orientation is that bike has either met an accident or is not on stand properly


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
