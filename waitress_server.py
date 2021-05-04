import sys
sys.path.insert(0, "fizzbuzz_api")
from fizzbuzz_api import flask_app
from waitress import serve

# add logger file to waitress logger
import logging
logger = logging.getLogger("waitress")
logger.setLevel(logging.WARN)
file_handler = logging.FileHandler("fizzbuzz_api/logs/waitress.log")
logger.addHandler(file_handler)

# serveing options
fizzbuzz_app = flask_app("fizzbuzz_api/config/fizzbuzz.cfg")
app = fizzbuzz_app.create_app()

host = "0.0.0.0"
port = 80
threads = 5

# start server
serve(app, host=host, port=port, threads=threads)