
http://www.allbuttonspressed.com/projects/djangoappengine

Important: Don't use dev_appserver.py directly. This won't work as expected because manage.py runserver uses a customized dev_appserver.py configuration. Also, never run manage.py runserver together with other management commands at the same time. The changes won't take effect. That's an App Engine SDK limitation which might get fixed in a later release.

manage.py remote allows you to execute a command on the production database (e.g., manage.py remote shell or manage.py remote createsuperuser)
manage.py deploy uploads your project to App Engine (use this instead of appcfg.py update)

http://www.django-rest-framework.org/tutorial/quickstart