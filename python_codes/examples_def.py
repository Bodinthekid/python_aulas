

def calcular_media(lista):
    total = sum(lista)
    media = total / len(lista)
    return media

lista = [12,14]
resultado_media = calcular_media(lista)
print(resultado_media)


#########################################

def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = int(input("qual numero voce quer verificar a paridade "))
resultado_paridade = verificar_paridade(numero)
print(resultado_paridade)
    
#########################################
    
def imprime_nome(nome):
    print(f"Nome: {nome}")

imprime_nome("Erickson")
imprime_nome("Renan")
imprime_nome("Daniel")

########################################

def area(base, altura):

    area = base * altura

    print(area)

    return area

base = int(input("qual a base? "))
altura = int(input("qual a altura? "))

area(base,altura)

#######################################

def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    print(fahrenheit)
    return fahrenheit

celsius_para_fahrenheit(float(input("2 qual e a temperatura em *C? ")))