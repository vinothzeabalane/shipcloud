import requests

# r = requests.get('https://api.shipcloud.io/v1/carriers', auth=('2de2fbb4b2de6cbbd25756539f58e210', ''))
# 
# print(r.text)

datas={
  "company": "Muster-Company",
  "first_name": "Max",
  "last_name": "Mustermann",
  "street": "Musterstrae",
  "street_no": "42",
  "zip_code": "54321",
  "city": "Musterstadt",
  "country": "DE",
  "phone": "555-555"
}

r = requests.post('https://api.shipcloud.io/v1/addresses',auth=('2de2fbb4b2de6cbbd25756539f58e210', ''), data = datas)

print(r.text)