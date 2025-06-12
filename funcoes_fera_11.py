import random
import matplotlib.pyplot as plt
from colour import Color

###############################################################################
#                                   Caixeiro                                  #
###############################################################################


def cria_cidades(n, xy_minimo=0, xy_maximo=300):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
      n: Número de cidades que serão visitadas pelo caixeiro.
      xy_minimo: Valor mínimo possível das coordenadas x e y.
      xy_maximo: Valor máximo possível das coordenadas x e y.

    """
    cidades = {}
    num_digitos = len(str(abs(n)))

    for i in range(n):
        cidades[i] = (
            random.randint(xy_minimo, xy_maximo),
            random.randint(xy_minimo, xy_maximo),
        )

    return cidades


def plota_cidades(cidades):
    """Plota as cidades do problema do caixeiro viajante

    Nota: código de base criado pelo Google Gemini e modificado aqui.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    x = [cidades[cidade][0] for cidade in cidades]
    y = [cidades[cidade][1] for cidade in cidades]
    
    # plotando as cidades
    plt.scatter(x, y, color="blue")

    # nomes das cidades
    for cidade, (x, y) in cidades.items():
        plt.annotate(
            cidade,
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    plt.xlabel("Coordenada x")
    plt.ylabel("Coordenada y")
    plt.show()
    
    
def plota_trajeto(cidades, trajeto):
    """Plota o trajeto do caixeiro

    Nota: código de base criado pelo Google Gemini e modificado aqui.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      trajeto: lista contendo a ordem das cidades que foram viszitadas

    """
    x = [cidades[cidade][0] for cidade in cidades]
    y = [cidades[cidade][1] for cidade in cidades]

    # plotando as cidades
    plt.scatter(x, y, color="blue")

    # nomes das cidades
    for cidade, (x, y) in cidades.items():
        plt.annotate(
            cidade,
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    # plotando os trajetos
    for i in range(len(trajeto) - 1):
        cidade1 = trajeto[i]
        cidade2 = trajeto[i + 1]
        plt.plot(
            [cidades[cidade1][0], cidades[cidade2][0]],
            [cidades[cidade1][1], cidades[cidade2][1]],
            color="red",
        )

    # trajeto de volta à cidade inicial
    cidade1 = trajeto[-1]
    cidade2 = trajeto[0]
    plt.plot(
        [cidades[cidade1][0], cidades[cidade2][0]],
        [cidades[cidade1][1], cidades[cidade2][1]],
        color="red",
    )

    plt.xlabel("Coordenada x")
    plt.ylabel("Coordenada y")
    plt.show()


def dist_euclidiana(coord1, coord2):
    """Computa a distância Euclidiana entre dois pontos em R^2

    Args:
      coord1: lista contendo as coordenadas x e y de um ponto.
      coord2: lista contendo as coordenadas x e y do outro ponto.

    """
    x1 = coord1[0]
    x2 = coord2[0]
    y1 = coord1[1]
    y2 = coord2[1]

    distancia = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return distancia


def cria_candidato_caixeiro(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    nomes_cidades = list(cidades.keys())
    caminho = random.sample(nomes_cidades, k=len(nomes_cidades))
    return caminho


def populacao_caixeiro(tamanho_populacao, cidades):
    """Cria uma população no problema do caixeiro viajante

    Args:
      tamanho_populacao: tamanho da população.
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_caixeiro(cidades))

    return populacao


def funcao_objetivo_caixeiro(candidato, cidades):
    """Funcao objetivo de um candidato no problema do caixeiro viajante

    Args:
      candidato: uma lista contendo o caminho percorrido
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    distancia = 0

    for pos in range(len(candidato) - 1):
        coord_cidade_partida = cidades[candidato[pos]]
        coord_cidade_chegada = cidades[candidato[pos + 1]]
        distancia += dist_euclidiana(
            coord_cidade_partida, coord_cidade_chegada
        )

    # distância para retornar à cidade inicial
    coord_cidade_final = cidades[candidato[-1]]
    coord_cidade_inicial = cidades[candidato[0]]
    distancia += dist_euclidiana(coord_cidade_final, coord_cidade_inicial)

    return distancia


def funcao_objetivo_pop_caixeiro(populacao, cidades):
    """Funcao objetivo de uma populacao no problema do caixeiro viajante

    Args:
      populacao: lista contendo os individuos do problema
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_caixeiro(individuo, cidades))

    return fitness


###############################################################################
#                                Caixeiro Ímpar                               #
###############################################################################


def cria_cidades_impar(n, xy_minimo=0, xy_maximo=300):
    """Cria um dicionário aleatório de cidades com suas posições (x,y), com a chave do docionário sendo um número inteiro.

    Args:
      n: Número de cidades que serão visitadas pelo caixeiro.
      xy_minimo: Valor mínimo possível das coordenadas x e y.
      xy_maximo: Valor máximo possível das coordenadas x e y.

    """
    cidades = {}

    for i in range(n):
        cidades[i] = (
            random.randint(xy_minimo, xy_maximo),
            random.randint(xy_minimo, xy_maximo),
        )

    return cidades


def calc_min_idx_par(cidades):
    """Calcula o índice do dicionário a partir do qual todas as cidades são pares.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    min_idx_par = len(list(cidades.keys()))//2 + 1
    return min_idx_par
    
    
def cria_candidato_caixeiro_impar(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante que prefere cidades ímpares.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    
    caminho_0 = [0]

    cidades_menos0 = list(cidades.keys())
    cidades_menos0.remove(0)
    
    caminho_menos0 = random.sample(cidades_menos0, k=len(cidades_menos0))
    
    caminho_impar = [i for i in caminho_menos0 if i%2 != 0]
    caminho_par = [i for i in caminho_menos0 if i%2 == 0]
   
    caminho = caminho_0 + caminho_impar + caminho_par
    
    return caminho


def populacao_caixeiro_impar(tamanho_populacao, cidades):
    """Cria uma população no problema do caixeiro viajante que prefere cidades ímpares.

    Args:
      tamanho_populacao: tamanho da população.
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_caixeiro_impar(cidades))

    return populacao



###############################################################################
#                              Múltiplos Caixeiro                             #
###############################################################################


def plota_multiplos_trajetos(cidades, individuo):
    """Plota os trajetos dos caixeiros no problema dos múltiplos caixeiros viajantes.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      individuo: lista contendo listas, cada uma representando um trajeto contendo a ordem das cidades que foram visitadas.

    """
    x = [cidades[cidade][0] for cidade in cidades]
    y = [cidades[cidade][1] for cidade in cidades]

    # plotando as cidades
    plt.scatter(x, y, color="blue")

    # nomes das cidades
    for cidade, (x, y) in cidades.items():
        plt.annotate(
            cidade,
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    cor1 = Color("royalblue")
    cor2 = Color("pink")

    color_range = list(cor1.range_to(cor2, len(individuo)))

    for trajeto, cor in zip(individuo, color_range):
        # plotando os trajetos
        for i in range(len(trajeto) - 1):
            cidade1 = trajeto[i]
            cidade2 = trajeto[i + 1]
            plt.plot(
                [cidades[cidade1][0], cidades[cidade2][0]],
                [cidades[cidade1][1], cidades[cidade2][1]],
                color=cor.hex,
            )

    # trajeto de volta à cidade inicial
    cidade1 = trajeto[-1]
    cidade2 = trajeto[0]
    plt.plot(
        [cidades[cidade1][0], cidades[cidade2][0]],
        [cidades[cidade1][1], cidades[cidade2][1]],
        color="red",
    )

    plt.xlabel("Coordenada x")
    plt.ylabel("Coordenada y")
    plt.show()



def converte_para_total(candidato_original):
    """Transforma uma lista de listas em uma lista corrida, mantendo a ordem de aparição dos elementos.

    Args:
      candidato_original: lista contendo listas, cada uma representando um trajeto contendo a ordem das cidades que foram visitadas.

    """

    candidato_total = [cidade for caminho in candidato_original for cidade in caminho]
    ultimas_cidades = [caminho[-1] for caminho in candidato_original]
    indices_original = [candidato_total.index(cidade) for cidade in ultimas_cidades]

    return candidato_total, indices_original


def desconverte_de_total(candidato_total, indices_original):
    """Transforma uma lista corrida em uma lista de listas, baseando-se no índice em que cada lista interna termina.

    Args:
      candidato_total: lista contendo a ordem das cidades que foram visitadas.
      indices_original: lista contendo o índice em que cada lista interna deve terminar.

    """
    
    novo = []

    aux = 0
    for i in indices_original:
        novo.append(candidato_total[aux:i+1])
        aux = i+1

    return novo


def sorteia_num_cidades(valor_max):
    """Sorteia um número de cidades a ser percorrido por um caixeiro no problema dos múltiplos caixeiros viajantes.
    
    Args:
      valor_max: número máximo de cidade que um caixeiro pode visitar.
    """
    
    valores_possiveis = range(1, valor_max + 1)
    gene = random.choice(valores_possiveis)
    return gene


def calc_n_cidades_multiplos_cx(cidades, n_caixeiros):
    """Calcula o número de cidades percorrida por cada caixeiro no problema dos múltiplos caixeiros viajantes.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      n_caixeiros: inteiro que representa o número de caixeiros do problema.
    """
    cidade_por_caixeiro = []

    n_cidades = len(cidades)
    aux_max = n_cidades - n_caixeiros + 1

    for i in range(n_caixeiros):
        if i == n_caixeiros - 1:
            cidade_por_caixeiro.append(n_cidades - sum(cidade_por_caixeiro))
            break

        gene = sorteia_num_cidades(aux_max)
        cidade_por_caixeiro.append(gene)

        aux_max -= (gene + 1)
        if aux_max < 1:
            aux_max = 1

    return cidade_por_caixeiro


def cria_candidato_multiplos_cx(cidades, n_caixeiros):
    """Sorteia os caminhos possíveis para cada caixeiro no problema dos múltiplos caixeiros viajantes

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      n_caixeiros: inteiro que representa o número de caixeiros do problema.
    """
    
    cidades_por_caixeiro = calc_n_cidades_multiplos_cx(cidades, n_caixeiros)

    candidato = []
    cidades_disponiveis = list(cidades.keys()).copy()

    for ccx in cidades_por_caixeiro:
        caminho = random.sample(cidades_disponiveis, k=ccx)
        candidato.append(caminho)
        for cidade in caminho:
            cidades_disponiveis.remove(cidade)

    return candidato


def populacao_multiplos_cx(tamanho_populacao, cidades, n_caixeiros):
    """Cria uma população no problema do caixeiro viajante que prefere cidades ímpares.

    Args:
      tamanho_populacao: tamanho da população.
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      n_caixeiros: inteiro que representa o número de caixeiros do problema.
    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_multiplos_cx(cidades, n_caixeiros))

    return populacao


def funcao_objetivo_cx(caminho, cidades):
    """Funcao objetivo de um caixeiro no problema do caixeiro viajante

    Args:
      caminho: uma lista contendo o caminho percorrido
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no plano cartesiano das cidades como valores.

    """
    distancia = 0

    for pos in range(len(caminho) - 1):
        coord_cidade_partida = cidades[caminho[pos]]
        coord_cidade_chegada = cidades[caminho[pos + 1]]
        distancia += dist_euclidiana(
            coord_cidade_partida, coord_cidade_chegada
        )

    # distância para retornar à cidade inicial
    coord_cidade_final = cidades[caminho[-1]]
    coord_cidade_inicial = cidades[caminho[0]]
    distancia += dist_euclidiana(coord_cidade_final, coord_cidade_inicial)

    return distancia


def funcao_objetivo_multiplos_cx(candidato, cidades):
    """Funcao objetivo de um caixeiro no problema dos múltiplos caixeiros viajantes

    Args:
      candidato: uma lista de listas contendo o caminho percorrido por cada caixeiro
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    
    distancia = 0

    for caminho in candidato:
        distancia += funcao_objetivo_cx(caminho, cidades)

    return distancia


def funcao_objetivo_pop_multiplos_cx(populacao, cidades):
    """Funcao objetivo de uma populacao no problema dos múltiplos caixeiros viajantes

    Args:
      populacao: lista contendo os individuos do problema
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_multiplos_cx(individuo, cidades))

    return fitness



###############################################################################
#                                   Seleção                                   #
###############################################################################


def selecao_torneio_min(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de invíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        min_fitness = min(fitness_sorteados)
        indice_min_fitness = fitness_sorteados.index(min_fitness)
        individuo_selecionado = sorteados[indice_min_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


def cruzamento_ordenado(pai, mae, chance_de_cruzamento):
    """Cruzamento ordenado entre dois individuos

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        tamanho_individuo = len(mae)

        # pontos de corte
        corte1 = random.randint(0, tamanho_individuo - 2)
        corte2 = random.randint(corte1 + 1, tamanho_individuo)

        # filho1
        filho1 = [None] * tamanho_individuo
        filho1[corte1:corte2] = mae[corte1:corte2]
        pai_ = pai[corte2:] + pai[:corte2]
        posicao = corte2 % tamanho_individuo
        for valor in pai_:
            if valor not in filho1:
                filho1[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo

        # filho2
        filho2 = [None] * tamanho_individuo
        filho2[corte1:corte2] = pai[corte1:corte2]
        mae_ = mae[corte2:] + mae[:corte2]
        posicao = corte2 % tamanho_individuo
        for valor in mae_:
            if valor not in filho2:
                filho2[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo

        return filho1, filho2
    else:
        return pai, mae


def cruzamento_ordenado_intervalos(pai, mae, chance_de_cruzamento, cidades):
    """Cruzamento ordenado entre dois individuos dividido em dois intervalos (ímpares e pares) para o problema do caixeiro viajante que prefere cidades ímpares.
 
    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
 
    """
    if random.random() < chance_de_cruzamento:
        min_idx_par = calc_min_idx_par(cidades)
 
        mae_impar = mae[1:min_idx_par]
        pai_impar = pai[1:min_idx_par]
 
        mae_par = mae[min_idx_par:]
        pai_par = pai[min_idx_par:]
 
        filho1_impar, filho2_impar = cruzamento_ordenado(pai_impar, mae_impar, 1)
        filho1_par, filho2_par = cruzamento_ordenado(pai_par, mae_par, 1)
 
        filho1 = [0] + filho1_impar + filho1_par
        filho2 = [0] + filho2_impar + filho2_par
        return filho1, filho2
    else:
        return pai, mae
    

def cruzamento_ordenado_multiplos_cx(pai, mae, chance_de_cruzamento):
    """Cruzamento ordenado entre dois individuos no problema dos múltiplos caixeiros viajantes.

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:

        pai_total, indices_pai = converte_para_total(pai)
        mae_total, indices_mae = converte_para_total(mae)

        filho1_total, filho2_total = cruzamento_ordenado(pai_total, mae_total, 1)

        filho1 = desconverte_de_total(filho1_total, indices_pai)
        filho2 = desconverte_de_total(filho2_total, indices_mae)

        return filho1, filho2
    else:
        return pai, mae


###############################################################################
#                                   Mutação                                   #
###############################################################################


def mutacao_troca(populacao, chance_de_mutacao):
    """Aplica mutacao de troca em um indivíduo

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene1 = random.randint(0, len(individuo) - 1)
            gene2 = random.randint(0, len(individuo) - 1)

            while gene1 == gene2:
                gene1 = random.randint(0, len(individuo) - 1)
                gene2 = random.randint(0, len(individuo) - 1)

            individuo[gene1], individuo[gene2] = (
                individuo[gene2],
                individuo[gene1],
            )

def mutacao_troca_cx_impar(populacao, chance_de_mutacao, cidades):
    """Aplica mutacao de troca em um indivíduo no problema do caixeiro viajante que prefere cidades ímpares.

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
    """
    
    min_idx_par = calc_min_idx_par(cidades)
    
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene1 = random.randint(1, len(individuo) - 1)
            if gene1 < min_idx_par:
                gene2 = random.randint(1, min_idx_par - 1)
            else:
                gene2 = random.randint(min_idx_par, len(individuo) - 1)
                
            while gene1 == gene2:
                gene1 = random.randint(1, len(individuo) - 1)
                gene2 = random.randint(1, len(individuo) - 1)
                
                if gene1 < min_idx_par:
                    gene2 = random.randint(1, min_idx_par - 1)
                else:
                    gene2 = random.randint(min_idx_par, len(individuo) - 1)

            individuo[gene1], individuo[gene2] = (
                individuo[gene2],
                individuo[gene1],
            )


def mutacao_troca_multiplos_cx(populacao, chance_de_mutacao):
    """Aplica mutacao de troca em um indivíduo no problema dos múltiplos caixeiros viajantes.

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """    
    for individuo in populacao:
        if random.random() < chance_de_mutacao:

            individuo_total, indices_individuo = converte_para_total(individuo)

            gene1 = random.randint(0, len(individuo_total) - 1)
            gene2 = random.randint(0, len(individuo_total) - 1)

            while gene1 == gene2:
                gene1 = random.randint(0, len(individuo_total) - 1)
                gene2 = random.randint(0, len(individuo_total) - 1)

            individuo_total[gene1], individuo_total[gene2] = (
                individuo_total[gene2],
                individuo_total[gene1],
            )

            individuo = desconverte_de_total(individuo_total, indices_individuo)
    

def mutacao_tamanho(populacao, chance_de_mutacao):
    """Aplica mutacao que altera o tamanho do trajeto de dois caixeiros em uma cidade no problema dos múltiplos caixeiros viajantes.

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:

            individuo_total, indices_individuo = converte_para_total(individuo)

            sorteado = random.choice(indices_individuo[:-1])
            if random.random() < 0.5:
                # diminue
                while sorteado == indices_individuo[indices_individuo.index(sorteado) - 1] - 1:
                    sorteado = random.choice(indices_individuo[:-1])
                novo_indice = sorteado - 1
            else:
                #aumenta
                while sorteado == indices_individuo[indices_individuo.index(sorteado) + 1] + 1:
                    sorteado = random.choice(indices_individuo[:-1])
                novo_indice = sorteado + 1

            indices_individuo[indices_individuo.index(sorteado)] = novo_indice

            individuo = desconverte_de_total(individuo_total, indices_individuo)