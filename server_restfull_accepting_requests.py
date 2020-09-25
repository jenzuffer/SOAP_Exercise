#!flask/bin/python
from flask import Flask, request, redirect, session, url_for
from settings import weather_api_key
import requests
import os
import platform

app = Flask(__name__)

def get_ifconfig_ip():
    return os.popen('curl -s ifconfig.me').readline()

@app.route('/', methods=['GET'])
def index():
    headers = request.headers
    data = request.get_data()
    external_ip = get_ifconfig_ip() 
    return f"""
    <html>
    <head>
        <title>title 1 here</title>
    </head>
    <body>
        <h1>Hello world</h1>
        <div> information about server and client: 
        <br>
           client: <br>
           headers: {headers} <br>
           data: {data} <br>
           <br><br>
        server: <br>
           os name: {os.name} <br>
           platform: {platform.system()} <br>
           release of platform: {platform.release()} <br>
           server IP: {external_ip} <br>
        </div>
    </body>
    </html>
    """

def cityweatherreport(city_name):
    weather_url_query = f"""http://api.weatherstack.com/current?access_key={weather_api_key}&query={city_name}"""
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

@app.route('/weatherreport', methods=['POST'])
def get_weather_report():
    cityname = request.get_json(force=True)
    weather_report = cityweatherreport(cityname)
    return f''' city name: {weather_report}'''

