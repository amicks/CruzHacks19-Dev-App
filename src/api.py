from db import db, Hackers as HackersModel
from flask_restful import Api, Resource
from webargs import fields
from webargs.flaskparser import use_kwargs

api = Api()

types = {
    'public_id': fields.Integer,
    'team_id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
    'gender': fields.String,
    'age': fields.Integer,
    'needs_transportation': fields.Boolean,
    'rsvp_status': fields.Boolean,
    'app_status': fields.Boolean,
    'shirt_size': fields.String,
    'university': fields.String,
    'class_year': fields.Integer
}

def query_to_dict(query):
    return dict((col, getattr(query, col)) for col in query.__table__.columns.keys())

@api.resource('/hackers/')
class Hackers(Resource):

    @use_kwargs({'public_id': types['public_id'](required=True)})
    def get(self, public_id):
        res = query_to_dict(HackersModel.query.filter_by(public_id=public_id).first())
        del res['private_id']
        return res

    @use_kwargs({
        'team_id': types['team_id'](missing=None),
        'first_name': types['first_name'](required=True),
        'last_name': types['last_name'](required=True),
        'email': types['email'](required=True),
        'gender': types['gender'](missing=None),
        'age': types['age'](required=True),
        'needs_transportation': types['needs_transportation'](required=True),
        'rsvp_status': types['rsvp_status'](missing=None),
        'app_status': types['app_status'](missing=None),
        'shirt_size': types['shirt_size'](required=True),
        'university': types['university'](missing=None),
        'class_year': types['class_year'](missing=None)
    })
    def post(self, first_name, last_name, email, age, needs_transportation, rsvp_status, app_status,
             shirt_size, gender, team_id, university, class_year):
        new_hacker = HackersModel(first_name, last_name, email, age, needs_transportation, rsvp_status,
                                  app_status, shirt_size, gender, team_id, university, class_year)
        db.session.add(new_hacker)
        db.session.commit()

        res = query_to_dict(new_hacker)
        del res['private_id']
        return res