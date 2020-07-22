## Django send mail example
---
## How to run it?
You can run it in your local computer by following this instruction
1. Clone this repository
2. Active your virtual environment
```
* if you use ubuntu
source ~/yourdirectoryenv/bin/activate
* if you use windows
basedir/nameofenv/Script/activate
```
3. Install dependency by run
```
pip install -r requirement.txt 
```
4. Migrate first your db by do
```
python manage.py migrate
```
5. Input your email and password in
```
* django_email/setting.py
* and find
EMAIL_HOST_USER = 'youremail@yourdomain.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
```
5. Run the server by do
```
python manage.py runserver
```
6. Open your browser then go to localhost:8000

