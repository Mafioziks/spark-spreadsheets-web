from datetime import datetime
from config import db, ma
import hashlib
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field


class AccessScope(db.Model):
    __tablename__ = 'access_scope'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    last_name = db.Column(db.String(32))
    first_name = db.Column(db.String(32))
    email = db.Column(db.String(130))
    password = db.Column(db.String(130))
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

    @staticmethod
    def hash(password):
        return hashlib.sha256(password).hexdigest()


class UserToken(db.Model):
    __tablename__ = 'user_token'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, index=True)
    token_type = db.Column(db.Enum(('access', 'refresh')), nullable=False)
    token = db.Column(db.String(130))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class TokenAccessScope(db.Model):
    __tablename__ = 'token_access_scope'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token_id = db.Column(db.Integer, index=True)
    access_scope_id = db.Column(db.Integer, index=True)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email")


class UserSparkSession(db.Model):
    __tablename__ = 'spark_session'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    session = db.Column(db.Integer, nullable=False)


class SparkSessionTask(db.Model):
    __tablename__ = 'spark_task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_id = db.Column(db.Integer)


class AccessScopeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AccessScope
        load_instance = True
        include_relationships = True


class UserTokenSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserToken
        load_instance = True
        include_relationships = True
