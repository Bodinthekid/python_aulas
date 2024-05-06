import time

lampada = input("a lampada esta funcionando? sim/nao* ")
altura_lampada = 2.50

if lampada == "sim":
    time.sleep(1)
    print("a lampada esta funcionando")
    time.sleep(1)
    print("a lampada nao precisa ser trocada")
    time.sleep(1)
else:
    time.sleep(1)
    print("a lampada precisa ser trocada")
    time.sleep(1)
    
    nossa_altura = float(input("qual e a sua altura? coloque em decimal usando ponto* "))

    if nossa_altura >= altura_lampada:
        time.sleep(1)
        print("nao precisamos de pegar nada para dar altura")
        time.sleep(1)
        print("desenroscando a lampada")
        time.sleep(1)
        print("trocando a lampada")
        time.sleep(1)
        print("lampada trocada")
        time.sleep(1)
        print("lampada funciona")
        time.sleep(1)
    else:
        print("precisamos de pegar alguma coisa para dar altura")
        time.sleep(1)
        print("desenroscando a lampada")
        time.sleep(1)
        print("trocando a lampada")
        time.sleep(1)
        print("lampada trocada") 
        time.sleep(1)
        print("lampada funciona") 
        time.sleep(1)

