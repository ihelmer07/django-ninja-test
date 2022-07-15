Repo explaining major drawback of the super awesome [django-ninja framework](https://github.com/vitalik/django-ninja)

Please look at the tests in the backend/api folder to show apples to apples comparison for when trying to create a new object with M2M relationship.

I tried to make this as apples to apples as possible by using django-ninja's `ModelSchema` and drf's `ModelSerializer` and `ModelViewSet`.

# DISCLAIMER
I am very new to django-ninja and this could be a simple fix. 
I will update this repo if I learn of the 'correct' way to accomplish this in django-ninja.



### Set Up

```shell
py -m venv venv
pip install -r requirements.txt
py manage.py migrate
py manage.py test

```
