## Curso de Capacitación en Python

## Semana 0 - Funciones y Variables - 22/5/24


---

# Creando Código con Python

VS Code es un tipo especial de editor de texto llamado compilador. En la parte superior, notarás un editor de texto. En la parte inferior, verás una terminal donde puedes ejecutar comandos.

En la terminal, puedes ejecutar `code hello.py` para empezar a codificar. En el editor de texto de arriba, puedes escribir `print("hello, world")`. Este es un programa canónico famoso que casi todos los programadores escriben durante su proceso de aprendizaje.

En la ventana de la terminal, puedes ejecutar comandos. Para ejecutar este programa, necesitarás mover tu cursor a la parte inferior de la pantalla, haciendo clic en la ventana de la terminal. Ahora puedes escribir un segundo comando en la ventana de la terminal. Junto al signo de dólar, escribe `python hello.py` y presiona la tecla enter en tu teclado.

Recuerda que las computadoras realmente solo entienden ceros y unos. Por lo tanto, cuando ejecutas `python hello.py`, Python interpretará el texto que creaste en hello.py y lo traducirá a los ceros y unos que la computadora puede entender.

El resultado de ejecutar el programa `python hello.py` es `hello, world`. ¡Felicidades! Acabas de crear tu primer programa.

## Funciones

Las funciones son verbos o acciones que la computadora o el lenguaje de programación ya sabrán cómo realizar. En tu programa hello.py, la función `print` sabe cómo imprimir en la ventana de la terminal. La función `print` toma argumentos. En este caso, `"hello, world"` son los argumentos que la función `print` toma.

## Bugs

Los bugs son una parte natural de la programación. ¡Estos son errores, problemas que debes resolver! ¡No te desanimes! Esto es parte del proceso de convertirse en un gran programador. Imagina en nuestro programa hello.py que accidentalmente escribimos `print("hello, world"` y notamos que nos falta el `)` final requerido por el compilador. Si cometo este error a propósito, verás que el compilador mostrará un error en la ventana de la terminal.

A menudo, los mensajes de error te informarán de tus errores y te darán pistas sobre cómo corregirlos. Sin embargo, habrá muchas veces en las que el compilador no será tan amable.

## Mejorando Tu Primer Programa en Python

Podemos personalizar tu primer programa en Python. En nuestro editor de texto en hello.py, podemos agregar otra función. `input` es una función que toma un mensaje como argumento. Podemos editar nuestro código para decir:

```python
input("What's your name? ")
print("hello, world")
```

Sin embargo, esta edición sola no permitirá que tu programa muestre lo que tu usuario ingresa. Para eso, necesitaremos presentarte las variables.

## Variables

Una variable es simplemente un contenedor para un valor dentro de tu propio programa. En tu programa, puedes introducir tu propia variable editando tu código para que lea:

```python
name = input("What's your name? ")
print("hello, world")
```

Nota que este signo igual `=` en el medio de `name = input("What's your name? ")` tiene un papel especial en la programación. Este signo igual literalmente asigna lo que está a la derecha a lo que está a la izquierda. Por lo tanto, el valor devuelto por `input("What's your name? ")` se asigna a `name`.

Si editas tu código como sigue, notarás un error:

```python
name = input("What's your name? ")
print("hello, name")
```

El programa devolverá `hello, name` en la ventana de la terminal, sin importar lo que el usuario escriba.

Editando más nuestro código, podrías escribir:

```python
name = input("What's your name? ")
print("hello,")
print(name)
```

El resultado en la ventana de la terminal sería:

```
What's your name? David
hello
David
```

¡Nos estamos acercando al resultado que podríamos pretender!

