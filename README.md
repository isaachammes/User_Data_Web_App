# User Data Web App and API

Both the web app and API accept data about users in either a json file or json object. Statistics are calculated based off of the inputed data and returned via the API or displayed as visualizations in the web app.

**Calculated Statistics**

percent_female_vs_male: Percentage of users that are female.<br />
percent_first_names_start_a_to_m: Percentage of users with first names that start with A-M. Users with first names that do not start with A-Z are left out of the calculation.<br />
percent_last_names_start_a_to_m: Percentage of users with last names that start with A-M. Users with last names that do not start with A-Z are left out of the calculation.<br />
percent_by_state: Percentage of users that are in each state. This is only calculated for the ten most populous states.<br />
percent_female_by_state: Percentage of users that female in each state. This is only calculated for the ten most populous states.<br />
percent_male_by_state: Percentage of users that male in each state. This is only calculated for the ten most populous states.<br />
percent_by_age: Percentage of users that are in the following age ranges 0-20, 21-40, 41-60, 61-80, 81-100, and >100.<br />

**Web-App-URL** : `https://user-data-analyzer.herokuapp.com`

**API-URL** : `https://user-data-analyzer.herokuapp.com/get_statistics`

**Method** : `POST`

**Auth required** : NO

**Data Constraints**

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

## Example API Usage

```
POST https://user-data-analyzer.herokuapp.com/get_statistics HTTP/1.1
content-type: application/json
Accept: application/json

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

## Success Response by Accept Header

**'Accept': 'application/json'**

```
HTTP/1.1 200 OK
Connection: close
Server: gunicorn
Date: Sat, 29 May 2021 21:02:54 GMT
Content-Disposition: attachment; filename=result.json
Content-Type: application/json
Content-Length: 348
Cache-Control: no-cache
Via: 1.1 vegur

{
  "percent_female_vs_male": 100.0,
  "percent_first_names_start_a_to_m": 0.0,
  "percent_last_names_start_a_to_m": 100.0,
  "percent_by_state": {
    "Kansas": 100.0
  },
  "percent_male_by_state": {
    "Kansas": 0.0
  },
  "percent_female_by_state": {
    "Kansas": 100.0
  },
  "percent_by_age": {
    "0-20": 100.0,
    "21-40": 0.0,
    "41-60": 0.0,
    "61-80": 0.0,
    "81-100": 0.0,
    ">100": 0.0
  }
}
```

**'Accept': 'text/plain'**

```
HTTP/1.1 200 OK
Connection: close
Server: gunicorn
Date: Sat, 29 May 2021 21:03:52 GMT
Content-Disposition: attachment; filename=result.txt
Content-Type: text/plain; charset=utf-8
Content-Length: 421
Cache-Control: no-cache
Via: 1.1 vegur

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
HTTP/1.1 200 OK
Connection: close
Server: gunicorn
Date: Sat, 29 May 2021 21:04:22 GMT
Content-Disposition: attachment; filename=result.xml
Content-Type: text/xml; charset=utf-8
Content-Length: 587
Cache-Control: no-cache
Via: 1.1 vegur

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
