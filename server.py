from flask import render_template, request
from flask_cors import CORS
from python_module.search import searchDB
from python_module.ad import adDB
from python_module.cache import cacheDB
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')
CORS(app.app)  # allow all domain cors


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['search']
    data=dict()
    data['result'] = searchDB(keyword)
    data['ad']=adDB(keyword)
    data['keyword']=keyword

    return render_template('result.html', data=data)


@app.route('/cache/<title>')
def cache(title):
    data=cacheDB(title)
    return render_template('cache.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True)
