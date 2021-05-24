# Get Statistics API

Used to extract information from user data. The request Accept header can be added if you would like the response content to be in xml or plain text 
instead of json by specifying application/xml or text/plain respectively. Also, additional person objects can be added to the results list in the request
as needed. It is not limited to a single person.

**URL** : `https://user-data-analyzer.herokuapp.com/get_statistics`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
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
   ]
}
```

**Data example**

```json
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

## Success Response

**Code** : `200 OK`

**Content example**

```json
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
