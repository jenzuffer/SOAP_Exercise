import requests
import pprint
import unicodedata

def test_rest_post():
    url = 'https://restfull.christiansretsimpletestserver.xyz/weatherreport'
    headers = {'content-type': 'text/xml'}
    body = {'cityname': 'Dublin'}
    print('body: ', body, '\n\n response content: ')
    response = requests.post(url, json=body, headers=headers)
    r_content = response.content.decode()
    r_content = unicodedata.normalize("NFKD", r_content)
    r_content = r_content.replace('\n', '')
    pprint.pprint(r_content)

def main():
    test_rest_post()    
    

if __name__ == '__main__':
    main()
