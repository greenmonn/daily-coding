# importing the requests library 
import requests 
import time
  
# defining the api-endpoint  
API_ENDPOINT = "http://localhost:8080/api/image"
# API_ENDPOINT = "http://52.78.16.193:8080/api/image"

n = 16

for i in range(n*n):
    cell = open('./cells/cell' + str(i), 'r').read()

    # data to be sent to api 
    data = {'n': i, 
            'c': cell} 
  
    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data)
