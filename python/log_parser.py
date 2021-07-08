#!/usr/bin/env python3

# 127.0.0.1 is the IP address of the client (remote host) which made the request to the server.
# user-identifier is the RFC 1413 identity of the client. Usually "-".
# frank is the userid of the person requesting the document. Usually "-" unless .htaccess has requested authentication.
# [10/Oct/2000:13:55:36 -0700] is the date, time, and time zone that the request was received, by default in strftime format %d/%b/%Y:%H:%M:%S %z.
# "GET /apache_pb.gif HTTP/1.0" is the request line from the client. The method GET, /apache_pb.gif the resource requested, and HTTP/1.0 the HTTP protocol.
# 200 is the HTTP status code returned to the client. 2xx is a successful response, 3xx a redirection, 4xx a client error, and 5xx a server error.
# 2326 is the size of the object returned to the client, measured in bytes.
# https://en.wikipedia.org/wiki/Common_Log_Format

#127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] GET /apache_pb.gif HTTP/1.0 200 2326
        

log = """127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] GET /apache_pb.gif HTTP/1.0 200 2326
         127.0.0.1 - alice [11/Dec/2019:18:03:45 -0700] GET /apache_pb.gif HTTP/1.0 200 2326
         0.0.0.0 - tom [25/Dec/2019:16:23:15 -0700] GET /apache_pb.gif HTTP/1.0 200 2326"""

output = [
    {
    "IP": "127.0.0.1", 
    "user-identifier": "-",
    "userid": "frank",
    "date": "10/Oct/2000",
    "time": "13:55:36",
    "zone": "-0700",
    "method": "GET",
    "resource": "/apache_pb.gif",
    "protocol": "HTTP/1.0",
    "status-code": "200",
    "obj size": "2326"
    }, 
    {
    "IP": "127.0.0.1", 
    "user-identifier": "-",
    "userid": "alice",
    "date": "11/Dec/2019",
    "time": "18:03:45",
    "zone": "-0700",
    "method": "GET",
    "resource": "/apache_pb.gif",
    "protocol": "HTTP/1.0",
    "status-code": "200",
    "obj size": "2326"
    }, 
    {
    "IP": "0.0.0.0", 
    "user-identifier": "-",
    "userid": "tom",
    "date": "25/Dec/2019",
    "time": "16:23:15",
    "zone": "-0700",
    "method": "GET",
    "resource": "/apache_pb.gif",
    "protocol": "HTTP/1.0",
    "status-code": "200",
    "obj size": "2326"
    }
]

    
def parse_datetime(datetime):
    the_date = datetime[1:12]
    the_time = datetime[13:]
    return the_date, the_time

def parse_log_entries(log):
    log_entries = log.splitlines()
    fields = ["IP", "user-identifier", "userid", "datetime", "zone", "method", "resource", "protocol", "status-code", "obj size"]
    list_of_log_entries = []

    for log_entry in log_entries:
        dict_log_entry = {}
        for index, i in enumerate(log_entry.split()):
            if fields[index] == "datetime":
                date_time_obj = parse_datetime(i)
                dict_log_entry["date"] = date_time_obj[0]
                dict_log_entry["time"] = date_time_obj[1]
            elif fields[index] == "zone":
                dict_log_entry[fields[index]] = i[:5]
            else:    
                dict_log_entry[fields[index]] = i 
        list_of_log_entries.append(dict_log_entry)
    return list_of_log_entries

print(parse_log_entries(log))

assert parse_log_entries(log)==output