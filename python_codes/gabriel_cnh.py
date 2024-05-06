


idade = 17
possui_cnh = True
if idade >= 18 and possui_cnh:
    print("pode seguir viagem")
else:
    print("desca do carro pfv")


dinheiro = 20
combo1 = {'carne' , 'farofa' , 'batata'}
combo2 = {'frango' , 'alface' , 'maionese'}
combo3 = {'peixe' , 'vinagrete' , 'mandioca'}
if dinheiro == 10:
    print('quero o combo1')
if dinheiro == 15 :
    print('quero o combo3')
if dinheiro == 20 :
    print('quero o combo2')

#exemplo 1
velocidade = 200
if velocidade <= 120 :
    print('velocidade dentro do limite')
elif velocidade > 120  and velocidade < 200:
    print('voçe ultrapassou o limite')
else:
    print ('preso em nome da lei')

#exemplo 2
velocidade = 100
if velocidade <= 120 :
    print ('velocidade dentro do limite')
elif velocidade > 120 :
    print ('voçe ultrapassou o limite')
elif velocidade >= 200 :
    print ('preso em nome da lei')

#exemplo 3
frase = "O gabriel pediu meu carro emprestado ontem de noite"
if "dia" in frase:
    print("44444")
elif "noite" in frase:
    print("55555")
elif "o" in frase:
    print("66666")