from flask import Flask , jsonify
from flask_cors import CORS
from flasker.models import setup_db , Plant

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(
        app ,resources={r"/api/*":{"origins":"*"}}
    )
    
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers","Content-Type,Authorization")
        response.headers.add("Access-Control-Allow-Methods","GET,PATCH,DELETE,POST,OPTIONS")
        return response 
    
    @app.route('/')
    def hello():
        return jsonify({'message':'Hello World!'})
    
    
    @app.route('/smiley')
    def smiley():
        return ':)'
    
    
    # if test_config == None:
    #     app.config.from_py('config.py',silent=True)
    return app 