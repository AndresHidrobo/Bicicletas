#Eco Rider

estandar_bike = 200.0
premium_bike = 500.0
total = 0
subtotal = 0
total_timer = 0
day_charge = 0
discount = 0
penalty = 0

flag_1 = True

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
    if not main_menu.isnumeric():
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

    Por favor seleccione el tipo de bicicleta deseado: """)

                if not type_bike.isnumeric():
                    print("\nPor favor elige una opción válida\n")
                    continue

                type_bike = int(type_bike)

                if type_bike == 1:

                    while True:
                        timer = input("\nIngrese el tiempo que desea alquilar la bicicleta (En minutos): ")

                        if not timer.isnumeric():
                            print("\nTiempo no válido.\n")
                            continue

                        timer = float(timer)

                        if timer <= 0:
                            print("\nPor favor elija un igual o mayor a 1 minuto.\n")
                            continue

                        else:
                            total_timer = timer * estandar_bike
                            break
                    break

                elif type_bike == 2:

                    while True:
                        timer = input("\nIngrese el tiempo que desea alquilar la bicicleta (En minutos): ")

                        if not timer.isnumeric():
                            print("\nTiempo no válido.\n")
                            continue

                        timer = float(timer)

                        if timer <= 0:
                            print("\nPor favor elija un igual o mayor a 1 minuto.\n")
                            continue

                        else:
                            total_timer = timer * premium_bike
                            break
                    break

                else:
                    print("\nOpción no válida, por favor seleccióne una opción.\n")
                    continue

            total_timer += total_timer

            while True:
                answer =input("""
    ¿Desea agregar más bicicletas?

    1. Si.
    2. No.

    Elija una opción: """).lower()

                if not answer.isnumeric():
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

            if not back.isnumeric():
                print("Por favor elige una opción válida.")
                continue

            back = int(back)

            if back == 0:
                break

            else:
                print("Opción no válida, por favor seleccióne una opción.")
                continue

    elif main_menu == 3:
        while True:
            payment = input("""
Metodos de pago disponibles:

1. Efectivo.
2. Tarjeta.
3. Puntos.

Por favor seleccione el método de pago: """)

            if not payment.isnumeric():
                print("Por favor elige una opción válida.")
                continue

            payment = int(payment)

            if payment == 1:
                discount = 1
                break

            elif payment == 2:
                if timer >= 60:
                    discount = 0.90
                    break
                
                elif timer < 60:
                    discount = 1
                    break

            elif payment == 3:
                if timer < 10:
                    discount = 1
                    break

                elif timer >= 10:
                    discount = 0.85
                    break

            else:
                print("Opción no válida, por favor seleccióne una opción.")
                continue

        while True:
            day_charge = input("""
¿El día corresponde a sábado, domingo o feriado?

1. Si.
2. No

Seleccione una opción: """)

            if not day_charge.isnumeric():
                print("Por favor elige una opción válida.")
                continue

            day_charge = int(day_charge)

            if day_charge == 2:
                day_charge = 1
                break

            elif day_charge == 1:
                day_charge = 1.05
                break

            else:
                print("Opción no válida, por favor seleccióne una opción.")
                continue

        while True:
            penalty = input("""
¿La bicicleta se entregó dentro del tiempo estimado?

1. Si.
2. No.

Seleccione una opción: """)

            if not penalty.isnumeric():
                print("Por favor elige una opción válida.")
                continue

            penalty = int(penalty)

            if penalty == 1:
                penalty = 5000.0
                break

            elif penalty == 2:
                penalty = 0
                break

            else:
                print("Opción no válida, por favor seleccióne una opción.")
                continue

        subtotal = total_timer * day_charge
        total = (subtotal * discount) + penalty

        print(f"\nEl total a pagar es de ${total:.2f}.\n")
        break

    if main_menu == 4:
        flag_1 = False
        print("\nSe ha cerrado el menú.\n\n¡Gracias por eleginros!")
        break

    else:
        print("Opción no válida, por favor seleccióne una opción.")
        continue