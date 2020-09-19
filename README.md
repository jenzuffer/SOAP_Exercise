Installation instructions:
requires: python, pip, virtualenv(pip install virtualenv)

virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt

author detail: Christian Falk Moustesgård

Brief summary of the applications development and implementation, including business and technical features:
i plan to run the application on my dedicated machine at: 163.172.84.14, its running debian 9. 
The SOAP client and server are written in python using the requests library. The first target will be for a client to enter a city name and the server will return the weather. 
I will also try to make a nginx proxy configuration work with the soap server so it can run under my domain as a service on a subdomain. https://www.christiansretsimpletestserver.xyz/SoapServiceServer
