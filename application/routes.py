from flask import Response, request
from application import feature_switch
from application import app
import json

@app.route("/feature", methods=["GET", "POST"])
def feature():
    if (request.method == "GET"):
        response = feature_switch.get_feature(request.args.get("email"), request.args.get("featureName"))
        return Response(status = response.status, response = response.message)
    elif (request.method == "POST"):
        if (not set(['email', 'featureName', 'enable']).issubset(set(request.json.keys()))):
            return Response(status=304)
        print(request.json)
        response = feature_switch.post_feature(request.json["email"], request.json["featureName"], request.json["enable"])
        return Response(status=response.status, response = response.message)
        
        

@app.route("/account", methods=["POST"])
def account():
    response = feature_switch.post_account(request.args)
    return Response(status=response.status, response = response.message)