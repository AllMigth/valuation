from flask import Flask
from flask import request

app = Flask(__name__) 

@app.route('/')   
def index():
    return 'Hola mundo.' 
    

# params/libros/1    
#VALIDANDO RUTAS

# LOS VALORES VIENEN EN STRING

#es un servidor rest tal vez necesitamos un numero
#
@app.route('/params/')                              #Esta linea es por si viene sin parametro
@app.route('/params/<name>/<last_name>')    
def params(name='este es un valor por default', last_name='last name'):    #se crea un parametro por default, por si no llega el parametro
    return 'El parametro es: {} {}'.format(name, last_name) 


if __name__ == '__main__':
    app.run( debug = True , port = 8000)   #se encarga de ejecutar nuestro servidor en el puerto 5000