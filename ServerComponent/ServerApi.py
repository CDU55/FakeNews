from flask import Flask
from flask_restful import Resource, Api , reqparse
import Services
from TextExtraction import ImplementParse
from TextExtraction.APIs import TwitterAPI

app = Flask(__name__)
api = Api(app)

server_request_args = reqparse.RequestParser()
server_request_args.add_argument("html", type=str, help="The html with the news is required.", required=True)


class ServerApi(Resource):
    def __init__(self):
        self.myService = Services.AnalysisService()

    def post(self):
        args = server_request_args.parse_args()
        text_extract_result = TwitterAPI.getDataFromTwitter(args['html'])
        if text_extract_result != "Data not found":
            validation_result = self.myService.analyseRequest(text_extract_result)
        else:
            validation_result = text_extract_result
        return {"response": validation_result}

    def get(self):
        return {"response": "Make the request with post method."}


api.add_resource(ServerApi, "/")

if __name__ == '__main__':
    app.run()
