# Funcion para saber si un numero es primo o no
def primo(num, n=2):
    if num % n == 0:
        print("No es primo")
    else:
        print("Es primo")

# Funcion fibonachi


def fibona(n):
    if n > 1:
        return fibona(n-1) + fibona(n-2)
    return n

# Funcion par o impar


def par_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Impar"

# separar

# imprimir los gitos


def dig(n):

    return [int(a) for a in str(n)]


# 50 iteraciones
for i in range(50):
    number = fibona(i)
    print(f"({i})", number, par_impar(number),
          primo(number), dig(number))

# for i in range(50):
#     print(fibona(i), primo(i), par_impar(i), dig(i))
