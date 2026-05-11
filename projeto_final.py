while True:
    print('========== MENU ==========')
    print('1 - Controle de Consumo de Água')
    print('2 - Sistema de Avaliação Acadêmica')
    print('3 - Controle de Estoque')
    print('4 - Simulador de Caixa Eletrônico')
    print('5 - Sistema de Controle de Vendas')
    print('6 - Sistema de Monitoramento de Temperatura')
    print('7 - Sistema de Login com Tentativas Limitadas')
    print('8 - Sair')
    servico = int(input('Selecione o Serviço Que Quer Realizar: '))
    if servico == 1:
        print('===== Controle de Consumo de Água =====')
        metro = int(input('Digite Quantos Metros Tem: '))
        if metro <= 10:
            valor =  20
        elif metro > 11 and metro <= 20:
            valor = 20 + ((metro - 10) * 2.5)
        elif metro > 20:
            valor = 20 + ((metro - 20) * 3.5) + (10 * 2.5)
        else:
            print('> Operação Invalida')
        print(f'> O valor à ser pago é R$ {valor:.2f}')

    elif servico == 2:
        print('===== Sistema de Avaliação Acadêmica =====')
        nota1 = int(input('Digite a Primeira Nota: '))
        nota2 = int(input('Digite a Segunda Nota: '))
        nota3 = int(input('Digite a Terceira Nota: '))

        def calcular_media():
            soma = (nota1 + nota2 + nota3) / 3
            return soma
        resultado = calcular_media()
        print('===== Sistema de Avaliação Acadêmica =====')
        print(f'> Sua média é: {resultado:.2f}')
        if calcular_media() >= 7:
            print('> Aprovado')
        elif calcular_media() >= 5 and calcular_media() < 7:
            print('> Recuperação')
        elif calcular_media() < 5:
            print('> Reprovado')
        else:
            print('> Digite as Notas Novamente')
    elif servico == 3:
        print('===== Controle de Estoque =====')
        estoque = []
        qnts_produtos = int(input('Digite Quantos Produtos Quer Inserir: '))
        for i in range(qnts_produtos):
            produto = input('Digite o Produto: ')
            quantidade = input('Digite a Quantidade do Produto: ')
            estoque.append((produto, quantidade))
            sair = input('Deseja Sair (S/N): ')
            if sair.upper() == 'S':
                break
        produto = produto.strip()
        produto = produto.lower()
        estoque.sort(reverse=True)
        print('===== Sistema De Estoque =====')
        for produto, quantidade in estoque:  
            print(f'> Produto: {produto.title()}')
            print(f'> Quantidade: {quantidade}')
            print('-' * 20)
        print(f'> O Produto com maior quantidade de estoque é: {estoque[0][0].title()} e a sua quantidade é: {estoque[0][1]}')
    elif servico == 4:
        print('===== Simulador de Caixa Eletrônico =====')
        valor = int(input("Digite o valor do saque: "))
        if valor % 10 != 0:
            print("> O valor deve ser múltiplo de 10.")
        else:
            notas100 = valor // 100
            valor %= 100

            notas50 = valor // 50
            valor %= 50

            notas20 = valor // 20
            valor %= 20

            notas10 = valor // 10
        print('===== Simulador de Caixa Eletrônico =====')
        print("> Notas entregues:")
        print(f"> 100: {notas100}")
        print(f"> 50: {notas50}")
        print(f"> 20: {notas20}")
        print(f"> 10: {notas10}")
    elif servico == 5:
        print('===== Sistema de Controle de Vendas =====')
        controle_vendas= []
        total_dinheiro = 0
        total_cartao = 0
        while True:
            venda = int(input('Digite O Valor Da Venda ou 0 Para Sair: '))
            if venda == 0:
                break
            pagamento = int(input('Digite Qual A Forma De Pagamento (1 - Dinheiro ou 2 - Cartão): '))
            controle_vendas.append(venda)
            if pagamento == 1:
                total_dinheiro += venda
            elif pagamento == 2:
                total_cartao += venda

        for venda in controle_vendas:
            total = sum(controle_vendas)
            qntd = len(controle_vendas)
            media = total // qntd

        print("===== Resumo do dia: =====")
        print("> Total vendido:", total)
        print("> Quantidade de vendas:", qntd)
        print("> Média das vendas:", media)
        print("> Total vendido em dinheiro:", total_dinheiro)
        print("> Total vendido em cartão:", total_cartao)
    
    elif servico == 6:
        print('===== Sistema de Monitoramento de Temperatura =====')
        conjunto_temperaturas = []
        while True:
            temperatura = int(input('Digite a temperatura: '))
            if temperatura == -1:
                break
            conjunto_temperaturas.append(temperatura)
        maximo = (max(conjunto_temperaturas))
        minimo = (min(conjunto_temperaturas))   
        for temperatura in conjunto_temperaturas:
            media = sum(conjunto_temperaturas) // len(conjunto_temperaturas)
        acima_80 = 0
        for t in conjunto_temperaturas:
            if t > 80:
                acima_80 += 1
        print('===== CLIMA TEMPO =====')
        print(f'> A Temperatura Maxima é {maximo}')
        print(f'> A Temperatura Mínima é {minimo}')
        print(f'> A Temperatura Média é {media}')
        print(f'> Quantidade de vezes acima de 80°C: {acima_80}')

    elif servico == 7:
        print('===== Sistema de Login com Tentativas Limitadas =====')
        for i in range(3):
            usuario = input('Digite seu Nome de Usuário: ')
            senha = input('Digite Sua Senha: ')

            if usuario == 'admin' and senha == '1234':
                print('> Acesso Permitido')
                break
            else:
                print('> Acesso Negado')
                if i == 2:
                    print('> Conta Bloqueada')

    elif servico == 8:
        print('> Saiu Do Programa')
        break
    else:
        print('> Digite o Número Do Serviço Corretamente')
        