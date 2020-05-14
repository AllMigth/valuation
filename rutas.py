from flask import Flask
from flask import request

app = Flask(__name__)  #nuevo objeto

@app.route('/')     #decorador o wrap  RUTAS A LAS QUE EL USUARIO PUEDE ENTRAR
def index():
    return 'Rutas.' 
    
# @app.route('/saluda')     #decorador o wrap  RUTAS A LAS QUE EL USUARIO PUEDE ENTRAR
# def saluda():
#     return 'Otro mensaje'  

#Usando parametros 
@app.route('/params')    
def params():
    #aqui
    #http://127.0.0.1:8000/params?params1=Juan%20Garzon
    param = request.args.get('params1','no contiene este parametro')
    return 'El parametro es: {}'.format(param) 


if __name__ == '__main__':
    app.run( debug = True , port = 8000)   #se encarga de ejecutar nuestro servidor en el puerto 5000