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
    number =1000
    locations = [
      [ -33.890542, 151.274856],
      [ -33.923036, 151.259052],
      [ -34.028249, 151.157507],
      [ -33.80010128657071, 151.28747820854187],
      [-33.950198, 151.259302]
    ];

    locations2 = [
        [42.503454, -92],
        [39.499633, -88],
        [45.81, 15.97]

    ];

    locations3=[ [15.97, 45.81], 
               [83.92, 35.96], 
                
               [11.07, 49.45], 
               (40.856362525282094, -97.39066408255889), 
               [-90.89833333, 31.58694444]




    ];

    #tweet = es.get(index = 'twitter', doc_type = 'tweets', id = 1) 

    dp_res = request.form['dropdown']
    selected = dp_res
    
    #selected="sports"
    print selected
    res = es.search(index="tweet", doc_type="tweetmap", q=selected)
    locationst=[]

        
    print("%d documents found" % res['hits']['total'])
    print res[0]
    for doc in res['hits']['hits']:
            #print doc
        #print("%s) %s" % (doc['_id'], doc['_source']['text']))
        #print doc['_source']['coordinates']

        if doc['_source']['coordinates']:
            print  ('has')
            x= doc['_source']['coordinates']['coordinates']
            y= doc['_source']['coordinates']
            print x
           
          
            locationst.append(x)

        # select a random coordinates    
        else:
            radius = 1113000.0                       #Choose your own radius
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
            locationst.append((xLat, yLong))
    
    print locationst        
            

    return render_template('home.html', marker_list= locationst, count=number)


@application.route('/', methods=['GET','POST'])
def home():

    return render_template('home.html', count =1000, marker_list = [])


if __name__ == '__main__':
    application.run(host='0.0.0.0')
