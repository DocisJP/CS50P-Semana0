# Demuestra formateo con comas (para mas información: buscar la documentación de float)

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")
