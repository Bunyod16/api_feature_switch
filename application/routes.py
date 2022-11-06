from flask import request, jsonify, make_response
from application import feature_switch
from application import app

@app.route('/feature', methods=['GET', 'POST'])
def feature():
    if (request.method == 'GET'):
        return make_response(feature_switch.get_feature(request.args.get('email'), request.args.get('featureName')))
    elif (request.method == 'POST'):
        if (not set(['email', 'featureName', 'enable']).issubset(set(request.json.keys()))):
            return make_response("", 304)
        else:
            return make_response(feature_switch.post_feature(request.json['email'], request.json['featureName'], request.json['enable']))
