# **Ethos**

Repositório dedicado a implementação de métodos para auxiliar as pesquisas do Projeto Ethos, mantido pelo Núcleo de Pesquisa em Engenharia de Software Social e Colaborativa [NuPESSC](http://nupessc.caf.ufv.br/).  
Atualmente possui um recorte da BibliotecaRIT, contendo um método para extração de dados de Issues do GitHub, e arquivos .ipynb para análise de problemas éticos e contagem de substantivos em comentários de Issues de repositórios do GitHub.

## **Configuração**

Olhando agora para os elementos da linguagem Python 3, e para sua formação foi necessário a presença de diversas bibliotecas, em que foi criado um arquivo, ```requirements.txt``` que irá instalar todas as dependências necessárias, bastando apenas ter instalado o [pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/), após isso, basta executar o comando:

```
pip3 install -r requirements.txt
```

<br>

Ademais, a biblioteca [NLTK](https://www.nltk.org/) precisa instalar externamente alguns itens, bastando executar o arquivo ```nltkmodule.py``` como mostrado abaixo.

```
python3 nltkmodules.py
```

## **Como Executar**

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
* 4 para filtrar comentários por  autor, tanto para issues abertas quanto  fechadas
* 5 para filtrar comentários por  data, para issues abertas e fechadas
