from flask import render_template, Flask

app = Flask(__name__)


@app.route('/training/<profession>')
def training(profession):
    return render_template(template_name_or_list='index.html', profession=profession)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
