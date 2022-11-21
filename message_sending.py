# module to send distress message
import os
from twilio.rest import Client
def sendAlert(numbers, lat, long):

    account_sid = 'AC62039638273b770e141d0ff65514e57c'
    auth_token = '0973b02cd0e6270e30ae446aceabb356'
    client = Client(account_sid, auth_token)

    for i in numbers:
        message = client.messages .create(
                 #to='+916266358665',
                 to = str(i),
                 from_= '+19706505827',
                body=str('This is the distress signal and your vehicle location can be tracked at : https://www.google.com/search?q=' + lat +'%2C+' + long)
        )

    print(message.sid)
    print(f"Distress Alerts have been sent to {numbers}")


