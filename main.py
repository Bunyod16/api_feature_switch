from flask import Flask, Response, request
from feature_switch import get_feature, post_feature, post_account

app = Flask(__name__)

@app.route("/feature", methods=["GET", "POST"])
def feature():
    if (request.method == "GET"):
        response = get_feature(request.args)
        return Response(status = response.status, response = response.json)
    elif (request.method == "POST"):
        response = post_feature(request.args)
        return Response(status=response.status, response = response.json)

@app.route("/account", methods=["GET"])
def account():
    response = post_account(request.args)
    return Response(status=response.status, response = response.json)
