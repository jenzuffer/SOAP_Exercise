from pysimplesoap.server import SoapDispatcher, SOAPHandler
from http.server import HTTPServer
import requests

def cityweatherreport(city_name):
    key = ''
    weather_url_query = f"""http://api.weatherstack.com/current?access_key={key}&query={city_name}"""
    response = requests.get(weather_url_query)
    content = response.content.decode()
    query = content.split('query":"', 1)[1].split('","language')[0]
    lat = content.split('lat":"', 1)[1].split('","lon')[0]
    lon = content.split('lon":"', 1)[1].split('","timezone_id')[0]
    city_time = content.split('localtime":"', 1)[1].split('","localtime_epoch')[0]
    temperature = content.split('temperature":', 1)[1].split(',"weather_code"')[0]
    weather_description = content.split('"weather_descriptions":', 1)[1].split(',"wind_speed"')[0]
    wind_speed = content.split('wind_speed":', 1)[1].split('"wind_degree')[0]
    humid = content.split('"humidity":', 1)[1].split(',"cloudcover')[0]
    weather_report = f"""Weather report for {city_name}: \n"""
    weather_report += f"""query: {query} \n lat: {lat} \n lon: {lon} \n city_time: {city_time}"""
    weather_report += f"""\ntemperature: {temperature} \n weather_description: {weather_description}
        \n wind_speed: {wind_speed} \n humid: {humid} 
    """
    print('weather_report: ', weather_report)
    return{'weather_report': weather_report}


def server_accepting_soap_requests():
    dispatcher = SoapDispatcher(
        name="WeatherServer",
        location="http://127.0.0.1:8050/",
        action='http://127.0.0.1:8050/', # SOAPAction
        namespace="http://example.com/pysimplesoapsamle/", 
        prefix="ns0",
        trace = True,
        ns = True)
    dispatcher.register_function('CityWeatherReport', cityweatherreport,
            returns={'weather_report': str},
            args={'city_name': str})
    print('starting server')
    httpd = HTTPServer(("", 8050), SOAPHandler)
    httpd.dispatcher = dispatcher
    httpd.serve_forever()

def main():
    server_accepting_soap_requests()
    

if __name__ == '__main__':
    main()
    
