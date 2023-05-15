1) Make this one time for install module
   ```pip install phonenumbers```

2) Make this one time for install module,
   where {account_sid}, {auth_token}, {verify_sid}
   are your keys on twilio. Put keys in polls/tasks.py
   for functions send_phone and smss
   ```pip install twilio```

3) Make this one time for install module
   ```pip install -U Celery```

4) Make this one time set up ports
   ```docker run -d -p 5672:5672 rabbitmq```

5) Make this one time for install module
   ```pip install eventlet```

6) Make this one time for set up broker
   ``` celery -A djangocelery worker --loglevel=info -P eventlet```

7) Make this one time for start app
   ```python manage.py runserver```