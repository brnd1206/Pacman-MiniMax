# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState
from multiAgents import MultiAgentSearchAgent


class MinimaxAgent(MultiAgentSearchAgent):
    
    def getAction(self, gameState):
        """
        Retorna a ação do minimax do gameState atual usando self.depth
        e self.evaluationFunction.
        """
        def minimax(agentIndex, depth, state):
            # 1. Condição de Parada
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state)

            numAgents = state.getNumAgents()
            nextAgent = (agentIndex + 1) % numAgents
            nextDepth = depth + 1 if nextAgent == 0 else depth
            
            # Pega as ações legais
            actions = state.getLegalActions(agentIndex)
            
            # --- CORREÇÃO 1: Proibir o Pac-Man de ficar parado ---
            if agentIndex == 0 and Directions.STOP in actions:
                actions.remove(Directions.STOP)

            # Caso não haja ações (encurralado)
            if not actions:
                return self.evaluationFunction(state)
            
            scores = []
            for action in actions:
                successor = state.generateSuccessor(agentIndex, action)
                scores.append(minimax(nextAgent, nextDepth, successor))

            # 4. Lógica de Max e Min
            if agentIndex == 0: # Turno do Pac-Man (MAX)
                maxScore = max(scores)
                
                # Se estamos na raiz (primeira jogada)
                if depth == 0:
                    # Encontra todas as ações que empataram com a pontuação máxima
                    bestIndices = [i for i in range(len(scores)) if scores[i] == maxScore]
                    # --- CORREÇÃO 2: Escolhe aleatoriamente entre os empates ---
                    return actions[random.choice(bestIndices)]
                
                return maxScore
            
            else: # Turno dos Fantasmas (MIN)
                return min(scores)

        return minimax(0, 0, gameState)

def betterEvaluationFunction(currentGameState: GameState):
    pos = currentGameState.getPacmanPosition()
    food = currentGameState.getFood().asList()
    ghostStates = currentGameState.getGhostStates()

    # Calcula a distância de Manhattan para a comida mais próxima
    foodDistances = [manhattanDistance(pos, f) for f in food]
    if len(foodDistances) > 0:
        minFoodDistance = min(foodDistances)
    else:
        minFoodDistance = 0

    # Distância para o fantasma mais próximo
    ghostDistances = [manhattanDistance(pos, ghost.getPosition()) for ghost in ghostStates]
    minGhostDistance = min(ghostDistances)

    # Aumenta a pontuação se o fantasma estiver assustado, mas penaliza se estiver muito perto
    scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
    if min(scaredTimes) > 0:
        minGhostDistance = 0  # Ignora fantasmas assustados

    return currentGameState.getScore() - (1.5 / (minFoodDistance + 1)) + (2 / (minGhostDistance + 1))

# Abbreviation
better = betterEvaluationFunction
