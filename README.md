Installation instructions:
requires: python > 3.5, pip, virtualenv(pip install virtualenv)

virtualenv venv or python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt

author detail: Christian Falk Moustesgård

Brief summary of the applications development and implementation, including business and technical features:

i plan to run the application on my dedicated machine at: 163.172.84.14:8050, its running debian 9. 
The SOAP client and server are written in python using the PySimpleSOAP library. The first target will be for a client to enter a city name in a SOAP requests and the server will return in a SOAP body a reponse with the weather. 
I will also try to make a nginx proxy configuration work with the soap server so it can run under my domain as a service on a subdomain. 

running dedicated remotely: screen -d -m -S servicename python3 server_accepting_soap_requests.py

soapservice.christiansretsimpletestserver.xyz
