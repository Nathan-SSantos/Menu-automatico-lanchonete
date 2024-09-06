# Constantes para os preços
PRECO_CARNE = 5.0
PRECO_FRANGO = 4.0
PRECO_VEGETARIANO = 4.0
PRECO_COCA_COLA = 4.0
PRECO_AGUA = 2.0
PRECO_SUCO_LIMAO = 3.0
PRECO_EXTRA = 1.0

# Inicialização das variáveis
valorSanduiche = 0.0
valorBebida = 0.0
quantExtra = 0
tipoSanduiche = ''
tipoBebida = ''
listaExtras = []

# Menu de sanduíches
print('1. Com carne - R$ 5,00\n2. Com frango - R$ 4,00\n3. Vegetariano - R$ 4,00')

# Loop até uma escolha válida para sanduíche
while True:
    try:
        escolhaSanduiche = int(input('\nQual vai querer? (somente número)\n'))

        if escolhaSanduiche == 1:
            valorSanduiche = PRECO_CARNE
            tipoSanduiche = 'de carne'
            break
        elif escolhaSanduiche == 2:
            valorSanduiche = PRECO_FRANGO
            tipoSanduiche = 'de frango'
            break
        elif escolhaSanduiche == 3:
            valorSanduiche = PRECO_VEGETARIANO
            tipoSanduiche = 'vegetariano'
            break
        else:
            print("Opção inválida. Escolha um número entre 1 e 3.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

# Loop até resposta válida para extra
while True:
    extra = input('\nVocê quer ingrediente extra? (s/n)\n').lower()

    if extra in ['s', 'n']:
        break
    else:
        print("Por favor, insira 's' para sim ou 'n' para não.")

# Se o usuário quiser extras, continua perguntando
while extra == 's':
    quantExtra += 1
    print('Aqui está o cardápio de extras, cada um custa R$ 1,00:')
    print('1. Batata palha\n2. Milho e ervilha\n3. Maionese caseira')

    try:
        escolhaExtra = int(input('Qual vai querer? (somente número)\n'))

        if escolhaExtra == 1:
            listaExtras.append('Batata palha')
        elif escolhaExtra == 2:
            listaExtras.append('Milho e ervilha')
        elif escolhaExtra == 3:
            listaExtras.append('Maionese caseira')
        else:
            print("Opção inválida! Escolha entre 1, 2 ou 3.")
            quantExtra -= 1
            continue

    except ValueError:
        print('Por favor, insira um número válido.')
        quantExtra -= 1
        continue

    # Verifica se o usuário quer mais extras
    while True:
        extra = input('\nQuer mais ingrediente extra? (s/n)\n').lower()

        if extra in ['s', 'n']:
            break
        else:
            print("Por favor, insira 's' para sim ou 'n' para não.")

# Menu de bebidas
print('\nAgora, aqui está o cardápio de bebidas:')
print('1. Lata de coca-cola - R$ 4,00\n2. Água sem gás - R$ 2,00\n3. Suco de limão - R$ 3,00')

# Loop até uma escolha válida para bebida
while True:
    try:
        escolhaBebida = int(input('\nQual vai querer? (somente número)\n'))

        if escolhaBebida == 1:
            valorBebida = PRECO_COCA_COLA
            tipoBebida = 'coca-cola'
            break
        elif escolhaBebida == 2:
            valorBebida = PRECO_AGUA
            tipoBebida = 'água sem gás'
            break
        elif escolhaBebida == 3:
            valorBebida = PRECO_SUCO_LIMAO
            tipoBebida = 'suco de limão'
            break
        else:
            print("Opção inválida. Escolha um número entre 1 e 3.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

# Cálculo da conta
conta = valorSanduiche + (quantExtra * PRECO_EXTRA) + valorBebida

# Exibição do pedido e valor total
print('\nObrigado! Aqui está o seu pedido:')
print(f'Sanduíche: {tipoSanduiche}')
print(f'Bebida: {tipoBebida}')
print(f'Quantidade de extras: {quantExtra}')

# Exibe os extras escolhidos
if listaExtras:
    print(f'Extras escolhidos: {", ".join(listaExtras)}')

print(f'\nValor da conta: R$ {conta:.2f}')
