# happy-birthday

[webpage](https://birthday.lucas.su-keun.kim)

## dependencies: 

nginx
certbot
~~mailutils~~
~~postfix~~
~~opendkim~~
SMTP2GO
python3

python: flask, gunicorn


## stuff

command to start web app on localhost port 5001:

-> gunicorn -w 2 -b 127.0.0.1:5001 app:app

command to restart web app (it has been set up as a systemd service):

-> sudo systemctl restart birthday.service

check status:

-> sudo systemctl status birthday.service
