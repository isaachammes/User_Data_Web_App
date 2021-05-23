def process_users(user_data):
    total_users = len(user_data)
    count_female = 0
    count_by_state = {}
    count_female_by_state = {}
    count_male_by_state = {}
    count_by_first_name_start_letter = {'A-M': 0, 'N-Z': 0}
    count_by_last_name_start_letter = {'A-M': 0, 'N-Z': 0}
    count_by_age = {'0-20': 0, '21-40': 0, '41-60': 0, '61-80': 0, '81-100': 0, '>100': 0}

    for user in user_data:
        gender = user['gender']
        state = user['location']['state']
        first_letter_first_name = ord(user['name']['first'][0])
        first_letter_last_name = ord(user['name']['last'][0])
        age = user['dob']['age']
    
        if gender == 'female':
            count_female += 1
            if state in count_by_state:
                count_by_state[state] += 1
                count_female_by_state[state] += 1
            else:
                count_by_state[state] = 1
                count_female_by_state[state] = 1
                count_male_by_state[state] = 0
        else:
            if state in count_by_state:
                count_by_state[state] += 1
                count_male_by_state[state] += 1
            else:
                count_by_state[state] = 1
                count_female_by_state[state] = 0
                count_male_by_state[state] = 1
            
        if first_letter_first_name >= 65 and \
            first_letter_first_name <= 77 or \
            first_letter_first_name >= 97 and \
            first_letter_first_name <= 109:
            count_by_first_name_start_letter['A-M'] += 1
        elif first_letter_first_name > 77 and \
             first_letter_first_name <= 90 or \
             first_letter_first_name > 109 and \
             first_letter_first_name <= 122:
            count_by_first_name_start_letter['N-Z'] += 1
        
        if first_letter_last_name >= 65 and \
           first_letter_last_name <= 77 or \
           first_letter_last_name >= 97 and \
           first_letter_last_name <= 109:
            count_by_last_name_start_letter['A-M'] += 1
        elif first_letter_last_name > 77 and \
            first_letter_last_name <= 90 or \
            first_letter_last_name > 109 and \
            first_letter_last_name <= 122:
            count_by_last_name_start_letter['N-Z'] += 1
    
        if age < 0:
            error = 1
        elif age < 21:
            count_by_age['0-20'] += 1
        elif age < 41:
            count_by_age['21-40'] += 1
        elif age < 61:
            count_by_age['41-60'] += 1
        elif age < 81:
            count_by_age['61-80'] += 1
        elif age < 101:
            count_by_age['81-100'] += 1
        else:
            count_by_age['>100'] += 1

    return {
        'total_users': total_users, \
        'count_female': count_female, \
        'count_by_state': count_by_state, \
        'count_female_by_state': count_female_by_state, \
        'count_male_by_state': count_male_by_state, \
        'count_by_first_name_start_letter': count_by_first_name_start_letter, \
        'count_by_last_name_start_letter': count_by_last_name_start_letter, \
        'count_by_age': count_by_age,
    }

def get_percent(part, whole):
    percent = (part/whole) * 100
    return round(percent, 2)

def get_population_percentage_by_state(count_by_state, total_users):
    number_of_states = len(count_by_state)
    
    if number_of_states > 10:
        count_by_state = sorted(count_by_state.items(), key=lambda x: x[1], reverse=True)[:10]
    else:
        count_by_state = sorted(count_by_state.items(), key=lambda x: x[1], reverse=True)
        
    population_by_state_percent = {}
    
    for state in count_by_state:
        population_by_state_percent[state[0]] = get_percent(state[1], total_users)
    
    return population_by_state_percent

def get_sex_percentage_by_state(count_sex_by_state, count_by_state):
    number_of_states = len(count_by_state)
    
    if number_of_states > 10:
        count_by_state = sorted(count_by_state.items(), key=lambda x: x[1], reverse=True)[:10]
    else:
        count_by_state = sorted(count_by_state.items(), key=lambda x: x[1], reverse=True)

    sex_percentage_by_state = {}

    for state in count_by_state:
        sex_percentage_by_state[state[0]] = get_percent(count_sex_by_state[state[0]], state[1])

    return sex_percentage_by_state

def get_percentage_by_age(count_by_age, total_users):
    percentage_by_age = {}

    for age_range in count_by_age:
        percentage_by_age[age_range] = get_percent(count_by_age[age_range], total_users)

    return percentage_by_age