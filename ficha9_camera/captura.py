import cv2
import requests

# URL da webcam
webcam_url = "https://rooftop.tryfail.net:50000/image.jpeg"

cap = cv2.VideoCapture(webcam_url)
ret, frame = cap.read()
if ret:
  # escreve na mesma diretoria do script python o ficheiro webcam.jpg
  cv2.imwrite('captura.jpg', frame)
cap.release()

url = 'api/images/'
files = {'images': open('captura.jpg', 'rb')}

r = requests.post(url, files=files)
r.text

if r.status_code == requests.codes.ok:
    print('A imagem foi enviada com sucesso!')
else:
    print('Ocorreu um erro ao enviar a imagem. Código de status:', r.status_code)