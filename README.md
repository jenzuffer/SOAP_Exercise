#Installation instructions:
##requires: python(used 3.8), pip, virtualenv(pip install virtualenv)

###virtualenv venv or python3 -m virtualenv venv
###source venv/bin/activate
###pip3 install -r requirements.txt
###flask requires command: export FLASK_APP=server_restfull_accepting_requests

#author detail: Christian Falk Moustesgård

##Brief summary of the applications development and implementation, including business and technical features:

i plan to run the application on my dedicated machine at: 163.172.84.14:8050, its running debian 9. 
The SOAP client and server are written in python using the PySimpleSOAP library. The target will be for a client to enter a city name in a SOAP requests and the server will return in a SOAP body a reponse with the weather. There is also
a client reaching the self made SOAP service using the requests library.
I will also try to make a nginx proxy configuration work with the soap server so it can run under my domain as a service on a subdomain. Same with the RESTfull service implementation.
The RESTfull service will also for simplicity sake be made with python using flask to expose endpoints with and will run on 163.172.84.14:5000.

running dedicated remotely: screen -d -m -S soap_service python3 server_accepting_soap_requests.py
                            screen -d -m -S restfull_service flask run

https://soapservice.christiansretsimpletestserver.xyz/
https://restfull.christiansretsimpletestserver.xyz/

to test the remote service run the client with: python3 client_posting_soap_requests.py and python3 
client_restfull_posting_requests.py and check the response from https://restfull.christiansretsimpletestserver.xyz/ simple GET method
