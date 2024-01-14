# LOGGER
- Write-behind pattern

How to run the flask server - 
first create a virtual env and activate it
`
pip install -r requirements.txt
`
`/home/aryaman-gupta/Desktop/batcave/logger/env/bin/gunicorn -w 4 "app.main:create_app()"
`
`
gears-cli run ./app/write-behind.py REQUIREMENTS rgsync pymongo
`