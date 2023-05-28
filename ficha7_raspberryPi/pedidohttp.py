#$ python -m pip install requests ---> this code makes the library work because it's not pre-installed with python
import requests
import time

while True:
    #Gets the current value of bitcoin
    r = requests.get("http://iot.dei.estg.ipleiria.pt/api/api.php?sensor=btc", auth=('user','pass'))

    if r.status_code == 200:
        print(time.strftime("%Y-%m-%d %H:%M:%S"), end="")
        print(r.text)
    else:
        print("Request failed with status code: " + r.status_code)
    
    time.sleep(5)