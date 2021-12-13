import cv2 as cv

#Valor de 0 para buscar cámaras que estén trabajando en la pc
capturaVideo = cv.VideoCapture(0)

#Si no hay ningun video, se termina el programa
if not capturaVideo.isOpened():
    print("No se encontró ninguna cámara")
    exit()

#Mientras tenga un valor true entonces se lee la captura de video
#El método read() devuelve dos valores, 1 el tipo de cámara que se está trabajando y el segundo
#es el resultado de la cámara
while True:
    tipoCamara, Camara=capturaVideo.read()

    #Escala de grises
    grises = cv.cvtColor(Camara, cv.COLOR_BGR2GRAY)

    #Se muestran las imagenes en escala de grises
    cv.imshow("Cámara en vivo", grises)

    #Cuando se presione la letra 'q'
    if cv.waitKey(1)==ord("q"):
        break
#Se detiene el video
capturaVideo.release()

#Se cierran todas las ventanas emergentes
cv.destroyAllWindows()
