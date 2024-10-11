from sys import argv
from Similaridade.SobekCommandLineJava.bin.ControladoraSimilaridade import ControladoraSimilaridade
from RIT.BibliotecaRIT.BibliotecaRITFachada import BibliotecaRITFachada
import networkx as nx
import matplotlib.pyplot as plt


if(len(argv) > 1):
    path = argv[1].split(',')
    path[0] = "Similaridade/Textos/" + path[0]
    path[1] = "Similaridade/Textos/" + path[1]

    with open(path[0], 'r') as arquivo:
        arquivo1 = arquivo.read()

    with open(path[1], 'r') as arquivo:
        arquivo2 = arquivo.read()

    print("------------------------------------------------------------")
    print("1 - Cálculo de Similaridade de Cossenos")
    print("2 - Cálculo de Similaridade por Grafos")
    tipoCalculo = int(input("Digite o Tipo de Cálculo: "))
    print("------------------------------------------------------------")

    nivelSimilaridade = ControladoraSimilaridade.calcularSimilaridade(arquivo1, arquivo2, tipoCalculo)
    print(nivelSimilaridade)

else:
    
    usuario = input("Digite o nome do usuário: ")
    repositorio = input("Digite o nome do Repositório: ")

    tokens = str(input("Digite os tokens a serem utilizados: "))
    tokens = tokens.split(',')
    BibliotecaRITFachada.initTokens(tokens)

    visao = int(input("Digite a visão a ser usada: "))
    pagina = int(input("Digite a página inicial: "))

    if(visao == 4):
        arg = input("Digite o nome do Autor: ")
        BibliotecaRITFachada.extrairDadosGitHub(usuario, repositorio, visao, arg, pagina)
    if(visao == 5):
        arg = input("Digite a data (yyyy-mm-dd): ")
        BibliotecaRITFachada.extrairDadosGitHub(usuario, repositorio, visao, arg, pagina)

    BibliotecaRITFachada.extrairDadosGitHub(usuario, repositorio, visao, pagina)