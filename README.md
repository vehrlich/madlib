## Coding exercise

Demonstrates usage of REST API and Docker to serve 3rd party service API response.

Simply run: `docker-compose -f docker-compose.yml up --build -d` from the root directory.

To get your juicy response run in a terminal after build: `curl -L http://localhost:8000/madlib`  
Or use browser and hit http://localhost:8000/madlib

If everything is ok, you should get JSON response `{'detail': TEMPLATED_SENTENCE}` consisting of adjective, verb, and noun from 3rd party service.  
If there is an HTTP error on the 3rd party service you get error response `{'detail': 'Unable to fetch data'}`

To execute tests, run in terminal: `docker exec -it madlib_app python manage.py test madlib `


**Note:** Do not use on the production. Or at least don't change `DEBUG=False` in settings.py.
