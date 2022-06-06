from slowloris_defense import *
import threading
import firewall_manager
import request_handler
import constants
import multiprocessing
import logging_manager
import website_manager
import sys

logger = logging_manager.logging_manager()
firewall = firewall_manager.firewall_defense()

def main():
    IPs_per_host = {} #This will be used to inspect the number of requests per host, in order to detect possible DoS attacks (of the flood type).
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((constants.HOST, constants.PORT))
        server_socket.listen()

        logger.info(f"Running server on {constants.HOST}:{constants.PORT}...")
        while True:
            try:
                sock, client_address = server_socket.accept()
                client_ip = client_address[0]
                IPs_per_host[client_ip] = IPs_per_host[client_ip] + 1 if client_ip in IPs_per_host else 1 #Increment the number of requests from this IP. Unless it is the first request from this IP, in which case it will be 1.
                if firewall.is_ip_ok(client_ip) and not firewall.possible_DoS_attack(sock, client_ip, IPs_per_host[client_ip]):
                    client_thread = threading.Thread(target = request_handler.handle_request, args = (sock, client_address))
                    client_thread.start()

            except TimeoutError as e:
                sock.close()
                logger.warning(f"Timed out! Error: {e}")
                firewall.block_ip(client_address)

            except socket.timeout as e:
                logger.warning("socket timed out")
                #it happens every once in a while because it didn't accept any incoming connections, no need to log it.
                pass

            except KeyboardInterrupt:
                logger.error("The program was aborted by the administrator.")
                break

            except Exception as e:
                logger.error("Unknown error")

        firewall.stop_blocking()


if __name__ == "__main__":
    website_process = multiprocessing.Process(target=website_manager.run_app)
    website_process.start()
    main()
    
    #using sys exit because website_process.kill() cant kill flask
    sys.exit()
