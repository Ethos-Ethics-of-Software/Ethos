# **Ethos**

Repositório dedicado a implementação de métodos para auxiliar as pesquisas do Projeto Ethos, mantido pelo Núcleo de Pesquisa em Engenharia de Software Social e Colaborativa [NuPESSC](http://nupessc.caf.ufv.br/).  
Atualmente conta com o cálculo da similaridade entre dois textos por meio da similaridade de cossenos e por meio da similaridade entre grafos. Também possui um recorte da BibliotecaRIT, contendo um método para extração de dados de issues do GitHub.

## **Configuração**
Sabendo que o código utiliza de elementos externos, como a ferramenta [SOBEK]() e sendo desevolvido em Python, é necessário fazer a instalação de alguns elementos. Primeiramente devemos instalar as dependências de Java, para execução da ferramenta SOBEK, em que iremos instalar a linguagem Java, e seu exeucutador JDK, usando dos comandos abaixo:

```
sudo apt install default-jre
```
```
sudo apt install default-jdk
```

<br>

Além disso, é necessário que o arquivo executavél da ferramenta tenha permissão para rodar no sistema, de forma que devemos ir até a pasta do arquivo ```SobekCommandLineJava```, e executar o comando:

```
chmod +x SobekCommandLineJava
```

<br>

Olhando agora para os elementos da linguagem Python 3, e para sua formação foi necessário a presença de diversas bibliotecas, em que foi criado um arquivo, ```requirements.txt``` que irá instalar todas as dependências necessárias, bastando apenas ter instalado o [pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/), após isso, basta executar o comando:

```
pip3 install -r requirements.txt
```

<br>

Ademais, a biblioteca [NLTK](https://www.nltk.org/) precisa instalar externamente alguns itens, bastando executar o arquivo ```nltkmodule.py``` como mostrado abaixo.

```
python3 nltkmodules.py

```

## **Como Executar o Cálculo da Similaridade**

Estando na pasta raiz, no terminal digite o seguinte comando para executar a aplicação:

```
python3 main.py "Texto1.txt,Texto2.txt"
```
Sendo "Texto1.txt" e "Texto2.txt" o nome dos arquivos de texto a serem comparados, e eles precisam estar na pasta localizada em Similaridade/Textos.

## **Como Executar o Recorte da RIT**

Para extrair os dados das issues do GitHub , estando na pasta raiz, basta executar o arquivo main do programa com o seguinte comando:

```
python3 main.py
```

No menu é necessário fornecer os seguintes dados:
- Nome do usuário dono do repositório
- Nome do repositório
- Tokens do Git a serem utilizados
- Nome do usuário selecionado para o filtro (apenas utilizando a visão 4)
- Data para o filtro (apenas utilizando a visão 5)
- Página inicial para extração dos dados
    - deve ser utilizado quando ocorrer algum erro durante a extração dos dados, como por exemplo, não forem extraídos os dados de todas as _issues_ do repositório por não possuir tokens suficientes ou erro de conexão com a internet. Por padrão preencha com o valor 1.

### **Visões**

* 1 para filtrar por comentários de _issues_ abertas
* 2 para filtrar por comentários de _issues_ fechadas
* 3 para filtrar por comentários de _issues_ abertas e fechadas
Caso não seja especificada nenhuma visão, esta será utilizada.
* 4 para filtrar comentários por  autor, tanto para issues abertas quanto  fechadas
* 5 para filtrar comentários por  data, para issues abertas e fechadas