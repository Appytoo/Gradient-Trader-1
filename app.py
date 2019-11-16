from flask import Flask,request,jsonify
from flask_restful import reqparse,Resource,Api
import json
from sentiment import getTweets
from flask_cors import CORS

#creating a flask app
app=Flask(__name__)
CORS(app) # This will enable CORS for all routes
api=Api(app)

class JsonAccumulator(Resource):
    
    def post(self):
        print('post function called')
        json_data = request.get_json(force=True)
        print(json_data)

        query =  json_data['query']
        result = {}

        p, n = getTweets(query)

        result['possitive'] = p
        result['negative'] = n
        return json.dumps(result)

api.add_resource(JsonAccumulator,'/prediction')

if __name__=='__main__':
	app.run(debug=True)