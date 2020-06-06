import math
while True:
    import re
    expresion = r'([0-9]+|[\w]+)\s([-|+|*|/|^|#]|[\w]+)\s([0-9]+|[\w]+)'
    expresion1 = r'([\w]+)\s([0-9]+|[\w]+)'
    resultado = re.compile(expresion)
    resultado1 = re.compile(expresion1)
    prueba = raw_input("entrada: ")
    busqueda=re.search(resultado,prueba)
    busqueda1=re.search(resultado1,prueba)
    if busqueda:
        print busqueda.group(1)
        numero1=busqueda.group(1)
        print busqueda.group(2)
        operacion=busqueda.group(2)
        print busqueda.group(3)
        numero2=busqueda.group(3)
        
        if numero1 == "cero":
            numero1 = 0
        if numero1 == "uno":
            numero1 = 1
        if numero1 == "dos":
            numero1 = 2
        if numero1 == "tres":
            numero1 = 3
        if numero1 == "cuatro":
            numero1 = 4
        if numero1 == "cinco":
            numero1 = 5
        if numero1 == "seis":
            numero1 = 6
        if numero1 == "siete":
            numero1 = 7
        if numero1 == "ocho":
            numero1 = 8
        if numero1 == "nueve":
            numero1 = 9
        if operacion == "mas":
            operacion = "+"
        if operacion == "menos":
            operacion = "-"
        if operacion == "por":
            operacion = "*"
        if operacion == "entre":
            operacion = "/"
        if numero2 == "cero":
            numero2 = 0
        if numero2 == "uno":
            numero2 = 1
        if numero2 == "dos":
            numero2 = 2
        if numero2 == "tres":
            numero2 = 3
        if numero2 == "cuatro":
            numero2 = 4
        if numero2 == "cinco":
            numero2 = 5
        if numero2 == "seis":
            numero2 = 6
        if numero2 == "siete":
            numero2 = 7
        if numero2 == "ocho":
            numero2 = 8
        if numero2 == "nueve":
            numero2 = 9
        try:
            numero1=int(numero1)
            numero2=int(numero2)

            if operacion=="+" or "-" or "*" or "/":
                if operacion=="+":
                    r=numero1+numero2
                          
                elif operacion=="-":
                    r=numero1-numero2
                            
                elif op=="*":
                    r=numero1*numero2
                           
                elif operacion=="/":
                    r=numero1/numero2

                elif operacion=="^":
                    r=numero1**numero2

                elif operacion=="#":
                    r=numero1**(1.0/numero2)
                print ("el resultado es:  %s %s %s = %s" % (numero1, operacion, numero2, r)) 

        except:
            print"qr";
        
            
    elif busqueda1:
        print busqueda1.group(1)
        operacion=busqueda1.group(1)
        print busqueda1.group(2)
        numero2=busqueda1.group(2)

        
        try:
            numero2=int(numero2)

            if operacion=="sen" or "cos" or "tan":
                if operacion=="sen":
                    r=math.sin(n2)
                    
                elif operacion=="cos":
                    r=math.cos(n2)
                    
                elif operacion=="tan":
                    r=math.tan(n2)

          
            
                print ("el resultado es: %s %s = %s" % (operacion, numero2, r))
        except:  
            print"qr";
            
   
