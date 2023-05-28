import requests
import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPI.GIO! You need to use 'sudo' to run the program.")

GPIO.setmode(GPIO.BCM)
out_channel = GPIO.setup(2, GPIO.OUT)


print ("Prima CTRL+C para terminar.\n")
while True:
    try:
        r = requests.get("http://iot.dei.estg.ipleiria.pt/api/api.php?sensor=btc", auth=('user','pass')) #Phase 1 project - to get the temperature
        
        if r.status_code == 200:
            print(r.text)
            if r.text > 20:
                print("Vou ligar o LED do RPI")
                GPIO.output(out_channel,GPIO.HIGH)
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