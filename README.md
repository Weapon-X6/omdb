# OMDB
An app that retrieves and stores information about movies


### Features

* Use the OMDb API to fetch information about movies
* Increase efficiency by limiting the number of times the API is queried
* Use Signals, Celery and Redis to improve the overall scalability & performance
* Include a small demo module to connect to the GitHub API to😀!



### Installation

Install dependencies
```python
pip install -r requirements.txt
```
Run migrations

```python
python manage.py migrate
```

## Execution
To use this app you need an API key obtained by free at https://www.omdbapi.com/apikey.aspx.
Once you have a key, it’s passed in the URL as the *apikey* parameter. Note: Free
keys are limited to 1,000 requests per day.

For example, this is how you use your key by loading it from an environment variable
```python
import os
import requests
params = {"apikey": os.environ["DJANGO_OMDB_KEY"], "t": "ben stiller"}
resp = requests.get("https://www.omdbapi.com/", params=params)
# URL called: https://www.omdbapi.com/?apikey=<key>&t=ben+stiller
print(resp.json())
```

running django
```
python manage.py runserver
```
also run Celery in another terminal
```
celery -A course4_proj worker -l DEBUG
```
