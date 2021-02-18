# Libraries
from pprint import pprint
from flask import Flask
from flask import json
from flask import request
import os

# Reading env variables
port = os.environ.get('PORT')
validator = os.environ.get('VALIDATOR')
secret = os.environ.get('SECRET')

# Process info from Meraki
def process_data(data):
    pprint(data, indent=1)

#FLASK
app = Flask(__name__)

# GET METHOD TO SEND VALIDATOR TO MERAKI
@app.route('/', methods=['GET'])
def get_validator():
    print("Validator sent to Meraki")
    return validator

# POST METHOD TO RECEIVE CLIENTS INFO FROM MERAKI
@app.route('/', methods=['POST'])
def post_data():
    data = request.json
    print("POST RECEIVED")

    # Verify secret
    if data['secret'] != secret:
        print("WRONG Secret", data['secret'])
        return("invalid secret",403)
    else:
        print("Secret OK", data['secret'])

   
    # Do something with data (commit to database)
    process_data(data)

    # Return success message
    return "POST Received OK"


# Launch application
app.run(port=port , host="0.0.0.0", debug=False)
