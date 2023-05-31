import requests
import time
import datetime

def post2API(nome, valor):
    #o pedido HTTP é sempre realizado para a API do seu grupo
    now = datetime.datetime.now()
    r = requests.post('http://127.0.0.1/EI_TI/projeto/TI-ProjFase1/api/api.php', data=payload)
    if r.status_code != 200:
        print("Erro " + r.text)
    


try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPI.GIO! You need to use 'sudo' to run the program.")

GPIO.setmode(GPIO.BCM)
out_channel = GPIO.setup(2, GPIO.OUT)


print ("Prima CTRL+C para terminar.\n")
while True:
    try:
        r = requests.get("http://127.0.0.1/EI_TI/projeto/TI-ProjFase1/api/api.php?sensor=alarme", auth=('user','pass')) #Phase 1 project - to get the temperature
        
        if r.status_code == 200:
            print(r.text)
            if r.text > 20:
                print("Vou ligar o LED do RPI")
                GPIO.output(out_channel,GPIO.HIGH)
                payload = {'nome': 'alarme',
                           'valor': '1',
                           'hora':now}
                now = datetime.datetime.now()
                print(now.strftime("%H:%M:%S"))
                r = requests.post('http://127.0.0.1/EI_TI/projeto/TI-ProjFase1/api/api.php', data=payload) #g123 is the number of the group which i don't know
                if r.status_code != 200:
                    print("Erro " + r.text)
            else:
                print("Vou desligar o LED do RPI")
                GPIO.output(out_channel,GPIO.LOW)
    except KeyboardInterrupt:
        print("A aplicacao foi interrompida!\n")
    except Exception as e:
        print("Erro inesperado: ", e)
    finally:
        GPIO.cleanup()
        print("Terminou o programa")
    time.sleep(5)