# %%
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
#de cada letra en la cadena. Los espacios no deben ser considerados
def frecuencias_letras(cadena: str) -> dict:
    frecuencias = {}
    for letra in cadena:
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    return frecuencias


# %%
print (frecuencias_letras ("ornitorrinco"))

# %%
#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def doble (numero):
    return numero * 2


# %%
lista = [1,4,5,6,8]
resultado = map (doble, lista)


# %%
lista_resultado = list (resultado)

# %%
print(lista_resultado)

# %%
#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def buscar_palabras(lista_palabras, objetivo):
    resultado = []
    for palabra in lista_palabras:
        if objetivo in palabra:
            resultado.append(palabra)
    return resultado



# %%
palabras = ["fotografia","fotovoltaica","coche","fotomaton","palo"]
print(buscar_palabras (palabras, "foto"))

# %%
#4.Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))


    

# %%
a = [10,8,6,79,25]
b=  [8,5,13,6,4]
print(diferencia_listas(a,b))

# %%
#Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado.
def evaluar_media(numeros, nota_aprobado=5):
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)


# %%
notas = [5,7,8,1,4]
print(evaluar_media(notas))

# %%
#6.Escribe una función que calcule el factorial de un número de manera recursiva
def factorial (n):
   if n == 1 or n== 0:
     return 1
   return n * factorial(n-1)

# %%
print(factorial(6))

# %%
#7.Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: ''.join(map(str, tupla)), lista_tuplas))


# %%
lista = [('a','b'), (1,6), (7,4)]
print(tuplas_a_strings(lista))

# %%
#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
#indicando si la división fue exitosa o no.

def dividir_numeros(num1,num2):
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("Error: Debes ingresar un valor numérico.")
        return
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return
    else:
        print(f"La división fue exitosa. Resultado: {resultado}")




# %%
dividir_numeros(6,3)

# %%
#9.Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def filtrar_mascotas(mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in mascotas_prohibidas, mascotas))


# %%
lista_mascotas = ["Leon","Tigre","Perro","Mapache","Delfin","Oso"]
filtrar_mascotas(lista_mascotas)


# %%
#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    pass

def promedio_lista(numeros):
    if not numeros:  
        raise ListaVaciaError("La lista está vacía. No se puede calcular el promedio.")
    
    return sum(numeros) / len(numeros)


try:
    numeros = [40, 20, 30]
    print("Promedio:", promedio_lista(numeros))
    
    vacia = []
    print("Promedio:", promedio_lista(vacia)) 
except ListaVaciaError as e:
    print("Error:", e)


# %%
#11.Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        
        print(f"Tu edad es: {edad}")
    
    except ValueError as e:
        print(f"Error: {e}")



# %%
pedir_edad()

# %%
#12.Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map
def longitudes_palabras(frase):
    palabras = frase.split() 
    longitudes = list(map(len, palabras)) 
    return longitudes

    

# %%
print(longitudes_palabras("La comida esta rica"))

# %%
#13.Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def letras_mayus_minus(caracteres):
   
    caracteres_unicos = set(caracteres)
    resultado = list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))
    
    return resultado


# %%
#14.Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def palabras_con_letra(lista_palabras, letra):
    letra = letra.lower()  
    resultado = list(filter(lambda p: p.lower().startswith(letra), lista_palabras))
    return resultado





# %%
palabras_ejercio = ['Circo', 'Animal', 'Safari', 'Seleccion', 'Coche', 'Peaje']
print(palabras_con_letra(palabras_ejercio,'S'))

# %%
#15.Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))




# %%
Numeros_lista = [3,10,20]
print(sumar_tres(Numeros_lista))

# %%
#16.Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def palabras_mas_largas(cadena, n):
    palabras = cadena.split()
    resultado = list(filter(lambda p: len(p) > n, palabras))
    return resultado


# %%
cadena_de_texto = "Hoy hace una temperatura elevada"
print(palabras_mas_largas(cadena_de_texto,5))

# %%
#17.Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()
from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)


# %%
print(lista_a_numero([1,5,7,9]))

# %%
#18.Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 88},
    {"nombre": "María", "edad": 19, "calificacion": 90},
    {"nombre": "Pedro", "edad": 21, "calificacion": 76},
    {"nombre": "Lucía", "edad": 23, "calificacion": 97}
]

