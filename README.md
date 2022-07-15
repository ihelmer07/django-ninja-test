Repo explaining major drawback of the super awesome [django-ninja framework](https://github.com/vitalik/django-ninja)

Please look at the tests in the backend/api folder to show apples to apples comparison for when trying to create a new object with M2M relationship.

### Set Up

```shell
py -m venv venv
pip install -r requirements.txt
py manage.py migrate
py manage.py test

```
