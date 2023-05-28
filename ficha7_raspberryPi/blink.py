import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPI.GIO! You need to use 'sudo' to run the program.")

GPIO.setmode(GPIO.BCM)
out_channel = GPIO.setup(2, GPIO.OUT)

while True:
    #sets led to low
    GPIO.output(out_channel,GPIO.LOW)
    time.sleep(1)
    GPIO.output(out_channel,GPIO.HIGH)