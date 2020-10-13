from flask import Flask, render_template, request, redirect
from  data_base import data_base, tests
import os

os.system('sh ../url_env/bin/activate')

app = Flask(__name__)
#app.secret_key

@app.route('/')
def index():
    return render_template('index.html', title = 'Bytely | The best url shortener')

@app.route('/form/', methods=['GET', 'POST'])
def form_manager():
    if request.method == 'GET':
        return render_template('form.html', title = 'Shorten your URL as faster as light')
    elif request.method == 'POST':
        url = request.form['url_box']
        if not tests.begins_with_http(url):
            url = 'https://{}'.format(url)
        if tests.exists(url):
            shortened = 'http://localhost:5000/links/{}/'.format(data_base.add_to_database(url))
            return render_template('form.html', title = 'Shorten your URL as faster as light', url = url, shortened = shortened)
        else:
            return render_template('form.html', title = 'Invalid link', url = 'Please, enter a valid url')
        
@app.route('/links/<page_number>/')
def redir(page_number):
    real_url = data_base.get_url(page_number)
    if real_url is None:
        return redirect(url_for('error_page'))
    else:
        return redirect(real_url)
    
@app.errorhandler(404)
def error_page(error):
    return render_template('error.html')

@app.route('/about+author/')
def author():
    return render_template('author.html')


if __name__ == '__main__':
    app.run(debug=True)