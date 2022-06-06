from database_model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time
import constants

engine = create_engine(consts.SQLITE_PATH)
Base.metadata.create_all(engine)

class database_manager:
    def __init__(self):
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()


    def add_user(self, username, password, email, full_name):
        time_of_creation = round(time.time())
        new_user = User(username=username, password=password, email=email, time_of_creation=time_of_creation, full_name=full_name)
        self.session.add(new_user)
        self.session.commit()


    def add_website(self, host, ip, user_id):
        time_of_creation = round(time.time())
        new_website = Website(host=host, ip=ip, user_id=user_id, time_of_creation=time_of_creation)
        self.session.add(new_website)
        self.session.commit()


    def get_user_by_id(self, id):
        user = self.session.query(User).filter_by(id=id).first()
        return user


    def get_user_by_username(self, username):
        user = self.session.query(User).filter_by(username=username).first()
        return user


    def get_website_by_host(self, host):
        website = self.session.query(Website).filter_by(host=host).first()
        return website


    def add_blocked_ip(self, ip, reason_id):
        time_of_creation = round(time.time())
        new_block = BlockedIPs(ip=ip, reason_id=reason_id, time_of_creation=time_of_creation)
        self.session.add(new_block)
        self.session.commit()


    def get_ip_by_host(self, host):
        return self.get_website_by_host(host).ip


    def get_all_blocked_ips(self):
        ips = self.session.query(BlockedIPs).all()
        return ips


    def is_ip_blocked(self, ip):
        ips = [ip_blocked.ip for ip_blocked in self.get_all_blocked_ips()]
        return (ip) in ips


    def change_password(self, id, new_password):
        user = self.session.query(User).filter_by(id=id).first()
        user.password = new_password
        self.session.commit()


    def remove_ip(self, ip):
        self.session.query(BlockedIPs).filter_by(ip=ip).delete()
        self.session.commit()


    def delete_user(self, id):
        self.session.query(User).filter_by(id=id).delete()
        self.session.commit()


    def get_id_by_username(self, username):
        return self.session.query(User).filter_by(username=username).first().id


    def get_all_users(self):
        users = self.session.query(User).all()
        return users


    def is_user(self, username, password):
        """
        This function checks if the username and password are correct (if the user even exists).
        Input: username and password.
        Output: True if the username and password are correct, False otherwise.
        """
        users = [(user.username, user.password) for user in self.get_all_users()]
        return (username, password) in users


    def is_username_exists(self, username):
        usernames = [user.username for user in self.get_all_users()]
        return username in usernames
