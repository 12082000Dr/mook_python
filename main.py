import logging
import random
import time
from datetime import datetime

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "giuewrgrt645tdhtr7rstwe4dsgdffh"
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")

@app.route("/python")
def main_page():
    start_time = time.time()
    value = str(random.randint(0, 5000))

    current_datetime = datetime.now()

    logging.info(f"{current_datetime}; value:{value}; time:{time.time() - start_time}")
    return value

if __name__ == '__main__':
    app.run()