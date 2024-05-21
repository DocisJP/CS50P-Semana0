# Einstein

Incluso si no has estudiado física (recientemente o nunca), es posible que hayas escuchado la famosa ecuación de Einstein, en la cual E representa la energía (medida en julios), m representa la masa (medida en kilogramos), y c representa la velocidad de la luz (medida aproximadamente en 300000000 metros por segundo), según Albert Einstein y otros. Básicamente, la fórmula significa que la masa y la energía son equivalentes.

En un archivo llamado einstein.py, implementa un programa en Python que solicite al usuario la masa como un número entero (en kilogramos) y luego muestre el número equivalente de julios como un número entero. Asume que el usuario ingresará un número entero.

**Sugerencias:**

- Recuerda que `input` devuelve una cadena, según [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recuerda que `int` puede convertir una cadena en un entero, según [docs.python.org/3/library/functions.html#int](https://docs.python.org/3/library/functions.html#int).
- Recuerda que Python viene con varias funciones integradas, según [docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html).

## Antes de Comenzar

Ejecuta \`cd\` solo en tu ventana de terminal. Deberías ver que el símbolo del sistema de tu terminal se asemeja a lo siguiente:

```bash
$
```

Luego ejecuta

```bash
mkdir einstein
```

para crear una carpeta llamada \`einstein\` en tu espacio de código.

Luego ejecuta

```bash
\`cd einstein\`
```

para cambiar el directorio a esa carpeta. Ahora deberías ver el símbolo del sistema de tu terminal como \`faces/ $\`. Ahora puedes ejecutar

```bash
code einstein.py
```

para crear un archivo llamado \`einstein.py\` donde escribirás tu programa.

## Como Testear

Aquí te mostramos cómo probar tu código manualmente:

Ejecuta tu programa con `python einstein.py`. Escribe 1 y presiona Enter. Tu programa debería mostrar:

'90000000000000000'

Ejecuta tu programa con `python einstein.py`. Escribe 14 y presiona Enter. Tu programa debería mostrar:

'1260000000000000000'

Ejecuta tu programa con `python einstein.py`. Escribe 50 y presiona Enter. Tu programa debería mostrar:

'4500000000000000000'

Puedes ejecutar lo siguiente para verificar tu código usando check50, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

```bash
check50 cs50/problems/2022/python/einstein
```

### Como Entregar

En tu terminal, ejecuta el código de abajo para entregar tu trabajo.

```bash
submit50 cs50/problems/2022/python/einstein
```
