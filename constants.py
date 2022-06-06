#All the variables and values below are constants to be used in the program.
HOST = "127.0.0.1"
PORT = 8000
SQLITE_PATH = "sqlite:///database.db?check_same_thread=False"
LOGGING_FILENAME = "logs.txt"
SQL_WHITELIST = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.@#<>/ " #These characters are allowed
INJECTION_DETECTING_REGEX = "'(''|[^'])*'"
