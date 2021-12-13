#Para las imagenes
import cv2

#Para trabajar con matrices para este proyecto
import numpy as np

#Los valores de gauss y kernel tienen que ser números impares
valorGauss = 3
valorKernel = 3

original=cv2.imread('monedas.jpg') #Obtener imagen

#Pasar la imagen a escala de grises
#Parámetro 1: La imagen a procesar, Parámetro 2: El color a aplicar, para la escala de grises
#Se passa a escala de grises para que que el proceso de eliminación de ruido sea más rapido y eficaz
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)


#Realiza un suavizado de la imagen para la eliminación del ruido de la imagen
#Para que las imagenes puedan analizarse mucho mejor
#Se usan dos variables para el suavizado, no con todas las imágenes funcionaría el mismo valor
#Param 1: Imagen en la escala de grises
#Param 2: Los dos valores(Gauss, Kernel)
#Param 3: Valor de 0, por recomendación de la documentación
#Tiene que ser una matriz con valores iguales
gauss = cv2.GaussianBlur(gris, (valorGauss, valorGauss), 0) 

#Proceso para eliminar los ruidos de la imagen (Ya que la eliminación de ruidos
#con el proceso Gauss no es suficiente, aún que ruidos que eliminar
#Param 1: La imagen suavizada con el proceso Gauss
#Param 2 y param 3: Valores de 0 a 255
canny=cv2.Canny(gauss, 60, 100)


#En la monedas aun siguen habiendo muchos distintos tipos de contornos, para el conteo
#de monedas solo se necesita identificar el contorno circular correspondiente de la moneda
#uit8 Enteros con 8 bytes, por defecto siempre se trabaja con ese valor
kernel = np.ones((valorKernel,valorKernel), np.uint8)

#Se necesita hacer un cierre de la imagen porque es lo que nos importa en este caso
#Transformaciones morfológicas: En este caso se utilzia el morph_close para eliminar el ruido
#dentro de las monedas, el param 3 se usa el valor kernel convertido
cierre = cv2.morphologyEx (canny, cv2.MORPH_CLOSE, kernel)


#ubicando los contornos mediante puntos (simple), esto devuelve dos resultados, contorno y jerarquia
#el findcontours, el 2 param saca los datos de forma externa
#El tercer param puede se simple o 
#el .copy() de la imagen procesada "cierre" es porque hubo un cambio de morfología 
contornos, jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Monedas encontradas: {}".format(len(contornos))) #Conteo de las monedas

#Dibujando los contornos
#Se necesita la imagen inicial, los contornos para dibujar
#El 3er param indica que serán todos los contornos encontrados, si es -1, se dibujarán todos los contornos
#El 4to param es el color rgb, en este caso es un color verde
#El 5to param el el grosor del contorno
cv2.drawContours(original, contornos, -1, (0,255,0), 3) 

#Mostrar imágenes
# cv2.imshow("Grises", gris)
# cv2.imshow("Gauss", gauss)
# cv2.imshow("Canny", canny)
cv2.imshow("Resultado", original)

cv2.waitKey(0) # 0 para que las ventanas que se abran no se cierren. 1 es para videos