import cv2
#'C:\\Users\\Alvaro\\Downloads\\Proyecto-Tennis\\Proyecto-python\\MonedasContorno\\contorno.jpg'
#path = r'C:\Users\Alvaro\Downloads\Proyecto-Tennis\Proyecto-python\MonedasContorno\contorno.jpg'
imagen = cv2.imread('contorno.jpg')
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY_INV)
contorno, jeraquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contorno, -1, (0,255,0), 3)
#Mostrar
cv2.imshow('ImagenOriginal', imagen)
# cv2.imshow('ImagenGris', grises)
# cv2.imshow('Imagen Umbral0', umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()