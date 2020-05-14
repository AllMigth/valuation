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
    #http://127.0.0.1:8000/params?params1=Juan%20Garzon&params2=Pedro Picapiedra
    param = request.args.get('params1','no contiene este parametro')
    param_dos = request.args.get('params2','no contiene este parametro')
    return 'El parametro es: {}, {}'.format(param, param_dos) 


if __name__ == '__main__':
    app.run( debug = True , port = 8000)   #se encarga de ejecutar nuestro servidor en el puerto 5000