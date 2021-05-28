from helpers import *
from flask import Flask, render_template, request, send_file
from accept_types import get_best_match
from dict2xml import dict2xml
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return render_template('index.html')

@app.route('/get_statistics', methods=['POST'])
#API to retrieve statistics. Accepts JSON objects or files.
def get_statistics():
    #Checks if request is a json object. If not, it assumes that it is a file.
    if request.headers.get('content-type') == 'application/json':
        user_data = request.json['results']
    else:
        user_data = json.load(request.files['file'])['results']
    #Determines the best return type based on the Accept header
    try:
        return_type = get_best_match(request.headers.get('Accept'), ['text/plain', 'application/xml', 'application/json'])
    except:
        return_type = None
    #Converts JSON data to python dictionary containing the needed counts for calculating statistics
    user_statistics = process_users(user_data)
    #Calculates all relevant statistics and stores the data in a dictionary
    percent_female_vs_male = get_percent(
                                user_statistics['count_female'],
                                user_statistics['total_users'])
    percent_first_names_start_a_to_m = get_percent(
                                            user_statistics['count_by_first_name_start_letter']['A-M'],
                                            user_statistics['count_by_first_name_start_letter']['A-M'] +
                                            user_statistics['count_by_first_name_start_letter']['N-Z']
                                            )
    percent_last_names_start_a_to_m = get_percent(
                                            user_statistics['count_by_last_name_start_letter']['A-M'],
                                            user_statistics['count_by_last_name_start_letter']['A-M'] +
                                            user_statistics['count_by_last_name_start_letter']['N-Z']
                                            )
    percent_by_state = get_population_percentage_by_state(
                            user_statistics['count_by_state'], 
                            user_statistics['total_users']
                            )
    percent_male_by_state = get_sex_percentage_by_state(
                                user_statistics['count_male_by_state'], 
                                user_statistics['count_by_state']
                                )
    percent_female_by_state = get_sex_percentage_by_state(
                                    user_statistics['count_female_by_state'], 
                                    user_statistics['count_by_state']
                                    )
    percent_by_age = get_percentage_by_age(
                        user_statistics['count_by_age'], 
                        user_statistics['total_users']
                        )

    #Sorting male and female by state statistics
    percent_male_by_state = dictionary_sort_by_value(percent_male_by_state)
    percent_female_by_state = dictionary_sort_by_value(percent_female_by_state)

    result = {
        'percent_female_vs_male': percent_female_vs_male,
        'percent_first_names_start_a_to_m': percent_first_names_start_a_to_m,
        'percent_last_names_start_a_to_m': percent_last_names_start_a_to_m,
        'percent_by_state': percent_by_state,
        'percent_male_by_state': percent_male_by_state,
        'percent_female_by_state': percent_female_by_state,
        'percent_by_age': percent_by_age
    }

    #Returns proper type based on the request Accept header but defaults to JSON if others are not specified
    if return_type == 'application/xml':
        xml_result = dict2xml(result)
        xml_file_result = convert_result_to_file(xml_result)
        return send_file(xml_file_result, as_attachment=True,
                     attachment_filename='result.xml',
                     mimetype='text/xml')

    elif return_type == 'text/plain':
        text_result = convert_to_plain_text(result)
        text_file_result = convert_result_to_file(text_result)
        return send_file(text_file_result, as_attachment=True,
                     attachment_filename='result.txt',
                     mimetype='text/plain')

    else:
        json_result = json.dumps(result)
        json_file_result = convert_result_to_file(json_result)
        return send_file(json_file_result, as_attachment=True,
                     attachment_filename='result.json',
                     mimetype='application/json')

if __name__ == "__main__":
  app.run()