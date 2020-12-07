from Analysers.Handlers import NewsFilterSocialMediaHandler
from Analysers.Models import AnalysisResult
from DataLayer.DataSetEntry import SocialMediaDataSetEntry

handler = NewsFilterSocialMediaHandler()
post = SocialMediaDataSetEntry(1, 1, 1, 1, 1, 1)
result = AnalysisResult()
handler.handle(post, result)
for element in result.elements:
    print(element.validation_result)
    print(element.validation_message)
