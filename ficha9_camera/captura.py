import cv2
import requests

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

if ret:
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