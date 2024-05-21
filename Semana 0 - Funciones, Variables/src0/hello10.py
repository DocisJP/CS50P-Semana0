# Demuestra definir una funcion con un parametro con un valor default


def hello(to="world"):
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)
