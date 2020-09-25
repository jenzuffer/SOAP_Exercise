#Installation instructions: <br/>
##requires: python(used 3.8), pip, virtualenv(pip install virtualenv) <br/>

###virtualenv venv or python3 -m virtualenv venv <br/>
###source venv/bin/activate <br/>
###pip3 install -r requirements.txt <br/>
###flask requires command: export FLASK_APP=server_restfull_accepting_requests <br/>

#author detail: Christian Falk Moustesgård <br/>

##Brief summary of the applications development and implementation, including business and technical features: <br/>

i plan to run the application on my dedicated machine at: 163.172.84.14:8050, its running debian 9. 
The SOAP client and server are written in python using the PySimpleSOAP library. The target will be for a client to enter a city name in a SOAP requests and the server will return in a SOAP body a reponse with the weather. There is also
a client reaching the self made SOAP service using the requests library. <br/>
I will also try to make a nginx proxy configuration work with the soap server so it can run under my domain as a service on a subdomain. Same with the RESTfull service implementation. <br/>
The RESTfull service will also for simplicity sake be made with python using flask to expose endpoints with and will run on 163.172.84.14:5000.
 <br/>
running dedicated remotely: screen -d -m -S soap_service python3.8 server_accepting_soap_requests.py <br/>
                            screen -d -m -S restfull_service flask run --port 5050
<br/>
https://soapservice.christiansretsimpletestserver.xyz/
<br/>
https://restfull.christiansretsimpletestserver.xyz/
<br/>
to test the remote service run the client with: python3.8 client_posting_soap_requests.py 
<br/> 
python3.8 client_restfull_posting_requests.py  <br/>

check the response from https://restfull.christiansretsimpletestserver.xyz/ for testing simple GET request
