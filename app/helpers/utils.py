import time
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, make_response

def make_api_response(schema, model, status_code=200):
    result = schema.dump(model)
    return make_response(jsonify(result.data), status_code)

def utc_now_ts():
    return int(time.time())

def hash_password(password):
    return generate_password_hash(password)

def check_password(user_hashed_password, user_password):
    if check_password_hash(user_hashed_password, user_password):
        return True
    else:
        return False

def format_date(date, dt_format):
    return datetime.datetime.fromtimestamp(int(date)).strftime(dt_format)
