from flask import Flask
from flask import request

app = Flask(__name__) 

@app.route('/')   
def index():
    return 'Rutas.' 
    
#VALIDANDO RUTAS

@app.route('/params')    
def params():
    return 'El parametro es: {}, {}'.format(param, param_dos) 


if __name__ == '__main__':
    app.run( debug = True , port = 8000)   #se encarga de ejecutar nuestro servidor en el puerto 5000