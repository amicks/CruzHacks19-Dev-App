from flask_restful import Api, Resource
api = Api()

@api.resource('/hackers')
class Hackers(Resource):
    def get(self):
        return {'foo': 'bar'}