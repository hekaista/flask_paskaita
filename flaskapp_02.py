from flask import Flask, render_template, request
import sys

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/orai")
def orai():
    return render_template("orai.html")


@app.route("/ciklas")
def ciklas():
    return render_template("ciklas.html")


@app.route("/naujienos")
def naujienos():
    return render_template("naujienos.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        kintamasis = request.form['laukelis']
        return render_template("vardas.html", sablono_kint=kintamasis)
    else:
        return render_template("forma.html")


@app.route("/pasisveikink5", methods=['GET', 'POST'])
def pasisveikink5():
    if request.method == 'POST':
        kintamasis = request.form['laukelis']
        return render_template("sveik_ciklas.html", sablono_kint=kintamasis)
    else:
        return render_template("forma.html")


@app.route("/<kintamasis>")
def user(kintamasis):
    return render_template("vardas.html", sablono_kint=kintamasis)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = 5000
    app.run(host='0.0.0.0', port=port)