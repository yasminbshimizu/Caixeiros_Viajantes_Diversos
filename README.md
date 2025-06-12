<div align="center">
  <img src="https://github.com/user-attachments/assets/ccb6f5f1-0e07-4eb2-aa7c-5f681c57a59c" alt="Descrição da imagem" width="1000"/>
</div>

<h1 align="center">Caixeiros Viajantes Diversos 📦</h1>

<h3 align="center">Resolução do problema do Caixeiro Viajante que prefere cidades ímpares e do problema dos múltiplos Caixeiros Viajantes com algoritimos genéticos</h3>

<p align="center"><strong>Autores:</strong> Vítor Gabriel Dreveck e Yasmin Barbosa Shimizu</p>
<p align="center"><strong>Orientador:</strong> Prof. Dr. Daniel R. Cassar</p>

<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

## 📝 Descrição

O problema do **caixeiro viajante** é um clássico problema de otimização combinatória com complexidade NP-difícil estudada, principalmente, por cientistas da computação. É dado pelo enunciado "Dada uma lista de cidades e as distâncias entre cada par de cidades, qual é a rota mais curta possível que visita cada cidade exatamente uma vez e retorna à cidade de origem?"[2], e sua resolução pode ser aplicada, por exemplo, a logística, encontrando as rotas mais curtas para distibuição de mercadoria e, assim, minimizando os custos operacionais. [1][2] Uma das abordagens computacionais possíveis para a resolução do problema do caixeiro viajante é a construção de algoritmos genéticos, que buscam otimizar problemas complexos baseando-se na teoria da evolução de Darwin, com operadores de seleção, cruzamento e mutação. [1]

Neste trabalho, buscamos trazer diferentes abordagens para a resolução do problema do caixeiro viajante e resolvê-las utilizando algoritmos genéticas. Essas abordagens foram: 

* **Caixeiro viajante que prefere cidades ímpares:** Qual o caminho de menor distância no problema do caixeiro viajante, com a peculiaridade de passar primeiro pelas cidades de índice ímpar? Considere que, além das condições tradicionais do problema, o caixeiro sempre começa na cidade de índice zero, passa por todas as cidades ímpares, e só então percorre pelas cidades pares, retornando à cidade zero no fim do trajeto.

* **Múltiplos caixeiros viajantes:** Qual o caminho de menor distância no problema do caixeiro viajante, com a peculiaridade de existir mais de um caixeiro? Considere que, além das condições tradicionais do problema, cada caixeiro passa por pelo menos uma cidade, começa em uma cidade diferente e jamais visita cidades já visitadas por outros caixeiros.
  
## 📔 Notebooks, scripts e arquivos do projeto
* `Fera_Formidavel_10.ipynb`: otimização do problema do caixeiro viajante que prefere cidades ímpares através de um algoritmo genético.
* `Fera_Formidavel_11.ipynb`: otimização do problema dos múltiplos caixeiros viajantes através de um algoritmo genético.
* `funcoes_caixeiros.py`: script com as funções construídas, necessárias para a evolução dos algoritmos genéticos.
* `README.md`: descrição geral do projeto.
  
## 🖇️ Informações técnicas
* Linguagem de programação: `Python 3.9`
* Software:  `Jupyter Notebook`, `Visual Studio Code`
* Bibliotecas e Módulos: `random`, `matplotlib.pyplot`, `colour`, `pprint`, `functools`, `itertools`

### Como executar o algoritmo?
Os algoritmos genéticos desenvolvidos neste trabalho podem ser executados em compiladores de Python como Jupyter Notebook, Visual Studio Code e Google Colab. Para tal, é necessário:
1. A instalação das bibliotecas citadas acima, utilizando, por exemplo, o método `!pip install <nome_da_biblioteca>`;
2. O download do *script* `funcoes_caixeiro.py` e do notebook que se deseja executar (`Fera_Formidavel_10` ou `Fera_Formidavel_11`) no mesmo diretório;
3. Execução do notebook em um compilador de Python.
   
## 🧬 Construindo e evoluindo o algoritmo genético

