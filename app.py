import firebase_admin
from firebase_admin import credentials,firestore

import flask
from flask import abort,jsonify,request,redirect

import json
import requests

# init the flask app
app=flask.Flask(__name__)


cred = credentials.Certificate("lets_food.json")
firebase_app=firebase_admin.initialize_app(cred)
store=firestore.client()


@app.route('/addRestaurant',methods=['POST'])
def addRestaurant():
    data=request.get_json(force=True)
    dict={}
    dict['name']=data.get("name")
    dict['mobile']=data.get("mobile")
    dict['address']=data.get("address")
    dict['location']={
                        "lat":data.get("lat"),
                        "lang":data.get("lang")
                    }
    dict['type']=data.get("type")
    
    dict['rest_id']=data.get("Rest_id")
    dict["ratings"]=data.get("Ratings")
    dict["imageUrl"]=data.get("imageUrl")
    dict["createdAt"]=firestore.SERVER_TIMESTAMP

    store.collection("RESTAURANTS").add(dict)

    return jsonify({"Response":200})











if  __name__=='__main__':
    app.run(host='localhost',port=5001,debug=False)