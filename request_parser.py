
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
