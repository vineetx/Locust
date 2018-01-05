# Locust
API Test


#Locust env setup :-


#update system (CentOs)

$ sudo yum update

$ sudo yum upgrade -y


#Install python 3.6

$ sudo yum install python36 python36.virtualenv python36-pip

$ python3 -V


#install Locust

$ sudo pip-3.6 install locust


#write locustfile.py

$ vim locustfile.py


#run Locust server

$ locust --host=https://<host where to hit the api>
  


#Linux

yum install tmux
