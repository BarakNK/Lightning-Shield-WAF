import os
import time
from database_manager import database_manager
from database_models import *
import constants


class firewall_defense:
    def __init__(self):
        """
        the constructor of the firewall defense class,
        first we begin from loading the db and blocking the ips needed to be blocked
        """
        self.db = database_manager()
        self.load_ips_from_db()
        self.start_blocking()


    def start_blocking(self):
        """
        This function blocks all of the ips from the database through the firewall
        """
        ips_str = ""
        for ip in self.get_ips_list():
            ips_str += "," + ip
        ips_str[:-1]
        os.system(f'netsh advfirewall firewall add rule name="{constants.FIREWALL_RULE_NAME}" dir=in action=block remoteip={ips_str}')


    def stop_blocking(self):
        """
        This function stops blocking the ips by deleting the firewall rules we set before.
        """
        os.system(f'netsh advfirewall firewall delete rule name="{constants.FIREWALL_RULE_NAME}"')


    def unblock_ip(self, ip_address):
        self.db.remove_ip(ip_address)
        self.load_ips_from_db()
        self.stop_blocking()
        self.start_blocking()


    def block_ip(self, ip_address):
        self.db.add_blocked_ip(ip=ip_address, reason_id=0)
        self.load_ips_from_db()
        self.stop_blocking()
        self.start_blocking()


    def is_ip_ok(self, ip):
        """
        This function checks if the ip is blocked or not.
        Input: ip - string.
        Output: True if the ip is not blocked, False otherwise.
        """
        ips_list = self.load_ips_from_db()
        if ips_list is None or ip not in ips_list:
            return True
        return False


    def load_ips_from_db(self):
        self.ips = self.db.get_all_blocked_ips()


    def get_ips_list(self):
        return [ip_address.ip for ip_address in self.db.get_all_blocked_ips()]


    def possible_DoS_attack(self, sock, ip, connections_count):
        """
        This function checks if the given IP address has too many connections, which might indicate a possible DoS attack.
        Input: sock - a socket object.
            ip - string.
            connections_count - int, counting how many connections does the given IP address has.
        Output: True if there are too many connections (also using the firewall to block this IP), False otherwise.
        """
        if connections_count > constants.MAX_CONNECTIONS_PER_IP:
            self.block_ip(ip)
            sock.close()
            return True
        return False
