import requests

img = input("Enter image url:")

url = f"https://api.apilayer.com/image_to_text/url?url={img}"

payload = {}
headers= {
  "apikey": ""
}

response = requests.request("GET", url, headers=headers, data = payload)
box = response.json()


print(box["all_text"])