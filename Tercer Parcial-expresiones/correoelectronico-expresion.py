import re

expresion = r'^([A-Za-z0-9]+)([@])([a-z]+)([.])([a-z]+)$'
resul = re.compile(expresion)
prueba = raw_input("entrada: ")
busqueda=re.search(resul,prueba)

if busqueda:
    print busqueda.group()
else:
    print"qr"
