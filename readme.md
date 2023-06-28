# SENTIMENT ANALYZER API   

A Django Rest Framework Project To Analyze Text Sentiment Using A Pre-trained Machine Learning Model.


<br>

# Setup

To setup this project locally, follow the instructions below:

1. Create a directory and change directory:
```bash
$ mkdir API_Project/
$ cd API_Project/
```
2. Create a Python virtual environment:
```bash
$ python -m venv venv
```
3. Now activate the virtual environment:
```bash
$ source venv/bin/activate
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For Windows machines
```posh
PS> .\venv\Scripts\activate
```
4. Clone the project from github:
```bash
(venv)$ git clone 
(venv)$ cd sentiment_analyzer/
```
5. Install the *requirements.txt*:
```bash
(venv)$ pip install -r requirements.txt
```
6. Finally, collect the API Key and DB credentials from the admin and paste it in the project's directory for the project to run.

```
sentiment_analyzer/
├── manage.py
├── db.sqlite3
├── sentiment_analyzer/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── .env # --> Here
└── analyzer_api/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```
---

<br>

Now, run the following commands and you are ready to go!

```bash
(venv)$ python manage.py makemigrations
```

```bash
(venv)$ python manage.py migrate
```

```bash
(venv)$ python manage.py runserver
```
---
<br>

### Go to [localhost:8000]() or [127.0.0.1:8000]() to acces the API.