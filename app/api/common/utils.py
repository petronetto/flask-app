from flask import jsonify, make_response

def make_api_response(schema, model, status_code=200):
    result = schema.dump(model)
    return make_response(jsonify(result.data), status_code)
