from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "Rannahvhea Angelique Agulto Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
