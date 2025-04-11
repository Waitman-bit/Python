num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
cont = input("Digite qual conta quer fazer: ")

if cont == "adição" or cont == "adiçao":
    print("A soma é:", num1 + num2)
elif cont == "subtração" or cont == "subtraçao":
      print("A subtração é:", num1 - num2)
elif cont == "multiplicação" or cont == "multiplicaçao":
      print("A multiplicação é:", num1 * num2)
elif cont == "divisão" or cont == "divisao":
      print("A divisão é:", num1 / num2)
else:
    print("Operação inválida!")
