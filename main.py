
while True:
    numero_informado = int(input("Digite um numero Par que tambem seja maior que 2 (0u 0 para encerrar o Programa) : "))

    if numero_informado == 0:
        print("Programa Encerrado, Obrigado!")
        break

    elif numero_informado <= 2 or numero_informado % 2 != 0:
        print("Informação Invalida, Digite um numero Par acima de 2:")
        continue

    for i in range(2, numero_informado):
        primo2 = True

        for m in range(2,numero_informado - i):
            if (numero_informado - i) % m == 0:
                primo2 = False
                break

        if primo2:
            print(f"Os dois números primos que somados deram {numero_informado} são: {i} + {numero_informado - i}")
            break
    continue