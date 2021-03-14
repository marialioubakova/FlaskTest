from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route("/")
def index():
    return '''<html>
    Привет от приложения Flask
    <br>
    <img src="static/img.png" width=100%>
    </html>
    '''


if __name__ == '__main__':
    # os.environ пытается получить значение переменной окружения с именем PORT, а
    # если не получается, то выставляет порт 5000
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
    # app.run()
    serve(app, host='0.0.0.0', port=5000)
