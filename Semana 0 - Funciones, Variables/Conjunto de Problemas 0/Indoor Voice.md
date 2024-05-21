ESCRIBIR TODO EN MAYÚSCULAS ES COMO GRITAR.

Es mejor usar tu “voz interior” a veces, escribiendo todo en minúsculas.

En un archivo llamado `indoor.py`, implementa un programa en Python que solicite al usuario una entrada y luego muestre esa misma entrada en minúsculas. La puntuación y los espacios en blanco deben mostrarse sin cambios. Puedes, pero no es obligatorio, solicitar explícitamente al usuario, pasando una cadena (`str`) propia como argumento a `input`.

### Pistas

- Recuerda que `input` devuelve una cadena (`str`), según [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recuerda que una cadena (`str`) tiene varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Antes de Comenzar

Ejecuta \`cd\` solo en tu ventana de terminal. Deberías ver que el símbolo del sistema de tu terminal se asemeja a lo siguiente:

```bash
$
```

Luego ejecuta

```bash
mkdir indoor
```

para crear una carpeta llamada \`indoor\` en tu espacio de código.

Luego ejecuta

```bash
cd indoor
```

para cambiar el directorio a esa carpeta. Ahora deberías ver el símbolo del sistema de tu terminal como \`indoor/ $\`. Ahora puedes ejecutar

```bash
code indoor.py
```

para crear un archivo llamado \`indoor.py\` donde escribirás tu programa.

### Cómo Probar

Así es cómo puedes probar tu código manualmente. En el símbolo del sistema `indoor/ $` en tu terminal:

1. Ejecuta tu programa con `python indoor.py`. Escribe HELLO y presiona Enter. Tu programa debería mostrar hello.
2. Ejecuta tu programa con `python indoor.py`. Escribe THIS IS CS50 y presiona Enter. Tu programa debería mostrar this is cs50.
3. Ejecuta tu programa con `python indoor.py`. Escribe 50 y presiona Enter. Tu programa debería mostrar 50.
4. Si encuentras un error que dice que tu archivo no se puede abrir, revisa tus pasos para asegurarte de que estás dentro de tu carpeta indoor y has guardado tu archivo indoor.py allí. ¿Recuerdas cómo?

Puedes ejecutar lo siguiente para verificar tu código usando check50, un programa que CS50 usará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

`check50 cs50/problems/2022/python/indoor`

¡Caritas sonrientes verdes significan que tu programa ha pasado una prueba! Caritas tristes rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que check50 muestra para ver la entrada que check50 le entregó a tu programa, qué salida esperaba y qué salida realmente dio tu programa.

### Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

`submit50 cs50/problems/2022/python/indoor`
