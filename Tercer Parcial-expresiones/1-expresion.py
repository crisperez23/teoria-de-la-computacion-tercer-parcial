import re

expresion = r'^([a-z]{3,5})$'
resul = re.compile(expresion)
prueb= raw_input("entrada: ")
busqueda=re.search(resul,prueb)

if busqueda:
    print busqueda.group()
else:
    print"qr"
