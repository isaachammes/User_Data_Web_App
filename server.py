from helpers import *
from flask import Flask, render_template, request
from accept_types import get_best_match
from dict2xml import dict2xml
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return render_template('index.html')

@app.route('/get_statistics', methods=['GET','POST'])
def get_statistics():

    if request.headers.get('content-type') == 'application/json':
        user_data = request.json['results']
    else:
        user_data = json.load(request.files['file'])['results']

    try:
        return_type = get_best_match(request.headers.get('Accept'), ['text/plain', 'application/xml', 'application/json'])
    except:
        return_type = None

    user_statistics = process_users(user_data)

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

    result = {
        'percent_female_vs_male': percent_female_vs_male,
        'percent_first_names_start_a_to_m': percent_first_names_start_a_to_m,
        'percent_last_names_start_a_to_m': percent_last_names_start_a_to_m,
        'percent_by_state': percent_by_state,
        'percent_male_by_state': percent_male_by_state,
        'percent_female_by_state': percent_female_by_state,
        'percent_by_age': percent_by_age
    }

    if return_type == 'application/xml':
        xml_result = dict2xml(result)
        return app.response_class(xml_result, mimetype='text/xml')

    elif return_type == 'text/plain':
        plain_text_result = convert_to_plain_text(result)
        return app.response_class(plain_text_result, mimetype='text/plain')

    else:
        json_result = json.dumps(result)
        return result

if __name__ == "__main__":
  app.run()