from aspectlib import Aspect
import logging
import time

logging.basicConfig(filename='database.log', filemode='w', level=logging.DEBUG)


@Aspect(bind=True)
def query_aspect(cutpoint, *args, **kwargs):
    logging.info("A query will be executed against the database")
    start_time = time.time()
    function_call_result = yield
    end_time = time.time()
    logging.info("The query execution took {} seconds".format(end_time - start_time))


@Aspect(bind=True)
def insert_aspect(cutpoint, *args, **kwargs):
    logging.info("An insert statement will be executed against the database")
    for (index, value) in enumerate(args[0]):
        if value is None:
            logging.info("None value on param number {}, it might generate an exception if"
                         " the field is non nullable".format(index+1))
    start_time = time.time()
    function_call_result = yield
    end_time = time.time()
    logging.info("The insert statement execution took {} seconds".format(end_time - start_time))
