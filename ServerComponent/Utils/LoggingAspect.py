from aspectlib import Aspect
import logging

logging.basicConfig(filename='classifier.log', filemode='w', level=logging.DEBUG)


@Aspect(bind=True)
def logging_aspect(cutpoint, *args, **kwargs):
    logging.info("{} got called with the following parameters:[{}] [{}]"
                 .format(cutpoint.__name__, args, kwargs))
    function_call_result = yield
    logging.info("{} returned : {}".format(cutpoint.__name__, function_call_result))
