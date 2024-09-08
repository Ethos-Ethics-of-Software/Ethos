# Biblioteca usada para gerar e analisar os grafos
import networkx as nx
import matplotlib.pyplot as plt

from preProcessamento import PreProcessamento

class SimilaridadeGrafos:
    @classmethod
    def simGrafos(cls, grafoComentario, grafoTopico, idioma, tipoCalculo = 2):
        # Variaveis usadas para RC e os demais calculos
        RC = 0
        nosGrafoComentario = list(grafoComentario.nodes)
        nosGrafoTopico = list(grafoTopico.nodes)
        frequenciaGrafoComentario = PreProcessamento.frequenciaGrafoComentario(grafoComentario)

        # Variaveis para calculo de DC
        DC = 0
        listaVerticesComentario = []
        listaVerticesTopico = []
        dicionarioDistanciaComentario = dict(nx.all_pairs_shortest_path_length(grafoComentario))
        dicionarioDistanciaTopico = dict(nx.all_pairs_shortest_path_length(grafoTopico))
        distanciaGrafoComentario = 0
        distanciaGrafoTopico = 0

        # Variaveis usadas para o calculo de PC
        PC = 0
        verticesgrafoComentario = grafoComentario.number_of_nodes()
        verticesgrafoTopico = grafoTopico.number_of_nodes()
        somatorioVerticesComentario = 0
        somatorioVerticesTopico = 0

        # Encontrando valores das variaveis de RC e DC
        for noComentario in nosGrafoComentario:
            for noTopico in nosGrafoTopico:
                if(noComentario == noTopico):
                    try:
                        RC += float(grafoComentario.nodes[noComentario]['frequencia']) / frequenciaGrafoComentario
                    except KeyError:
                        RC += 0
                     
                    listaVerticesComentario.append(noComentario)
                    listaVerticesTopico.append(noTopico)

                # Dependendo do Idioma usado no Projeto iremos fazer uma chamada diferente
                # para a função de dicionario de sinonimos
                elif('' in noComentario == 0 and '' in noTopico == 0):
                    if(idioma == 'pt'):
                        if(PreProcessamento.dicionarioSinonimosPortugues(noComentario, noTopico) == 1):
                            try:
                                RC += float(grafoComentario.nodes[noComentario]['frequencia']) / frequenciaGrafoComentario
                            except KeyError:
                                RC += 0
                            
                            listaVerticesComentario.append(noComentario)
                            listaVerticesTopico.append(noTopico)

                    elif(idioma == 'en'):
                        if(PreProcessamento.dicionarioSinonimosIngles(noComentario, noTopico) == 1):
                            try:
                                RC += float(grafoComentario.nodes[noComentario]['frequencia']) / frequenciaGrafoComentario
                            except KeyError:
                                RC += 0
                            
                            listaVerticesComentario.append(noComentario)
                            listaVerticesTopico.append(noTopico)

                else:
                    palavra = PreProcessamento.tokenize(noComentario)
                    palavra = PreProcessamento.algoritmoStemming(palavra, idioma)

                    palavra1 = PreProcessamento.tokenize(noTopico)
                    palavra1 = PreProcessamento.algoritmoStemming(palavra1, idioma)

                    if(palavra == palavra1):
                        try:
                            RC += float(grafoComentario.nodes[noComentario]['frequencia']) / frequenciaGrafoComentario
                        except KeyError:
                            RC += 0
                        
                        listaVerticesComentario.append(noComentario)
                        listaVerticesTopico.append(noTopico)

        # Verificamos se a lista é maior que 1, se sim podemos calcular DC
        if(len(listaVerticesComentario) > 1):
            # Encontrando o caminho dos nos similares em cada grafo
            for comentario in listaVerticesComentario:
                for comentarioComparado in listaVerticesComentario:
                    try:
                        distanciaGrafoComentario += int(dicionarioDistanciaComentario[comentario][comentarioComparado])
                    except KeyError:
                        distanciaGrafoComentario += 0

            for topico in listaVerticesTopico:
                for topicoComparado in listaVerticesTopico:
                    try:
                        distanciaGrafoTopico += int(dicionarioDistanciaTopico[topico][topicoComparado])
                    except KeyError:
                        distanciaGrafoTopico += 0

        # Após calculado o valor do somatorio de distancia de cada grafo
        # calculamos, e verificamos se esta dentro do modulo
        DC = distanciaGrafoTopico - distanciaGrafoComentario

        if(DC < 0):
            DC = DC * -1

        DC = 1/(1 + DC)

        # Fazendo os calculos de vertices vizinhos para o calculo de PC
        for comentario in listaVerticesComentario:
            somatorioVerticesComentario += PreProcessamento.contarVerticesVizinhos(grafoComentario, comentario)/verticesgrafoComentario

        for topico in listaVerticesTopico:
            somatorioVerticesTopico += PreProcessamento.contarVerticesVizinhos(grafoTopico, topico)/verticesgrafoTopico

        # Após calculado o valor do somatorio de distancia de cada grafo
        # calculamos, e verificamos se esta dentro do modulo
        PC = somatorioVerticesTopico - somatorioVerticesComentario

        if(PC < 0):
            PC = PC * -1

        PC = 1/(1 + PC)

        return ((RC + DC + PC)/3)