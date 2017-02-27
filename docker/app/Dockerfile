FROM python:3.6.0

RUN apt-get update

RUN pip install uwsgi
RUN apt-get install -y nginx

RUN pip install Django

#RUN  uwsgi --socket :8001 --chdir /var/app/ --wsgi-file flights/wsgi.py
#RUN uwsgi \
 #   --chdir=/var/app/flights \
 #   --module=myapp.wsgi:application \
 #   --env DJANGO_SETTINGS_MODULE=myapp.settings \
 #   --master --pidfile=/usr/local/var/run/uwsgi/project-master.pid \
 #   --socket=127.0.0.1:29000 \
 #   --processes=5 \
 #   --uid=505 --gid=505 \
 #   --harakiri=20 \
 #   --max-requests=5000 \
 #   --vacuum \
 #   --daemonize=/usr/local/var/log/uwsgi/myapp.log

COPY nginx.conf /etc/nginx/nginx.conf