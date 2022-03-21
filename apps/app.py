#------------third party Library-------------
from flask import Flask,request

#-------------------standard Library----------
import json

# craete an object
app = Flask (__name__)


@app.route("/add_2_numbers", methods = ["GET"])
def addition_two_numbers():
    return json.dumps((int(request.args.get("first_num")))+(int(request.args.get("second_num"))))


app.run(debug=False)


