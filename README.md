Automatic Quality User Story Artisan Prototype - Backend
=======
This is an implementation of the AQUSA tool described in http://bit.ly/1IveMpa

### Installation
  * Tested with Python 3.4
  * Install Flask: `pip install Flask`
  * Install libraries using `pip install -r requirements.txt`
  * Create a database on Postgres
  * Delete the folder migrations.
  * Comment the line: `manager.add_command('translate', translate())` inside manage.py file.
  * Run the command: `./manage.py db init` in order to create all the migration files.
  * run migrations: `./manage.py db migrate` && `./manage.py db upgrade`. 
  * Install NLTK prerequisite 'Punkt Tokenizer' by running `nltk.download` in the Python interactive shell.
  * In order to install the nltk data, first you need to open the Python interactive shell by using the console command: `python` or `python3`, depends of your version
  * Once you have the Python interactive shell, run:
  ```python
    >>> import nltk
    >>> nltk.download()
  ```
  * Then, with the Download window opened, go to the tab 'Models' and select 'punkt'. Click to Download button, then it should work.
  * Run the translations with `./manage.py translate`. This will throw an error, but this is not a problem.
  * Test if the application works by running `nosetests`
  * Run server by executing `./run.py`
  * Or run shell by executing `./shell.py`

### Instructions for installing the stanford dependency
  * Download the stanford POStagger from
  * Move the files `stanford-postagger-withModel.jar` and `english-left3words-distsim.tagger` to this folder


### Usage
This is the backend of this application, exposing a simple API to be used by front end applications such as a Ruby on Rails web front-end or an iOS mobile client.

* POST to `/unique_string/project/new_story`
* GET stories from `/unique_string/project/stories`
* GET report from `/unique_string/project/report`

As a demo, you can browse to '/unique_string/project/upload_file' and upload a simple CSV. The report page also serves a simple HTML view.

Code Improvements
-------

### External links
- http://stackoverflow.com/questions/4867197/failed-loading-english-pickle-with-nltk-data-load