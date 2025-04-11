# Criando uma lista
frutas = ["maçã", "banana", "laranja", "uva",]

# Acessando elementos da lista
print("Primeira fruta:", frutas[0])  # Índice 0
print("Última fruta:", frutas[-1])  # Índice -1 (último elemento)

# Adicionando elementos
frutas.append("manga")  # Adiciona no final
print("Lista após adicionar manga:", frutas)

# Removendo elementos
frutas.remove("banana")  # Remove pelo valor
print("Lista após remover banana:", frutas)

# Verificando se um elemento está na lista
if "uva" in frutas:
    print("Uva está na lista!")

# Percorrendo a lista com um loop
for fruta in frutas:
    print("Fruta:", fruta)

# Pegando o tamanho da lista
print("Número de frutas:", len(frutas))

# Ordenando a lista
frutas.sort()
print("Lista ordenada:", frutas)
