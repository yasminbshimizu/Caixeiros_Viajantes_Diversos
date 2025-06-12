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

* **Múltiplos caixeiros viajantes:** Qual o caminho de menor distância no problema do caixeiro viajante, com a peculiaridade de existir mais de um caixeiro? Considere que, além das condições tradicionais do problema, cada caixeiro começa em uma cidade diferente e jamais visita cidades já visitadas por outros caixeiros.
  
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

* **Caixeiro viajante que prefere cidades ímpares:**

* **Múltiplos caixeiros viajantes:**

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
