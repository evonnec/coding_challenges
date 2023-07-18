"""
A user has begun flooding the company's API with thousands and thousands of requests in a very short period, causing increased 
latency and downtime for our customers.py

To stop them, we need to be able to detect when they are sending too many requests so that we can respond with an error to mitigate negative
side effects on other users.py

To keep things simple, our goal is to implement a solution that will limit requests across all users (global rate limit
vs user specific rate limits)

Write a function called validRequestRate that will be invoked by API server

It should:
- take no arguments
- return true if function has been called 3 times or fewer in last 1 second
- return false otherwise

If making assumptions and tradeoffs (i.e. global variables) be aware of how it affects your solution

if using timestamps, we recommend using ones with millisecond-level precision to ensure that requests are limited with the correct
granularity

don't worry about a request object. function will be called when request happens, so get the current time to determine 
the time of the request
"""
import time

call_list = []

def keepTrackOfCalls():
    # accumulate number of calls in 1 second
    call_list.append(int(time.time()* 1000))

    # time.sleep(0.3)
    # add the request
    def recurse_delete(call_list):
        # run the deletion and recurse thru the call list
        if call_list[-1] - call_list[0] > 1000:
            del call_list[0]
            recurse_delete(call_list)
            
    #call the recurse deletion
    recurse_delete(call_list)
    #return the number of calls
    return(len(call_list))


def validRequestRate():
    if keepTrackOfCalls() <= 3:
        return True
    else:
        call_list.clear()
        return False
    
print(validRequestRate())
print(validRequestRate())
print(validRequestRate())
print(validRequestRate())
print(validRequestRate())
print(validRequestRate())
print(validRequestRate())
print(validRequestRate())
# validRequestRate()
# validRequestRate()
# validRequestRate()
# validRequestRate()
# validRequestRate()
# validRequestRate()
# validRequestRate()