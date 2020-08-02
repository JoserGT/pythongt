menu = """
Bienvenido al conversor de moneda

¿Que moneda deseas convertir?

1- Pesos colombianos 
2- Quetzal guatemalteco
3- Pesos mexicanos

Elige una opcion por favor:  """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuantos pesos colombianos tienes:  ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos/valor_dolar
    dolares = round (dolares,2)
    dolares = str(dolares)
    print("Tienes  $" + dolares  + " dolares")
elif opcion ==2:
    quetzal = input("Cuantos quetzales guatemaltecos tienes:  ")
    quetzal = float(quetzal)
    valor_dolar = 7.70871
    dolares = quetzal/valor_dolar
    dolares = round (dolares,2)
    dolares = str(dolares)
    print("Tienes  $" + dolares  + " dolares")
elif opcion ==3:
    pesos = input("Cuantos pesos mexicanos tienes:  ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos/valor_dolar
    dolares = round (dolares,2)
    dolares = str(dolares)
    print("Tienes  $" + dolares  + " dolares")
else:
    print("Introduce por favor un numero correcto")    