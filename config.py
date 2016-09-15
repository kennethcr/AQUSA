import os
basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED=True
UPLOAD_FOLDER= os.path.join(basedir,"tmp")
DEVELOPMENT = True
DEBUG = True
LANGUAGES = {
  'ma': 'Machine',
  'en': 'English'
}