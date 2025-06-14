from flask import Flask
from app.routes import routes
import os

app = Flask(__name__, template_folder='app/templates')  # <-- importante
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
