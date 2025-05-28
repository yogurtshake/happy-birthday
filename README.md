# happy-birthday

[webpage](https://birthday.lucas.su-keun.kim)

## What's Happening Here?

I have set up my VPS (a GCP Compute Engine VM) to send out automated Happy Birthday emails to people whose information I have either entered manually or collected through the simple form on the webpage linked above.

The webpage is accessible through the domain birthday.lucas.su-keun.kim (a sub-sub-domain of su-keun.kim), which points to my server's internet-facing static IP. 

I have Nginx on this server acting as a reverse proxy for a couple of domains - for traffic coming from birthday.lucas.su-keun.kim, it directs to the webpage which is an extremely simple python (Flask) webapp, "app.py" running on a port on localhost. The page accepts input for a form consisting of a field for Name, Email, and Date of Birth. The HTML can be found in the templates folder in the file "form.html".

I have SQLite handle the form entries and save them in my simple database (which is not kept on this repo) which consists of a table, "birthdays", where the email address is the primary key. This ensures that duplicate entries are not allowed and that an entry can be updated by entering the same email address and different Name and/or DoB.

I have a script, "birthday_emailer.py", that finds which birthdays in the database are equal to today's date (only comparing month and day, of course) and sends a happy birthday email to the corresponding email address(es). How does it send the emails? Not by self-hosted email, that's for sure. I use the free tier of the service SMTP2GO and send via their SMTP server using the python library "smtplib". The free tier of SMTP2GO allows for 1000 emails sent per month (more than enough for this tiny project). 

The contents of the happy birthday email can be found in "birthday_emailer.py" where the only variable in the body that changes is the person's name. I set the "from" address as lucas@su-keun.kim (which does not actually exist) and the "reply-to address" as my own Gmail address. SPF and DKIM are set up for my domain, su-keun.kim, to accommodate SMTP2GO's server. 

Finally, I set up a cron job to run "birthday_emailer.py" every single day at 09:00 on the timezone America/Toronto.



## dependencies: 

nginx,
certbot,
~~mailutils~~
~~postfix~~
~~opendkim~~
SMTP2GO,
python3

python: flask, gunicorn, python-dotenv


## stuff for me

**command to restart web app (it has been set up as a systemd service):**

-> sudo systemctl restart birthday.service

check status:

-> sudo systemctl status birthday.service

command to manually start web app on localhost port 5001:

-> gunicorn -w 2 -b 127.0.0.1:5001 app:app
