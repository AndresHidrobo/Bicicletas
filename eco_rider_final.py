#Eco Rider

estandar_bike = 200.0
premium_bike = 500.0
total = 0
subtotal = 0
total_timer = 0
all_time=0
day_charge = 0
discount = 0
penalty = 0
bicis=[]
save=""
flag_1 = True
i=0
while flag_1:
    main_menu = input("""
        ¡Bienvenido a EcoRider!

        -----------------------
        |1.Alquilar bicicleta. |
        |2.Consultar tarifas.  |
        |3.Pagar.              |
        |4.Salir del sistema.  |
        -----------------------

Por favor seleccione una opción del menú: """)
    if not main_menu.isnumeric(): #En caso de ingresar algo que no sea un número repite la pregunta
        print("\nPor favor elige una opción válida.\n")
        continue

    main_menu = int(main_menu)

    if main_menu == 1:

        flag_2 =True
        while flag_2:
            while True:
                type_bike = input("""

                Bicicletas disponibles:

                    1. Estandar
                    2. Premium

    Por favor seleccione el tipo de bicicleta deseado(#): """)

                if not type_bike.isnumeric(): #En caso de ingresar algo que no sea un número repite la pregunta
                    print("\nPor favor elige una opción válida\n")
                    continue

                type_bike = int(type_bike)

                if type_bike == 1:

                    while True:
                        timer = input("\nIngrese el tiempo que desea alquilar la bicicleta (En minutos): ")

                        if not timer.isnumeric(): #En caso de ingresar algo que no sea un número repite la pregunta
                            print("\nTiempo no válido.\n")
                            continue

                        timer = float(timer)

                        if timer <= 0:
                            print("\nPor favor elija un igual o mayor a 1 minuto.\n")
                            continue

                        else:
                            total_timer = timer * estandar_bike
                            save=f"Tipo de bici: Estandar | Tiempo de uso {timer} minutos | Precio por minuto: {estandar_bike}$ | Precio individual: {total_timer}$"
                            bicis.append(save)
                            i=i+1
                            break
                    break

                elif type_bike == 2:

                    while True:
                        timer = input("\nIngrese el tiempo que desea alquilar la bicicleta (En minutos): ")

                        if not timer.isnumeric(): #En caso de ingresar algo que no sea un número repite la pregunta
                            print("\nTiempo no válido.\n")
                            continue

                        timer = float(timer)

                        if timer <= 0:
                            print("\nPor favor elija un igual o mayor a 1 minuto.\n")
                            continue

                        else:
                            total_timer = timer * premium_bike
                            save=f"Tipo de bici: Premium | Tiempo de uso {timer} minutos | Precio por minuto: {premium_bike}$ | Precio individual: {total_timer}$"
                            bicis.append(save)
                            i=i+1
                            break
                    break
                else:
                    print("\nOpción no válida, por favor seleccióne una opción.\n")
                    continue

            all_time = all_time+total_timer

            while True:
                answer =input("""
    ¿Desea agregar más bicicletas ?

    1. Si.
    2. No.

    Elija una opción(#): """).lower()

                if not answer.isnumeric(): #En caso de ingresar algo que no sea un número repite la pregunta
                    print("\nPor favor elige una opción válida\n")
                    continue

                answer = int(answer)

                if answer == 1:
                    flag_2 = True
                    break
                
                elif answer == 2:
                    flag_2 = False
                    break

                else:
                    print ("\nPor favor seleccione una opción válida.\n")
                    continue

    elif main_menu == 2:
        while True:
            back = input("""
Tarifas EcoRider:

- Bicicleta estandar: $200.00 por minuto.
- Bicicleta premium: $500.00 por minuto.

- Recargo por fin de semana o feriado: +5%.
- Recargo por entrega fuera del tiempo establecido: $5000.00

- Más de 60 minutos y pago con tarjeta: 10% de descuento.
- Más de 10 minutos y pago con puntos: -15% de descuento.


Presione '0' para regresar al menú anterior: """)

            if not back.isnumeric(): #En caso de ingresar algo que no sea un número repite la pregunta
                print("Por favor elige una opción válida.")
                continue

            back = int(back)

            if back == 0:
                break

            else:
                print("Opción no válida, por favor seleccióne una opción.")
                continue

    elif main_menu == 3: #Inicia proceso para pagar
        if all_time==0: #En caso de no tener ninguna bicicleta no procede
            print("No se ha registrado ninguna bicicleta") 
        else:
            while True:#Solicita al usuario que metodo de pago desea usar
                payment = input("""
    Metodos de pago disponibles:

    1. Efectivo.
    2. Tarjeta.
    3. Puntos.

    Por favor seleccione el método de pago(#): """)

                if not payment.isnumeric(): #En caso de ingresar algo que no sea un número repite la pregunta
                    print("Por favor elige una opción válida.")
                    continue

                payment = int(payment)

                if payment == 1:
                    discount = 0
                    percentage=0
                    break

                elif payment == 2:
                    if timer >= 60:
                        discount = all_time*0.10
                        percentage=10
                        break
                    
                    elif timer < 60:
                        discount = 0
                        percentage=0
                        break

                elif payment == 3:
                    if timer < 10:
                        discount = 0
                        percentage=0
                        break

                    elif timer >= 10:
                        discount = all_time*0.15
                        percentage=15
                        break

                else:
                    print("Opción no válida, por favor seleccióne una opción.")
                    continue

            while True:
                day_charge = input("""
    ¿El día corresponde a sábado, domingo o feriado?

    1. Si.
    2. No

    Seleccione una opción(#): """)

                if not day_charge.isnumeric(): #En caso de ingresar algo que no sea un número repite la pregunta
                    print("Por favor elige una opción válida.")
                    continue

                day_charge = int(day_charge)

                if day_charge == 2:
                    day_charge = 0
                    day_percentage=0
                    break

                elif day_charge == 1:
                    day_charge = all_time*0.05
                    day_percentage=5
                    break

                else:
                    print("Opción no válida, por favor seleccióne una opción.")
                    continue

            while True:
                #
                penalty = input("""
    ¿La bicicleta se entregó dentro del tiempo estimado?

    1. Si.
    2. No.

    Seleccione una opción(#): """)

                if not penalty.isnumeric(): #En caso de ingresar algo que no sea un número repite la pregunta
                    print("Por favor elige una opción válida.")
                    continue

                penalty = int(penalty)

                if penalty == 1:
                    penalty = 0
                    break

                elif penalty == 2:
                    penalty = 5000
                    break

                else:
                    print("Opción no válida, por favor seleccióne una opción.")
                    continue

            for a in range(0,i):
                print(bicis[a])
            total = all_time-discount+day_charge+penalty
            
            print(f"\nEl descuento aplicado es del {percentage:.2f}%, con valor de: {discount}$")
            print(f"\nEl precio del recargo adicional si aplica es de: {day_percentage:.2f}%, con valor de: {day_charge}$.")
            print(f"\nEl precio a pagar por penalización es de: {penalty:.2f}.\n")
            print(f"\nEl total a pagar es de ${total:.2f}.\n")
            break

    elif main_menu == 4: #Termina el proceso
        flag_1 = False
        print("\nSe ha cerrado el menú.\n\n¡Gracias por elegirnos!")
        break

    else:
        print("Opción no válida, por favor seleccióne una opción.")
        continue