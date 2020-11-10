import Services
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class ServerApi(Resource):
    def __init__(self):
        self.myService = Services.AnalysisService()

    def post(self, request):
        request_json = request.get_json()
        validation_result = self.myService.analyseRequest(request)
        return validation_result

api.add_resource(ServerApi, "/")

if __name__ == '__main__' :
    app.run()
