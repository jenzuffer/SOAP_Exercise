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
        location="https://soapservice.christiansretsimpletestserver.xyz/",
        action='https://soapservice.christiansretsimpletestserver.xyz/',  # SOAPAction
        namespace="https://soapservice.christiansretsimpletestserver.xyz/sample.wsdl",
        soap_ns='soap',
        trace=True,
        ns="ns0",
        )
    response = client.CityWeatherReport(city_name="Madrid")
    result = response.weather_report
    print('result: ', result) 

def test_weather_with_request():
    url = 'https://soapservice.christiansretsimpletestserver.xyz/'
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=utf-8'}
    body = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CityWeatherReport xmlns="https://soapservice.christiansretsimpletestserver.xyz/">
      <city_name>"Berlin"</city_name>
    </CityWeatherReport>
  </soap:Body>
</soap:Envelope>'''
    print('body: ', body, '\n\n response content: ')
    response = requests.post(url,data=body,headers=headers)
    r_content = response.content.decode(errors='ignore').replace('\n', '').replace('&quot;', '')
    pprint.pprint(r_content)

def main():
    test_number_conversion_service()
    test_weather_conversion_service()
    test_weather_with_request()

if __name__ == '__main__':
    main()
