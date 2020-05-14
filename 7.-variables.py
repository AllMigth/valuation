from flask import Flask
from flask import render_template

#app = Flask(__name__, template_folder= "templates")
app = Flask(__name__)

@app.route('/user/<name>')     
def index(name='Juan'):
    age = 22 
    my_list = [1,2,3,4]
    return render_template('user.html', nombre=name, age=age, list = my_list)      
    

if __name__ == '__main__':
    app.run( debug = True , port = 5000) 