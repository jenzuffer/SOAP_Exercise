import requests
import pprint
from pysimplesoap.client import SoapClient

def test_number_conversion_service():
    url = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso'
    headers = {'content-type': 'text/xml'}
    body = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
      <ubiNum>32482348234</ubiNum>
    </NumberToWords>
  </soap:Body>
</soap:Envelope>'''
    print('body: ', body, '\n\n response content: ')    
    response = requests.post(url,data=body,headers=headers)
    pprint.pprint(response.content)

def test_weather_conversion_service():
    client = SoapClient(
        location="http://localhost:8050/",
        action='http://localhost:8050/',  # SOAPAction
        namespace="http://example.com/sample.wsdl",
        soap_ns='soap',
        trace=True,
        ns="ns0",
        )
    response = client.CityWeatherReport(city_name="Madrid")
    result = response.weather_report
    print('result: ', result) 

def main():
    #test_number_conversion_service()
    test_weather_conversion_service()

if __name__ == '__main__':
    main()
