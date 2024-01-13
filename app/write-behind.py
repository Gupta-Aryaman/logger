# Gears Recipe for a single write behind

# import redis gears & mongo db libs
from rgsync import RGJSONWriteBehind, RGJSONWriteThrough
from rgsync.Connectors import MongoConnector, MongoConnection

mongoUrl = 'mongodb://127.0.0.1:27017/'

# MongoConnection(user, password, host, authSource?, fullConnectionUrl?)
connection = MongoConnection('', '', '', '', mongoUrl)

# change MongoDB database
db = 'logDB'

# change MongoDB collection & it's primary key
testConnector = MongoConnector(connection, db, 'logDB_collection', 'traceId')

# change redis keys with prefix that must be synced with mongodb collection
RGJSONWriteBehind(GB,  keysPrefix='LogEntity',
                  connector=testConnector, name='LogWriteBehind',
                  version='99.99.99')