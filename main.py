from sys import argv
from RIT.BibliotecaRIT.BibliotecaRITFachada import BibliotecaRITFachada
import networkx as nx
import matplotlib.pyplot as plt


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

BibliotecaRITFachada.extrairDadosGitHub(usuario, repositorio, visao,"", pagina)