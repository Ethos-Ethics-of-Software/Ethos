import requests

class Requisicao:
    _tokens = []

    @classmethod
    def init_tokens(cls, tokens: list):
        cls._tokens = tokens

    @classmethod
    def request(cls, url):
        tokens = cls._tokens.copy()
        for i in range(len(tokens)):
            try:
                headers = {'Authorization': 'token ' + tokens[i]}
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return response
                else:
                    if(response.status_code):
                        print(response.status_code)
                    cls._tokens.pop(i)
            except Exception as e:
                if(response.status_code):
                    print(response.status_code)
                cls._tokens.pop(i)
