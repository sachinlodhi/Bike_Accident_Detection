# Module for extraction of the latitude, longitude and acceleration
from bs4 import BeautifulSoup
def get_data(xmlstr):
    xmlstr = xmlstr.decode('ascii')  # changing the binary string to string(ascii)
    # print(xmlstr)
    # print(xmlstr)

    soup = BeautifulSoup(xmlstr, features='lxml')
    # print(soup.string)
    # Extraction of the longitude and latitude
    lat = soup.find('latitude')
    long = soup.find('longitude')
    # The first coordinate x value from the accelerometer sensor of android determine the position of the vehicle
    accel1 = soup.find('accelerometer1') # button edgewise
    # print(accel1.string)
    accel2 = soup.find('accelerometer2') # headwise
    # print(accel2.string)
    accel3 = soup.find('accelerometer3') # for flat phone
    print(accel3.string)
    # print("\n")
    # print( lat.string, long.string, accel1.string)
    return [lat.string, long.string, accel3.string]
