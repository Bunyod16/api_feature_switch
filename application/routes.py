from flask import Response, request
from application import feature_switch
from application import app

@app.route("/feature", methods=["GET", "POST"])
def feature():
    if (request.method == "GET"):
        response = feature_switch.get_feature(request.args.get("email"), request.args.get("featureName"))
        return Response(status = response.status, response = response.message)
    elif (request.method == "POST"):
        response = feature_switch.post_feature(request.args.get("email"), request.args.get("featureName"), request.args.get("access"))
        return Response(status=response.status, response = response.message)

@app.route("/account", methods=["POST"])
def account():
    response = feature_switch.post_account(request.args)
    return Response(status=response.status, response = response.message)