Puedes aprender más en la [documentación de Python sobre tipos de datos](https://docs.python.org/3/library/stdtypes.html).

## Comentarios

Los comentarios son una forma para que los programadores rastreen lo que están haciendo en sus programas e incluso informen a otros sobre sus intenciones para un bloque de código. En resumen, ¡son notas para ti mismo y para otros que verán tu código!

Puedes agregar comentarios a tu programa para poder ver qué está haciendo tu programa. Podrías editar tu código como sigue:

```python
# Pregunta al usuario su nombre
name = input("What's your name? ")
print("hello,")
print(name)
```

Los comentarios también pueden servir como una lista de tareas para ti.

## Pseudocódigo

El pseudocódigo es un tipo importante de comentario que se convierte en un tipo especial de lista de tareas, especialmente cuando no entiendes cómo lograr una tarea de codificación. Por ejemplo, en tu código, podrías editar tu código para decir:

```python
# Pregunta al usuario su nombre
name = input("What's your name? ")

# Imprime hola
print("hello,")

# Imprime el nombre ingresado
print(name)
```

## Mejorando Aún Más Tu Primer Programa en Python

Podemos editar más nuestro código como sigue:

```python
# Pregunta al usuario su nombre
name = input("What's your name? ")

# Imprime hola y el nombre ingresado
print("hello, " + name)
```

Resulta que algunas funciones toman muchos argumentos. Podemos usar una coma `,` para pasar múltiples argumentos editando nuestro código como sigue:

```python
# Pregunta al usuario su nombre
name = input("What's your name? ")

# Imprime hola y el nombre ingresado
print("hello,", name)
```

La salida en la terminal, si escribimos "David", sería `hello, David`. Éxito.

## Cadenas y Parámetros

Una cadena, conocida como `str` en Python, es una secuencia de texto. Retrocediendo un poco en nuestro código a lo siguiente, hubo un efecto secundario visual de tener el resultado aparecer en múltiples líneas:

```python
# Pregunta al usuario su nombre
name = input("What's your name? ")
print("hello,")
print(name)
```

Las funciones toman argumentos que influyen en su comportamiento. Si miramos la documentación para `print`, notarás que podemos aprender mucho sobre los argumentos que toma la función `print`. Mirando esta documentación, aprenderás que la función `print` incluye automáticamente un código `end='\n'`. Este `\n` indica que la función `print` creará automáticamente un salto de línea cuando se ejecute. La función `print` toma un argumento llamado `end` y el valor predeterminado es crear una nueva línea.

Sin embargo, ¡podemos proporcionar técnicamente un argumento para `end` nosotros mismos para que no se cree una nueva línea!

Podemos modificar nuestro código como sigue:

```python
# Pregunta al usuario su nombre
name = input("What's your name? ")
print("hello,", end="")
print(name)
```

Al proporcionar `end=""` estamos sobrescribiendo el valor predeterminado de `end` para que nunca cree una nueva línea después de esta primera declaración `print`. Al proporcionar el nombre como "David", la salida en la ventana de la terminal será `hello, David`.

Por lo tanto, los parámetros son argumentos que puede tomar una función.

Puedes aprender más en la [documentación de Python sobre `print`](https://docs.python.org/3/library/functions.html#print).

## Un pequeño problema con las comillas

Nota cómo agregar comillas como parte de tu cadena es un desafío. `print("hello,"friend"")` no funcionará, y el compilador mostrará un error. Generalmente, hay dos enfoques para solucionar esto. Primero, podrías simplemente cambiar las comillas a comillas simples. Otro enfoque más comúnmente utilizado sería codificar como `print("hello, \"friend\"")`. Las barras invertidas indican al compilador que el carácter siguiente debe considerarse una comilla en la cadena y evitar un error del compilador.

## Formateando Cadenas

Probablemente la forma más elegante de usar cadenas sería la siguiente:

```python
# Pregunta al usuario su nombre
name = input("What's your name? ")
print(f"hello, {name}")
```

Nota la `f` en `print(f"hello, {name}")`. Esta `f` es un indicador especial para que Python trate esta cadena de una manera especial, diferente a los enfoques anteriores que hemos ilustrado en esta lección. Espera que utilices este estilo de cadenas con bastante frecuencia en este curso.

---

Claro, Juampi. Aquí tienes la traducción del texto listo para armar un PDF:

---

**Creando Código con Python**

VS Code es un tipo especial de editor de texto que se llama compilador. En la parte superior, notarás un editor de texto. En la parte inferior, verás una terminal donde puedes ejecutar comandos.

En la terminal, puedes ejecutar el código `hello.py` para comenzar a programar.

En el editor de texto, puedes escribir `print("hello, world")`. Este es un programa canónico famoso que casi todos los programadores escriben durante su proceso de aprendizaje.

En la ventana de la terminal, puedes ejecutar comandos. Para ejecutar este programa, debes mover tu cursor a la parte inferior de la pantalla, haciendo clic en la ventana de la terminal. Ahora puedes escribir un segundo comando en la ventana de la terminal. Al lado del signo de dólar, escribe `python hello.py` y presiona la tecla Enter en tu teclado.

Recuerda que las computadoras realmente solo entienden ceros y unos. Por lo tanto, cuando ejecutas `python hello.py`, Python interpretará el texto que creaste en `hello.py` y lo traducirá en ceros y unos que la computadora puede entender.

El resultado de ejecutar el programa `python hello.py` es `hello, world`.

¡Felicidades! Acabas de crear tu primer programa.

**Funciones**

Las funciones son verbos o acciones que la computadora o el lenguaje de programación ya saben cómo realizar.

En tu programa `hello.py`, la función `print` sabe cómo imprimir en la ventana de la terminal.

La función `print` toma argumentos. En este caso, "hello, world" son los argumentos que toma la función `print`.

**Errores**

Los errores son una parte natural de la programación. ¡Son errores, problemas para resolver! ¡No te desanimes! Esto es parte del proceso para convertirse en un gran programador.

Imagina que en nuestro programa `hello.py` accidentalmente escribimos `print("hello, world"` nota que nos faltó el paréntesis final requerido por el compilador. Si cometo este error a propósito, verás que el compilador mostrará un error en la ventana de la terminal.

A menudo, los mensajes de error te informarán de tus errores y te darán pistas sobre cómo corregirlos. Sin embargo, habrá muchas veces en que el compilador no será tan amable.

**Mejorando Tu Primer Programa en Python**

Podemos personalizar tu primer programa en Python.

En nuestro editor de texto en `hello.py` podemos agregar otra función. `input` es una función que toma un mensaje como argumento. Podemos editar nuestro código para decir:

```python
input("What's your name? ")
print("hello, world")
```

Sin embargo, esta sola edición no permitirá que tu programa muestre lo que el usuario ingresa. Para eso, necesitaremos introducirte a las variables.

**Variables**

Una variable es simplemente un contenedor para un valor dentro de tu propio programa.

En tu programa, puedes introducir tu propia variable editando el código para que lea:

```python
name = input("What's your name? ")
print("hello, world")
```

Nota que este signo igual `=` en el medio de `name = input("What's your name? ")` tiene un papel especial en la programación. Este signo igual literalmente asigna lo que está a la derecha a lo que está a la izquierda. Por lo tanto, el valor devuelto por `input("What's your name? ")` se asigna a `name`.

Si editas tu código de la siguiente manera, notarás un error:

```python
name = input("What's your name? ")
print("hello, name")
```

El programa devolverá `hello, name` en la ventana de la terminal independientemente de lo que escriba el usuario.

Editando aún más nuestro código, podrías escribir:

```python
name = input("What's your name? ")
print("hello,")
print(name)
```

El resultado en la ventana de la terminal sería:

```
What's your name? David
hello
David
```

Nos estamos acercando al resultado que podríamos desear.

Puedes aprender más en la documentación de Python sobre tipos de datos.

**Comentarios**

Los comentarios son una forma de que los programadores rastreen lo que están haciendo en sus programas e incluso informen a otros sobre sus intenciones para un bloque de código. En resumen, son notas para ti y para otros que verán tu código.

Puedes agregar comentarios a tu programa para poder ver qué es lo que tu programa está haciendo. Podrías editar tu código de la siguiente manera:

```python
# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)
```

Los comentarios también pueden servir como una lista de tareas para ti.

**Pseudocódigo**

El pseudocódigo es un tipo importante de comentario que se convierte en un tipo especial de lista de tareas, especialmente cuando no entiendes cómo lograr una tarea de programación. Por ejemplo, en tu código, podrías editarlo para que diga:

```python
# Ask the user for their name
name = input("What's your name? ")

# Print hello
print("hello,")

# Print the name inputted
print(name)
```

**Mejorando Aún Más Tu Primer Programa en Python**

Podemos editar aún más nuestro código de la siguiente manera:

```python
# Ask the user for their name
name = input("What's your name? ")

# Print hello and the inputted name
print("hello, " + name)
```

Resulta que algunas funciones toman muchos argumentos.

Podemos usar una coma `,` para pasar múltiples argumentos editando nuestro código de la siguiente manera:

```python
# Ask the user for their name
name = input("What's your name? ")

# Print hello and the inputted name
print("hello,", name)
```

El resultado en la terminal, si escribimos "David", sería `hello, David`. Éxito.

**Cadenas y Parámetros**

Una cadena, conocida como `str` en Python, es una secuencia de texto.

Retrocediendo un poco en nuestro código hasta lo siguiente, hubo un efecto secundario visual de tener el resultado apareciendo en múltiples líneas:

```python
# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)
```

Las funciones toman argumentos que influyen en su comportamiento. Si miramos la documentación de `print` notarás que podemos aprender mucho sobre los argumentos que toma la función `print`.

Al observar esta documentación, aprenderás que la función `print` incluye automáticamente un fragmento de código `end='\n'`. Este `\n` indica que la función `print` creará automáticamente un salto de línea cuando se ejecute. La función `print` toma un argumento llamado `end` y el valor predeterminado es crear una nueva línea.

Sin embargo, técnicamente podemos proporcionar un argumento para `end` nosotros mismos, de modo que no se cree una nueva línea.

Podemos modificar nuestro código de la siguiente manera:

```python
# Ask the user for their name
name = input("What's your name? ")
print("hello,", end="")
print(name)
```

Al proporcionar `end=""` estamos sobrescribiendo el valor predeterminado de `end` para que nunca cree una nueva línea después de esta primera declaración `print`. Proporcionando el nombre como "David", el resultado en la ventana de la terminal será `hello, David`.

Por lo tanto, los parámetros son argumentos que pueden ser tomados por una función.

Puedes aprender más en la documentación de Python sobre `print`.

**Un pequeño problema con las comillas**

Nota cómo agregar comillas como parte de tu cadena es desafiante.

`print("hello,"friend"")` no funcionará, y el compilador lanzará un error.

Generalmente, hay dos enfoques para solucionar esto. Primero, podrías simplemente cambiar las comillas a comillas simples.

Otra, más comúnmente utilizada, sería codificar como `print("hello, \"friend\"")`. Las barras invertidas le indican al compilador que el siguiente carácter debe ser considerado como una comilla en la cadena y evitar un error del compilador.

**Formateo de Cadenas**

Probablemente, la forma más elegante de usar cadenas sería la siguiente:

```python
# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")
```

Nota el `f` en `print(f"hello, {name}")`. Este `f` es un indicador especial para Python para tratar esta cadena de una manera especial, diferente de los enfoques anteriores que hemos ilustrado en esta conferencia. Espera usar este estilo de cadenas con bastante frecuencia en este curso.

---

**Más sobre Cadenas**

Nunca debes esperar que tu usuario coopere como se pretende. Por lo tanto, necesitarás asegurarte de que la entrada de tu usuario sea corregida o verificada.

Resulta que las cadenas incorporan la capacidad de eliminar espacios en blanco de una cadena.

Utilizando el método `strip` en `name` como `name = name.strip()`, se eliminarán todos los espacios en blanco a la izquierda y derecha de la entrada del usuario. Puedes modificar tu código para que sea:

```python
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")
```

Ejecutando nuevamente este programa, independientemente de cuántos espacios escribas antes o después del nombre, eliminará todos los espacios en blanco.

Usando el método `title`, se pondrá en mayúscula la primera letra de cada palabra del nombre del usuario:

```python
# Ask the user

 for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Capitalize the first letter of each word
name = name.title()

# Print the output
print(f"hello, {name}")
```

A estas alturas, es posible que estés muy cansado de escribir `python` repetidamente en la ventana del terminal. Puedes usar la flecha hacia arriba de tu teclado para recordar los comandos del terminal más recientes que has hecho.

Nota que puedes modificar tu código para ser más eficiente:

```python
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str and capitalize the first letter of each word
name = name.strip().title()

# Print the output
print(f"hello, {name}")
```

Esto crea el mismo resultado que tu código anterior.

¡Podríamos incluso ir más allá!

```python
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")
```

Puedes aprender más sobre cadenas en la documentación de Python sobre `str`.

---

**Enteros o `int`**

En Python, un entero se refiere como `int`.

En el mundo de las matemáticas, estamos familiarizados con los operadores `+`, `-`, `*`, `/` y `%`. Ese último operador `%` o operador de módulo puede no ser muy familiar para ti.

No tienes que usar la ventana del editor de texto en tu compilador para ejecutar código en Python. En tu terminal, puedes ejecutar `python` solo. Se te presentará `>>>` en la ventana del terminal. Luego, puedes ejecutar código en vivo, interactivo. Podrías escribir `1+1`, y ejecutará ese cálculo. Este modo no se usará comúnmente durante este curso.

Abriendo VS Code nuevamente, podemos escribir `code calculator.py` en la terminal. Esto creará un nuevo archivo en el que crearemos nuestra propia calculadora.

Primero, podemos declarar algunas variables.

```python
x = 1
y = 2

z = x + y

print(z)
```

Naturalmente, cuando ejecutamos `python calculator.py` obtenemos el resultado en la ventana del terminal de `3`. Podemos hacer esto más interactivo usando la función `input`.

```python
x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
```

Al ejecutar este programa, descubrimos que la salida es incorrecta como `12`. ¿Por qué podría ser esto?

Anteriormente, hemos visto cómo el signo `+` concatena dos cadenas. Debido a que tu entrada desde tu teclado en tu computadora llega al compilador como texto, se trata como una cadena. Por lo tanto, necesitamos convertir esta entrada de una cadena a un entero. Podemos hacerlo de la siguiente manera:

```python
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
```

El resultado ahora es correcto. El uso de `int(x)` se llama "casting", donde un valor se cambia temporalmente de un tipo de variable (en este caso, una cadena) a otro (aquí, un entero).

Podemos mejorar aún más nuestro programa de la siguiente manera:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
```

Esto ilustra que puedes ejecutar funciones sobre funciones. Primero se ejecuta la función interna, y luego la externa. Primero se ejecuta la función `input`. Luego, la función `int`.

Puedes aprender más en la documentación de Python sobre `int`.

**La Legibilidad Gana**

Al decidir tu enfoque para una tarea de programación, recuerda que se puede argumentar razonablemente por muchos enfoques para el mismo problema.

Independientemente del enfoque que tomes para una tarea de programación, recuerda que tu código debe ser legible. Debes usar comentarios para darte a ti mismo y a otros pistas sobre lo que está haciendo tu código. Además, debes crear código de una manera que sea legible.

**Conceptos Básicos de `float`**

Un valor de punto flotante es un número real que tiene un punto decimal, como `0.52`.

Puedes cambiar tu código para admitir flotantes de la siguiente manera:

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)
```

Este cambio permite a tu usuario ingresar `1.2` y `3.4` para presentar un total de `4.6`.

Imaginemos, sin embargo, que deseas redondear el total al número entero más cercano. Mirando la documentación de Python para `round`, verás que los argumentos disponibles son `round(number, [ndigits])`. Esos corchetes indican que algo opcional puede ser especificado por el programador. Por lo tanto, podrías hacer `round(n)` para redondear un dígito a su número entero más cercano. Alternativamente, podrías codificar de la siguiente manera:

```python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the result
print(z)
```

La salida se redondeará al número entero más cercano.

¿Qué pasa si queremos formatear la salida de números largos? Por ejemplo, en lugar de ver `1000`, podrías desear ver `1,000`. Podrías modificar tu código de la siguiente manera:

```python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the formatted result
print(f"{z:,}")
```

Aunque bastante críptico, ese `print(f"{z:,}")` crea un escenario donde el `z` resultante incluirá comas donde el resultado podría parecer `1,000` o `2,500`.

**Más sobre Flotantes**

¿Cómo podemos redondear valores de punto flotante? Primero, modifica tu código de la siguiente manera:

```python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(z)
```

Al ingresar `2` como `x` y `3` como `y`, el resultado `z` es `0.6666666666`, aparentemente infinito como podríamos esperar.

Imaginemos que queremos redondear esto. Podríamos modificar nuestro código de la siguiente manera:

```python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result and round
z = round(x / y, 2)

# Print the result
print(z)
```

Como podríamos esperar, esto redondeará el resultado a los dos puntos decimales más cercanos.

También podríamos usar f-string para formatear la salida de la siguiente manera:

```python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(f"{z:.2f}")
```

Este código críptico de f-string muestra lo mismo que nuestra estrategia de redondeo anterior.

Puedes aprender más en la documentación de Python sobre `float`.

---

**`def`**

¿No sería bueno crear nuestras propias funciones?

Volvamos a nuestro código final de `hello.py` escribiendo `code hello.py` en la ventana del terminal. Tu código inicial debería verse de la siguiente manera:

```python
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")
```

Podemos mejorar nuestro código para crear nuestra propia función especial que diga "hola" por nosotros.

Borrando todo nuestro código en nuestro editor de texto, comencemos desde cero:

```python
name = input("What's your name? ")
hello()
print(name)
```

Al intentar ejecutar este código, tu compilador lanzará un error. Después de todo, no hay una función definida para `hello`.

Podemos crear nuestra propia función llamada `hello` de la siguiente manera:

```python
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)
```

Nota que todo bajo `def hello()` está indentado. Python es un lenguaje indentado. Utiliza la indentación para entender qué es parte de la función anterior. Por lo tanto, todo en la función `hello` debe estar indentado. Cuando algo no está indentado, lo trata como si no estuviera dentro de la función `hello`. Al ejecutar `python hello.py` en la ventana del terminal, verás que tu salida no es exactamente como deseas.

Podemos mejorar aún más nuestro código:

```python
# Create our own function
def hello(to):
    print("hello,", to)

# Output using our own function
name = input("What's your name? ")
hello(name)
```

Aquí, en las primeras líneas, estás creando tu función `hello`. Esta vez, sin embargo, le estás diciendo al compilador que esta función toma un solo parámetro: una variable llamada `to`. Por lo tanto, cuando llamas a `hello(name)` la computadora pasa `name` a la función `hello

` como `to`. Así es como pasamos valores a funciones. ¡Muy útil! Al ejecutar `python hello.py` en la ventana del terminal, verás que la salida es mucho más cercana a nuestro ideal presentado anteriormente en esta conferencia.

Podemos cambiar nuestro código para agregar un valor predeterminado a `hello`:

```python
# Create our own function
def hello(to="world"):
    print("hello,", to)

# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()
```

Prueba tu código tú mismo. Nota cómo el primer `hello` se comportará como podrías esperar, y el segundo `hello`, que no recibe un valor, por defecto, imprimirá `hello, world`.

No tenemos que tener nuestra función al inicio de nuestro programa. Podemos moverla hacia abajo, pero necesitamos decirle al compilador que tenemos una función `main` y una función `hello` separada.

```python
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()

# Create our own function
def hello(to="world"):
    print("hello,", to)
```

Esto solo, sin embargo, creará un error de cierto tipo. Si ejecutamos `python hello.py`, ¡nada sucede! La razón de esto es que nada en este código está realmente llamando a la función `main` y trayendo nuestro programa a la vida.

La siguiente modificación muy pequeña llamará a la función `main` y restaurará nuestro programa a su estado de funcionamiento:

```python
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()

# Create our own function
def hello(to="world"):
    print("hello,", to)

main()
```

---

**Devolviendo Valores**

Puedes imaginar muchos escenarios en los que no solo quieres que una función realice una acción, sino que también devuelva un valor de vuelta a la función principal. Por ejemplo, en lugar de simplemente imprimir el cálculo de `x + y`, podrías querer que una función devuelva el valor de este cálculo a otra parte de tu programa. Esta "devolución" de un valor la llamamos un valor de retorno.

Volviendo a nuestro código de `calculator.py` escribiendo `code calculator.py`. Borra todo el código allí. Rehaz el código de la siguiente manera:

```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()
```

Efectivamente, `x` se pasa a `square`. Luego, el cálculo de `x * x` se devuelve a la función principal.

---

**Resumiendo**

A través del trabajo de esta única conferencia, has aprendido habilidades que usarás innumerables veces en tus propios programas. Has aprendido sobre:

- Creación de tus primeros programas en Python;
- Funciones;
- Errores;
- Variables;
- Comentarios;
- Pseudocódigo;
- Cadenas;
- Parámetros;
- Cadenas formateadas;
- Enteros;
- Principios de legibilidad;
- Flotantes;
- Creación de tus propias funciones; y
- Valores de retorno.

