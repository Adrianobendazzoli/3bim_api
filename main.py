from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def raiz():
    return {'mensagem': 'Minha primeira API em FastApi!'}

@app.get('/clientes')
def clientes():
    return {'mensagem': 'aiii!'}