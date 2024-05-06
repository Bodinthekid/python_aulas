

def restaurante_yudi(num_items2):
    
    num_items2 = int(num_items2)
    
    cardapio = []

    for a in range(num_items2):
        refeições = {}
    
        key = "preço"
        value = input("Digite o valor do preço: ")
        key2 = "iten1"
        value2 = input("Digite o iten1: ")
        key3 = "iten2"
        value3 = input("Digite o iten2: ")
        key4 = "iten3"
        value4 = input("Digite o iten3: ")
        
        refeições[key] = value
        refeições[key2] = value2
        refeições[key3] = value3
        refeições[key4] = value4
        
        cardapio.append(refeições)

    for menu in cardapio:
        print(f'preço da refeiçao {menu}')

    meu_dinheiro = int(input("escolha um produto de acordo com o preço "))

    a = 'preço'

    for menu in cardapio:
        preço_menu = int(menu.get(a))

        if meu_dinheiro == preço_menu:
            output = (f'o lanche que voce escolheu e {menu}')
    
    return output

num_items2 = "2"

menu_escolhido = restaurante_yudi(num_items2)

print(menu_escolhido)


cardapio = [{'preço': '20','item1':'carne' , 'item2':'farofa' , 'item3':'batata'},
            {'preço': '15','item1':'frango' , 'item2':'alface' , 'item3':'maionese'},
            {'preço': '17','item1':'peixe' , 'item2':'vinagrete' , 'item3':'mandioca'}]
