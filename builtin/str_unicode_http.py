import requests
url = "http://192.168.122.99:88/" # This is Nginx HTTP server on local Hyper-V virtual machine
#url = "http://ocw.aca.ntu.edu.tw/ntu-ocw/"
response = requests.get(url)
html = response.text
print(html) # No need to process the received data
#print(type(html))
#print(html.encode('latin-1').decode('unicode_escape'))
#print(html.encode())

