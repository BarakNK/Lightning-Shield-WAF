from database_manager import *
import requests
import logging_manager

logger = logging_manager.logging_manager()
database = database_manager()

def get_server_response(http_request):
    """
    Getting the response from the read protected server that the client tries to reach
    """
    response = None
    http_headers = http_request["headers"]
    real_ip = database.get_ip_by_host(http_headers["Host"])
    cookies = http_request["cookie"]
    
    if http_request["http_type"] == "GET":
        response = requests.get("http://" + real_ip + http_request["path"], headers=http_headers, cookies=cookies)
        
    elif http_request["http_type"] == "POST":
        response = requests.post("http://" + real_ip + http_request["path"], data=http_request["data"])#, cookies=cookies)
    
    if response is not None:
        return requests_object_to_http_response(response)
    else:
        logger.warning(f"Cant connect to {http_headers['Host']} on {real_ip}")
 

def requests_object_to_http_response(response):
    """
    parsing the response object we get from the original web server into an http answer -
    into an http response we can nsfer to the original web server, it consists of the answer (for example 200 OK)
    , headers, \r\n\r\n and the content itself.
    """
    http_code = response.status_code
    http_code_textual = response.reason
    response_headers = response.headers
    content = response.content
    
    response_headers = update_response_headers(response_headers, content)
    
    first_line = f"HTTP/1.1 {http_code} {http_code_textual}\r\n"
    headers_string = ""
    for header in response_headers:
        headers_string += f"{header}: {response_headers[header]}\r\n"
 
    headers_string += "\r\n"
 
    return first_line.encode() + headers_string.encode() + content


def update_response_headers(response_headers, content):
    """
    since we wont be coding all of the possible transfer encoding types, we want to remove
    the headers, and transfer it in a simple way (with content length).
    """

    if "Content-Length" not in response_headers:
        response_headers["Content-Length"] = len(content)
    
    if "Transfer-Encoding" in response_headers:
        del response_headers["Transfer-Encoding"]
    
    if "Connection" in response_headers:
        response_headers["Connection"] = "close"
    
    return response_headers
