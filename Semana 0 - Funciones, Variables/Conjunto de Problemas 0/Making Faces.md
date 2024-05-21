# Haciendo Caras

Antes de que existieran los emojis, estaban los emoticonos, donde texto como :) era una cara feliz y texto como :( era una cara triste. ¡Hoy en día, los programas tienden a convertir los emoticonos en emoji automáticamente!

En un archivo llamado faces.py, implementa una función llamada `convert` que acepte una cadena como entrada y devuelva esa misma entrada con cualquier :) convertido en 🙂 (también conocido como una cara ligeramente sonriente) y cualquier :( convertido en 🙁 (también conocido como una cara ligeramente fruncida). Todo otro texto debe ser devuelto sin cambios.

Luego, en ese mismo archivo, implementa una función llamada `main` que solicite entrada al usuario, llame a `convert` con esa entrada e imprima el resultado. Eres bienvenido, pero no es necesario, solicitar explícitamente la entrada al usuario, como pasando una cadena propia como argumento a input. Asegúrate de llamar a `main` al final de tu archivo.

**Sugerencias:**

- Recuerda que `input` devuelve una cadena, según [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recuerda que una cadena viene con bastantes métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Un emoji en realidad es solo un carácter, así que puedes citarlo como cualquier cadena, como "😐". Y puedes copiar y pegar el emoji desde esta página en tu propio código según sea necesario.

## Antes de Comenzar

Ejecuta \`cd\` solo en tu ventana de terminal. Deberías ver que el símbolo del sistema de tu terminal se asemeja a lo siguiente:

```bash
$
```

Luego ejecuta

```bash
mkdir faces
```

para crear una carpeta llamada \`faces\` en tu espacio de código.

Luego ejecuta

```bash
 cd faces
```

para cambiar el directorio a esa carpeta. Ahora deberías ver el símbolo del sistema de tu terminal como \`faces/ $\`. Ahora puedes ejecutar

```bash
code faces.py
```

para crear un archivo llamado \`einstein.py\` donde escribirás tu programa.

### Como Testear

Así es como testeas tu codigo manualmente:

1. Ejecuta tu programa con 'python faces.py'. Tipea 'Hello :)' y apreta enter. Tu programa debería mostrar este output:
   \`Hello 🙂\`
2. Ejecuta tu programa con 'python faces.py'. Tipea 'Goodbye :(' y apreta enter. Tu programa debería mostrar este output:
   \`Goodbye 🙁\`
3. Ejecuta tu programa con 'python faces.py'. Type 'Hello :) Goodbye :(' y apreta enter. Tu programa debería mostrar este output:
   \`Hello 🙂 Goodbye 🙁\`

Puedes ejecutar lo siguiente para verificar tu código usando check50, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

```bash
check50 cs50/problems/2022/python/faces
```

¡Las caritas sonrientes verdes significan que tu programa ha pasado una prueba! Las caritas tristes rojas indicarán que tu programa produjo algo inesperado. Visita la URL que check50 muestra para ver la entrada que check50 entregó a tu programa, qué salida esperaba y qué salida dio tu programa realmente.

### Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

```bash
submit50 cs50/problems/2022/python/faces
```
