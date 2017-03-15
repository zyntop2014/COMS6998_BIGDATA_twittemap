# twittemap
CloudComputingTwitt
Team member: Yanan Zhang uni:yz3054 , Shuyang Zhao uni:sz2631
1. open the virtual environment and install the software

command: 

<<<<<<< HEAD
source twitt/bin/activate
=======
source tweet/bin/activate
>>>>>>> eb162de5c825199e1a068e4fce3f7a8a3dbaba63
pip install -r requirements.txt

2. Streaming Tweets
Create an EC2 instance
Pull the repo from Github
command :

python streaming.py’

3.run application: search tweets keyword through dropdown menu 

command:
python application.py

4. deploy using EB 

<<<<<<< HEAD
http://couldtwittmap.us-west-2.elasticbeanstalk.com/
=======
http://cloudmap.us-west-2.elasticbeanstalk.com/
>>>>>>> eb162de5c825199e1a068e4fce3f7a8a3dbaba63

command:
eb init
eb create
eb open


5. Assumptions

Due to large amount of data that are lack of coordinates, we specify random coordinates to 
Since those are random so sometimes the coordinates are not realistic.
