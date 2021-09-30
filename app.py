import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

@app.route("/")
def test():
    return "Test is successful"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)