from src.api import phoneapis
import requests
from pyrogram import Client
import time

api_id = 
api_hash = ""

GROUP_ID = -1003892217921


def search_number(number):

    app = Client(
        "osint_session",
        api_id=api_id,
        api_hash=api_hash
    )

    with app:

        # Send command
        app.send_message(
            GROUP_ID,
            f"/num {number}"
        )

        print("Command sent")

        # Wait for response
        time.sleep(10)

        # Read latest message
        for msg in app.get_chat_history(GROUP_ID, limit=1):

            if msg.text:
                print(msg.text)

            elif msg.caption:
                print(msg.caption)


def carrierlookup():
    phonenum = input("Enter Mobile Number with country code : ")
    api_key = phoneapis()
    url = ("http://apilayer.net/api/validate?access_key="+api_key+"&number="+phonenum)
    resp = requests.get(url)
    details = resp.json()
    print('')
    print("Country : "+ details['country_name'])
    print("Location : "+ details['location'])
    print("Carrier : "+ details['carrier'])
    print("------------------------- TELEGRAM DATA ---------------------------")
    clean_number = phonenum.replace("+91", "")
    search_number(clean_number)


