from flask import Flask
from flask_restful import Resource, Api, reqparse

import Services

app = Flask(__name__)
api = Api(app)

server_request_args = reqparse.RequestParser()
server_request_args.add_argument("html", type=str, help="The html with the news is required.", required=True)
server_request_args.add_argument("url", type=str, help="The url of the news article is required.", required=True)


class ServerApi(Resource):
    def __init__(self):
        pass
        self.myService = Services.AnalysisService()

    def post(self):
        args = server_request_args.parse_args()
        return {"response": self.myService.analyseRequest(args['html'], args['url'])}

    def get(self):
        return {"response": "Make the request with post method."}


api.add_resource(ServerApi, "/")

if __name__ == '__main__':
    app.run()
