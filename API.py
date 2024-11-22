import requests

img = input("Enter image url:")

url = f"https://api.apilayer.com/image_to_text/url?url={img}"

payload = {}
headers= {
  "apikey": "YOUR_API_KEY"
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text)