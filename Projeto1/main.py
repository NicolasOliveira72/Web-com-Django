# Primeiros códigos em python:

# Função para imrimir uma variável que foi mudada o tipo

idade = 30
idade = "Projeto"
def imprimir():
    print(idade)
imprimir()
print()



# perador lógico:

print(False and True)
print()


#Estrutura condicional if, else e elif, para calcular o desconto:

compra = 450
if compra < 200:
        print("Sem desconto")
elif compra >= 200 and compra < 300:
        print("Desconto 1")
elif compra >= 300 and compra < 400:
        print("Desconto 2")
else:
        print("Desconto 3")
print()



# Operador ternário:

idade = 20
resultado = ('Falso','Verdadeiro')[idade>30]
print(resultado)
print()


# Visualizando recursos do python:

print(dir())


