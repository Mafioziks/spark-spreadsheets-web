from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')


@app.route('/')
def home():
    """
    Home route
    :return:
    """
    # TODO: Add Vue.js one page site frontend with this file
    return render_template('home.html')


if __name__ == '__main__':
    print('Starting Spark Spreadsheet App')
    print('==============================')

    app.run(host='0.0.0.0', port=5000, debug=True)


