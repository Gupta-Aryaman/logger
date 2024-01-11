import flask

def create_app():
    # using flask, can handle 10k req/sec can use better later

    app = flask.Flask(__name__)

    @app.get("/")
    async def h():
        return "Hello, World!"

    return app
