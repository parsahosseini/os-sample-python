import json
import numpy as np
from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
    return json.dumps({"number": float(np.random.rand())})


if __name__ == "__main__":
    application.run()
