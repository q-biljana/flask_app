# flask_app


This simple flask app sends out a POST request in text. If the request is "Hello", the app returns a response of "Hi". If the response returns anything else other than "Hello", an error is returned.

#### Files: 
* app.py - python code using Flask to send the POST request and compare with the response 
* requirements.txt - Flask version and Flask dependencies requirements 
* Dockerfile 

### To run this app inside a docker container : 
1. run "  docker build -t [tagged name] :<tagged version > . "
   * eg. docker build -t flask_rest:v1 .
1. after the image build, run the container with: "docker run -d -p 5000:5000 <tagged name> :<tagged version > "

1. the endpoint for the [POST] request is given by: http://0.0.0.0:5000/restapi

