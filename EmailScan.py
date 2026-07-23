import requests
import json


def GetEmail():
    #email = input("Enter the Email : ")
    #HaveIbeenPwned(email)
    api_key = "208dee094fmsh7b43b025cdc30dbp1ddce9jsn5eb291965213"
    term = input("Enter email or phone: ")
    check_breach(term, api_key)



def HaveIbeenPwned(email):
    url = "https://haveibeenpwned.com/api/v2/breachedaccount/"+email
    print('')
    print("Checking for Breached Data")
    print('')
    rqst = requests.get(url,timeout=10)
    sc = rqst.status_code

    if sc == 200:
        print("The Email has been Breached")
        json_out = rqst.content.decode('utf-8', 'ignore')
        simple_out = json.loads(json_out)
        for item in simple_out:
            print('\n'
                  '[+] Breach      : ' + str(item['Title']) + '\n'
                  '[+] Domain      : ' + str(item['Domain']) + '\n'
                  '[+] Date        : ' + str(item['BreachDate']) + '\n'
                  '[+] Fabricated  : ' + str(item['IsFabricated']) + '\n'
                  '[+] Verified    : ' + str(item['IsVerified']) + '\n'
                  '[+] Retired     : ' + str(item['IsRetired']) + '\n'
                  '[+] Spam        : ' + str(item['IsSpamList']))

    elif sc == 404:
        print('The Email is Not Breached')

    elif sc == 503:
        print('\n')
        print('[-] Error 503 : Request Blocked by Cloudflare DDoS Protection')
    elif sc == 403:
        print('\n')
        print('[-] Error 403 : Request Blocked by haveibeenpwned API')
        print(rqst.text)
    else:
        print('\n')
        print('[-] An Unknown Error Occurred')


        print(rqst.text)

import requests
import json
import os

def check_breach(term, api_key):
    try:
        api_url = "https://breachdirectory.p.rapidapi.com/"

        headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "breachdirectory.p.rapidapi.com"
        }

        querystring = {
            "func": "auto",
            "term": term
        }

        response = requests.get(
            api_url,
            headers=headers,
            params=querystring
        )

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            result = response.json()

            current_dir = os.path.dirname(os.path.abspath(__file__))
            json_file_path = os.path.join(current_dir, "response.json")

            with open(json_file_path, "w") as json_file:
                json.dump(result, json_file, indent=4)

            print("[+] Results saved to response.json")
            print(json.dumps(result, indent=4))

        else:
            print(f"[-] Error: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"[-] Exception: {e}")


# Example Usage
