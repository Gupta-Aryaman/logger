import flask
import redis

def create_app():
    # using flask, can handle 10k req/sec can use better later

    app = flask.Flask(__name__)

    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    @app.get("/")
    async def h():
        r.set("1","entry")
        return "OK"

    return app
