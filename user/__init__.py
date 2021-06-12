from flask import session
from models import UserSchema
from utils.api_transform import dict_for_api


def validate_email():
    return {'message': 'Email validated!'}


def view():
    if session.get('user'):
        user_schema = UserSchema()
        api_ready_data = dict_for_api(user_schema.dump(session.get('user')))
        return api_ready_data

    return {'message': 'User not found'}, 404
