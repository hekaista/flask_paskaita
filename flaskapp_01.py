from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Čia yra mano pirmasis namų puslapis su Flask</h1>"

@app.route("/<kintamasis>") #apsišašom adresą, ir pasakom kad po slasho bus išvestas kažkas ko neturim aprašę linkuose
def user(kintamasis):
    return f"<h1>Sveiki {kintamasis} atvykę į Flask puslapį</h1>"

if __name__ == "__main__":
    app.run()
