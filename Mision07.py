#Bruno Omar Jimenez Mancilla
#Un programa que despliega un menu que deja hacer disitntas funciones

def dividir(dividendo,divisor):
    residuo = dividendo
    div = 0
    while residuo >= divisor:
        residuo -= divisor
        div += 1
    return div


def encontrarMayor():
    n = 0
    z = 0
    while n != -1:
        n = int(input("Teclea un número entero positivo: [Presiona -1 para salir]"))
        if n <= 0:
            print("Este valor es inválido")
            if n >= z:
                z = n
    print("el mayor es: ",z)
    input("Preiona cualquier tecla para continuar...")

def main():
    x = -1
    while x != 3:
        print("Mision 07. Ciclos While")
        print("Autor: Bruno Omar Jimenez Mancilla")
        print("A01748931")
        print("1. Dividir           ")
        print("2. Encontrar el mayor")
        print("3. Salir             ")
        x = int(input("¿Que deseas hacer? "))
        if x == 1:
            dividendo = int(input("Teclea el numero de deseas dividir: "))
            divisor = int(input("Teclea el divisor: "))
            div = dividir(dividendo,divisor)
            res = dividendo - (div*divisor)
            print(div, ", sobra ",res)
            input("Preiona cualquier tecla para continuar...")
        elif x == 2:
            encontrarMayor()
        elif x == 3:
            print("Gracias por usar este programa, regresa pronto! :)")
        else:
            print(x," es un valor inválido")
            input("Presiona cualquier tecla para regresar al menú")


main()