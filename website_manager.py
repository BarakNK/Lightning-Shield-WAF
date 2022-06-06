from flask import Flask, jsonify, request, render_template, redirect, url_for
import random
from database_manager import database_manager
from main import logger
import re
import constants

db_manager = database_manager()

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)
app.config['SECERET_KEY'] = 'very-super-seceret-key'

@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def home():
    if request.method == 'GET':
        return render_template('index.html')

    else:
        name = request.form['name']
        email = request.form['email']
        ip = request.form['ip']
        domain = request.form['domain']

        msg = parse_user_data(name, email, ip, domain)
        return render_template("index.html", msg=msg)


def run_app():
    port = random.randint(2000, 9000)
    logger.info(f"Running website on port {port}")
    app.run(# Starts the site
        host='0.0.0.0',  # EStablishes the host.
        port=port,  # Randomly select the port the machine hosts on.
        debug=False)


"""
A function that parrses the data, it returns a string that will
be shown to the username.
"""
def parse_user_data(name, email, ip, domain):
    if len(name) < 1 or len(name) > 20:
        return "The username is invalid"
    if not re.fullmatch(constants.EMAIL_VALIDATE_REGEX, email):
        return "The email is invalid"
    if not is_valid_ip(ip):
        return "The ip is invliad"
    if "." not in domain:
        return "The domain is invalid"
    
    add_user_and_website(name, email, ip, domain)
    return "Your website has been added seccsfully"


"""
Adding the user and the website to the database and logging it
in the logs
"""
def add_user_and_website(name, email, ip, domain):
    logger.info(f"Adding a new user: {name}, {email}")
    db_manager.add_user(name, "", email, name)

    logger.info(f"{name} has added a new website: {domain} {ip}")
    db_manager.add_website(domain, ip, db_manager.get_id_by_username(name))


"""
Checking if the ip we received from the website is valid, returning True if it is,
and return False if it is'nt.
"""
def is_valid_ip(ip):
    try:
        parts = ip.split('.')
    except Exception as e:
        return False

    if len(parts) != 4:
        return False
    
    for part in parts:
        if int(part) < 0 or int(part) > 255:
            return False

    return True
