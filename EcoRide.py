normal_bike=float(200)
premium_bike=float(500)
total=0
discount=0 
surcharge=0 
penalty=2000
confirmation=False
run=True #Inicia y controla el ciclo
while run is True:
    i=1
    j=1
    k=1
    l=1
    m=1
    
    print(" ----------------------")
    print("|        EcoRider      |")
    print("| 1.Alquilar bicicleta |")
    print("| 2.Consultar tarifas  |")
    print("| 3.Ver Factura total  |")
    print("| 4.Salir del sistema  |")
    print(" ----------------------")
    #El usuario ingresa un número para decidir como proceder
    option=int(input("Selecione una opción(#) para proceder: "))
    #Selecionar la opción 1 para iniciar el proceso de alquilar una bicicleta
    if option==1:
        i=1
        while i!=0:
            discount=0 
            surcharge=0
            #Despliega el segundo menú para seleccionar el tipo de bicicleta
            print(" ----------------------------")
            print("|  Tipos de bicis disponibles |")
            print("|     1.Bicicleta estandar    |")
            print("|     2.Bicicleta premium     |")
            print(" ----------------------------")
            bike=int(input("Seleccione el tipo de bici que desea alquilar (#) (Ingrese 0 para regresar al menú anterior): "))
            if bike==1: #Al seleccionar la bicicleta estandar procede por aca
                while j!=0: #Ciclo para controlar el ingreso de los datos de forma correcta
                    confirmation=False
                    #Solicita el tiempo en minutos que desee alquilar la bici al usuario
                    time=int(input("Por favor ingrese el tiempo(en minutos) que desea alquilar la bicicleta: "))
                    #Procede si el usuario ingresa un tiempo válido
                    if time>0:
                        #Se genera el costo del tiempo al usar esta bicicleta
                        cost=normal_bike*time                        
                        while k!=0:
                            payment_method= input("Método de pago (efectivo / tarjeta / puntos): ").lower() #'.lower()' Convierte la entrada en minúsculas
                            #Aplicando condiciones según los requerimientos 
                            #Si el usuario usa la bicicleta más de 60 minutos y paga con tarjeta
                            if payment_method=="efectivo":
                                #Si es fin de semana, se aplica un recargo del 5%
                                while l!=0:
                                    day= input("¿Es fin de semana? (Si/no): ").lower() 
                                    if day == "si": 
                                        surcharge= cost * 0.05 
                                        print("Recargo del 5 porciento aplicado por fin de semana.")
                                        while m!=0:
                                        #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                            out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower() 
                                            if out_time == "si":
                                                print("Penalización fija de $2000 aplicada por retraso.")
                                                #Calculando el total
                                                total= cost - discount + surcharge + penalty
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            elif out_time == "no":
                                                print("No se le aplicará ninguna penalización por devolverla a tiempo")
                                                #Calculando el total
                                                total= cost - discount + surcharge
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            else:
                                                print("Ingrese una respuesta válida")
                                    if day=="no":
                                        print("No se aplica ningun recargo adicional por no ser fin de semana")
                                        while m!=0:
                                        #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                            out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower() 
                                            if out_time == "si":
                                                print("Penalización fija de $2000 aplicada por retraso.")
                                                #Calculando el total
                                                total= cost - discount + surcharge + penalty
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            elif out_time == "no":
                                                print("No se le aplicará ninguna penalización por devolverla a tiempo")
                                                #Calculando el total
                                                total= cost - discount + surcharge
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            else:
                                                print("Ingrese una respuesta válida")
                                    else:
                                        print("Ingrese una respuesta válida")
                            elif payment_method=="tarjeta":
                                if time > 60 and payment_method == "tarjeta": 
                                    discount= cost * 0.10 
                                    print("Descuento del 10 porciento aplicado por uso prolongado y pago con tarjeta.")
                                                           
                                #Si es fin de semana, se aplica un recargo del 5%
                                while l!=0:
                                    day= input("¿Es fin de semana? (Si/no): ").lower() 
                                    if day == "si": 
                                        surcharge= cost * 0.05 
                                        print("Recargo del 5 porciento aplicado por fin de semana.")
                                        while m!=0:
                                        #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                            out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower() 
                                            if out_time == "si":
                                                print("Penalización fija de $2000 aplicada por retraso.")
                                                #Calculando el total
                                                total= cost - discount + surcharge + penalty
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            elif out_time == "no":
                                                print("No se le aplicará ninguna penalización por devolverla a tiempo")
                                                #Calculando el total
                                                total= cost - discount + surcharge
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            else:
                                                print("Ingrese una respuesta válida")
                                    if day=="no":
                                        print("No se aplica ningun recargo adicional por no ser fin de semana")
                                        while m!=0:
                                        #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                            out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower() 
                                            if out_time == "si":
                                                print("Penalización fija de $2000 aplicada por retraso.")
                                                #Calculando el total
                                                total= cost - discount + surcharge + penalty
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            elif out_time == "no":
                                                print("No se le aplicará ninguna penalización por devolverla a tiempo")
                                                #Calculando el total
                                                total= cost - discount + surcharge
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            else:
                                                print("Ingrese una respuesta válida")
                                    else:
                                        print("Ingrese una respuesta válida")           
                            elif payment_method=="puntos":   
                                if time < 10:
                                    print("No hay descuento por uso corto con puntos")
                                else:
                                    print("Recibira un descuento del 10% por uso prolongado y pagar en puntos")
                                    discount= cost * 0.10
                                #Si es fin de semana, se aplica un recargo del 5%
                                while l!=0:
                                    day= input("¿Es fin de semana? (Si/no): ").lower() 
                                    if day == "si": 
                                        surcharge= cost * 0.05 
                                        print("Recargo del 5 porciento aplicado por fin de semana.")
                                        while m!=0:
                                        #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                            out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower() 
                                            if out_time == "si":
                                                print("Penalización fija de $2000 aplicada por retraso.")
                                                #Calculando el total
                                                total= cost - discount + surcharge + penalty
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            elif out_time == "no":
                                                print("No se le aplicará ninguna penalización por devolverla a tiempo")
                                                #Calculando el total
                                                total= cost - discount + surcharge
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            else:
                                                print("Ingrese una respuesta válida")
                                    if day=="no":
                                        print("No se aplica ningun recargo adicional por no ser fin de semana")
                                        while m!=0:
                                        #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                            out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower() 
                                            if out_time == "si":
                                                print("Penalización fija de $2000 aplicada por retraso.")
                                                #Calculando el total
                                                total= cost - discount + surcharge + penalty
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            elif out_time == "no":
                                                print("No se le aplicará ninguna penalización por devolverla a tiempo")
                                                #Calculando el total
                                                total= cost - discount + surcharge
                                                
                                                m=0
                                                l=0
                                                k=0
                                                j=0
                                            else:
                                                print("Ingrese una respuesta válida")
                                    else:
                                        print("Ingrese una respuesta válida")
                            else:
                                print("Ingrese un metodo de pago correcto")
                            
    
                        """while confirmation==False:
                            total2=total2+total
                            again=input("Se ha registrado la bicicleta con exito, ¿Desea agregar otra bicicleta al alquiler? (si/no): ".lower())
                            if again=="si":
                                j=0
                                confirmation=True
                            elif again=="no":
                                j=0
                                i=0
                                confirmation=True
                            else:
                                print("Ingrese una respuesta válida")
                                confirmation=False"""
                    else:
                        print("Ingrese un tiempo valido")
            elif bike==2: #Al seleccionar la bicicleta premium procede por aca
                while j!=0: #Ciclo para controlar el ingreso de los datos de forma correcta
                    confirmation=False
                    #Solicita el tiempo en minutos que desee alquilar la bici al usuario
                    time=int(input("Por favor ingrese el tiempo(en minutos) que desea alquilar la bicicleta: "))
                    if time>0:
                        cost=premium_bike*time
                        total=total+cost
                        while confirmation==False:
                            again=input("Se ha registrado la bicicleta con exito, ¿Desea agregar otra bicicleta al alquiler? (si/no): ".lower())
                            if again=="si":
                                j=0
                                confirmation=True
                            elif again=="no":
                                j=0
                                i=0
                                confirmation=True
                            else:
                                print("Ingrese una respuesta válida")
                                confirmation=False
                    else:
                        print("Ingrese un tiempo valido")
            elif bike==0:
                i=1
            else:
                print("Digite una opción(#) valida")
    #Seleccionar la opción 2 para visualizar la tarifa del tipo de bicicleta
    elif option==2:
        print(" ---------------------------")
        print("|      Precio de tarifas    |")
        print("| -Bicicleta estandar: 200$ |")
        print("| -Bicicleta premium:  500$ |")
        print(" ---------------------------")
    #Seleccionar la opción 3 para ver el total pagado durante la sesión
    elif option==3:
        print("El total pagado durante el proceso es de: ",total)
    #Seleccionar la opción 4 para finalizar el proceso
    elif option==4:
        print("Ha finalizado el proceso hasta luego")
        #Seleccionar la opción 4 cambia el valor del booleano terminando el proceso
        run=False
    #En caso de entrar un valor inválido no procede y repite el ciclo
    else:
        print("Ingrese una opción valida")