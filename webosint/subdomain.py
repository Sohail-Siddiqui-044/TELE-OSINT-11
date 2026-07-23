import requests


def SubDomain(host, port):

    url = "https://www.virustotal.com/vtapi/v2/domain/report"

    params = {
        "apikey": "1af37bfeb7b1628ba10695fb187987a6651793e37df006a5cdf8786b0e4f6453",
        "domain": host
    }

    try:

        response = requests.get(url, params=params, timeout=10)

        print("Status Code:", response.status_code)

        # Check empty response
        if response.text.strip() == "":
            print("Empty response from VirusTotal")
            return

        data = response.json()

        # Debug output
        # print(data)

        if "subdomains" not in data:
            print("No subdomains found")
            return

        print("\nSubdomains Found:\n")

        for sub in data["subdomains"]:
            print(sub)

    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON response")

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

    except KeyError:
        print("Key not found in API response")
