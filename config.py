import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'YOUR_OWN_PERSONAL_SECRET_KEY'
    GOOGLE_API_KEY = 'AIzaSyB456wC7rCOMx-c83Dq-DEq8UTI55rz3jc'
