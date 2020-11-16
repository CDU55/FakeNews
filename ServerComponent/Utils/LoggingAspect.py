from aspectlib import Aspect
import logging

@Aspect(bind=True)
def logging_aspect(cutpoint, *args, **kwargs):
    logging.info("{} got called with the followsing parameters:[{}] [{}]".format(cutpoint,args,kwargs))
    function_call_result=yield
    logging.info("{} returned : {}".format(cutpoint,function_call_result))

