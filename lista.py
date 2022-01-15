def estaEnRango(valor, minimo, maximo):

    try:
        if valor >= minimo and valor <= maximo:
            return True
        else:
            return False
    except IndentationError:
        return False

# Devuelve True o False determinando que valor se encuentra entre el mínimo y el máximo. 

def estaEnLista(valor, lista):

    try:
        if valor in lista:
            return True
        else:
            return False
    except IndentationError:
        return False

# Devuelve True o False determinando si el valor está en la lista.
min=1
max=20
variable=int(input(f"introduce un valor entre {min} y {max}: "))
lista=[6,14,11,3,2,1,15,19]


if estaEnRango(variable, min, max):

    try:        
        if estaEnLista(variable, lista):
            print(f"el numero {variable} está dentro de la lista")
        else:
            print(f"el numero {variable} está en el rango pero no está en la lista")
    except IndentationError:
        print("esto no ha salido según lo esperado")
else:
    print(f"en número {variable} no está entre {min} y {max}" )

"""Faycal Baammi"""
