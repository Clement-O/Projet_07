# GrandPy Bot - Project 7 OpenClassrooms

You will need to create a "config.py" file in the same folder as "grandpybot.py" and add those lines :
```python
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'YOUR_OWN_PERSONAL_SECRET_KEY'
    GOOGLE_API_KEY = 'PERSONAL_GOOGLE_API_KEY'
```
Without them, the script will simply fail. (It won't be able to initialize and query the Google Maps API).

A live demo is available here : ADD_ADDRESS .