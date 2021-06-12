from flask import render_template
# from flask_session import Session
from config import connexion_app, app

import connexion
# app = connexion.App(__name__, specification_dir='./')

connexion_app.add_api('swagger.yml')
connexion_app.app.template_folder = 'client/dist'
connexion_app.app.static_folder = 'client/dist'
connexion_app.app.static_url_path ='client/dist'


@app.route('/')
def home():
    """
    Home route
    :return:
    """
    # TODO: Add Vue.js one page site frontend with this file
    return render_template('index.html')


if __name__ == '__main__':
    print('Starting Spark Spreadsheet App')
    print('==============================')
    # app.config["SESSION_PERMANENT"] = False
    # app.config["SESSION_TYPE"] = "filesystem"
    app.run(host='0.0.0.0', port=5000, debug=True)


