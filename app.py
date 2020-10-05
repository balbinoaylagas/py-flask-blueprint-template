from flask import Flask
from webapp.webapp import webapp_bp
from webapp.home.home import home_bp

app = Flask(__name__)

app.register_blueprint(webapp_bp)
app.register_blueprint(home_bp, url_prefix="/home")


@app.route("/")
def home():
    return "home"


if __name__ == "__main__":
    app.run(debug=True)
