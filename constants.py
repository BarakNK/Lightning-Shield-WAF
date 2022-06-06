#All the variables and values below are constants to be used in the program.
HOST = "127.0.0.1"
PORT = 8000
SQLITE_PATH = "sqlite:///database.db?check_same_thread=False"
LOGGING_FILENAME = "logs.txt"
SQL_WHITELIST = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.@#<>/ " #These characters are allowed
INJECTION_DETECTING_REGEX = "'(''|[^'])*'"
FIREWALL_RULE_NAME = "Lightning Shield - WAF"
MAX_CONNECTIONS_PER_IP = 25 #There is usually no point in having more than 25 connections per IP. Too many connections may cause a DoS.
LOGGING_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
SOCKET_TIMEOUT = 25 #This is the time in seconds that the socket will wait for a response from the user. (To avoid slow-loris attacks)
EMAIL_VALIDATE_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
