import requests
import json

class RequisicoesGit:

    @classmethod
    def requisicaoIssues(cls, usuario, repositorio, token):
        headers = {'Authorization': 'token ' + token}
        resposta = requests.get(f'https://api.github.com/repos/{usuario}/{repositorio}/issues', headers=headers)
                
        if(resposta.status_code == 200):
            return resposta.json()
        else:
            return resposta.status_code

    @classmethod
    def requisicaoComentarios(cls, usuario, repositorio, numeroIssue, token):
        
        headers = {'Authorization': 'token ' + token}
        resposta = requests.get(f'https://api.github.com/repos/{usuario}/{repositorio}/issues/{numeroIssue}/comments', headers=headers)
        
        if(resposta.status_code == 200):
            return resposta.json()
        else:
            return resposta.status_code