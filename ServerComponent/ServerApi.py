import Services

class ServerApi:
    def __init__(self):
        self.myService = Services.AnalysisService()

    def process_request(self, request):
        validation_result = self.myService.analyseRequest(request)
        return validation_result
