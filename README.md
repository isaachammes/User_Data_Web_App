# User Data Web App and API

Both the web app and API accept data about users in either a json file or json object. Statistics are calculated based off of the inputed data and returned via the API or displayed as visualizations in the web app.

**Calculated Statistics**

percent_female_vs_male: Percentage of users that are female.
percent_first_names_start_a_to_m: Percentage of users with first names that start with A-M. Users with first names that do not start with A-Z are left out of the calculation.
percent_last_names_start_a_to_m: Percentage of users with last names that start with A-M. Users with last names that do not start with A-Z are left out of the calculation.
percent_by_state: Percentage of users that are in each state. This is only calculated for the ten most populous states.
percent_female_by_state: Percentage of users that female in each state. This is only calculated for the ten most populous states.
percent_male_by_state: Percentage of users that male in each state. This is only calculated for the ten most populous states.
percent_by_age: Percentage of users that are in the following age ranges 0-20, 21-40, 41-60, 61-80, 81-100, and >100.

**Web-App-URL** : `https://user-data-analyzer.herokuapp.com`

**API-URL** : `https://user-data-analyzer.herokuapp.com/get_statistics`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```
{
   "results":[
      {
         "gender":[male or female],
         "name":{
            "first":[any string],
            "last":[any string]
         },
         "location":{
            "state":[any string]
         },
         "dob":{
            "age":[positive integer]
         }
      }
      ...
   ]
}
```

**Request Content Example**

```
{
   "results":[
      {
         "gender": "female",
         "name":{
            "first": "Sara",
            "last": "Johnson"
         },
         "location":{
            "state":"Kansas"
         },
         "dob":{
            "age":12
         }
      }
   ]
}
```

## Example API Usage with Python Requests

```
import requests

URL = 'https://user-data-analyzer.herokuapp.com/get_statistics'
headers = {"Accept": "application/json"}
user_data = content_example

response = requests.post(URL, json=user_data, headers=json_header)
```

## Success Response

**Code** : `200 OK`

**Response File Content Examples by Accept Header**

**'Accept': 'application/json'**

```
{
  "percent_by_age": {
    "0-20": 100.0,
    "21-40": 0.0,
    "41-60": 0.0,
    "61-80": 0.0,
    "81-100": 0.0,
    ">100": 0.0
  },
  "percent_by_state": {
    "Kansas": 100.0
  },
  "percent_female_by_state": {
    "Kansas": 100.0
  },
  "percent_female_vs_male": 100.0,
  "percent_first_names_start_a_to_m": 0.0,
  "percent_last_names_start_a_to_m": 100.0,
  "percent_male_by_state": {
    "Kansas": 0.0
  }
}
```

**'Accept': 'text/plain'**

```
Percentage female versus male: 100.0%
Percentage of first names that start with A-M versus N-Z: 0.0%
Percentage of last names that start with A-M versus N-Z: 100.0%
Percentage of people in each state: Kansas: 100.0% 
Percentage of females in each state: Kansas: 100.0% 
Percentage of males in each state: Kansas: 0.0% 
Percentage of people by age: 0-20: 100.0% 21-40: 0.0% 41-60: 0.0% 61-80: 0.0% 81-100: 0.0% >100: 0.0% 
```

**'Accept': 'application/xml'**

```
<percent_by_age>
  <_0-20>100.0</_0-20>
  <_21-40>0.0</_21-40>
  <_41-60>0.0</_41-60>
  <_61-80>0.0</_61-80>
  <_81-100>0.0</_81-100>
  <__100>0.0</__100>
</percent_by_age>
<percent_by_state>
  <Kansas>100.0</Kansas>
</percent_by_state>
<percent_female_by_state>
  <Kansas>100.0</Kansas>
</percent_female_by_state>
<percent_female_vs_male>100.0</percent_female_vs_male>
<percent_first_names_start_a_to_m>0.0</percent_first_names_start_a_to_m>
<percent_last_names_start_a_to_m>100.0</percent_last_names_start_a_to_m>
<percent_male_by_state>
  <Kansas>0.0</Kansas>
</percent_male_by_state>
```

## Failed Response

**Code** : `200 OK`

**Response Content Examples by Accept Header**

**'Accept': 'application/json'**

```
{
  "percent_by_age": {
    "0-20": 100.0,
    "21-40": 0.0,
    "41-60": 0.0,
    "61-80": 0.0,
    "81-100": 0.0,
    ">100": 0.0
  },
  "percent_by_state": {
    "Kansas": 100.0
  },
  "percent_female_by_state": {
    "Kansas": 100.0
  },
  "percent_female_vs_male": 100.0,
  "percent_first_names_start_a_to_m": 0.0,
  "percent_last_names_start_a_to_m": 100.0,
  "percent_male_by_state": {
    "Kansas": 0.0
  }
}
```
