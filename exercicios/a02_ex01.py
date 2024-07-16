# Exercício
# Crie um endpoint que retorna "olá mundo" usando HTML e escreva seu teste.
# Dica: para capturar a resposta do HTML do cliente de testes, você pode
#  usar response.text


from fastapi import FastAPI

# 1º importar o tipo de resposta em HTML do modulo fastAPI.responses
from fastapi.responses import HTMLResponse

app = FastAPI()


# 2º usar o parametro apropriado em response_model, segundo a documentação
@app.get('/', response_class=HTMLResponse, response_model=None)
def read_root():
    # 3º retornar uma string do html
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>fastAPI</title>
</head>
<body>
    <h1>Ola Mundo</h1>
</body>
</html>
    """
