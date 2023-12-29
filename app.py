from flask import request 
from flask import jsonify 
import sys 
from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
	now = datetime.now()
	print("now =", now)
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	return {
    		"from_ip" : request.remote_addr,
			"from_port" : request.environ.get('REMOTE_PORT'), 
	    	"date" : dt_string
        }
        

app.run(host=sys.argv[1], port=sys.argv[2])


