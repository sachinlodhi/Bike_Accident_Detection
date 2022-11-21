# Module for extraction of the latitude, longitude and acceleration
from bs4 import BeautifulSoup


def get_data(xmlstr):
    xmlstr = xmlstr.decode('ascii')  # changing the binary string to string(ascii)
    # print(xmlstr)
    print(xmlstr)

    soup = BeautifulSoup(xmlstr, features='lxml')
    # Extraction of the longitude and latitude
    lat = soup.find('latitude')
    long = soup.find('longitude')
    # The first coordinate x value from the accelerometer sensor of android determine the position of the vehicle
    accel1 = soup.find('accelerometer1')
    # print( lat.string, long.string, accel1.string)
    return [lat.string, long.string, accel1.string]
