import requests
import webbrowser

def reverseImg():
    try:
        img_path = input("Enter Image Path: ")

        searchUrl = "https://www.google.com/searchbyimage/upload"

        with open(img_path, 'rb') as img:
            multipart = {
                'encoded_image': (img_path, img),
                'image_content': ''
            }

            headers = {
                "User-Agent": "Mozilla/5.0"
            }

            response = requests.post(
                searchUrl,
                files=multipart,
                headers=headers,
                allow_redirects=False
            )

        if "Location" in response.headers:
            fetchUrl = response.headers["Location"]
            print("Opening browser...")
            webbrowser.open(fetchUrl)
        else:
            print("Failed.")
            print("Status Code:", response.status_code)
            print(response.text[:500])

    except FileNotFoundError:
        print("Error: File not found")

    except Exception as e:
        print("Error:", e)
        
if __name__ == "__main__":
    reverseImg()
