from flask import Flask

app = Flask(__name__)  #nuevo objeto

@app.route('/')     #decorador o wrap  RUTAS A LAS QUE EL USUARIO PUEDE ENTRAR
def index():
    return 'Run file'         #Regresar un string


if __name__ == '__main__':
    app.run( debug = True , port = 8000)   #se encarga de ejecutar nuestro servidor en el puerto 5000