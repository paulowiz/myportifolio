from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def new():
    return render_template('index.html')  # if you want to render a .html file,
    # import render_template from flask and use
    # render_template("index.html") here.


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/works.html')
def works():
    return render_template('works.html')


@app.route('/work.html')
def work():
    return render_template('work.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/components.html')
def components():
    return render_template('components.html')


@app.route('/contact.html')
def contact():
    return render_template('components.html')


if __name__ == '__main__':
    app.debug = True
    app.run()  # go to http://localhost:5000/ to view the page.