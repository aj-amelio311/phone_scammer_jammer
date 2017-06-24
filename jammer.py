import time
from twilio.rest import Client

account_sid = "xxx"
auth_token = "xxx"

client = Client(account_sid, auth_token)

def jam_it():
        while True:
                call = client.calls.create(
                        to="15555555555",
                        from_="xxx",
                        url="phone_message.xml"
                )
                time.sleep(3)

jam_it()
          