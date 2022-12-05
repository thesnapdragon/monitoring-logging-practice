from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Summary, Counter

app = Flask(__name__)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
COUNTER = Counter('test_counter', 'Description of counter')

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@REQUEST_TIME.time()
@app.route("/")
def hello_world():
    COUNTER.inc()
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()
