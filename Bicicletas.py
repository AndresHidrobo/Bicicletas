normal_bike=float(200)
premium_bike=float(500)
total=0
total_history=0
run=True #Inicia y controla el ciclo
while run:
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
        while i!=0:
            j=1
            k=1
            l=1
            m=1 
            discount=0 
            surcharge=0
            penalty=2000
            #Despliega el segundo menú para seleccionar el tipo de bicicleta
            print(" -----------------------------")
            print("|  Tipos de bicis disponibles |")
            print("|     1.Bicicleta estandar    |")
            print("|     2.Bicicleta premium     |")
            print(" ----------------------------")
            bike=int(input("Seleccione el tipo de bici que desea alquilar (#) (Ingrese 0 para regresar al menú anterior): "))
            print("\n")
            if bike==1: #Al seleccionar la bicicleta estandar procede por aca
                type_bc="Estandar"
                while j!=0: #Ciclo para controlar el ingreso de los datos de forma correcta
                    #Solicita el tiempo en minutos que desee alquilar la bici al usuario
                    time=int(input("Por favor ingrese el tiempo(en minutos) que desea alquilar la bicicleta: "))
                    print("\n")
                    #Procede si el usuario ingresa un tiempo válido
                    if time>0:
                        #Se genera el costo del tiempo al usar esta bicicleta
                        cost=normal_bike*time                        
                        while k!=0:
                            payment_method= input("Método de pago (efectivo / tarjeta / puntos): ").lower() #'.lower()' Convierte la entrada en minúsculas
                            print("\n")
                            #Aplicando condiciones según los requerimientos 
                            #Si el usuario usa la bicicleta más de 60 minutos y paga con tarjeta
                            match payment_method:
                                case "efectivo":
                                    #Si es fin de semana, se aplica un recargo del 5%
                                    while l!=0:
                                        day= input("¿Es fin de semana? (Si/no): ").lower()
                                        match day:
                                            case "si":
                                                surcharge= cost * 0.05 
                                                print("Recargo del 5 porciento aplicado por fin de semana.")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")
                                                    
                                            case "no":
                                                print("No se aplica ningun recargo adicional por no ser fin de semana")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")        
                                            case _:
                                                print("Ingrese una respuesta válida")
                                case "tarjeta":
                                    #al pagar con tarjeta, si se registra un tiempo mayor a 60 minutos el usuario recibe un descuento del 10% 
                                    if time > 60: 
                                        discount= cost * 0.10 
                                        print("Descuento del 10 porciento aplicado por uso prolongado y pago con tarjeta.")
                                    #Si es fin de semana, se aplica un recargo del 5%
                                    while l!=0:
                                        day= input("¿Es fin de semana? (Si/no): ").lower()
                                        match day:
                                            case "si":
                                                surcharge= cost * 0.05 
                                                print("Recargo del 5 porciento aplicado por fin de semana.")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")
                                                    
                                            case "no":
                                                print("No se aplica ningun recargo adicional por no ser fin de semana")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")        
                                            case _:
                                                print("Ingrese una respuesta válida")   
                                case "puntos":
                                    #Si el tiempo de uso es menor de 10 minutos no recibe descuento, aplica en caso contrario 
                                    if time < 10:
                                        print("No hay descuento por uso corto con puntos")
                                    else:
                                        print("Recibira un descuento del 10% por uso prolongado y pagar en puntos")
                                        discount= cost * 0.10
                                    #Si es fin de semana, se aplica un recargo del 5%
                                    while l!=0:
                                        day= input("¿Es fin de semana? (Si/no): ").lower()
                                        match day:
                                            case "si":
                                                surcharge= cost * 0.05 
                                                print("Recargo del 5 porciento aplicado por fin de semana.")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")
                                                    
                                            case "no":
                                                print("No se aplica ningun recargo adicional por no ser fin de semana")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {normal_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")        
                                            case _:
                                                print("Ingrese una respuesta válida")
                                case _:
                                                print("Ingrese una respuesta válida") 
                    else:
                        print("Ingrese un tiempo valido")
            elif bike==2: #Al seleccionar la bicicleta premium procede por aca
                type_bc="Premium"
                j=1
                k=1
                l=1
                m=1 
                while j!=0: #Ciclo para controlar el ingreso de los datos de forma correcta
                    #Solicita el tiempo en minutos que desee alquilar la bici al usuario
                    time=int(input("Por favor ingrese el tiempo(en minutos) que desea alquilar la bicicleta: "))
                    print("\n")
                    #Procede si el usuario ingresa un tiempo válido
                    if time>0:
                        #Se genera el costo del tiempo al usar esta bicicleta
                        cost=premium_bike*time                        
                        while k!=0:
                            payment_method= input("Método de pago (efectivo / tarjeta / puntos): ").lower() #'.lower()' Convierte la entrada en minúsculas
                            print("\n")
                            #Aplicando condiciones según los requerimientos 
                            #Si el usuario usa la bicicleta más de 60 minutos y paga con tarjeta
                            match payment_method:
                                case "efectivo":
                                    #Si es fin de semana, se aplica un recargo del 5%
                                    while l!=0:
                                        day= input("¿Es fin de semana? (Si/no): ").lower()
                                        match day:
                                            case "si":
                                                surcharge= cost * 0.05 
                                                print("Recargo del 5 porciento aplicado por fin de semana.")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")
                                                    
                                            case "no":
                                                print("No se aplica ningun recargo adicional por no ser fin de semana")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")        
                                            case _:
                                                print("Ingrese una respuesta válida")
                                case "tarjeta":
                                    #al pagar con tarjeta, si se registra un tiempo mayor a 60 minutos el usuario recive un descuento del 10% 
                                    if time > 60: 
                                        discount= cost * 0.10 
                                        print("Descuento del 10 porciento aplicado por uso prolongado y pago con tarjeta.")
                                    #Si es fin de semana, se aplica un recargo del 5%
                                    while l!=0:
                                        day= input("¿Es fin de semana? (Si/no): ").lower()
                                        match day:
                                            case "si":
                                                surcharge= cost * 0.05 
                                                print("Recargo del 5 porciento aplicado por fin de semana.")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")
                                                    
                                            case "no":
                                                print("No se aplica ningun recargo adicional por no ser fin de semana")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")        
                                            case _:
                                                print("Ingrese una respuesta válida")   
                                case "puntos":
                                    #Si el tiempo de uso es menor de 10 minutos no recibe descuento, aplica en caso contrario 
                                    if time < 10:
                                        print("No hay descuento por uso corto con puntos")
                                    else:
                                        print("Recibira un descuento del 10% por uso prolongado y pagar en puntos")
                                        discount= cost * 0.10
                                    #Si es fin de semana, se aplica un recargo del 5%
                                    while l!=0:
                                        day= input("¿Es fin de semana? (Si/no): ").lower()
                                        match day:
                                            case "si":
                                                surcharge= cost * 0.05 
                                                print("Recargo del 5 porciento aplicado por fin de semana.")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")
                                                    
                                            case "no":
                                                print("No se aplica ningun recargo adicional por no ser fin de semana")
                                                print("\n")
                                                while m!=0:
                                                #Si devuelve la bicicleta fuera del tiempo, se aplica una penalización
                                                    out_time= input("¿La bicicleta fue devuelta fuera de tiempo? (Si/no): ").lower()
                                                    match out_time:
                                                        case "si":
                                                            print("Penalización fija de $2000 aplicada por retraso.")
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                            
                                                        case "no":
                                                            print("No se le aplica penalización por retraso.")
                                                            penalty=0
                                                            #Calculando el total
                                                            total= cost - discount + surcharge + penalty
                                                            #Se guarda un dato total adicional para usarlo en "Ver facturas totales"
                                                            total_history=total_history+total
                                                            print("\n" + "="*30)
                                                            print("Sucessfully Register Product!")
                                                            print("="*30)
                                                            #Se imprime el resumen del encargo
                                                            print(f"Service resume: \n Type: {type_bc} | Time Use: {time} | Price Per Minute: {premium_bike}$ | \nDiscount (if apply): {discount}$ | Recharges (if apply): {surcharge}$ | Penalty (if apply): {penalty}$ | Total Cost: {total}$")
                                                            #Se imprime el resumen del encargo
                                                            validation = True
                                                            while validation:
                                                                answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
                                                                if answer == 'y':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0  
                                                                    break
                                                                elif answer == 'n':
                                                                    m=0
                                                                    l=0
                                                                    k=0
                                                                    j=0
                                                                    i=0
                                                                    validation = False
                                                                    break
                                                                
                                                                else:
                                                                    print("ERROR: Response with 'Y' or 'N'.")
                                                            print("\n" + "="*30)
                                                            print("Thanks For Use Our Services")
                                                            print("="*30)
                                                        case _:
                                                            print("Ingrese una respuesta válida")        
                                            case _:
                                                print("Ingrese una respuesta válida")
                                case _:
                                                print("Ingrese una respuesta válida") 
                    else:
                        print("Ingrese un tiempo valido")
            elif bike==0:
                i=1
            else:
                print("Ingrese una respuesta válida")        
    elif option==2:
        print(" ---------------------------")
        print("|      Precio de tarifas    |")
        print("| -Bicicleta estandar: 200$ |")
        print("| -Bicicleta premium:  500$ |")
        print(" ---------------------------")
    #Seleccionar la opción 3 para ver el total pagado durante la sesión
    elif option==3:
        print(f"El total pagado durante el proceso es de: {total_history}$")
    #Seleccionar la opción 4 para finalizar el proceso
    elif option==4:
        print("Ha finalizado el proceso hasta luego")
        #Seleccionar la opción 4 cambia el valor del booleano terminando el proceso
        run=False
    #En caso de entrar un valor inválido no procede y repite el ciclo
    else:
        print("Ingrese una opción valida")