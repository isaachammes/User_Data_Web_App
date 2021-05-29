import pytest
import json
import requests

URL = 'http://127.0.0.1:5000/get_statistics'
json_header = {'Accept': 'application/json'}
text_header = {'Accept': 'text/plain'}
xml_header = {'Accept': 'application/xml'}

with open('test.json') as f:
    test_data = json.load(f)

bad_request = {
    'invalid': 'request'
}

def test_file_request_status():
    files = {'file': open('test.json')}
    response = requests.post(URL, files=files)
    assert response.status_code == 200
    assert response.headers['Content-Length'] == '660'

def test_json_response():
    response = requests.post(URL, json=test_data, headers=json_header)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

def test_text_response():
    response = requests.post(URL, json=test_data, headers=text_header)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/plain; charset=utf-8'

def test_xml_response():
    response = requests.post(URL, json=test_data, headers=xml_header)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/xml; charset=utf-8'

def test_data_accuracy():
    response = requests.post(URL, json=test_data, headers=json_header)
    results = json.loads(response.text)
    assert results['percent_female_vs_male'] == 80.0
    assert results['percent_first_names_start_a_to_m'] == 80.0
    assert results['percent_last_names_start_a_to_m'] == 60.0
    assert results['percent_by_state'] == {'Extremadura': 20.0, 'Kansas': 20.0, 'Minas Gerais': 20.0, 'Nord-TrÃ¸ndelag': 20.0, 'Victoria': 20.0}
    assert results['percent_male_by_state'] == {'Extremadura': 100.0, 'Kansas': 0.0, 'Minas Gerais': 0.0, 'Nord-TrÃ¸ndelag': 0.0, 'Victoria': 0.0}
    assert results['percent_female_by_state'] == {'Extremadura': 0.0, 'Kansas': 100.0, 'Minas Gerais': 100.0, 'Nord-TrÃ¸ndelag': 100.0, 'Victoria': 100.0}
    assert results['percent_by_age'] == {'0-20': 0.0, '21-40': 60.0, '41-60': 20.0, '61-80': 20.0, '81-100': 0.0, '>100': 0.0}

def test_bad_request():
    response = requests.post(URL, json=bad_request, headers=json_header)
    assert response.status_code == 400
