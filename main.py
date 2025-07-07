from nps import Nps

if __name__ == '__main__':
    print('📊 Rodando teste do NPS')
    avaliacao = Nps()

    notas_exemplo = [8, 9, 7, 8, 9, 8, 9, 10, 8, 9]
    for nota in notas_exemplo:
        avaliacao.adicionar_nota(nota)

    print(f"NPS calculado: {avaliacao.calcular_nps()}")
    print(f"Classificação: {avaliacao.avaliar_classificacao()}")
    print(f"Quantidade de avaliações: {len(avaliacao)}")
    print(avaliacao)
    print(repr(avaliacao))
