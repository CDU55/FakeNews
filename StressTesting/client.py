import requests
import sys
import time
import threading

def make_request(request_count):
    start_time=time.time()
    url_addr="http://127.0.0.1:5000/"
    results=[]
    for request_index in range(0,request_count):
        response=requests.post(url_addr)
        results.append(response)
    execution_time=time.time()-start_time
    return results,execution_time

def append_results_to_list(url,list):
    list.append(requests.post(url))

def make_request_threads(request_count):
    start_time=time.time()
    url_addr="http://127.0.0.1:5000/"
    results=[]
    threads=[]
    for request_index in range(0,request_count):
        thread=threading.Thread(target=append_results_to_list,args=(url_addr,results))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    execution_time=time.time()-start_time
    return results,execution_time

requests_number=int(sys.argv[1])
results,time_elapsed=make_request(requests_number)
print("One thread requests time for {} requests : {}".format(requests_number,time_elapsed))
results,time_elapsed=make_request_threads(requests_number)
print("Multi thread requests time for {} requests : {}".format(requests_number,time_elapsed))
success=0
fail=0
for result in results:
    if result.status_code==200:
        success+=1
    else:
        fail+=1

print("Successful request : {}".format(success))
print("Failed request : {}".format(fail))
print(results[1].json())


