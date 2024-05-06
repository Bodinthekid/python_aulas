#Variáveis e Tipos de Dados em Python
#Variáveis: São espaços na memória reservados para armazenar valores. Em Python, as variáveis não precisam ser explicitamente declaradas e seus tipos são dinamicamente inferidos.

#Tipos de Dados:

#Números: Inteiros (int) e de ponto flutuante (float).
#Strings: Sequência de caracteres delimitada por aspas simples ('') ou duplas ("").
#Listas: Sequência mutável de elementos delimitada por colchetes ([]).
#Dicionários: Coleção não ordenada de pares chave-valor delimitada por chaves ({})

#Exemplos:
#python

# Números
idade = 25
altura = 1.75

# Strings
nome = "João"
sobrenome = 'Silva'

# Listas
numeros = [1, 2, 3, 4, 5]

# Dicionários
aluno = {'nome': 'Maria', 'idade': 20}

cidade1 = "londres"
cidade2 = "lisboa"
cidade3 = "brasilia"
cidade4 = "sao paulo"

endereço = {'cidades': cidade1, "rua":"gwtwtwt3e" , "numero": 22,
            'cidades': cidade2, "rua":"gwtwtwt3e" , "numero": 3,
            'cidades': cidade3, "rua":"gwtwtwt3e" , "numero": 12,
            'cidades': cidade4, "rua":"gwtwtwt3e" , "numero": 14
            }

#Operadores
#Operadores Aritméticos: São utilizados para realizar operações matemáticas.
#Operadores Relacionais: São utilizados para comparar valores.
#Operadores Lógicos: São utilizados para combinar condições.
#Exemplos:
# Operadores Aritméticos
soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 5
resto_divisao = 10 % 3

# Operadores Relacionais
igualdade = (5 == 5)
maior_que = (10 > 5)
menor_que = (3 < 8)
maior_igual = (10 >= 5)
menor_igual = (3 <= 8)
diferente = (0 != 8)

# Operadores Lógicos
and_operador = (True and False)
or_operador = (True or False)
not_operador = not True

#Controle de Fluxo
#Condicional (if-elif-else)
#Estrutura: A estrutura condicional if permite executar um bloco de código se uma condição for verdadeira. O elif (else if) permite verificar múltiplas condições em sequência. O else é executado caso nenhuma das condições anteriores seja verdadeira.
#Exemplo:

idade = 18
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 13:
    print("Você é um adolescente.")
else:
    print("Você é uma criança.")

#Loops (for e while)
#Loop for: Utilizado para iterar sobre uma sequência (por exemplo, uma lista) ou um intervalo de números.
#Loop while: Utilizado para repetir um bloco de código enquanto uma condição for verdadeira.
#Exemplos:
    
for numero in range(5):
    print(numero)

# Loop while
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    

#Exemplos Práticos
#Criando Programas Simples: Os exemplos práticos incluem a aplicação dos conceitos aprendidos para resolver problemas simples, como cálculos matemáticos, manipulação de strings, iteração sobre listas, entre outros.
#Exercícios Práticos: São propostos exercícios para que os alunos pratiquem e consolidem os conhecimentos adquiridos durante a aula.