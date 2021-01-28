from flask import Flask, render_template, url_for,request

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')  # if you want to render a .html file,
    # import render_template from flask and use
    # render_template("index.html") here.


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return data
    else:
        return 'something happend wrong'


if __name__ == '__main__':
    app.debug = True
    app.run()  # go to http://localhost:5000/ to view the page.