estudiantes_destacados = list(filter(lambda est: est["calificacion"] >= 90, estudiantes))

print(estudiantes_destacados)



# %%
#19.Crea una función lambda que filtre los números impares de una lista dada.
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))



# %%
lista_numeros = [1,3,7,8,25,66,89,95]
print(filtrar_impares(lista_numeros))

# %%
#20.Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la funciónfilter()
elementos = [1, "vecino", 2, "retiro", 3, "vida", 4]

solo_enteros = list(filter(lambda x: isinstance(x, int), elementos))

print(solo_enteros)


# %%
#21.Crea una función que calcule el cubo de un número dado mediante una función lambda
cubo = lambda x: x**3



# %%
resultado = cubo(6)
print(resultado)

# %%
#22.Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()
from functools import reduce

numeros = [2, 3, 4, 6]

producto_total = reduce(lambda x, y: x * y, numeros)

print(producto_total) 



# %%
#23.Concatena una lista de palabras.Usa la función reduce() .
from functools import reduce
lista_palabras = ["Hola"," ","me"," ", "llamo"," ", "Sergio"]

# %%
frase_junta = reduce(lambda x,y : x + y, lista_palabras)
print(frase_junta)

# %%
#24.Calcula la diferencia total en los valores de una lista. Usa la función reduce()
from functools import reduce
lista_numeros_2 = [4,5,7,9,14,20]
diferencia_numeros = reduce(lambda x,y : x - y,lista_numeros_2)
print(diferencia_numeros)

# %%
#25.Crea una función que cuente el número de caracteres en una cadena de texto dada
def contar_caractares (cadena):
    return len(cadena)

# %%
Cadena = ("hola como estas")
contar_caractares(Cadena)

# %%
#26.Crea una función lambda que calcule el resto de la división entre dos números dados.
division = lambda x,y : x/y

# %%
division(10,2)

# %%
#27.Crea una función que calcule el promedio de una lista de números.
def media (numeros) :
    return sum(numeros)/len(numeros)
    

# %%
lista_numeros_3 = [4,5,8,10,55]
resultado = media(lista_numeros_3)
print(resultado)

# %%
#28.Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None 




# %%
datos = [2,5,4,6,2,8,4]
resultad = primer_duplicado(datos)
print(resultad)

# %%
#29.Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def enmascarar(valor):
    cadena = str(valor)
    if len(cadena) <= 4:
        return cadena
    return "#" * (len(cadena) - 4) + cadena[-4:]


# %%
print(enmascarar("abdcefghijk"))

# %%
#30.Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()
    return sorted(p1) == sorted(p2)


# %%
print(son_anagramas("Amor", "romA"))

# %%
#31.Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre():
    entrada = input("Ingresa una lista de nombres separados por comas: ")
    lista_nombres = [nombre.strip() for nombre in entrada.split(",")]

    nombre_buscar = input("Ingresa el nombre a buscar: ").strip()

    if nombre_buscar in lista_nombres:
        print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre_buscar}' NO está en la lista.")



# %%
buscar_nombre()

# %%
#32.Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def obtener_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado['nombre'] == nombre_completo:
            return f"{nombre_completo} ocupa el puesto de {empleado['puesto']}."
    return f"{nombre_completo} no trabaja aquí."



# %%
empleados = [
    {"nombre": "Cristina Pérez", "puesto": "Gerente"},
    {"nombre": "Luis Gómez", "puesto": "Contable"},
    {"nombre": "Rosa Martínez", "puesto": "Secretaria"}
]
print(obtener_puesto("Rosa Martínez", empleados))

# %%
#33.Crea una función lambda que sume elementos correspondientes de dos listas dadas.
suma_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# %%
a = [3,6,7]
b = [1,4,8]
resultado_listas = suma_listas(a,b)
print(resultado_listas)

# %%
#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
    #La parte que mas me ha costado es sin duda a partir de aquí, crear los arboles y las clases ha sido bastante reto y donde más tiempo he pasado.


# %%
arbol = Arbol()

arbol.crecer_tronco()

arbol.nueva_rama()

arbol.crecer_ramas()

arbol.nueva_rama()
arbol.nueva_rama()

arbol.quitar_rama(2)

info = arbol.info_arbol()
print(info)


