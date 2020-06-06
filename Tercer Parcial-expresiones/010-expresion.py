import re

expresion = r'^([0]{1}[1]{1}[0]{1})$'
resul = re.compile(expresion)
prueb = raw_input("entrada: ")
busqueda=re.search(resul,prueb)

if busqueda:
    print busqueda.group()
else:
    print"qr"
