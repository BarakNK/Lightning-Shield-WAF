from html import escape
import constants
import re

def attack_found(data_dict):
    """
    This function uses the attack detecting functions below to check for possible cases of an attack.
    Input: data_dict - a dictionary containing the data from the user request.
    Output: True if a possible attack is detected and False if it is not.
    """
    if csrf_referer(data_dict["headers"]) or detect_possible_sql_injection(data_dict["data"]):
        return True
    return False


def xss_and_sqli_mitigation(data_dict):
    """
    This function will sanitize the user input, in order to prevent XSS and SQL Injection attacks.
    Input: data_dict - a dictionary containing the data from the user request.
    Output: None. The function will modify the data_dict, there's no need to return.
    """
    for key, value in data_dict.items():
        value = "".join([char for char in value if char in constants.SQL_WHITELIST])
        data_dict[key] = escape(value)#re.escape(value)) #escapes both html and sql injection. First escape_string() is for sql injection, second escape() is for html (XSS).
    
    return data_dict


def csrf_referer(headers):
    """
    This function checks if the Referer header is set to the same domain (Host) as the request. (Note that the header is spelled referer, not referrer as spelled in English)
    Essentially checking if the user is trying to access the server from the same domain or from another domain which might be a CSRF attack.
    Input: headers - a dictionary containing the headers from the user request.
    Output: True if the Referer header is not set to the same domain as the request and False if it is.
    """
    if "Referer" in headers:
        refferer = headers["Referer"].split("//")[1].split("/")[0]
        if refferer != headers["Host"]:
            return True
        else:
            return False
    
    return False


def csrf_samesite_lax(data_dict):
    """
    This function sets the SameSite attribute to Lax for the cookie, in order to prevent CSRF attacks.
    Input: data_dict - a dictionary containing the data from the server response.
    Output: None. The function will modify the data_dict, there's no need to return.
    """
    if "Set-Cookie" in data_dict["headers"]:
        if "SameSite=Lax" not in data_dict["headers"]["Set-Cookie"]:
            if "SameSite" in data_dict["headers"]["Set-Cookie"]:
                set_cookie_attributes = data_dict["headers"]["Set-Cookie"].split(";")
                wanted_index = 0
                for index, attribute in enumerate(set_cookie_attributes):
                    if "SameSite" in attribute:
                        wanted_index = index
                        break
                set_cookie_attributes[wanted_index] = "SameSite=Lax"
                data_dict["headers"]["Set-Cookie"] = ";".join(set_cookie_attributes)

            else:
                data_dict["headers"]["Set-Cookie"] += "; SameSite=Lax"


def detect_possible_sql_injection(data_dict):
    """
    This function detect a possible SQL injection, return True if it is detected and False if it is not.
    The function will loop through the data and check if there is a possibility of an SQL injection in it.
    Note: This function is not 100% accurate, and might have some false positives but it is good enough for our purposes.
    Input: data_dict - a dictionary containing the data from the user request.
    Output: True if possible SQL Injection is detected and False if it is not.
    """
    for key, value in data_dict.items():
        if re.search(constants.INJECTION_DETECTING_REGEX, value):
            return True

    return False
