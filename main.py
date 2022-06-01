from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/prever", methods=["POST"])
def predicao():
    salario = float(request.form["sal"])
    idade = float(request.form["ida"])
    divida=float(request.form["divi"])
    modelo = pickle.load(open("model.pkl", "rb"))
    prever = modelo.predict([[salario, idade,divida]])
    return (f"Credito: {str(prever)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

