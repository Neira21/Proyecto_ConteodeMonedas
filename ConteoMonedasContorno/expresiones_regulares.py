#Expresiones regulares
import re

texto = 'El numero de telefono es 920-153123 y mi segundo número es 979-243731'
patron = r'\d{3}-\d{6}'
#print(re.search(patron,texto))
# coincidencias = re.findall(patron,texto)
# for coincidencia in coincidencias:
#     print(coincidencia.span())

coincidencias = re.finditer(patron,texto)
#.span:indica la posición en la que está
for coincidencia in coincidencias:
    print(coincidencia.span())


