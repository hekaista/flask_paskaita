from flask import Flask, render_template, request

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


@app.route("/pasisveikink5", methods=["GET", "POST"])
def pasisveikink5():
    if request.method == "GET":
        return render_template("pasisveikink5_forma.html")
    if request.method == "POST":
        tekstas = request.form["laukelis"]
        return render_template("pasisveikink5_rezultatai.html", tekstas=tekstas)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("forma.html")
    if request.method == "POST":
        kintamasis = request.form["laukelis"]
        return render_template("vardas.html", sablono_kint=kintamasis)


@app.route("/<kintamasis>")
def user(kintamasis):
    return render_template("vardas.html", sablono_kint=kintamasis)


if __name__ == "__main__":
    app.run()
