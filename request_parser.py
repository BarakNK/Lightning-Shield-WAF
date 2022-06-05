from requests_toolbelt.multipart import decoder

def parse_headers(headers_list):
    headers = {}
    for line in headers_list:
        if line != "":
            key, value = line.split(": ")
            headers[key] = value
    return headers


def parse_post(post_request):
    post_request_parts = post_request.split("\r\n\r\n")
    header_str = post_request_parts[0]
    headers = parse_headers(header_str.splitlines()[1:]) #[1:] because first line is GET and path
    data_str = '\r\n\r\n'.join(post_request_parts[1:])
    post_data = {}

    if "multipart/form-data" in headers["Content-Type"]: #if information passes in multipule lines
        boundary = headers["Content-Type"].split("boundary=")[1]
        content_type = headers["Content-Type"]
        result = decoder.MultipartDecoder(data_str.encode(), content_type)

        for parameter in result.parts:
            key = parameter.headers[b"Content-Disposition"].decode().split('name=\"')[1][0:-1]
            post_data[key] = parameter.text
 
    else: #if information passes regularly
        no_spaces_str = ''.join(data_str.split())
        parameters = no_spaces_str.split("&")
        for parameter in parameters:
            key, value = parameter.split("=")
            post_data[key] = value

    return {"headers": headers, "data": post_data}

def parse_cookie(cookie_header):
    if cookie_header is None:
        return None
    cookies_dict = {}
    cookies_list = cookie_header.split(";")
    for cookie in cookies_list:
        splitted_cookie = cookie.split("=")
        cookie_key = splitted_cookie[0]
        cookie_value = splitted_cookie[1]
        cookies_dict[cookie_key] = cookie_value
    return cookies_dict

def parse_request(http_request_str):
    http_request_list = http_request_str.splitlines()
    http_type, path = http_request_list[0].split(" ")[0:2]
    cookie = None
        
    if http_type == "GET":
        headers = parse_headers(http_request_list[1:])
        if "Cookie" in headers:
            cookie = headers["Cookie"]
        return {"headers": headers, #[1:] because first line is GET and path
                "http_type": http_type,
                "cookie": parse_cookie(cookie),
                "path": path}

    elif http_type == "POST":
        post_request = parse_post(http_request_str)
        headers = post_request["headers"]
        if "Cookie" in headers:
            cookie = headers["Cookie"]
        return {"headers": headers,
                "http_type": http_type,
                "path": path,
                "cookie": parse_cookie(cookie),
                "data": post_request["data"]}
