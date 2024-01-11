# LOGGER
- Write-behind pattern

How to run the flask server - 
first create a virtual env and activate it
`
pip install -r requirements.txt
`
`sudo gunicorn -w 4 "app.main:create_app()"
`
