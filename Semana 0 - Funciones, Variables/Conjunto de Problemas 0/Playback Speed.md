### Playback Speed

Algunas personas tienen la costumbre de hablar muy rápido al dar una conferencia, y sería bueno poder ralentizarlos, al estilo de la velocidad de reproducción 0.75 de YouTube, o incluso haciendo que hagan pausas entre palabras.

En un archivo llamado `playback.py`, implementa un programa en Python que solicite al usuario una entrada y luego muestre esa misma entrada, reemplazando cada espacio con ... (es decir, tres puntos).

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
mkdir playback
```

para crear una carpeta llamada \`playback\` en tu espacio de código.

Luego ejecuta

```bash
 cd playback
```

para cambiar el directorio a esa carpeta. Ahora deberías ver el símbolo del sistema de tu terminal como \`faces/ $\`. Ahora puedes ejecutar

```bash
code playback.py
```

para crear un archivo llamado \`playback.py\` donde escribirás tu programa.

### Cómo Probar

Así es cómo puedes probar tu código manualmente:

1. Ejecuta tu programa con `python playback.py`. Escribe This is CS50 y presiona Enter. Tu programa debería mostrar:
   This...is...CS50

1. Ejecuta tu programa con `python playback.py`. Escribe This is our week on functions y presiona Enter. Tu programa debería mostrar:
   This...is...our...week...on...functions

1. Ejecuta tu programa con `python playback.py`. Escribe Let's implement a function called hello y presiona Enter. Tu programa debería mostrar:
   Let's...implement...a...function...called...hello

Puedes ejecutar lo siguiente para verificar tu código usando check50, un programa que CS50 usará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

```bash
check50 cs50/problems/2022/python/playback
```

¡Caritas sonrientes verdes significan que tu programa ha pasado una prueba! Caritas tristes rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que check50 muestra para ver la entrada que check50 le entregó a tu programa, qué salida esperaba y qué salida realmente dio tu programa.

### Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

```bash
submit50 cs50/problems/2022/python/playback
```
