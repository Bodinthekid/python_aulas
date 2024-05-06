#from menu import restaurante_yudi
from examples_def import calcular_media,verificar_paridade,imprime_nome,area,celsius_para_fahrenheit

#num_items2 = "2"

#menu_escolhido = restaurante_yudi(num_items2)

#print(menu_escolhido)

lista = [12,14]
resultado_media = calcular_media(lista)
print(resultado_media)

numero = int(input("qual numero voce quer verificar a paridade "))
resultado_paridade = verificar_paridade(numero)
print(resultado_paridade)

imprime_nome("Erickson")
imprime_nome("Renan")
imprime_nome("Daniel")

base = int(input("qual a base? "))
altura = int(input("qual a altura? "))

area(base,altura)

celsius_para_fahrenheit(float(input("2 qual e a temperatura em *C? ")))