# %%
#36.Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo. Código a seguir: 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False . 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse. 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse. 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario. Caso de uso: 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente. 2. Agregar 20 unidades de saldo de "Bob". 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia". 4. Retirar 50 unidades de saldo a "Alicia".
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        # 1. Inicializar usuario
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    
    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= cantidad

   
    def transferir_dinero(self, otro_usuario, cantidad):
        if not self.cuenta_corriente or not otro_usuario.cuenta_corriente:
            raise ValueError("Ambos usuarios deben tener cuenta corriente.")
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene saldo suficiente.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

   
    def agregar_dinero(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad
        #En este ejercicio, pasé bastante tiempo, ya que me equivocaba en los ValueError, no conseguía el formato correcto y fue algo desesperante pero trás muchos prueba-error, conseguí dar con la tecla


# %%
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)

alicia.transferir_dinero(bob, 80)

alicia.retirar_dinero(50)

print(f"Saldo de Alicia: {alicia.saldo}")  
print(f"Saldo de Bob: {bob.saldo}")    
#En este caso, me pareció que, cuando me escupía el ValueError, lo había escrito mal pero erá porque Bob tenía saldo negativo y no podía seguir adelante



# %%
#37.Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto . Código a seguir: 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario. 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras. 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada. 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada. Caso de uso: Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    palabras = texto.lower().split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)



def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return " ".join(palabras_filtradas)



def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida")
    #Aquí, lo que no terminó de entender y tuve que utilizar la ayuda de la IA, es la última parte de procesar texto, no se muy bien en que puede ser útil, si me podéis ayudar estaría genial.




# %%

texto = "hola gente hola buena gente"

# Contar palabras
resultado_contar = procesar_texto(texto, "contar")
print("Conteo de palabras:", resultado_contar)

# Reemplazar palabra
resultado_reemplazar = procesar_texto(texto, "reemplazar", "gente", "poblacion")
print("Texto reemplazado:", resultado_reemplazar)

# Eliminar palabra
resultado_eliminar = procesar_texto(texto, "eliminar", "hola")
print("Texto sin palabra:", resultado_eliminar)


# %%
#38.Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
hora = int(input("Introduce la hora (0 a 23): "))

if 6 <= hora < 13:
    print("Es de día")
elif 13 <= hora < 20:
    print("Es de tarde")
elif 0 <= hora < 24:
    print("Es de noche")
else:
    print("Hora no válida")


# %%
#39.Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son: - 0 - 69 insuficiente - 70 - 79 bien - 80 - 89 muy bien - 90 - 100 excelente
nota = int(input("Introduce la calificación (0 a 100): "))

if 0 <= nota <= 69:
    print("Insuficiente")
elif 70 <= nota <= 79:
    print("Bien")
elif 80 <= nota <= 89:
    print("Muy bien")
elif 90 <= nota <= 100:
    print("Excelente")
else:
    print("Calificación no válida")


# %%
#40.Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math

def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        raise ValueError("Figura no válida")
#Este ejercicio fue un reto al principio, ya que no estaba seguro de como calcular el area de las diferentes figuras, especialmente la del circulo, ya que no me acordaba. El importar math tampoco lo tenía claro.

# %%
print(calcular_area("rectangulo", (7, 5)))  
print(calcular_area("circulo", (3,)))        
print(calcular_area("triangulo", (9, 3)))    


# %%
#41.En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente: 1. Solicita al usuario que ingrese el precio original de un artículo. 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento. 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

precio_original = float(input("Introduce el precio del artículo (€): "))

tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").lower()

if tiene_cupon == "sí" or tiene_cupon == "si":
    descuento = float(input("Introduce el valor del cupón (€): "))

    if descuento > 0:
        precio_final = precio_original - descuento

        if precio_final < 0:
            precio_final = 0
    else:
        print("El valor del cupón no es válido.")
        precio_final = precio_original

elif tiene_cupon == "no":
    precio_final = precio_original

else:
    print("Respuesta no válida. No se aplicará descuento.")
    precio_final = precio_original

print(f"El precio final de la compra es: {precio_final} €")
#Este sin duda fue el ejercio más complejo pero me gustó el reto de hacerlo y me pareció muy práctico e intituitivo. Es mucho texto pero al final se pudo sacar.


# %%



