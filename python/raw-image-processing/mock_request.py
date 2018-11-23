# importing the requests library 
import requests 
import time
  
# defining the api-endpoint  
API_ENDPOINT = "http://localhost:8080/api/image"

n = 10

for i in range(100):
    cell = open('./cells/cell' + str(i), 'rb').read()

    # data to be sent to api 
    data = {'number': i, 
            'cell': cell} 
  
    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data) 