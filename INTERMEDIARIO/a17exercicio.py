# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
quant_perg = 0
num_opcoes = 0

for pergunta in perguntas:
    quant_perg = quant_perg + 1
    print(pergunta['Pergunta'])
    print()
    print('Opções:')
    
    for i, opcao in enumerate(pergunta['Opções']):
          print(f"{i}) {opcao}")
          
    num_opcoes = len(pergunta['Opções'])
    print('Escolha uma opção:')
    escolha = input()
    escolha_int = None
    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None and escolha_int < num_opcoes:
        if(pergunta['Resposta'] == pergunta['Opções'][(escolha_int)]):
            acertos = acertos + 1
            print('Acertou :)')
        else:
            print('Errou :(')
    else:
        print('Digite somente um número das opções dadas!')
        break
        
        
print(f'Você acertou {acertos} perguntas de {quant_perg}!')
        