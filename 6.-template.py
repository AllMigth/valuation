from flask import Flask
from flask import render_template

#app = Flask(__name__, template_folder= "templates")
#template_folder = "nombre de la carpeta donde almacenamos nuestros templates"

#ESTO SE HACE EN CASO DE NO QUERER USAR LA CARPETA POR DEFECTO templates

app = Flask(__name__)

@app.route('/')     
def index():
    return render_template('index.html')      


if __name__ == '__main__':
    app.run( debug = True , port = 5000) 