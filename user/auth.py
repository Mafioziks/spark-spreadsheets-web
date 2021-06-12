from config import db
from models import User, AccessScope, UserToken, TokenAccessScope, UserSchema
from flask import redirect, request, session


def register():
    """
    Register user
    :return:
    """
    if request.json['password'] != request.json['passwordVerify']:
        return {
           'message': 'data error',
           'errors': {
               'password': 'not same password for password and repeated password field'
           }
        }, 400

    user = User()
    user.password = User.hash(request.json['password'].encode('utf-8'))
    user.email = request.json['email']
    user.first_name = request.json['firstName']
    user.last_name = request.json['lastName']

    db.session.add(user)
    db.session.commit()

    user_schema = UserSchema()

    session['user'] = user_schema.dump(user)

    return {'message': 'Check email to validate'}, 200, {'Access-Control-Allow-Origin': '*'}


def login():
    """
    Authentication endpoint
    :return:
    """

    if session.get('user') is not None:
        return {}, 200

    user = User.query \
        .filter_by(
            email=request.json['email'],
            password=User.hash(request.json['password'].encode('utf-8'))
        ).first()

    if user is None:
        return {'message': 'Failed to login'}, 401

    session['user'] = UserSchema().dump(user)

    return {'message': 'logged in'}


def logout():
    """Logging out user by removing user information from session"""
    if session.get('user'):
        session.pop('user')

    return {}


# Advanced authorization not implemented yet

def oauth_dialog():
    redirect(request.args.get('redirect_uri'), 200)


def get_secret(user):
    """
    Authorized endpoint

    :param user:
    :return:
    """
    return {'message': user}


def token_info(access_token):
    """
    OAuth auth sample

    :param access_token:
    :return:
    """

    token = UserToken.query \
        .filter(UserToken.token == access_token, UserToken.token_type == 'access') \
        .one_or_none()

    if None is token:
        return {'message': 'user unauthorized'}, 401

    token_scopes = TokenAccessScope.query \
        .filter(TokenAccessScope.token_id == token.id)

    # UID
    # SCOPE
    if not token:
        return None

    return {'uid': token.user_id, 'scope': ['uid']}


def basic_auth(username, password, required_scopes=None):
    """
    Basic authorization sample

    :param username:
    :param password:
    :param required_scopes:
    :return:
    """
    user = User.query \
        .filter(User.email == username, User.password == password) \
        .one_or_none()

    if None is user:
        return {'message': 'user not found'}, 404

    return {'sub': ['spreadsheets']}