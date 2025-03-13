#Ejercicio 1
mi_cadena = "Hola, soy Daniel"
mi_edad = 25
mi_lista = [1, 2, 3, 4, 5]
es_verdadero = True

print("saludo:",mi_cadena) 
print("edad:",mi_edad)
print("conteo:",mi_lista)
print("Estudiante:",es_verdadero)

#Ejercicio 2
print()
primeras_tres_letras = mi_cadena[:3]
print(primeras_tres_letras)

#Ejercicio 3
print()
primer_elemento = mi_lista[0]
print(primer_elemento)

#Ejercicio 4
print()
nueva_edad = mi_edad + 16
print(nueva_edad)

#Ejercicio 5
print()
ultimo_elemento = mi_lista[-1]
print(ultimo_elemento)

#Ejercicio 6
print()
names_amigos = 'harry,alex,susie,jared,gail,conner'
names_list = names_amigos.split(',')
print(names_list)

#Ejercicio 7
print()
primera_palabra = names_amigos.split(',')[0]
mayuscula= primera_palabra.upper()
resto_cadena = names_amigos [len(primera_palabra):]
nueva_lista_amigos = mayuscula + resto_cadena
print(nueva_lista_amigos)

#Ejercicio 8
print()
print(f"Mi edad es {mi_edad} años.")

#Ejercicio 9
print()
print('hello world')


#Ejercicio 10 
print()

Saludo_formal = "Hola, es un placer."
indice_hola = Saludo_formal.find("Hola")

palabra_seleccionada = Saludo_formal[indice_hola:indice_hola+4]

despedida_formal= Saludo_formal.replace("Hola, es un", "Adiós, fue un")

print("saludo:", Saludo_formal)
print("palabra reemplazada:", palabra_seleccionada)
print("despedida:",despedida_formal)
