from flask import Flask
import os
from routes.example_routes import blueprint as example_blueprint

app = Flask(__name__)
app.register_blueprint(example_blueprint)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
