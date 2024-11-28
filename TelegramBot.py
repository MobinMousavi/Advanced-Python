import requests

token = "YOUR_BOT_API_TOKEN"
url = f"https://api.telegram.org/bot{token}/getUpdates"

data = requests.get(url)
recievers = []

#print(data.text)
#print(data.json())

Updates = data.json()
for i in range(len(Updates["result"])):
  ID = Updates["result"][i]["message"]["from"]["id"]
  firstname = Updates["result"][i]["message"]["from"]["first_name"]
  username = Updates["result"][i]["message"]["from"]["username"]
  text = Updates["result"][i]["message"]["text"]
  print(ID,firstname,username,text)
  recievers.append(ID)


for i in list(set(recievers)):
  send_url = f"https://api.telegram.org/bot{token}/sendMessage"
  chat_id = i
  message = "تکراری ها رو حذف کردیم.😂"
  response = {"chat_id":chat_id,"text":message}
  data = requests.post(send_url,response)


#send_url = f"https://api.telegram.org/bot{token}/sendMessage"
#chat_id = input("Enter ID:")
#message = input("Enter Message:")
#response = {"chat_id":chat_id,"text":message}
#data = requests.post(send_url,response)