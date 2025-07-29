import requests
import json

url = "https://webhook.syscoin.com.br/webhook/teste-estagio"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiSm_Do28iLCJyZXNwb25zZSI6IlRlc3RlIn0.s6Sjq2r3X9-IdXVHV_XpeuOr5ddAB16F-H-vZ_I2jZ0",
    "Content-Type": "application/json"
}

data = {
    "Name": "Tamara Morais Frigo",
    "Response": "Sou dedicada, proativa e apaixonada por tecnologia. Tenho experiência com homologação e conhecimentos em Python, C#, React e Git. Estou pronta para aprender e contribuir com a equipe da Syscoin!"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(f"Status: {response.status_code}")
print("Resposta:", response.text)
