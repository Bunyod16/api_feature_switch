from flask import Response, request
from application import feature_switch
from application import app

@app.route("/feature", methods=["GET", "POST"])
def feature():
    if (request.method == "GET"):
        response = feature_switch.get_feature(request.args.get("email"), request.args.get("featureName"))
        return Response(status = response.status, response = response.message)
    elif (request.method == "POST"):
        if (not set(['email', 'featureName', 'enable']).issubset(set(request.json.keys()))):
            return Response(status=304)
        response = feature_switch.post_feature(request.json["email"], request.json["featureName"], request.json["enable"])
        return Response(status=response.status, response = response.message)
