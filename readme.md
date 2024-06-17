# Here I have mentioned all the details from scratch regarding Django

## creating the virtual environment

Here in this project I have used  
->Python 3.11  
-> django 5  
The project gives a basic overview of using django. In this project I have created a blogpost application using django.

The virtual environment creation command goes like

```sh {"id":"01J0JCVFTHJCTWNTJ9HPAGSYGC"}
conda create -n djangoenv python=3.11
```

```sh {"id":"01J0JD3YNNXPQ8DH8CJZKHXMC3"}
conda activate djangoenv
```

### installing packages

```sh {"id":"01J0JD3KEXFSPXKWDEECWV4F0F"}
pip install django
```

## Let's discuss about the file structure \

If we check the file structure
django_project  
|-django_project  
|-__init__.py  
|-asgi.py  
|-settings.py  
|-urls.py  
|-wsgi.py  
|-manage.py\