from flask import render_template
from flask import request
import config
from models import Quotes, quotes_schema
from sqlalchemy import func

app = config.connexion_app

app.add_api(config.basedir / 'swagger.yml')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/documentation')
def documentation():
    return render_template('documentation.html')


if __name__ == '__main__':
    app.run(debug=True)

