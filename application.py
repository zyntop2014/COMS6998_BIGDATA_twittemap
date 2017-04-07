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

host='search-twittmap-6s3aqfikqujq7wozww3cq2pcyu.us-east-1.es.amazonaws.com'
host="search-twitttrend-p3dwnc67tiu2brpgv3py5i4czq.us-west-2.es.amazonaws.com/"

host='search-movie-vpmtwgvr57yoata6seazfnpyfe.us-west-2.es.amazonaws.com'

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
) 

#r = requests.get('http://twittertrend2-dev.us-west-2.elasticbeanstalk.com/')




@application.route('/', methods=['POST'])
def map():

    
    # AWS sends JSON with text/plain
    try:
        js = json.loads(request.data)
    except:
        pass

    print (request.headers)

    hdr = request.headers.get('X-Amz-Sns-Message-Type')

        # Subscribe to the SNS topic
    if hdr == 'SubscriptionConfirmation' and 'SubscribeURL' in js:
        r = requests.get(js['SubscribeURL'])

    if hdr == 'Notification':
        tweet = js['Message']
        print (tweet)
            # Send this tweet to elastic search
            # postURL = 'http://localhost:9201/tweetmap/tweet'
        #postURL =  "https://search-twittmap-6s3aqfikqujq7wozww3cq2pcyu.us-east-1.es.amazonaws.com/"
        #r = requests.post(postURL , json = tweet)
        #es.index(index="tweet", doc_type="tweetmap", body= tweet)
            # Send this tweet to front-end
    
    # creating a map in the view
    try:
        dp_res = request.form['dropdown']
        dp_res2=request.form['dropdown2']
    except:
        return render_template('home1.html', marker_list = [], count='')

    selected = dp_res
    print request
    maxsize=int(dp_res2)
    print type(selected), dp_res2, maxsize
        
    #res = es.search(index="tweet", doc_type="tweetmap", q=selected, size=maxsize)
    res = es.search(index="twittertrend", doc_type="tweets", q=selected, size=maxsize)
    locationst=[]
   
    print("%d documents found" % res['hits']['total'])

    #print res['hits']
    for doc in res['hits']['hits']:
        #print doc
        #print("%s) %s" % (doc['_id'], doc['_source']['text']))
        #print doc['_source']['coordinates']
        text=doc['_source']['text']

        '''
        if doc['_source']['coordinates']:
            x= doc['_source']['coordinates']['coordinates']
            locationst.append([x, text])
        '''

        if doc['_source']['location']:
            x= doc['_source']['location']
            locationst.append(x)

        # select a random coordinates    
        else:
            
            radius = 2113000.0                       #Choose your own radius
            radiusInDegrees=float(radius/111300)            
            r = radiusInDegrees
            
            #   UScenter = {lat: 40.461881, lng: -99.757229};
            x0 = 40.84
            y0 = -99.757229
         
            u = float(random.uniform(0.0,1.0))
            v = float(random.uniform(0.0,1.0))
          
            w = r * math.sqrt(u)
            t = 2 * math.pi * v
        
            x = w * math.cos(t) 
            y = w * math.sin(t)
    
            xLat  = x + x0
            yLong = y + y0
            point = (xLat, yLong)
            locationst.append([point, text])
    
    # number of tweets   
    number = len(locationst)    
    #return render_template('home1.html', marker_list= locationst, count=number, selected=selected)
    return render_template('home1.html', marker_list = [], count='')


@application.route('/', methods=['GET','POST'])
def home():


    return render_template('home1.html', marker_list = [], count='')


if __name__ == '__main__':
    application.run(host='0.0.0.0')
