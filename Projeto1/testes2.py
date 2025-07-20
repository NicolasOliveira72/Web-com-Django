# Segunda parte dos códigos em linguagem python:

# Operações com texto;

texto = "Paralelepípido"
print(texto[0])
print(texto[2:8])
print(texto[-4])
print(texto[-6:-4])
print(texto[::2])
print()

# Tratando conflito de aspas simples e duplas:

frase = "Projeto em 'andamento'"
print(frase)
frase = 'Projeto em "andamento"'
print(frase)
frase = 'Projeto em \'andamento\''
print(frase)
frase = 'Projeto em' \
' andamento'
print(frase)
print()

# in e not in:

frase2 = "o projeto foi iniciado"
print(frase2.capitalize())

lisa = [144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0, 54, 46]
print(lisa[::-3])
num2 = len(lisa)
print(num2)
print(lisa.index(54))

# Estrutura de dicionário:

dicionario = {
    1 : "Projeto 1",
    2 : "Projeto 2",
    3 : "Projeto 3",
    4 : ["linguagem","python","progrmação"]
}
print(dicionario[2])
print(type(dicionario))
print(dicionario[4][2])

dicionario2 = dicionario.pop(3)
print()
print(dicionario2)
print(dicionario)
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

#  Interpolação de string com número: 

print()
carro = "fusca"
preco = 1000
print("carro: " + carro + " preço: " + str(preco))
print()
print("Carro: %s, preco: %d" % (carro, preco))
print()
print(f"Carro: {carro}, preco: {preco}")
