import requests
import time

print ("Prima CTRL+C para terminar.\n")
while True:
    try:
        r = requests.get("http://iot.dei.estg.ipleiria.pt/api/api.php?sensor=btc", auth=('user','pass')) #Phase 1 project - to get the temperature
        
        if r.status_code == 200:
            print(r.text)
            if r.text > 20:
                print("Vou ligar o LED do RPI")
            else:
                print("Vou desligar o LED do RPI")
        else:
            print("")
    except KeyboardInterrupt:
        print("A aplicacao foi interrompida!\n")
    except Exception as e:
        print("Erro inesperado: ", e)
    
    time.sleep(5)