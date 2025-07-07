from nps import Nps

print('--- Pesquisa de Satisfação ---')

pesquisa_nps = Nps()

while True:
    nota = input(
        'Em uma escala de 0 a 10, o quanto você recomendaria nossa empresa a um amigo ou colega?\n'
        'Digite "sair" para encerrar a pesquisa: '
    )
    
    if nota.lower() == 'sair':
        break
    
    try:
        valor = int(nota)
        pesquisa_nps.adicionar_nota(valor)
    except ValueError:
        print('Entrada inválida! Por favor, digite um número inteiro de 0 a 10 ou "sair".')

print(f'\nTotal de respostas: {len(pesquisa_nps)}')
print(f'NPS calculado: {pesquisa_nps.calcular_nps()}')
print(f'Classificação: {pesquisa_nps.avaliar_classificacao()}')
