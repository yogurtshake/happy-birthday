# happy-birthday

## dependencies: 

nginx
certbot
mailutils
postfix
opendkim
python3

python: flask, gunicorn


## stuff

command to start web app on localhost port 5001:

-> gunicorn -w 2 -b 127.0.0.1:5001 app:app