Para a otimização dos problemas, nos baseamos no algoritmo desenvolvido pelo Prof. Dr. Daniel Cassar para o problema tradicional do caixeiro viajante, fazendo as adaptações necessárias de acordo com o objetivo de cada problema. Assim, as funções alteradas foram:

* **Caixeiro viajante que prefere cidades ímpares:**
  - `cria_cidades_impar`, `cria_candidato_caixeiro_impar`, `populacao_caixeiro_impar`: criam cidades, candidato e população do problema de acordo com um índice numérico inteiro;
  - `calc_min_inx_par`: calcula o índice em que a primeira cidade de índice par aparece num candidato;
  - `cruzamento_ordenado_intervalos`: realiza o cruzamento ordenado em diferentes intervalos --- nesse caso, uma lista contendo os índices ímpares, e uma contendo os índices pares;
  - `mutacao_troca_cx_impar`: realiza a mutação de troca entre elementos de mesma paridade.

* **Múltiplos caixeiros viajantes:**
  - `plota_trajeto_multiplos_cx`: plota o trajetos de múltiplos caixeiros viajantes simultaneamente;
  - `calc_n_cidades_multiplos_cx`: calcula o número de cidades que cada caixeiro pode visitar dentre as possíveis, considerando que todos os caixeiros passam por pelo menos uma cidade;
  - `cria_candidato_multiplos_cx`, `populacao_multiplos_cx`: criam o candidato e a população do problema, considerando múltiplos caixeiros em cada indivíduo;
  - `funcao_objetivo_multiplos_cx`, `funcao_objetivo_pop_multiplos_cx`: calcula a somatória das distâncias percorridas por todos os caixeiros em seus respectivos trajetos, para um individuo e uma população;
  - `cruzamento_ordenado_multiplos_cx`: realiza o cruzamento ordenado para uma lista de listas --- cruzando cada elemento interna em ordem e mantendo o tamanho das listas dos pais;
  - `mutacao_troca_multiplos_cx`: aplica mutação de troca entre duas cidades no problema;
  - `mutacao_tamanho`: aplica uma mutação que altera o tamanho do trajeto de dois caixeiros em uma cidade.


## 🔢 Resultados Obtidos

* **Caixeiro viajante que prefere cidades ímpares:**

* **Múltiplos caixeiros viajantes:**
  

## 😁 Conclusão


## 📚 Referências

[1] Aulas da disciplina ATP-303 Redes Neurais e Algoritmos Genéticos, ministradas pelo Prof. Dr. Daniel R. Cassar na Ilum Escola de Ciência.

[2] WIKIPEDIA. Travelling salesman problem. Disponível em: https://en.wikipedia.org/wiki/Travelling_salesman_problem. Acesso em: 12 jun. 2025.

## 🧠 Contribuições dos Colaboradores

#### Para o Projeto:
* Vitor Dreveck: Construção da resolução do problema, implementação das funções necessárias para a resolução do problema, implementação de busca exaustiva, comentários descritivos no código .
* Yasmin Shimizu: Construção da resolução do problema, implementação das funções necessárias para a resolução do problema.

#### Para o Repositório GitHub:
* Vitor Dreveck: Upload de arquivos.
* Yasmin Shimizu: Documentação do readme.

**Orientação e Revisão:** Prof. Dr. Daniel R. Cassar.

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/170521728?v=4" width=115><br><sub> Vitor Dreveck</sub>](https://github.com/vitordreveck-ilum)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/171518829?v=4" width=115><br><sub>Yasmin Shimizu</sub>](https://github.com/yasminbshimizu)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Currículo Lattes</sub>](https://lattes.cnpq.br/7813674402525956)<br> [<sub>Linkedin</sub>](https://www.linkedin.com/in/yasminbshimizu/) | [<img loading="lazy" src="https://github.com/user-attachments/assets/463d4753-7fa4-4a42-aa54-409e4150bb51" width=115><br> <sub> Prof. Dr. Daniel R. Cassar </sub>](https://github.com/drcassar)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Currículo Lattes</sub>](http://lattes.cnpq.br/1717397276752482) | 
| :---: | :---: | :---: | 
