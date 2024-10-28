from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel, gettext

app = Flask(__name__)

# Configuración de idiomas soportados
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

babel = Babel(app)



# Función para detectar el idioma seleccionado
#@babel.localeselector
def get_locale():
    #language=request.accept_languages.best_match(["en", "es"])
    language=request.cookies.get('lang')
    print("selected language: ", language)
    return language

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index():
    lang=get_locale()
    return render_template('index.html', lang=lang)

@app.route('/set_language/<lang>')
def set_language(lang):
    response = redirect(url_for('index'))
    response.set_cookie('lang', lang)
    return response

if __name__ == '__main__':
    app.run(debug=True)
