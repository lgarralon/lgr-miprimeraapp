# Con esto retornamos texto
# from flask import Flask
# Para retornar una página web html, por ejemplo:
from flask import Flask, render_template

app = Flask (__name__)

# Para crear nuestras rutas, con este comando creamos la página principal

@app.route('/')
def home():
    return render_template('Home.html')

# Con este comeando creamos una ruta dentro de la principal

@app.route('/about')
def about():
    # para devolver texto, es retunr simplemente y texto entre comillas
    # return 'About Page'
    # para devolver una página html, un template, es con return render_template
    return render_template('about.html')

# Para arrancar nuestra aplicación

if __name__ == '__main__':
    app.run(debug=True)