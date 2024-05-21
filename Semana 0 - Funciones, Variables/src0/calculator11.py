# Demuestra definir una funcion con un valor de retorno

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
