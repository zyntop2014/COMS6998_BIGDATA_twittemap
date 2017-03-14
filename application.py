'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk 

'''
from flask import Flask, render_template, request
from flask_googlemaps import Map
from elasticsearch import Elasticsearch, RequestsHttpConnection
import random
import math

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'  

host='search-twittmap-6s3aqfikqujq7wozww3cq2pcyu.us-east-1.es.amazonaws.com'

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
) 


@application.route('/', methods=['POST'])
def map():
    # creating a map in the view

    #tweet = es.get(index = 'twitter', doc_type = 'tweets', id = 1) 

    dp_res = request.form['dropdown']
    selected = dp_res
    
    #selected="sports"
    print selected


    res = es.search(index="tweet", doc_type="tweetmap", q=selected, size=2000)
    locationst=[]

        
    print("%d documents found" % res['hits']['total'])

    #print res['hits']
    for doc in res['hits']['hits']:
            #print doc
        #print("%s) %s" % (doc['_id'], doc['_source']['text']))
        #print doc['_source']['coordinates']
        text=doc['_source']['text']
        if doc['_source']['coordinates']:
            
         
            x= doc['_source']['coordinates']['coordinates']
       
           
           
          
            locationst.append([x, text])

        # select a random coordinates    
        else:
            
            radius = 5113000.0                       #Choose your own radius
            radiusInDegrees=float(radius/111300)            
            r = radiusInDegrees
            
            #   UScenter = {lat: 40.461881, lng: -99.757229};
            x0 = 40.84
            y0 = -99.757229
         
            u = float(random.uniform(0.0,1.0))
            v = float(random.uniform(0.0,1.0))
            #print u, v
            w = r * math.sqrt(u)
            t = 2 * math.pi * v
            #print  w, t
            x = w * math.cos(t) 
            y = w * math.sin(t)
            #print x, y
  
            xLat  = x + x0
            yLong = y + y0
            point = (xLat, yLong)
            locationst.append([point, text])
    
       
    number = len(locationst)    


    return render_template('home.html', marker_list= locationst, count=number, selected=selected)


@application.route('/', methods=['GET','POST'])
def home():

    return render_template('home.html', marker_list = [], count='')


if __name__ == '__main__':
    application.run(host='0.0.0.0')
