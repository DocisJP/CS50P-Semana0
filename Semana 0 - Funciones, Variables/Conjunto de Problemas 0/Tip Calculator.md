Calculadora de Propinas
Y ahora, mi calculadora de propinas de mago.

— Morty Seinfeld

En Estados Unidos, es costumbre dejar propina para tu camarero después de cenar en un restaurante, típicamente una cantidad igual al 15% o más del costo de tu comida. ¡No te preocupes, sin embargo, hemos escrito una calculadora de propinas para ti, aquí abajo!

```python
def main():
    dolares = dolares_a_float(input("¿Cuánto fue la comida? "))
    porcentaje = porcentaje_a_float(input("¿Qué porcentaje te gustaría dejar de propina? "))
    propina = dolares * porcentaje
    print(f"Deja ${propina:.2f}")


def dolares_a_float(d):
    # TODO


def porcentaje_a_float(p):
    # TODO


main()
```

Bueno, hemos escrito la mayor parte de una calculadora de propinas para ti. Desafortunadamente, no tuvimos tiempo de implementar dos funciones:

dolares_a_float, que debería aceptar una cadena como entrada (formateada como $##.##, donde cada # es un dígito decimal), eliminar el signo $ inicial, y devolver el monto como un flotante. Por ejemplo, dado $50.00 como entrada, debería devolver 50.0.
porcentaje_a_float, que debería aceptar una cadena como entrada (formateada como ##%, donde cada # es un dígito decimal), eliminar el signo % al final, y devolver el porcentaje como un flotante. Por ejemplo, dado 15% como entrada, debería devolver 0.15.
Supón que el usuario ingresará valores en los formatos esperados.

Sugerencias:

Recuerda que input devuelve una cadena, según docs.python.org/3/library/functions.html#input.
Recuerda que float puede convertir una cadena en un flotante, según docs.python.org/3/library/functions.html#float.
Recuerda que una cadena viene con bastantes métodos, según docs.python.org/3/library/stdtypes.html#string-methods.

## Antes de Comenzar

Ejecuta \`cd\` solo en tu ventana de terminal. Deberías ver que el símbolo del sistema de tu terminal se asemeja a lo siguiente:

```bash
$
```

Luego ejecuta

```bash
mkdir tip
```

para crear una carpeta llamada \`tip\` en tu espacio de código.

Luego ejecuta

```bash
\`cd tip\`
```

para cambiar el directorio a esa carpeta. Ahora deberías ver el símbolo del sistema de tu terminal como \`tip/ $\`. Ahora puedes ejecutar

```bash
code tip.py
```

para crear un archivo llamado \`tip.py\` donde escribirás tu programa.

Puedes ejecutar lo siguiente para verificar tu código usando check50, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

```bash
check50 cs50/problems/2022/python/tip
```

## Como Entregar

En tu terminal, ejecuta el código de abajo para entregar tu trabajo.

```bash
submit50 cs50/problems/2022/python/tip
```
