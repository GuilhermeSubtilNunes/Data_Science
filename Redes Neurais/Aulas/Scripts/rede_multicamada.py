# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:47:47 2019

@author: guilherme.nunes
"""

import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

#a = sigmoid(0.5)
#b = sigmoidDerivada(a)

#a = sigmoid(-1.5)
#b = np.exp(0)
    
entradas = np.array([[0,0],
                    [0,1],
                    [1,0],
                    [1,1]])
    
saidas = np.array([[0],[1],[1],[0]])
                   
#pesos0 = np.array([[-0.424, -0.740, -0.961], #x1
#                   [0.358, -0.577, -0.469]]) #x2
                    
#pesos1 = np.array([[-0.017], [-0.893], [0.148]]) #camadaOculta 

#Tuning(melhoria em relação ao codigo acima)
pesos0 = 2*np.random.random((2,3)) - 1
pesos1 = 2*np.random.random((3,1)) - 1

epocas = 1000000    #TrainingTime
taxaAprendizagem = 0.5
momento = 1

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)
    
    #AplicacaoParaCamadaOculta
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print("Erro: " + str(mediaAbsoluta))
    
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
    
    pesos1Transporta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transporta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
    
    camadaOcultaTransposta = camadaOculta.T
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)
    
    camadaEntradaTransposta = camadaEntrada.T
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesosNovo0 * taxaAprendizagem)
    
    