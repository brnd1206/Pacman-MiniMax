# Pac-Man AI - Minimax Agent

Este projeto é uma implementação de Inteligência Artificial para o clássico jogo do Pac-Man. O objetivo principal é fazer com que o Pac-Man jogue sozinho e tome decisões inteligentes para vencer o jogo utilizando o algoritmo **Minimax**.

## Como funciona a Inteligência Artificial?
O núcleo do projeto reside no arquivo `seuPacManAgents.py`. O Pac-Man atua como o agente **Maximizador** (buscando a maior pontuação e sobrevivência), enquanto os fantasmas atuam como agentes **Minimizadores** (buscando a menor pontuação para o Pac-Man e tentando capturá-lo). 

A IA prevê o futuro do jogo simulando as possíveis jogadas de todos os agentes (Pac-Man e múltiplos fantasmas) até uma certa profundidade (*depth*), permitindo que o Pac-Man tome a melhor decisão no presente. O código também inclui proteções contra "congelamentos" e empates de ações.

## Pré-requisitos
* **Python 3.6** ou superior.
* Nenhuma biblioteca externa (como Pygame ou Numpy) é necessária. O projeto utiliza apenas as bibliotecas padrão do Python.

## Como instalar e executar

**1. Clone o repositório:**
```bash
git clone https://github.com/brnd1206/Pacman-MiniMax.git
cd Pacman-MiniMax
```

**2. Teste Básico:**

Para ver a IA em ação com uma profundidade de busca de 2 níveis (visão de curto prazo), execute:
```bash
python pacman.py --pacman MinimaxAgent -a depth=2
```

## Opções Avançadas de Teste
O motor do jogo permite testar a robustez do algoritmo Minimax através de vários parâmetros pelo terminal.

**Alterando a Profundidade da IA (Depth)**

Você pode aumentar o "poder de visão de futuro" do Pac-Man. Profundidades maiores evitam que o Pac-Man seja pego de surpresa ("miopia do Minimax"), mas exigem mais poder de processamento.
```bash
python pacman.py -p MinimaxAgent -a depth=3
```

**Mudando o Mapa do Jogo**

Para testar o agente em labirintos de tamanhos diferentes, use a flag `-l`:

* Pequeno:
```bash
python pacman.py -p MinimaxAgent -a depth=2 -l smallClassic
```
* Arena Aberta:
```bash
python pacman.py -p MinimaxAgent -a depth=2 -l openClassic
```
* Mapa Original:
```bash
python pacman.py -p MinimaxAgent -a depth=2 -l originalClassic
```

**Alterando a Quantidade de Fantasmas**
Teste a capacidade do agente de fugir de múltiplos inimigos usando a flag `-k`:

```bash
python pacman.py -p MinimaxAgent -a depth=2 -k 3
```

**Modo Turbo (Avaliação de Desempenho)**

Para testar a verdadeira taxa de vitórias (Win Rate) do algoritmo sem ter que assistir as partidas (modo silencioso/invisível), use a flag `-q` (Quiet) junto com `-n` (Number of games):
```bash
# Executa 10 partidas em velocidade máxima, no mapa médio com profundidade 3
python pacman.py -p MinimaxAgent -a depth=3 -l mediumClassic -n 10 -q
```
**Arquivo Principal**

As modificações e a inteligência artificial foram implementadas exclusivamente no arquivo:
* `seuPacManAgents.py` (Classe `MinimaxAgent`)
