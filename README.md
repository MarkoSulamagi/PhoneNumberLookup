- What does /hlr/sync mean in the endpoint?
- Why api2. and api3. subdomains are not working with HLR? 
- Python library needs updates to enable integration with new API endpoints.
HTTP Basic Auth requires changes in API.call_api()
- Application configurations in .ini file is a bit outdated. .env might be better solution

Endpoints

- GET /
RESPONSE:
Page

- POST /lookup 
REQUEST (application/json):
phone_numbers: ['+372534234', '+3723543934', '+54930232']


RESPONSE (application/json):
[
    {
      "status": "ON",
      "roamingNetwork": null,
      "roaming": false,
      "ported": false,
      "currentNetwork": {
        "countryPrefix": "372",
        "mccmnc": "24802",
        "countryCode": "EST",
        "countryName": "Estonia",
        "networkName": "Elisa Eesti"
      },
      "portedNetwork": null,
      "originalNetwork": {
        "countryPrefix": "372",
        "mccmnc": "24802",
        "countryCode": "EST",
        "countryName": "Estonia",
        "networkName": "Elisa Eesti"
      },
      "number": "+37256897563"
    },
    {'number': '+37256897561', 'error': 'Prefix based response used!'}  # WHAT\'S THIS?
    {"number": "+37255112233", 'error": 'Unknown Subscriber"},  # Number doesn\'t exist
    {"number": "+37255112233", 'error": 'Absent Subscriber"}  # Phone turned off
]

Python library:
- Had to extend Messente class (unneserarry)
- Had to overwrite call_api() method to enable basic auth


docker exec -it numberlookup_app_1 python -m unittest services.messente_api_tests


# ADD DEVELOPMENTS
LIMITS AND USAGE
STYLES LOADING INTO SEPARATE FILES
SWITCH INTL-TEL-INPUT DEPENDENCY
ADD NEW NUMBERS USING JAVASCRIPT

