from flask import Flask

app = Flask(__name__)           #nuevo objeto

@app.route('/')                 #decorador o wrap  RUTAS A LAS QUE EL USUARIO PUEDE ENTRAR
def index():
    return 'Hola mundo'         #Regresar un string

app.run()                       #se encarga de ejecutar nuestro servidor en el puerto 5000