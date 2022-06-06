import communicator
import request_parser
from defense_manager import *
from time import time
import logging_manager

logger = logging_manager.logging_manager()

def handle_request(sock, client_address):
    #measuring time of socket creation        
    time_created = time()

    #reading information from socket
    try:
        http_request_str = sock.recv(8000).decode()
    except Exception as e:
        logger.warning(f"data fetching from {client_address} failed")
        sock.close()
        return


    http_request = request_parser.parse_request(http_request_str)

    #mitigating attacks here
    if http_request["http_type"] == "POST":
        if attack_found(http_request):
            logger.warning(f"PASSWORD ATTACK FOUND {client_address}")
            sock.close()
            return

        http_request["data"] == xss_and_sqli_mitigation(http_request["data"])
        csrf_samesite_lax(http_request)

        logger.info(f"{client_address} sent - {http_request['data']}")

    server_response = communicator.get_server_response(http_request)
    sock.send(server_response)
    
    time_finished = time() #measuring the time it took to receive data
    logger.info(f"{client_address[0]} | {http_request['http_type']} - {http_request['path']} | request took {round(time_finished - time_created)}ms")
    sock.close()
 