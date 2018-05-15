# Phone Number Lookup 

Web application for looking up phone number operators. 
Using API provided by [Messente](https://messente.com).

Test environment can be found [here](http://0.0.0.0:8555).

### Scope of the application

Simple web application where user has the ability to look up if a 
phone number exists (is valid) and the name of the operator. 

Without any limitations the scope can grow quite large. I reduced the size of the scope by these limitations:


- There is no production build. Only development configuration.
- messente-python is missing a Hlr endpoint support. I created the integration for it. I included some unit tests, 
but not enough to cover everything.
- There is no error handling if Messente should have API errors. 
- Backend is written in Python 3. The application itself doesn't have tests. Only the Messente integration. 
Mostly because there's very little to test. 
- Frontend is written with Javascript (jquery) with webpack and ES6 compatibility. There are no tests in front end. 
- No application logging (didn't have time)
- Poor error handling (didn't have time)

### Architecture

![alt text](Architecture.png)

## Steps to run the application in development

The application is 100% built on docker containers. Dev/test/staging and live environments are all run in docker containers.
This will make development environment setups easy and team can be sure that all developers run with the same environment.

**To run the project in development**

**1. Clone the project**
`git clone git@github.com:MarkoSulamagi/PhoneNumberLookup.git`

**2. Install docker**
This is the environment specific part. Installing docker on Linux OSs is usually quite easy. 
I've noticed some installation issues with the Windows and Mac environments, but nothing that quick googling can't fix. 

https://docs.docker.com/install/

On Ubuntu 16.04 https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

**3. Install docker-compose**
https://docs.docker.com/compose/

On Ubuntu 16.04 https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04

**4. Build application**

`docker-compose build`

Docker needs to download all the dependencies, so it could take a while.

**5. Add configuraiton**

Rename .env.example into .env.

`cp .env.example .env`

Open .env files and replace the sample configuration with your own. Messente API username and password are required. 
You can sign up to [Messente]('https://messente.com').

**6. Run application**

`docker-compose up`

Docker needs to download all the dependencies, so it could take a while. 
Depending on the speed of the internet. Downloads only happen on first run. 

**8. Visit http://localhost:8555**

## Some development helpers. Only useful for additional development 

**Run Messente HLR API integration tests**

`docker exec -it numberlookup_app python -m unittest services.messente_api_tests`

**Install new JS library**

`docker exec -it numberlookup_npm npm install --save redux`

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
    {'number': '+37256897561', 'error': 'Prefix based response used!'}  # WHAT\'S THIS?
    {"number": "+37255112233", 'error": 'Unknown Subscriber"},  # Number doesn\'t exist
    {"number": "+37255112233", 'error": 'Absent Subscriber"}  # Phone turned off
]

Python library:
- Had to extend Messente class (unneserarry)
- Had to overwrite call_api() method to enable basic auth


docker exec -it numberlookup_app_1 python -m unittest services.messente_api_tests

- Env file

# ADD DEVELOPMENTS
LIMITS AND USAGE
STYLES LOADING INTO SEPARATE FILES
SWITCH INTL-TEL-INPUT DEPENDENCY
ADD NEW NUMBERS USING JAVASCRIPT

