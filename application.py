'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk 

'''
from flask import Flask, render_template, request

from elasticsearch import Elasticsearch, RequestsHttpConnection
import random
import math
import requests
from flask_socketio import SocketIO, send, emit
import json

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'  

#host='search-twittmap-6s3aqfikqujq7wozww3cq2pcyu.us-east-1.es.amazonaws.com'
#host="search-twitttrend-p3dwnc67tiu2brpgv3py5i4czq.us-west-2.es.amazonaws.com/"



@application.route('/', methods=['GET','POST'])
def home():


    return render_template('home1.html', marker_list = [], count='')


if __name__ == '__main__':
    application.run(host='0.0.0.0')
