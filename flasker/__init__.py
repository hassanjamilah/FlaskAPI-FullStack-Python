from flask import Flask , jsonify , request
from flask_cors import CORS
from flasker.models import setup_db , Plant
import os 
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
    
    '''
            PLANTS ENDPOINT
    '''
    
    '''
    Get All Plants 
    '''
    @app.route('/plants' , methods=['GET','POST'])
    def get_plants():
        page = request.args.get('page',1,type=int)
        start = (page-1)*10
        end = start + 10 
        plants = Plant.query.all()
        formated_plants = [plant.format() for plant in plants]
        return jsonify({
            "success":True , 
            'plants':formated_plants[start:end],
            'total_plants':len(formated_plants)
        })
    
    '''
    Get Specific Plant 
    '''
    @app.route('/plants/<int:plant_id>')
    def get_specific_plant(plant_id):
        plant = Plant.query.filter(Plant.id == plant_id).one_or_none()
        return jsonify({
            'success':True , 
            'plant':plant.format()
        })
    
    
    # if test_config == None:
    #     app.config.from_py('config.py',silent=True)
    return app 